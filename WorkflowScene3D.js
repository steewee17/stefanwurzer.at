/**
 * WorkflowScene3D.js
 * -----------------------------------------------------------------------------
 * Interaktive 3D-Prozesslandschaft in Three.js (Light-Tech / Full-Bleed SaaS Edition)
 * für stefanwurzer.at (KI-Befähigung & Agentic Systems).
 * 
 * Design-Spezifikation (High-End Light Tech):
 * - Nahtlose Verschmelzung mit dem warmen Off-White/Creme der Website (#FAFAF8 / #FFFFFF)
 * - Rechtsbündige räumliche Staffelung (Nodes schweben plastisch in der rechten Screen-Hälfte)
 * - Stark herangezoomte, cineastische Perspektive mit echten Tiefenebenen
 * - Helle Frosted-Glass Nodes (MeshPhysicalMaterial, Transmission 0.92, edles Gold-Rimlight)
 * - Gestochen scharfer, dunkler Anthrazit-Text auf den Nodes
 * - Luminous Neon-Tubes mit kontinuierlichem Energie-Wellen-Shader (Türkis & Gold)
 * - Kinetische Energie-Orbs mit strahlendem Kern und Partikel-Schweif
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

    // Light-Tech Farbpalette (Exakt abgestimmt auf stefanwurzer.at)
    this.colors = {
      bgWarm: 0xFAFAF8,          // Warmweiß / Creme der Website
      bgSec: 0xF7F5F0,
      brandGold: 0xB8962E,       // Executive Gold
      brandGoldLight: 0xD4B86A,  // Strahlendes Gold
      brandGoldPale: 0xF5EDD6,
      darkAnthrazit: 0x1A1A1A,
      rawCyan: 0x0EA5E9,         // Leuchtendes Türkis/Cyan für Rohdaten
      aiPurple: 0x9333EA,        // Anthropic Synapsen
      synthesizedGold: 0xF59E0B, // KI-Gold
      conduitBase: 0xE6DFD3      // Champagnerfarbene Glashülle
    };

    this.nodes = [];
    this.conduits = [];
    this.orbs = [];
    this.pulseMaterials = [];
    this.clock = new THREE.Clock();

    // Mouse Tracking
    this.mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    
    // Flow-Zentrum nach RECHTS versetzt (ca. X = 160 bis 180), damit links Raum für Text bleibt
    this.flowCenter = new THREE.Vector3(140, 15, 0);
    this.cameraDistance = 460; // Deutlich näher herangezoomt!

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
    // 1. Scene mit transparentem/warmem Hintergrund
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(this.colors.bgWarm);
    this.scene.fog = new THREE.FogExp2(this.colors.bgWarm, 0.00095);

    // 2. Camera (Fokussiert auf die rechte Bildschirmhälfte)
    const aspect = this.container.clientWidth / this.container.clientHeight;
    this.camera = new THREE.PerspectiveCamera(40, aspect, 1, 2800);
    this.updateCameraPosition();

    // 3. Renderer (High-DPI mit sauberer Tone Mapping Belichtung)
    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.08;
    this.container.appendChild(this.renderer.domElement);

    // 4. Helle, plastische Studio-Beleuchtung (Light-Tech Look)
    const ambientLight = new THREE.AmbientLight(0xfffbf5, 1.4);
    this.scene.add(ambientLight);

    const sunLight = new THREE.DirectionalLight(0xfff7ed, 2.2);
    sunLight.position.set(280, 450, 320);
    this.scene.add(sunLight);

    const goldFillLight = new THREE.DirectionalLight(0xfef08a, 1.3);
    goldFillLight.position.set(-150, 200, 200);
    this.scene.add(goldFillLight);

    const rimLight = new THREE.DirectionalLight(0xd4b86a, 1.8);
    rimLight.position.set(200, -180, -180);
    this.scene.add(rimLight);

    // Focal PointLight über der Reasoning Engine
    this.focalPointLight = new THREE.PointLight(this.colors.brandGoldLight, 3.2, 420);
    this.focalPointLight.position.set(160, 60, 50);
    this.scene.add(this.focalPointLight);
  }

  updateCameraPosition() {
    // Kamera fokussiert auf den Workflow rechts, mit dezenter Neigung
    this.camera.position.set(
      this.flowCenter.x + this.mouse.x * 28,
      this.flowCenter.y + 40 - this.mouse.y * 22,
      this.cameraDistance
    );
    this.camera.lookAt(new THREE.Vector3(this.flowCenter.x, this.flowCenter.y - 10, 0));
  }

  fitCameraToWorkflow() {
    if (!this.container || !this.camera) return;
    const aspect = this.container.clientWidth / this.container.clientHeight;
    this.camera.aspect = aspect;

    // Auf Breitbildschirmen schieben wir die Szene gezielt in die rechte Bildschirmhälfte
    // Bei schmalen Viewports zentrieren wir responsiv
    if (aspect > 1.3) {
      this.flowCenter.x = 180;
      this.cameraDistance = 470;
    } else if (aspect > 0.9) {
      this.flowCenter.x = 110;
      this.cameraDistance = 530;
    } else {
      this.flowCenter.x = 20;
      this.cameraDistance = 640;
    }

    this.camera.updateProjectionMatrix();
    this.updateCameraPosition();
  }

  createAtmosphere() {
    // 1. Elegantes, warmes 3D Bodenraster (Warmes Gold auf Weiß/Creme)
    const grid = new THREE.GridHelper(2000, 40, this.colors.brandGold, 0xE2DCD0);
    grid.position.y = -135;
    grid.material.opacity = 0.35;
    grid.material.transparent = true;
    this.scene.add(grid);

    // 2. Schwebende Lichtfunken (Golden & Champagne)
    const count = 180;
    const geom = new THREE.BufferGeometry();
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 1100 + 100;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 420;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 550;
    }
    geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const pCanvas = document.createElement('canvas');
    pCanvas.width = 32;
    pCanvas.height = 32;
    const ctx = pCanvas.getContext('2d');
    const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
    grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
    grad.addColorStop(0.3, 'rgba(212, 184, 106, 0.85)');
    grad.addColorStop(1, 'rgba(212, 184, 106, 0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 32, 32);

    const pTex = new THREE.CanvasTexture(pCanvas);
    const pMat = new THREE.PointsMaterial({
      size: 4.8,
      map: pTex,
      transparent: true,
      blending: THREE.NormalBlending,
      depthWrite: false,
      color: 0xD4B86A
    });

    this.ambientParticles = new THREE.Points(geom, pMat);
    this.scene.add(this.ambientParticles);
  }

  /**
   * Erzeugt gestochen scharfe Light-Tech Texturen für die Node-Fronten
   * Helles Milchglas mit tiefem Anthrazit-Text und warmen Gold-Akzenten.
   */
  createNodeTexture(data) {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 256;
    const ctx = canvas.getContext('2d');

    // Hochwertiges weißes/cremefarbenes Card-Panel
    ctx.fillStyle = 'rgba(255, 255, 255, 0.94)';
    ctx.fillRect(0, 0, 512, 256);

    // Warmes Gold-Highlight oben
    const topGrad = ctx.createLinearGradient(0, 0, 512, 0);
    topGrad.addColorStop(0, data.accentColor || '#B8962E');
    topGrad.addColorStop(1, '#E8D59A');
    ctx.fillStyle = topGrad;
    ctx.fillRect(0, 0, 512, 8);

    // Type Badge (Pill)
    ctx.fillStyle = 'rgba(184, 150, 46, 0.12)';
    if (ctx.roundRect) ctx.roundRect(28, 28, 180, 36, 6);
    else ctx.fillRect(28, 28, 180, 36);
    ctx.fill();

    ctx.font = '600 17px "Instrument Sans", system-ui, sans-serif';
    ctx.fillStyle = data.accentColor || '#B8962E';
    ctx.fillText((data.badge || 'NODE').toUpperCase(), 42, 52);

    // Live Indicator Dot (Grün)
    ctx.beginPath();
    ctx.arc(466, 46, 7, 0, Math.PI * 2);
    ctx.fillStyle = '#10B981';
    ctx.fill();
    ctx.beginPath();
    ctx.arc(466, 46, 12, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(16, 185, 129, 0.35)';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Node Title (Dunkles Anthrazit, gestochen scharf)
    ctx.font = '700 32px "Instrument Sans", system-ui, sans-serif';
    ctx.fillStyle = '#1A1A1A';
    ctx.fillText(data.title, 28, 120);

    // Subtitle
    ctx.font = '500 19px "Courier New", monospace';
    ctx.fillStyle = '#64748B';
    ctx.fillText(data.subtitle || 'pipeline process', 28, 158);

    // Divider Line
    ctx.strokeStyle = '#E2E8F0';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(28, 182);
    ctx.lineTo(484, 182);
    ctx.stroke();

    // Telemetrie / Status
    ctx.font = '600 18px "Instrument Sans", system-ui, sans-serif';
    ctx.fillStyle = '#B8962E';
    ctx.fillText(data.status || 'Active // 200 OK', 28, 220);

    const texture = new THREE.CanvasTexture(canvas);
    texture.minFilter = THREE.LinearFilter;
    texture.magFilter = THREE.LinearFilter;
    return texture;
  }

  buildWorkflowTopology() {
    this.workflowGroup = new THREE.Group();
    this.scene.add(this.workflowGroup);

    // 1. Großzügigere, gut lesbare Node-Dimensionen
    // Die Positionen sind nach rechts versetzt, sodass die Hauptebene bei X = 50 bis 400 liegt.
    const nodeConfigs = [
      {
        id: 'payload_ingest',
        title: 'Payload Ingest',
        badge: 'Webhook',
        subtitle: 'POST /payload-ingest',
        status: '200 OK // 4.2 req/s',
        accentColor: '#EC4899',
        pos: new THREE.Vector3(-180, -10, -20),
        size: [126, 68, 16]
      },
      {
        id: 'batch_normalizer',
        title: 'Batch Normalizer',
        badge: 'Code / JS',
        subtitle: 'Array Deduplicate',
        status: 'Buffer: 12 items/chunk',
        accentColor: '#F59E0B',
        pos: new THREE.Vector3(-45, -10, 0),
        size: [126, 68, 16]
      },
      {
        id: 'stream_dispatcher',
        title: 'Stream Dispatcher',
        badge: 'Batches / Split',
        subtitle: 'Rate-Limit Router',
        status: 'Active Loop Synced',
        accentColor: '#10B981',
        pos: new THREE.Vector3(85, -10, 15),
        size: [130, 70, 16]
      },
      {
        id: 'vector_context',
        title: 'Vector Context',
        badge: 'Vector DB',
        subtitle: 'POST /api/v1/query',
        status: 'Cosine: 0.94 // Top-5',
        accentColor: '#0EA5E9',
        pos: new THREE.Vector3(180, 42, -15),
        size: [126, 68, 16]
      },
      {
        id: 'reasoning_engine',
        title: 'Reasoning Engine',
        badge: 'AI Agent Core',
        subtitle: 'LangChain Orchestrator',
        status: 'Synthesizing Decision...',
        accentColor: '#B8962E',
        pos: new THREE.Vector3(305, 42, 10),
        size: [150, 78, 20],
        isHero: true
      },
      {
        id: 'anthropic_model',
        title: 'Anthropic Model',
        badge: 'LLM Feed',
        subtitle: 'Claude 3.5 Sonnet / 5',
        status: 'Tokens: 8.4k // T: 0.2',
        accentColor: '#CC785C',
        pos: new THREE.Vector3(305, -78, 30), // Untere Ebene
        size: [130, 64, 16],
        isSubNode: true
      },
      {
        id: 'confidence_gate',
        title: 'Confidence Gate',
        badge: 'IF Filter',
        subtitle: 'Score >= 0.75',
        status: '0.96 -> TRUE',
        accentColor: '#06B6D4',
        pos: new THREE.Vector3(435, 42, -5),
        size: [126, 68, 16]
      },
      {
        id: 'action_dispatch',
        title: 'Action Dispatch',
        badge: 'CRM Sync',
        subtitle: 'POST /api/v1/sync',
        status: '200 OK // Synced',
        accentColor: '#6366F1',
        pos: new THREE.Vector3(510, -26, 25),
        size: [126, 68, 16]
      },
      {
        id: 'telemetry_log',
        title: 'Telemetry & Log',
        badge: 'Telemetry',
        subtitle: 'Finalize & Archive',
        status: 'Completed // Logged',
        accentColor: '#B8962E',
        pos: new THREE.Vector3(560, 95, -30), // Obere Ebene
        size: [126, 68, 16]
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

    // Mattiertes Milchglas (Light Frosted Glass)
    const frostedGlassMat = new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      metalness: 0.05,
      roughness: 0.18,
      transmission: 0.92,
      thickness: 2.2,
      transparent: true,
      opacity: 0.96,
      reflectivity: 0.9,
      clearcoat: 0.8,
      clearcoatRoughness: 0.1
    });

    const frontMat = new THREE.MeshStandardMaterial({
      map: texture,
      transparent: true,
      roughness: 0.2,
      metalness: 0.05
    });

    const materials = [
      frostedGlassMat, frostedGlassMat, frostedGlassMat, frostedGlassMat,
      frontMat, frostedGlassMat
    ];

    const mesh = new THREE.Mesh(geometry, materials);
    mesh.position.copy(cfg.pos);
    mesh.castShadow = true;

    // Feine warme Gold-Kanten (Edler Kantenakzent)
    const edgesGeom = new THREE.EdgesGeometry(geometry);
    const edgeColor = cfg.isHero ? this.colors.brandGold : this.colors.brandGoldLight;
    const edgeMat = new THREE.LineBasicMaterial({
      color: edgeColor,
      transparent: true,
      opacity: cfg.isHero ? 0.95 : 0.65,
      linewidth: 2
    });
    const edgeLines = new THREE.LineSegments(edgesGeom, edgeMat);
    mesh.add(edgeLines);

    // Goldene Port-Konnektoren
    const portGeom = new THREE.SphereGeometry(3.2, 16, 16);
    const portMat = new THREE.MeshStandardMaterial({
      color: this.colors.brandGold,
      metalness: 0.8,
      roughness: 0.2
    });

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
        mesh.scale.set(1.04, 1.04, 1.04);
        edgeLines.material.opacity = 1.0;
      }
    };
  }

  getNode(id) {
    return this.nodes.find(n => n.cfg.id === id);
  }

  /**
   * Erzeugt helle, strahlende Neon-Röhren mit Lichtwellen-Shader
   */
  createPulseShaderMaterial(baseColorHex, pulseColorHex) {
    const material = new THREE.ShaderMaterial({
      uniforms: {
        uTime: { value: 0 },
        uBaseColor: { value: new THREE.Color(baseColorHex) },
        uPulseColor: { value: new THREE.Color(pulseColorHex) },
        uSpeed: { value: 3.8 }
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
          // Kontinuierliche pulsierende Energiewelle
          float wave = sin(vUv.x * 22.0 - uTime * uSpeed);
          float pulse = smoothstep(0.3, 0.98, wave);
          
          vec3 finalColor = mix(uBaseColor, uPulseColor, pulse);
          float alpha = mix(0.65, 1.0, pulse);
          
          gl_FragColor = vec4(finalColor, alpha);
        }
      `,
      transparent: true,
      blending: THREE.NormalBlending
    });

    this.pulseMaterials.push(material);
    return material;
  }

  createNeonConduits() {
    const n = id => this.getNode(id).cfg.pos;

    const conduitDefinitions = [
      // 1. Ingest -> Normalizer
      {
        id: 'p_ingest_norm',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('payload_ingest').x + 63, n('payload_ingest').y, n('payload_ingest').z),
          new THREE.Vector3(n('batch_normalizer').x - 63, n('batch_normalizer').y, n('batch_normalizer').z)
        ], false, 'centripetal', 0.2)
      },
      // 2. Normalizer -> Dispatcher
      {
        id: 'p_norm_disp',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('batch_normalizer').x + 63, n('batch_normalizer').y, n('batch_normalizer').z),
          new THREE.Vector3(n('stream_dispatcher').x - 65, n('stream_dispatcher').y, n('stream_dispatcher').z)
        ], false, 'centripetal', 0.2)
      },
      // 3. Dispatcher -> Telemetry Done Bypass (OBERE EBENE)
      {
        id: 'p_disp_telemetry_done',
        pulseColor: this.colors.brandGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('stream_dispatcher').x + 65, n('stream_dispatcher').y + 10, n('stream_dispatcher').z),
          new THREE.Vector3(220, 130, -50),
          new THREE.Vector3(420, 135, -55),
          new THREE.Vector3(n('telemetry_log').x - 63, n('telemetry_log').y, n('telemetry_log').z)
        ], false, 'centripetal', 0.5)
      },
      // 4. Dispatcher -> Vector Context
      {
        id: 'p_disp_vector',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('stream_dispatcher').x + 65, n('stream_dispatcher').y - 4, n('stream_dispatcher').z),
          new THREE.Vector3(135, 12, 5),
          new THREE.Vector3(n('vector_context').x - 63, n('vector_context').y, n('vector_context').z)
        ], false, 'centripetal', 0.3)
      },
      // 5. Vector Context -> Reasoning Engine
      {
        id: 'p_vector_reasoning',
        pulseColor: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('vector_context').x + 63, n('vector_context').y, n('vector_context').z),
          new THREE.Vector3(n('reasoning_engine').x - 75, n('reasoning_engine').y, n('reasoning_engine').z)
        ], false, 'centripetal', 0.2)
      },
      // 6. Anthropic Model -> Reasoning Engine (Vertikaler Inferenz-Feed)
      {
        id: 'p_anthropic_reasoning',
        pulseColor: this.colors.aiPurple,
        isVertical: true,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('anthropic_model').x, n('anthropic_model').y + 32, n('anthropic_model').z),
          new THREE.Vector3(n('anthropic_model').x - 6, -20, 20),
          new THREE.Vector3(n('reasoning_engine').x, n('reasoning_engine').y - 39, n('reasoning_engine').z)
        ], false, 'centripetal', 0.4)
      },
      // 7. Reasoning Engine -> Confidence Gate
      {
        id: 'p_reasoning_gate',
        pulseColor: this.colors.synthesizedGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('reasoning_engine').x + 75, n('reasoning_engine').y, n('reasoning_engine').z),
          new THREE.Vector3(n('confidence_gate').x - 63, n('confidence_gate').y, n('confidence_gate').z)
        ], false, 'centripetal', 0.2)
      },
      // 8. Confidence Gate -> Action Dispatch
      {
        id: 'p_gate_action',
        pulseColor: this.colors.synthesizedGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('confidence_gate').x + 63, n('confidence_gate').y + 5, n('confidence_gate').z),
          new THREE.Vector3(480, 8, 12),
          new THREE.Vector3(n('action_dispatch').x - 63, n('action_dispatch').y, n('action_dispatch').z)
        ], false, 'centripetal', 0.3)
      },
      // 9. Action Dispatch -> Telemetry
      {
        id: 'p_action_telemetry',
        pulseColor: this.colors.brandGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('action_dispatch').x + 63, n('action_dispatch').y, n('action_dispatch').z),
          new THREE.Vector3(540, 30, 0),
          new THREE.Vector3(n('telemetry_log').x - 30, n('telemetry_log').y - 30, n('telemetry_log').z)
        ], false, 'centripetal', 0.4)
      },
      // 10. Rückführung / Feedback Infinite Loop
      {
        id: 'p_loop_return',
        pulseColor: this.colors.brandGold,
        isFeedback: true,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('action_dispatch').x, n('action_dispatch').y - 32, n('action_dispatch').z),
          new THREE.Vector3(420, -95, 65),
          new THREE.Vector3(260, -100, 80),
          new THREE.Vector3(120, -75, 60),
          new THREE.Vector3(n('stream_dispatcher').x, n('stream_dispatcher').y - 35, n('stream_dispatcher').z)
        ], false, 'centripetal', 0.5)
      }
    ];

    conduitDefinitions.forEach(c => {
      // Helle, warme Neon-Tube
      const radius = c.isVertical ? 2.2 : 2.8;
      const geom = new THREE.TubeGeometry(c.curve, 64, radius, 12, false);
      const mat = this.createPulseShaderMaterial(0xDACFBD, c.pulseColor);
      const mesh = new THREE.Mesh(geom, mat);
      this.workflowGroup.add(mesh);

      // Zarter Umhüllungs-Halo
      const haloGeom = new THREE.TubeGeometry(c.curve, 64, radius * 1.7, 8, false);
      const haloMat = new THREE.MeshBasicMaterial({
        color: c.pulseColor,
        transparent: true,
        opacity: 0.16,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      const haloMesh = new THREE.Mesh(haloGeom, haloMat);
      this.workflowGroup.add(haloMesh);

      this.conduits.push({
        id: c.id,
        curve: c.curve,
        mesh,
        color: c.pulseColor
      });
    });
  }

  initDataStream() {
    this.streamPipelines = [
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
      {
        segments: [
          'p_disp_telemetry_done'
        ]
      }
    ];

    // Strahlende Sprite Texture
    const sCanvas = document.createElement('canvas');
    sCanvas.width = 64;
    sCanvas.height = 64;
    const sCtx = sCanvas.getContext('2d');
    const grad = sCtx.createRadialGradient(32, 32, 0, 32, 32, 32);
    grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
    grad.addColorStop(0.28, 'rgba(245, 158, 11, 0.95)');
    grad.addColorStop(0.65, 'rgba(184, 150, 46, 0.4)');
    grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
    sCtx.fillStyle = grad;
    sCtx.fillRect(0, 0, 64, 64);
    this.orbTexture = new THREE.CanvasTexture(sCanvas);

    // Kinetische Protagonist-Orbs
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

    // Glühender weißer Kern
    const coreGeom = new THREE.SphereGeometry(4.2, 16, 16);
    const coreMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const coreMesh = new THREE.Mesh(coreGeom, coreMat);
    group.add(coreMesh);

    // Strahlender Halo
    const spriteMat = new THREE.SpriteMaterial({
      map: this.orbTexture,
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      color: this.colors.rawCyan
    });
    const sprite = new THREE.Sprite(spriteMat);
    sprite.scale.set(38, 38, 1);
    group.add(sprite);

    // Partikel-Trail
    const trailLength = 12;
    const trailGeom = new THREE.BufferGeometry();
    const trailPositions = new Float32Array(trailLength * 3);
    const trailColors = new Float32Array(trailLength * 3);

    for (let i = 0; i < trailLength; i++) {
      trailPositions[i * 3] = 0;
      trailPositions[i * 3 + 1] = 0;
      trailPositions[i * 3 + 2] = 0;

      const alpha = 1.0 - (i / trailLength);
      trailColors[i * 3] = 0.85 * alpha;
      trailColors[i * 3 + 1] = 0.7 * alpha;
      trailColors[i * 3 + 2] = 0.3 * alpha;
    }

    trailGeom.setAttribute('position', new THREE.BufferAttribute(trailPositions, 3));
    trailGeom.setAttribute('color', new THREE.BufferAttribute(trailColors, 3));

    const trailMat = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.85,
      blending: THREE.NormalBlending,
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
    const geom = new THREE.SphereGeometry(2.8, 12, 12);
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
    sprite.scale.set(24, 24, 1);
    mesh.add(sprite);

    return { id, mesh, progress: offset };
  }

  buildHUDControls() {
    const hud = document.createElement('div');
    hud.id = 'wf3d-light-hud';
    hud.style.cssText = `
      position: absolute;
      bottom: 24px;
      right: 28px;
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(184, 150, 46, 0.3);
      border-radius: 8px;
      padding: 7px 12px;
      font-family: 'Instrument Sans', system-ui, sans-serif;
      font-size: 11px;
      color: #1A1A1A;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
      user-select: none;
    `;

    hud.innerHTML = `
      <div style="display:flex;align-items:center;gap:6px;padding-right:8px;border-right:1px solid #E2E8F0">
        <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#10B981;box-shadow:0 0 6px #10B981"></span>
        <span style="font-weight:700;color:#1A1A1A;letter-spacing:0.04em">60 FPS</span>
      </div>
      <button id="wf3d-btn-play" style="background:transparent;border:none;color:#1A1A1A;cursor:pointer;font-size:11px;font-weight:600;padding:2px 4px">
        <span id="wf3d-icon-play">⏸ PAUSE</span>
      </button>
      <button id="wf3d-btn-reset" title="Kamera zentrieren" style="background:transparent;border:none;color:#64748B;cursor:pointer;font-size:11px;font-weight:500">
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

    const baseSpeed = 0.35 * this.options.speed;

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

        // Transformation nach Reasoning Engine
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

        // Pulsieren
        const pulse = 1.0 + Math.sin(this.clock.getElapsedTime() * 8 + orb.id) * 0.16;
        orb.sprite.scale.set(38 * pulse, 38 * pulse, 1);

        // Trail
        orb.history.unshift(pos.clone());
        if (orb.history.length > 12) orb.history.pop();

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

    // 2. Pulse Shader Zeit updaten (Lichtwellen in den Neon-Tubes)
    this.pulseMaterials.forEach(mat => {
      mat.uniforms.uTime.value = time;
    });

    // 3. Node Dämpfung nach Impulsen
    this.nodes.forEach(n => {
      n.mesh.scale.lerp(n.baseScale, 0.08);
      const targetOpacity = n.cfg.isHero ? 0.95 : 0.65;
      n.edgeLines.material.opacity += (targetOpacity - n.edgeLines.material.opacity) * 0.08;
      n.mesh.position.y = n.cfg.pos.y + Math.sin(time * 1.5 + n.mesh.position.x * 0.02) * 1.3;
    });

    // 4. Datenstrom
    this.updateDataStream(delta);

    // 5. Ambient Partikel Drift
    if (this.ambientParticles) {
      this.ambientParticles.rotation.y = time * 0.01;
    }

    // 6. Focal Glow Light über Reasoning Engine
    if (this.focalPointLight) {
      this.focalPointLight.intensity = 3.0 + Math.sin(time * 3) * 0.5;
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
    const hud = document.getElementById('wf3d-light-hud');
    if (hud) hud.remove();
  }
}
