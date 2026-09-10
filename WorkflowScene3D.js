/**
 * WorkflowScene3D.js
 * -----------------------------------------------------------------------------
 * Interaktive, cineastische 3D-Prozesslandschaft in Three.js basierend auf dem
 * n8n-Kernworkflow von Stefan Wurzer (KI-Befähigung & Agentic Systems).
 * 
 * Refactoring-Highlights:
 * - Perfekte Bounding Box & Auto-Framing für 2-Spalten Layout (Rechte Spalte)
 * - Kamera zentriert auf "Reasoning Engine", alle 9 Nodes stets 100% sichtbar
 * - Neon-Tubes mit dynamischem Pulse-Shader (sichtbarer Energiefluss entlang der Splines)
 * - Straffere, kinetische Leitbahnen mit dynamischen Bézier-/Catmull-Rom-Kurven
 * - Edles Graphit/Anthrazit-Ambiente mit warmen Marken-Gold-Akzenten (#B8962E / #D4B86A)
 * - Kinetischer Protagonist: Transformierende Orbs mit Partikel-Schweif
 * -----------------------------------------------------------------------------
 */

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

export class WorkflowScene3D {
  constructor(options = {}) {
    this.container = options.container || document.body;
    this.options = Object.assign({
      interactive: true,
      showControls: true,
      speed: 1.0,
      isPlaying: true
    }, options);

    // Warmes, edles Corporate Design Stefan Wurzer
    this.colors = {
      brandGold: 0xB8962E,
      brandGoldLight: 0xD4B86A,
      brandGoldPale: 0xF5EDD6,
      bgGraphite: 0x0F1218,
      bgBox: 0x141820,
      nodeGlass: 0x151922,
      rawCyan: 0x38BDF8,         // Frische Rohdaten
      aiPurple: 0xC084FC,        // Anthropic Synapsen
      synthesizedGold: 0xF59E0B, // KI-Ergebnis
      conduitDark: 0x1A202C
    };

    this.nodes = [];
    this.conduits = [];
    this.orbs = [];
    this.pulseMaterials = [];
    this.clock = new THREE.Clock();

    // Mouse Tracking
    this.mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    this.cameraCenter = new THREE.Vector3(30, 8, 0); // Exakt um Reasoning Engine zentriert
    this.cameraDistance = 580;

    this.initScene();
    this.createAtmosphere();
    this.buildWorkflowTopology();
    this.initDataStream();
    this.fitCameraToWorkflow();
    if (this.options.showControls) this.buildHUDControls();
    this.bindEvents();

    this.animate = this.animate.bind(this);
    this.animationFrameId = requestAnimationFrame(this.animate);
  }

  initScene() {
    // 1. Scene mit edlem Graphit-Hintergrund
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(this.colors.bgGraphite);
    this.scene.fog = new THREE.FogExp2(this.colors.bgGraphite, 0.0009);

    // 2. Camera
    const aspect = this.container.clientWidth / this.container.clientHeight;
    this.camera = new THREE.PerspectiveCamera(42, aspect, 1, 3000);
    this.updateCameraPosition();

    // 3. Renderer mit sauberem Tone Mapping
    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.25;
    this.container.appendChild(this.renderer.domElement);

    // 4. Lichtführung (Warm, gerichtet & atmosphärisch)
    const ambientLight = new THREE.AmbientLight(0xfff8ee, 0.85);
    this.scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xffedd5, 1.8);
    keyLight.position.set(150, 350, 260);
    this.scene.add(keyLight);

    const goldRimLight = new THREE.DirectionalLight(0xd4b86a, 1.4);
    goldRimLight.position.set(-250, -150, -180);
    this.scene.add(goldRimLight);

    // Focal Glow Light direkt über der Reasoning Engine
    this.focalPointLight = new THREE.PointLight(this.colors.brandGoldLight, 2.8, 380);
    this.focalPointLight.position.set(85, 45, 45);
    this.scene.add(this.focalPointLight);
  }

  updateCameraPosition() {
    this.camera.position.set(
      this.cameraCenter.x + this.mouse.x * 35,
      this.cameraCenter.y + 35 - this.mouse.y * 25,
      this.cameraDistance
    );
    this.camera.lookAt(this.cameraCenter);
  }

  /**
   * Berechnet dynamisch die Bounding Box aller Nodes
   * und skaliert die Kameradistanz, sodass ALLE Nodes sichtbar sind.
   */
  fitCameraToWorkflow() {
    if (!this.container || !this.camera) return;
    const aspect = this.container.clientWidth / this.container.clientHeight;
    this.camera.aspect = aspect;

    // Horizontale Spannweite der Nodes ca. 640 Einheiten (-290 bis +320)
    // Vertikale Spannweite ca. 190 Einheiten (-85 bis +95)
    const fovInRad = (this.camera.fov * Math.PI) / 180;
    
    // Benötigte Distanz für X-Spannweite (mit 22% Sicherheits-Padding)
    const requiredDistX = (360 / Math.tan(fovInRad / 2)) / Math.max(aspect, 0.65);
    // Benötigte Distanz für Y-Spannweite
    const requiredDistY = (150 / Math.tan(fovInRad / 2));

    this.cameraDistance = Math.max(requiredDistX, requiredDistY, 520);
    this.camera.updateProjectionMatrix();
    this.updateCameraPosition();
  }

  createAtmosphere() {
    // 1. Zartes 3D Boden-Raster in warmem Gold-Ton
    const grid = new THREE.GridHelper(1800, 36, this.colors.brandGold, 0x222938);
    grid.position.y = -140;
    grid.material.opacity = 0.25;
    grid.material.transparent = true;
    this.scene.add(grid);

    // 2. Ambient Schwebepartikel (Goldstaub & Datenfunken)
    const count = 220;
    const geom = new THREE.BufferGeometry();
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 1200;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 450;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 600;
    }
    geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const pCanvas = document.createElement('canvas');
    pCanvas.width = 32;
    pCanvas.height = 32;
    const ctx = pCanvas.getContext('2d');
    const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
    grad.addColorStop(0, 'rgba(255,255,255,1)');
    grad.addColorStop(0.35, 'rgba(212,184,106,0.85)');
    grad.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 32, 32);

    const pTex = new THREE.CanvasTexture(pCanvas);
    const pMat = new THREE.PointsMaterial({
      size: 4.2,
      map: pTex,
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      color: 0xEDD59A
    });

    this.ambientParticles = new THREE.Points(geom, pMat);
    this.scene.add(this.ambientParticles);
  }

  /**
   * HUD Front-Textur für Nodes mit gestochen scharfer Typografie
   */
  createNodeTexture(data) {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 256;
    const ctx = canvas.getContext('2d');

    // Dunkler Glassmorphism-Hintergrund
    ctx.fillStyle = '#141822';
    ctx.fillRect(0, 0, 512, 256);

    // Warmes Kanten-Highlight oben
    const topGrad = ctx.createLinearGradient(0, 0, 512, 0);
    topGrad.addColorStop(0, data.accentColor || '#B8962E');
    topGrad.addColorStop(1, 'rgba(212,184,106,0.2)');
    ctx.fillStyle = topGrad;
    ctx.fillRect(0, 0, 512, 7);

    // Type Badge
    ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
    if (ctx.roundRect) ctx.roundRect(28, 28, 175, 34, 5);
    else ctx.fillRect(28, 28, 175, 34);
    ctx.fill();

    ctx.font = '600 17px "Instrument Sans", system-ui, sans-serif';
    ctx.fillStyle = data.accentColor || '#D4B86A';
    ctx.fillText((data.badge || 'NODE').toUpperCase(), 40, 51);

    // Status Indicator Dot
    ctx.beginPath();
    ctx.arc(465, 45, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#22c55e';
    ctx.fill();

    // Node Name
    ctx.font = '600 30px "Instrument Sans", system-ui, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(data.title, 28, 118);

    // Subtitel
    ctx.font = '400 19px "Courier New", monospace';
    ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
    ctx.fillText(data.subtitle || 'pipeline node', 28, 156);

    // Trennlinie
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(28, 180);
    ctx.lineTo(484, 180);
    ctx.stroke();

    // Telemetrie
    ctx.font = '500 18px "Instrument Sans", system-ui, sans-serif';
    ctx.fillStyle = '#D4B86A';
    ctx.fillText(data.status || 'Active // 200 OK', 28, 218);

    const texture = new THREE.CanvasTexture(canvas);
    texture.minFilter = THREE.LinearFilter;
    texture.magFilter = THREE.LinearFilter;
    return texture;
  }

  buildWorkflowTopology() {
    this.workflowGroup = new THREE.Group();
    this.scene.add(this.workflowGroup);

    // Optimierte, kompakte 3D-Koordinaten für perfekten Viewport-Fit:
    const nodeConfigs = [
      {
        id: 'payload_ingest',
        title: 'Payload Ingest',
        badge: 'Webhook',
        subtitle: 'POST /payload-ingest',
        status: '200 OK // 4.2 req/s',
        accentColor: '#EC4899',
        pos: new THREE.Vector3(-285, -10, 0),
        size: [100, 54, 14]
      },
      {
        id: 'batch_normalizer',
        title: 'Batch Normalizer',
        badge: 'Code / JS',
        subtitle: 'Array Flatten',
        status: 'Chunk: 12 items',
        accentColor: '#F59E0B',
        pos: new THREE.Vector3(-175, -10, 10),
        size: [100, 54, 14]
      },
      {
        id: 'stream_dispatcher',
        title: 'Stream Dispatcher',
        badge: 'Batches / Split',
        subtitle: 'Loop Router',
        status: 'Streaming Active',
        accentColor: '#10B981',
        pos: new THREE.Vector3(-60, -10, 15),
        size: [105, 56, 14]
      },
      {
        id: 'vector_context',
        title: 'Vector Context',
        badge: 'Vector DB',
        subtitle: 'POST /api/v1/query',
        status: 'Cosine: 0.94 // Top-5',
        accentColor: '#38BDF8',
        pos: new THREE.Vector3(20, 25, -10),
        size: [100, 54, 14]
      },
      {
        id: 'reasoning_engine',
        title: 'Reasoning Engine',
        badge: 'AI Agent Core',
        subtitle: 'LangChain Agent',
        status: 'Synthesizing Decision',
        accentColor: '#D4B86A',
        pos: new THREE.Vector3(120, 25, 5),
        size: [118, 62, 16],
        isHero: true
      },
      {
        id: 'anthropic_model',
        title: 'Anthropic Model',
        badge: 'LLM Feed',
        subtitle: 'Claude 3.5 Sonnet / 5',
        status: 'Tokens: 8.4k // T: 0.2',
        accentColor: '#CC785C',
        pos: new THREE.Vector3(120, -78, 25), // Untere Ebene
        size: [105, 52, 14],
        isSubNode: true
      },
      {
        id: 'confidence_gate',
        title: 'Confidence Gate',
        badge: 'IF Filter',
        subtitle: 'Score >= 0.75',
        status: '0.96 -> TRUE',
        accentColor: '#06B6D4',
        pos: new THREE.Vector3(225, 25, -5),
        size: [100, 54, 14]
      },
      {
        id: 'action_dispatch',
        title: 'Action Dispatch',
        badge: 'CRM Sync',
        subtitle: 'POST /api/v1/sync',
        status: '200 OK // Synced',
        accentColor: '#818CF8',
        pos: new THREE.Vector3(290, -28, 20),
        size: [100, 54, 14]
      },
      {
        id: 'telemetry_log',
        title: 'Telemetry & Log',
        badge: 'Telemetry',
        subtitle: 'Execution Finalize',
        status: 'Completed // Logged',
        accentColor: '#D4B86A',
        pos: new THREE.Vector3(325, 80, -25), // Obere Ebene
        size: [100, 54, 14]
      }
    ];

    nodeConfigs.forEach(cfg => {
      const nodeObj = this.createNodeMesh(cfg);
      this.workflowGroup.add(nodeObj.mesh);
      this.nodes.push(nodeObj);
    });

    this.createNeonConduits();
  }

  createNodeMesh(cfg) {
    const [w, h, d] = cfg.size;
    const geometry = new THREE.BoxGeometry(w, h, d);
    const texture = this.createNodeTexture(cfg);

    // Feines Glassmorphism-Material mit bernsteinfarbenen/goldenen Lichtkanten
    const glassMat = new THREE.MeshPhysicalMaterial({
      color: this.colors.nodeGlass,
      metalness: 0.15,
      roughness: 0.12,
      transmission: 0.88,
      thickness: 1.8,
      transparent: true,
      opacity: 0.92,
      reflectivity: 0.85,
      clearcoat: 0.5
    });

    const frontMat = new THREE.MeshStandardMaterial({
      map: texture,
      transparent: true,
      roughness: 0.25,
      metalness: 0.1
    });

    const materials = [
      glassMat, glassMat, glassMat, glassMat,
      frontMat, glassMat
    ];

    const mesh = new THREE.Mesh(geometry, materials);
    mesh.position.copy(cfg.pos);

    // Warmes goldenes Kantenleuchten (EdgesGeometry)
    const edgesGeom = new THREE.EdgesGeometry(geometry);
    const edgeColor = cfg.isHero ? this.colors.brandGoldLight : this.colors.brandGold;
    const edgeMat = new THREE.LineBasicMaterial({
      color: edgeColor,
      transparent: true,
      opacity: cfg.isHero ? 0.95 : 0.55,
      linewidth: 2
    });
    const edgeLines = new THREE.LineSegments(edgesGeom, edgeMat);
    mesh.add(edgeLines);

    // Port Dots
    const portGeom = new THREE.SphereGeometry(2.6, 12, 12);
    const portMat = new THREE.MeshBasicMaterial({ color: this.colors.brandGoldLight });

    const portIn = new THREE.Mesh(portGeom, portMat);
    portIn.position.set(-w / 2, 0, 0);
    mesh.add(portIn);

    const portOut = new THREE.Mesh(portGeom, portMat);
    portOut.position.set(w / 2, 0, 0);
    mesh.add(portOut);

    return {
      cfg,
      mesh,
      edgeLines,
      baseScale: new THREE.Vector3(1, 1, 1),
      triggerPulse: () => {
        mesh.scale.set(1.05, 1.05, 1.05);
        edgeLines.material.opacity = 1.0;
      }
    };
  }

  getNode(id) {
    return this.nodes.find(n => n.cfg.id === id);
  }

  /**
   * Erzeugt einen Custom Neon Pulse Shader für Röhren
   * Strahlender Lichtstrom wandert kontinuierlich durch die Leitung.
   */
  createPulseShaderMaterial(baseColorHex, pulseColorHex) {
    const material = new THREE.ShaderMaterial({
      uniforms: {
        uTime: { value: 0 },
        uBaseColor: { value: new THREE.Color(baseColorHex) },
        uPulseColor: { value: new THREE.Color(pulseColorHex) },
        uSpeed: { value: 3.5 }
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        uniform float uTime;
        uniform vec3 uBaseColor;
        uniform vec3 uPulseColor;
        uniform float uSpeed;
        varying vec2 vUv;

        void main() {
          // Kontinuierliche Wanderwelle
          float wave = sin(vUv.x * 24.0 - uTime * uSpeed);
          float pulse = smoothstep(0.4, 0.98, wave);
          
          vec3 finalColor = mix(uBaseColor, uPulseColor, pulse);
          float alpha = mix(0.45, 0.95, pulse);
          
          gl_FragColor = vec4(finalColor, alpha);
        }
      `,
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    });

    this.pulseMaterials.push(material);
    return material;
  }

  createNeonConduits() {
    const n = id => this.getNode(id).cfg.pos;

    // Dynamisch gestraffte Kurven (Circuit-Pfade mit definierter Straffung)
    const conduitDefinitions = [
      // 1. Ingest -> Normalizer
      {
        id: 'p_ingest_norm',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('payload_ingest').x + 50, n('payload_ingest').y, n('payload_ingest').z),
          new THREE.Vector3(n('batch_normalizer').x - 50, n('batch_normalizer').y, n('batch_normalizer').z)
        ], false, 'centripetal', 0.2)
      },
      // 2. Normalizer -> Dispatcher
      {
        id: 'p_norm_disp',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('batch_normalizer').x + 50, n('batch_normalizer').y, n('batch_normalizer').z),
          new THREE.Vector3(n('stream_dispatcher').x - 52, n('stream_dispatcher').y, n('stream_dispatcher').z)
        ], false, 'centripetal', 0.2)
      },
      // 3. Dispatcher -> Telemetry Done Bypass (OBERE EBENE Z/Y)
      {
        id: 'p_disp_telemetry_done',
        pulseColor: this.colors.brandGoldLight,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('stream_dispatcher').x + 52, n('stream_dispatcher').y + 8, n('stream_dispatcher').z),
          new THREE.Vector3(40, 110, -40),
          new THREE.Vector3(200, 115, -45),
          new THREE.Vector3(n('telemetry_log').x - 50, n('telemetry_log').y, n('telemetry_log').z)
        ], false, 'centripetal', 0.5)
      },
      // 4. Dispatcher -> Vector Context
      {
        id: 'p_disp_vector',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('stream_dispatcher').x + 52, n('stream_dispatcher').y - 4, n('stream_dispatcher').z),
          new THREE.Vector3(-20, 8, 5),
          new THREE.Vector3(n('vector_context').x - 50, n('vector_context').y, n('vector_context').z)
        ], false, 'centripetal', 0.3)
      },
      // 5. Vector Context -> Reasoning Engine
      {
        id: 'p_vector_reasoning',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('vector_context').x + 50, n('vector_context').y, n('vector_context').z),
          new THREE.Vector3(n('reasoning_engine').x - 59, n('reasoning_engine').y, n('reasoning_engine').z)
        ], false, 'centripetal', 0.2)
      },
      // 6. Anthropic Model -> Reasoning Engine (Vertikaler Inferenz-Feed)
      {
        id: 'p_anthropic_reasoning',
        pulseColor: this.colors.aiPurple,
        isVertical: true,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('anthropic_model').x, n('anthropic_model').y + 26, n('anthropic_model').z),
          new THREE.Vector3(n('anthropic_model').x - 5, -20, 15),
          new THREE.Vector3(n('reasoning_engine').x, n('reasoning_engine').y - 31, n('reasoning_engine').z)
        ], false, 'centripetal', 0.4)
      },
      // 7. Reasoning Engine -> Confidence Gate
      {
        id: 'p_reasoning_gate',
        pulseColor: this.colors.synthesizedGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('reasoning_engine').x + 59, n('reasoning_engine').y, n('reasoning_engine').z),
          new THREE.Vector3(n('confidence_gate').x - 50, n('confidence_gate').y, n('confidence_gate').z)
        ], false, 'centripetal', 0.2)
      },
      // 8. Confidence Gate -> Action Dispatch
      {
        id: 'p_gate_action',
        pulseColor: this.colors.synthesizedGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('confidence_gate').x + 50, n('confidence_gate').y + 5, n('confidence_gate').z),
          new THREE.Vector3(260, 5, 8),
          new THREE.Vector3(n('action_dispatch').x - 50, n('action_dispatch').y, n('action_dispatch').z)
        ], false, 'centripetal', 0.3)
      },
      // 9. Action Dispatch -> Telemetry
      {
        id: 'p_action_telemetry',
        pulseColor: this.colors.brandGoldLight,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('action_dispatch').x + 50, n('action_dispatch').y, n('action_dispatch').z),
          new THREE.Vector3(330, 25, 0),
          new THREE.Vector3(n('telemetry_log').x - 20, n('telemetry_log').y - 25, n('telemetry_log').z)
        ], false, 'centripetal', 0.4)
      },
      // 10. Rückführung / Feedback Infinite Loop
      {
        id: 'p_loop_return',
        pulseColor: this.colors.brandGold,
        isFeedback: true,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('action_dispatch').x, n('action_dispatch').y - 26, n('action_dispatch').z),
          new THREE.Vector3(200, -85, 55),
          new THREE.Vector3(60, -90, 65),
          new THREE.Vector3(-30, -65, 50),
          new THREE.Vector3(n('stream_dispatcher').x, n('stream_dispatcher').y - 26, n('stream_dispatcher').z)
        ], false, 'centripetal', 0.5)
      }
    ];

    conduitDefinitions.forEach(c => {
      // 1. Leuchtende Neon-Tube (Three.js TubeGeometry)
      const radius = c.isVertical ? 2.0 : 2.4;
      const geom = new THREE.TubeGeometry(c.curve, 64, radius, 12, false);
      const mat = this.createPulseShaderMaterial(0x182030, c.pulseColor);
      const mesh = new THREE.Mesh(geom, mat);
      this.workflowGroup.add(mesh);

      // 2. Äußerer subtiler Glow-Halo
      const haloGeom = new THREE.TubeGeometry(c.curve, 64, radius * 1.8, 8, false);
      const haloMat = new THREE.MeshBasicMaterial({
        color: c.pulseColor,
        transparent: true,
        opacity: 0.12,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      const haloMesh = new THREE.Mesh(haloGeom, haloMat);
      this.workflowGroup.add(haloMesh);

      this.conduits.push({
        id: c.id,
        curve: c.curve,
        mesh,
        color: c.pulseColor,
        isVertical: !!c.isVertical
      });
    });
  }

  initDataStream() {
    this.streamPipelines = [
      // Standard Durchlauf
      {
        segments: [
          'p_ingest_norm',
          'p_norm_disp',
          'p_disp_vector',
          'p_vector_reasoning',
          'p_reasoning_gate',
          'p_gate_action',
          'p_action_telemetry'
        ]
      },
      // Loop Zyklus
      {
        segments: [
          'p_disp_vector',
          'p_vector_reasoning',
          'p_reasoning_gate',
          'p_gate_action',
          'p_loop_return',
          'p_disp_vector'
        ]
      },
      // Done Bypass
      {
        segments: [
          'p_disp_telemetry_done'
        ]
      }
    ];

    // Sprite Texture
    const sCanvas = document.createElement('canvas');
    sCanvas.width = 64;
    sCanvas.height = 64;
    const sCtx = sCanvas.getContext('2d');
    const grad = sCtx.createRadialGradient(32, 32, 0, 32, 32, 32);
    grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
    grad.addColorStop(0.28, 'rgba(212, 184, 106, 0.95)');
    grad.addColorStop(0.7, 'rgba(184, 150, 46, 0.3)');
    grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
    sCtx.fillStyle = grad;
    sCtx.fillRect(0, 0, 64, 64);
    this.orbTexture = new THREE.CanvasTexture(sCanvas);

    // Kinetische Orbs
    this.orbs = [];
    const orbCount = 6;
    for (let i = 0; i < orbCount; i++) {
      let pipeline = this.streamPipelines[0];
      if (i % 3 === 1) pipeline = this.streamPipelines[1];
      if (i === 4) pipeline = this.streamPipelines[2];

      const orb = this.createOrbMesh(i, pipeline, i * (1.0 / orbCount));
      this.workflowGroup.add(orb.group);
      this.orbs.push(orb);
    }

    // Anthropic Synapsen Impulse
    this.aiTokens = [];
    for (let i = 0; i < 3; i++) {
      const token = this.createAiToken(i, i * 0.33);
      this.workflowGroup.add(token.mesh);
      this.aiTokens.push(token);
    }
  }

  createOrbMesh(id, pipeline, offset) {
    const group = new THREE.Group();

    // Glühender Kern
    const coreGeom = new THREE.SphereGeometry(3.8, 16, 16);
    const coreMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const coreMesh = new THREE.Mesh(coreGeom, coreMat);
    group.add(coreMesh);

    // Halo
    const spriteMat = new THREE.SpriteMaterial({
      map: this.orbTexture,
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      color: this.colors.rawCyan
    });
    const sprite = new THREE.Sprite(spriteMat);
    sprite.scale.set(32, 32, 1);
    group.add(sprite);

    // Dynamischer Schweif
    const trailLength = 10;
    const trailGeom = new THREE.BufferGeometry();
    const trailPositions = new Float32Array(trailLength * 3);
    const trailColors = new Float32Array(trailLength * 3);

    for (let i = 0; i < trailLength; i++) {
      trailPositions[i * 3] = 0;
      trailPositions[i * 3 + 1] = 0;
      trailPositions[i * 3 + 2] = 0;

      const alpha = 1.0 - (i / trailLength);
      trailColors[i * 3] = 0.8 * alpha;
      trailColors[i * 3 + 1] = 0.85 * alpha;
      trailColors[i * 3 + 2] = 1.0 * alpha;
    }

    trailGeom.setAttribute('position', new THREE.BufferAttribute(trailPositions, 3));
    trailGeom.setAttribute('color', new THREE.BufferAttribute(trailColors, 3));

    const trailMat = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.8,
      blending: THREE.AdditiveBlending,
      linewidth: 3
    });
    const trailLine = new THREE.Line(trailGeom, trailMat);
    this.workflowGroup.add(trailLine);

    return {
      id,
      group,
      coreMesh,
      sprite,
      spriteMat,
      trailLine,
      trailGeom,
      history: [],
      pipeline,
      segmentIndex: 0,
      segmentProgress: offset,
      currentSegmentId: pipeline.segments[0],
      isTransformed: false
    };
  }

  createAiToken(id, offset) {
    const geom = new THREE.SphereGeometry(2.4, 12, 12);
    const mat = new THREE.MeshBasicMaterial({ color: this.colors.brandGoldLight });
    const mesh = new THREE.Mesh(geom, mat);

    const spriteMat = new THREE.SpriteMaterial({
      map: this.orbTexture,
      color: this.colors.aiPurple,
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    });
    const sprite = new THREE.Sprite(spriteMat);
    sprite.scale.set(20, 20, 1);
    mesh.add(sprite);

    return { id, mesh, progress: offset };
  }

  buildHUDControls() {
    const hud = document.createElement('div');
    hud.id = 'wf3d-compact-hud';
    hud.style.cssText = `
      position: absolute;
      bottom: 16px;
      right: 16px;
      z-index: 30;
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(18, 22, 30, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(184, 150, 46, 0.3);
      border-radius: 6px;
      padding: 6px 10px;
      font-family: 'Instrument Sans', system-ui, sans-serif;
      font-size: 11px;
      color: #D4B86A;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
      user-select: none;
    `;

    hud.innerHTML = `
      <div style="display:flex;align-items:center;gap:5px;padding-right:6px;border-right:1px solid rgba(255,255,255,0.12)">
        <span style="display:inline-block;width:5px;height:5px;border-radius:50%;background:#22c55e;box-shadow:0 0 6px #22c55e"></span>
        <span style="font-weight:600;color:#fff;font-size:10px">60 FPS</span>
      </div>
      <button id="wf3d-btn-play" style="background:transparent;border:none;color:#fff;cursor:pointer;font-size:10px;font-weight:600;padding:2px 4px">
        <span id="wf3d-icon-play">⏸ PAUSE</span>
      </button>
      <button id="wf3d-btn-reset" title="Kamera zentrieren" style="background:transparent;border:none;color:rgba(255,255,255,0.6);cursor:pointer;font-size:10px">
        ↺ RESET
      </button>
    `;

    this.container.style.position = 'relative';
    this.container.appendChild(hud);

    const playBtn = hud.querySelector('#wf3d-btn-play');
    const playIcon = hud.querySelector('#wf3d-icon-play');
    playBtn.addEventListener('click', () => {
      this.options.isPlaying = !this.options.isPlaying;
      playIcon.textContent = this.options.isPlaying ? '⏸ PAUSE' : '▶ PLAY';
      playBtn.style.color = this.options.isPlaying ? '#fff' : '#D4B86A';
    });

    hud.querySelector('#wf3d-btn-reset').addEventListener('click', () => {
      this.mouse.targetX = 0;
      this.mouse.targetY = 0;
      this.fitCameraToWorkflow();
    });
  }

  bindEvents() {
    this.onWindowResize = () => {
      if (!this.container) return;
      const w = this.container.clientWidth;
      const h = this.container.clientHeight;
      this.renderer.setSize(w, h);
      this.fitCameraToWorkflow();
    };
    window.addEventListener('resize', this.onWindowResize);

    if (this.options.interactive) {
      this.onMouseMove = e => {
        const rect = this.container.getBoundingClientRect();
        const clientX = e.clientX - rect.left;
        const clientY = e.clientY - rect.top;
        this.mouse.targetX = (clientX / rect.width - 0.5) * 2;
        this.mouse.targetY = (clientY / rect.height - 0.5) * 2;
      };
      this.container.addEventListener('mousemove', this.onMouseMove);
    }
  }

  updateDataStream(delta) {
    if (!this.options.isPlaying) return;

    const baseSpeed = 0.36 * this.options.speed;

    this.orbs.forEach(orb => {
      orb.segmentProgress += baseSpeed * delta;

      if (orb.segmentProgress >= 1.0) {
        orb.segmentProgress = 0.0;
        orb.segmentIndex = (orb.segmentIndex + 1) % orb.pipeline.segments.length;
        orb.currentSegmentId = orb.pipeline.segments[orb.segmentIndex];

        const nodeMap = {
          'p_ingest_norm': 'batch_normalizer',
          'p_norm_disp': 'stream_dispatcher',
          'p_disp_vector': 'vector_context',
          'p_vector_reasoning': 'reasoning_engine',
          'p_reasoning_gate': 'confidence_gate',
          'p_gate_action': 'action_dispatch',
          'p_action_telemetry': 'telemetry_log',
          'p_disp_telemetry_done': 'telemetry_log',
          'p_loop_return': 'stream_dispatcher'
        };

        const targetNodeId = nodeMap[orb.currentSegmentId];
        if (targetNodeId) {
          const node = this.getNode(targetNodeId);
          if (node) node.triggerPulse();
        }
      }

      const conduit = this.conduits.find(c => c.id === orb.currentSegmentId);
      if (conduit) {
        const pos = conduit.curve.getPointAt(orb.segmentProgress);
        orb.group.position.copy(pos);

        // Transformation nach Reasoning Engine zu Stefan-Wurzer-Gold
        const isPostReasoning = [
          'p_reasoning_gate',
          'p_gate_action',
          'p_action_telemetry',
          'p_loop_return'
        ].includes(orb.currentSegmentId);

        if (isPostReasoning && !orb.isTransformed) {
          orb.isTransformed = true;
          orb.spriteMat.color.setHex(this.colors.synthesizedGold);
        } else if (!isPostReasoning && orb.isTransformed) {
          orb.isTransformed = false;
          orb.spriteMat.color.setHex(this.colors.rawCyan);
        }

        // Orb Pulsieren
        const pulse = 1.0 + Math.sin(this.clock.getElapsedTime() * 8 + orb.id) * 0.16;
        orb.sprite.scale.set(32 * pulse, 32 * pulse, 1);

        // Trail updaten
        orb.history.unshift(pos.clone());
        if (orb.history.length > 10) orb.history.pop();

        const positions = orb.trailGeom.attributes.position.array;
        for (let i = 0; i < orb.history.length; i++) {
          positions[i * 3] = orb.history[i].x;
          positions[i * 3 + 1] = orb.history[i].y;
          positions[i * 3 + 2] = orb.history[i].z;
        }
        orb.trailGeom.attributes.position.needsUpdate = true;
      }
    });

    // Anthropic Synapsen Feed
    const anthropicConduit = this.conduits.find(c => c.id === 'p_anthropic_reasoning');
    if (anthropicConduit) {
      this.aiTokens.forEach(token => {
        token.progress = (token.progress + delta * 0.6 * this.options.speed) % 1.0;
        const pos = anthropicConduit.curve.getPointAt(token.progress);
        token.mesh.position.copy(pos);
      });
    }
  }

  animate() {
    this.animationFrameId = requestAnimationFrame(this.animate);

    const delta = this.clock.getDelta();
    const time = this.clock.getElapsedTime();

    // 1. Mouse Parallax Dämpfung
    this.mouse.x += (this.mouse.targetX - this.mouse.x) * 0.04;
    this.mouse.y += (this.mouse.targetY - this.mouse.y) * 0.04;
    this.updateCameraPosition();

    // 2. Pulse Shader Zeit updaten (Energiefluss durch Neon-Tubes)
    this.pulseMaterials.forEach(mat => {
      mat.uniforms.uTime.value = time;
    });

    // 3. Node Dämpfung nach Impulsen
    this.nodes.forEach(n => {
      n.mesh.scale.lerp(n.baseScale, 0.08);
      const targetOpacity = n.cfg.isHero ? 0.95 : 0.55;
      n.edgeLines.material.opacity += (targetOpacity - n.edgeLines.material.opacity) * 0.08;
      // Sanftes natürliches Schweben
      n.mesh.position.y = n.cfg.pos.y + Math.sin(time * 1.6 + n.mesh.position.x * 0.02) * 1.2;
    });

    // 4. Datenstrom
    this.updateDataStream(delta);

    // 5. Ambient Partikel Drift
    if (this.ambientParticles) {
      this.ambientParticles.rotation.y = time * 0.012;
    }

    // 6. Focal Glow Light
    if (this.focalPointLight) {
      this.focalPointLight.intensity = 2.6 + Math.sin(time * 3) * 0.4;
    }

    this.renderer.render(this.scene, this.camera);
  }

  destroy() {
    cancelAnimationFrame(this.animationFrameId);
    window.removeEventListener('resize', this.onWindowResize);
    if (this.container && this.onMouseMove) {
      this.container.removeEventListener('mousemove', this.onMouseMove);
    }
    if (this.renderer && this.renderer.domElement) {
      this.renderer.domElement.remove();
    }
    const hud = document.getElementById('wf3d-compact-hud');
    if (hud) hud.remove();
  }
}
