/**
 * WorkflowScene3D.js
 * -----------------------------------------------------------------------------
 * Interaktive, cineastische 3D-Prozesslandschaft in Three.js basierend auf dem
 * n8n-Kernworkflow von Stefan Wurzer (KI-Befähigung & Agentic Systems).
 * 
 * Features:
 * - Räumliche 3D-Topologie (Obere Ebene: Bypass, Mitte: Pipeline, Unten: Anthropic LLM)
 * - Semi-transparente Glassmorphism-Nodes mit dezentem Brand-Gold-Rimlight & HUD-Labels
 * - Kinetische Datenpaket-Simulation ("Der Protagonist"): Infinite Stream aus Partikel-Orbs
 * - Farbmodulation an Reasoning Engine: Rohdaten-Cyan/Eisblau (#4DEEEA) -> Brand Gold (#D4B86A / #B8962E)
 * - Stationen-Reaktivität: Pulsieren & Glow-Impulse bei Node-Arrival
 * - Vertikaler KI-Synapsen-Feed vom Anthropic Chat Model
 * - Cinematic Isometric Camera mit sanftem Mouse-Parallax
 * - 60 FPS Performance (Additive Particle Buffer, Shared Geometries, Responsive Resize)
 * - Vollständig isoliertes Modul (Exportiert Klasse WorkflowScene3D)
 * -----------------------------------------------------------------------------
 */

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

export class WorkflowScene3D {
  /**
   * @param {Object} options
   * @param {HTMLElement} options.container - DOM-Element, in dem der Canvas gerendert wird
   * @param {boolean} [options.interactive=true] - Mouse-Parallax & Raycasting aktivieren
   * @param {boolean} [options.showControls=true] - Integrierte Dark-Tech Controls anzeigen
   * @param {Function} [options.onNodeSelect] - Callback bei Klick auf einen Node
   */
  constructor(options = {}) {
    this.container = options.container || document.body;
    this.options = Object.assign({
      interactive: true,
      showControls: true,
      onNodeSelect: null,
      autoRotate: false,
      speed: 1.0,
      isPlaying: true
    }, options);

    // Markenfarben Stefan Wurzer & n8n Palette
    this.colors = {
      brandGold: 0xB8962E,
      brandGoldLight: 0xD4B86A,
      brandGoldPale: 0xF5EDD6,
      darkBg: 0x0A0C10,
      nodeGlass: 0x12151C,
      rawCyan: 0x38BDF8,        // Frische Rohdaten (Eisblau/Cyan)
      aiPurple: 0xC084FC,       // Anthropic Synapsen
      synthesizedGold: 0xFACC15, // Reines KI-Ergebnis (Gold)
      gridColor: 0x2A2E38,
      conduitBase: 0x1E2433
    };

    this.nodes = [];
    this.conduits = [];
    this.orbs = [];
    this.ambientParticles = null;
    this.clock = new THREE.Clock();

    // Mouse Tracking
    this.mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    this.baseCameraPos = new THREE.Vector3(120, 150, 680);
    this.cameraTarget = new THREE.Vector3(140, -10, 0);

    // Initialisierung
    this.initScene();
    this.createAtmosphere();
    this.buildWorkflowTopology();
    this.initDataStream();
    if (this.options.showControls) this.buildHUDControls();
    this.bindEvents();

    this.animate = this.animate.bind(this);
    this.animationFrameId = requestAnimationFrame(this.animate);
  }

  initScene() {
    // 1. Scene
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(this.colors.darkBg);
    this.scene.fog = new THREE.FogExp2(this.colors.darkBg, 0.00085);

    // 2. Camera (Cineastische Isometrie)
    const aspect = this.container.clientWidth / this.container.clientHeight;
    this.camera = new THREE.PerspectiveCamera(40, aspect, 1, 3500);
    this.camera.position.copy(this.baseCameraPos);
    this.camera.lookAt(this.cameraTarget);

    // 3. Renderer
    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.15;
    this.container.appendChild(this.renderer.domElement);

    // 4. Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    this.scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xfff4e0, 1.6);
    keyLight.position.set(200, 400, 300);
    this.scene.add(keyLight);

    const rimLight = new THREE.DirectionalLight(0xd4b86a, 1.2);
    rimLight.position.set(-300, -200, -200);
    this.scene.add(rimLight);

    // Focal Gold PointLight über Reasoning Engine
    this.coreLight = new THREE.PointLight(this.colors.brandGoldLight, 2.5, 450);
    this.coreLight.position.set(220, 50, 40);
    this.scene.add(this.coreLight);
  }

  createAtmosphere() {
    // 1. Subtiles 3D-Bodenraster (Grid)
    const gridHelper = new THREE.GridHelper(2400, 48, this.colors.brandGold, this.colors.gridColor);
    gridHelper.position.y = -190;
    gridHelper.material.opacity = 0.22;
    gridHelper.material.transparent = true;
    this.scene.add(gridHelper);

    // 2. Schwebende Ambient-Micropartikel (Datenstaub)
    const count = 350;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(count * 3);
    const opacities = new Float32Array(count);

    for (let i = 0; i < count; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 1600;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 600;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 900;
      opacities[i] = Math.random() * 0.7 + 0.3;
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('opacity', new THREE.BufferAttribute(opacities, 1));

    // Custom Particle Sprite
    const canvas = document.createElement('canvas');
    canvas.width = 32;
    canvas.height = 32;
    const ctx = canvas.getContext('2d');
    const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
    grad.addColorStop(0, 'rgba(255,255,255,1)');
    grad.addColorStop(0.3, 'rgba(212,184,106,0.8)');
    grad.addColorStop(1, 'rgba(212,184,106,0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 32, 32);

    const spriteTex = new THREE.CanvasTexture(canvas);
    const material = new THREE.PointsMaterial({
      size: 4.5,
      map: spriteTex,
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      color: 0xE8D59A
    });

    this.ambientParticles = new THREE.Points(geometry, material);
    this.scene.add(this.ambientParticles);
  }

  /**
   * Erstellt HUD Canvas-Textur für Node-Fronten
   */
  createNodeTexture(data) {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 256;
    const ctx = canvas.getContext('2d');

    // Hintergrund Glass Panel
    ctx.fillStyle = 'rgba(15, 18, 26, 0.95)';
    ctx.fillRect(0, 0, 512, 256);

    // Dezenter oberer Highlight-Glow
    const headerGrad = ctx.createLinearGradient(0, 0, 512, 0);
    headerGrad.addColorStop(0, data.accentColor || '#B8962E');
    headerGrad.addColorStop(1, 'rgba(212, 184, 106, 0.15)');
    ctx.fillStyle = headerGrad;
    ctx.fillRect(0, 0, 512, 8);

    // Node Type Badge
    ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
    if (ctx.roundRect) {
      ctx.roundRect(32, 32, 180, 36, 6);
    } else {
      ctx.fillRect(32, 32, 180, 36);
    }
    ctx.fill();

    ctx.font = '600 18px "Instrument Sans", -apple-system, sans-serif';
    ctx.fillStyle = data.accentColor || '#D4B86A';
    ctx.fillText((data.badge || 'NODE').toUpperCase(), 46, 56);

    // Live Indicator Dot
    ctx.beginPath();
    ctx.arc(460, 50, 7, 0, Math.PI * 2);
    ctx.fillStyle = '#22c55e'; // Aktiv grün
    ctx.fill();
    ctx.beginPath();
    ctx.arc(460, 50, 12, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(34, 197, 94, 0.4)';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Node Title (Prägnante Typografie)
    ctx.font = '600 32px "Instrument Sans", -apple-system, sans-serif';
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(data.title, 32, 124);

    // Subtitle / Sub-Info
    ctx.font = '400 20px "Courier New", monospace';
    ctx.fillStyle = 'rgba(255, 255, 255, 0.55)';
    ctx.fillText(data.subtitle || 'n8n process stream', 32, 164);

    // Divider Line
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(32, 188);
    ctx.lineTo(480, 188);
    ctx.stroke();

    // Telemetrie Status
    ctx.font = '500 19px "Instrument Sans", -apple-system, sans-serif';
    ctx.fillStyle = '#D4B86A';
    ctx.fillText(data.status || 'Active // 200 OK', 32, 222);

    const texture = new THREE.CanvasTexture(canvas);
    texture.minFilter = THREE.LinearFilter;
    texture.magFilter = THREE.LinearFilter;
    return { texture, canvas, ctx };
  }

  buildWorkflowTopology() {
    this.workflowGroup = new THREE.Group();
    this.scene.add(this.workflowGroup);

    // 1. Topologische Node-Definitionen (Gemäß n8n JSON & Höhenstaffelung)
    const nodeConfigs = [
      {
        id: 'payload_ingest',
        title: 'Payload Ingest',
        badge: 'Webhook',
        subtitle: 'POST /payload-ingest',
        status: '200 OK // 4.2 req/s',
        accentColor: '#EC4899',
        pos: new THREE.Vector3(-380, 0, 0),
        size: [115, 60, 16]
      },
      {
        id: 'batch_normalizer',
        title: 'Batch Normalizer',
        badge: 'Code / JS',
        subtitle: 'Format & Deduplicate',
        status: 'Buffer: 12 items/chunk',
        accentColor: '#F59E0B',
        pos: new THREE.Vector3(-220, 0, 10),
        size: [115, 60, 16]
      },
      {
        id: 'stream_dispatcher',
        title: 'Stream Dispatcher',
        badge: 'Batches / Split',
        subtitle: 'Rate-Limit Router',
        status: 'Active Loop // Synced',
        accentColor: '#10B981',
        pos: new THREE.Vector3(-60, 0, 15),
        size: [120, 62, 16]
      },
      {
        id: 'vector_context',
        title: 'Vector Context',
        badge: 'Vector DB',
        subtitle: 'POST /api/v1/query',
        status: 'Top-K: 5 // Cosine 0.94',
        accentColor: '#38BDF8',
        pos: new THREE.Vector3(100, 35, -15),
        size: [115, 60, 16]
      },
      {
        id: 'reasoning_engine',
        title: 'Reasoning Engine',
        badge: 'AI Agent Core',
        subtitle: 'LangChain Orchestrator',
        status: 'Synthesizing Decision...',
        accentColor: '#D4B86A',
        pos: new THREE.Vector3(260, 35, 5),
        size: [140, 72, 20],
        isHero: true
      },
      {
        id: 'anthropic_model',
        title: 'Anthropic Model',
        badge: 'LLM Feed',
        subtitle: 'Claude 3.5 Sonnet / 5',
        status: 'Tokens: 8.4k // Temp 0.2',
        accentColor: '#CC785C',
        pos: new THREE.Vector3(260, -95, 35), // Untere Ebene!
        size: [118, 58, 16],
        isSubNode: true
      },
      {
        id: 'confidence_gate',
        title: 'Confidence Gate',
        badge: 'IF Filter',
        subtitle: 'Condition: score >= 0.75',
        status: 'Confidence: 0.96 -> TRUE',
        accentColor: '#06B6D4',
        pos: new THREE.Vector3(430, 35, -5),
        size: [115, 60, 16]
      },
      {
        id: 'action_dispatch',
        title: 'Action Dispatch',
        badge: 'CRM Sync',
        subtitle: 'POST /api/v1/sync',
        status: 'Dispatched // Handled',
        accentColor: '#818CF8',
        pos: new THREE.Vector3(580, -25, 25),
        size: [115, 60, 16]
      },
      {
        id: 'telemetry_log',
        title: 'Telemetry & Log',
        badge: 'Telemetry',
        subtitle: 'Finalize & Archive',
        status: 'Completed // Invoiced',
        accentColor: '#D4B86A',
        pos: new THREE.Vector3(700, 100, -35), // Obere Ebene!
        size: [115, 60, 16]
      }
    ];

    // Nodes im 3D-Raum generieren
    nodeConfigs.forEach(cfg => {
      const nodeObj = this.createNodeMesh(cfg);
      this.workflowGroup.add(nodeObj.mesh);
      this.nodes.push(nodeObj);
    });

    // 2. 3D-Spline Leitungsbahnen (Conduits)
    this.createConduits();
  }

  createNodeMesh(cfg) {
    const [w, h, d] = cfg.size;
    const geometry = new THREE.BoxGeometry(w, h, d);

    // Front Canvas Texture
    const texData = this.createNodeTexture(cfg);

    // Multi-Material: Frontseite mit HUD Canvas, Seiten mit Glassmorphism
    const glassMat = new THREE.MeshPhysicalMaterial({
      color: this.colors.nodeGlass,
      metalness: 0.2,
      roughness: 0.15,
      transmission: 0.85,
      thickness: 2.0,
      transparent: true,
      opacity: 0.9,
      reflectivity: 0.8,
      clearcoat: 0.6,
      clearcoatRoughness: 0.1
    });

    const frontMat = new THREE.MeshStandardMaterial({
      map: texData.texture,
      transparent: true,
      roughness: 0.2,
      metalness: 0.1
    });

    // Material Array für Box-Seiten: [+X, -X, +Y, -Y, +Z (Front), -Z (Back)]
    const materials = [
      glassMat, glassMat, glassMat, glassMat,
      frontMat, glassMat
    ];

    const mesh = new THREE.Mesh(geometry, materials);
    mesh.position.copy(cfg.pos);
    mesh.castShadow = true;
    mesh.receiveShadow = true;

    // Glowing Rim-Edges (Brand Gold / Accent)
    const edgesGeom = new THREE.EdgesGeometry(geometry);
    const edgeColor = cfg.isHero ? this.colors.brandGoldLight : this.colors.brandGold;
    const edgeMat = new THREE.LineBasicMaterial({
      color: edgeColor,
      transparent: true,
      opacity: cfg.isHero ? 0.85 : 0.45,
      linewidth: 2
    });
    const edgeLines = new THREE.LineSegments(edgesGeom, edgeMat);
    mesh.add(edgeLines);

    // Port-Dots (Verbindungspunkte links & rechts)
    const portGeom = new THREE.SphereGeometry(3, 16, 16);
    const portMat = new THREE.MeshBasicMaterial({ color: this.colors.brandGoldLight });

    const portIn = new THREE.Mesh(portGeom, portMat);
    portIn.position.set(-w / 2, 0, 0);
    mesh.add(portIn);

    const portOut = new THREE.Mesh(portGeom, portMat);
    portOut.position.set(w / 2, 0, 0);
    mesh.add(portOut);

    // Hero Halo wenn Reasoning Engine
    if (cfg.isHero) {
      const haloGeom = new THREE.PlaneGeometry(w * 1.6, h * 1.6);
      const haloMat = new THREE.MeshBasicMaterial({
        color: this.colors.brandGold,
        transparent: true,
        opacity: 0.12,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      const halo = new THREE.Mesh(haloGeom, haloMat);
      halo.position.z = -d;
      mesh.add(halo);
    }

    return {
      cfg,
      mesh,
      edgeLines,
      texData,
      baseScale: new THREE.Vector3(1, 1, 1),
      pulseTimer: 0,
      triggerPulse: () => {
        mesh.scale.set(1.05, 1.05, 1.05);
        edgeLines.material.opacity = 1.0;
      }
    };
  }

  getNode(id) {
    return this.nodes.find(n => n.cfg.id === id);
  }

  createConduits() {
    const n = id => this.getNode(id).cfg.pos;

    // Präzise Kurvendefinitionen basierend auf n8n Verbindungen
    const paths = [
      // 1. Ingest -> Normalizer
      {
        id: 'p_ingest_norm',
        color: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('payload_ingest').x + 58, n('payload_ingest').y, n('payload_ingest').z),
          new THREE.Vector3(n('batch_normalizer').x - 58, n('batch_normalizer').y, n('batch_normalizer').z)
        ])
      },
      // 2. Normalizer -> Dispatcher
      {
        id: 'p_norm_disp',
        color: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('batch_normalizer').x + 58, n('batch_normalizer').y, n('batch_normalizer').z),
          new THREE.Vector3(n('stream_dispatcher').x - 60, n('stream_dispatcher').y, n('stream_dispatcher').z)
        ])
      },
      // 3. Dispatcher -> Telemetry Bypass ("done" Zweig, OBERE EBENE Z/Y)
      {
        id: 'p_disp_telemetry_done',
        color: this.colors.brandGoldLight,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('stream_dispatcher').x + 60, n('stream_dispatcher').y + 10, n('stream_dispatcher').z),
          new THREE.Vector3(100, 140, -50),
          new THREE.Vector3(420, 150, -60),
          new THREE.Vector3(n('telemetry_log').x - 58, n('telemetry_log').y, n('telemetry_log').z)
        ])
      },
      // 4. Dispatcher -> Vector Context ("loop" Zweig)
      {
        id: 'p_disp_vector',
        color: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('stream_dispatcher').x + 60, n('stream_dispatcher').y - 5, n('stream_dispatcher').z),
          new THREE.Vector3(20, 15, 0),
          new THREE.Vector3(n('vector_context').x - 58, n('vector_context').y, n('vector_context').z)
        ])
      },
      // 5. Vector Context -> Reasoning Engine
      {
        id: 'p_vector_reasoning',
        color: this.colors.rawCyan,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('vector_context').x + 58, n('vector_context').y, n('vector_context').z),
          new THREE.Vector3(n('reasoning_engine').x - 70, n('reasoning_engine').y, n('reasoning_engine').z)
        ])
      },
      // 6. Anthropic Chat Model -> Reasoning Engine (UNTERE EBENE: Vertikaler Inferenz-Feed)
      {
        id: 'p_anthropic_reasoning',
        color: this.colors.aiPurple,
        isVerticalFeed: true,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('anthropic_model').x, n('anthropic_model').y + 29, n('anthropic_model').z),
          new THREE.Vector3(n('anthropic_model').x - 8, -25, 20),
          new THREE.Vector3(n('reasoning_engine').x, n('reasoning_engine').y - 36, n('reasoning_engine').z)
        ])
      },
      // 7. Reasoning Engine -> Confidence Gate
      {
        id: 'p_reasoning_gate',
        color: this.colors.synthesizedGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('reasoning_engine').x + 70, n('reasoning_engine').y, n('reasoning_engine').z),
          new THREE.Vector3(n('confidence_gate').x - 58, n('confidence_gate').y, n('confidence_gate').z)
        ])
      },
      // 8. Confidence Gate -> Action Dispatch (TRUE Zweig)
      {
        id: 'p_gate_action',
        color: this.colors.synthesizedGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('confidence_gate').x + 58, n('confidence_gate').y + 8, n('confidence_gate').z),
          new THREE.Vector3(500, 15, 10),
          new THREE.Vector3(n('action_dispatch').x - 58, n('action_dispatch').y, n('action_dispatch').z)
        ])
      },
      // 9. Action Dispatch -> Telemetry
      {
        id: 'p_action_telemetry',
        color: this.colors.brandGold,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('action_dispatch').x + 58, n('action_dispatch').y, n('action_dispatch').z),
          new THREE.Vector3(650, 40, 0),
          new THREE.Vector3(n('telemetry_log').x - 30, n('telemetry_log').y - 30, n('telemetry_log').z)
        ])
      },
      // 10. Rückführung (Feedback Infinite Loop von Action & False-Gate zurück zu Dispatcher)
      {
        id: 'p_loop_return',
        color: this.colors.brandGold,
        isFeedbackLoop: true,
        curve: new THREE.CatmullRomCurve3([
          new THREE.Vector3(n('action_dispatch').x, n('action_dispatch').y - 30, n('action_dispatch').z),
          new THREE.Vector3(440, -115, 75),
          new THREE.Vector3(180, -125, 95),
          new THREE.Vector3(-10, -95, 75),
          new THREE.Vector3(n('stream_dispatcher').x, n('stream_dispatcher').y - 31, n('stream_dispatcher').z)
        ])
      }
    ];

    // Render Tubes & Guides
    paths.forEach(p => {
      const geom = new THREE.TubeGeometry(p.curve, 64, 1.8, 8, false);
      const mat = new THREE.MeshBasicMaterial({
        color: p.color,
        transparent: true,
        opacity: p.isFeedbackLoop ? 0.35 : 0.45,
        wireframe: false
      });
      const mesh = new THREE.Mesh(geom, mat);
      this.workflowGroup.add(mesh);

      // Zarter Umhüllungs-Shader/Halo
      const glowGeom = new THREE.TubeGeometry(p.curve, 64, 3.8, 8, false);
      const glowMat = new THREE.MeshBasicMaterial({
        color: p.color,
        transparent: true,
        opacity: 0.1,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      const glowMesh = new THREE.Mesh(glowGeom, glowMat);
      this.workflowGroup.add(glowMesh);

      this.conduits.push({
        id: p.id,
        curve: p.curve,
        mesh,
        color: p.color,
        isFeedback: !!p.isFeedbackLoop,
        isVertical: !!p.isVerticalFeed
      });
    });
  }

  initDataStream() {
    // Kinetischer Datenpaket-Stream ("Der Protagonist")
    // Definition der zusammenhängenden Durchlauf-Pipelines:
    this.streamPipelines = [
      // Hauptzyklus: Ingest -> Norm -> Disp -> Vector -> Reasoning -> Gate -> Action -> Telemetry
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
      // Loop-Zyklus: Ingest -> Norm -> Disp -> Vector -> Reasoning -> Gate -> Action -> Return Loop -> Disp
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
      // Done-Bypass: Disp -> Telemetry direkt
      {
        segments: [
          'p_disp_telemetry_done'
        ]
      }
    ];

    // Sprite Texture für Orbs
    const orbCanvas = document.createElement('canvas');
    orbCanvas.width = 64;
    orbCanvas.height = 64;
    const ctx = orbCanvas.getContext('2d');
    const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
    grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
    grad.addColorStop(0.25, 'rgba(250, 204, 21, 0.9)');
    grad.addColorStop(0.65, 'rgba(184, 150, 46, 0.35)');
    grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 64, 64);
    this.orbTexture = new THREE.CanvasTexture(orbCanvas);

    // Initialisiere 7 zeitversetzte Datenpakete
    this.orbs = [];
    const orbCount = 7;
    for (let i = 0; i < orbCount; i++) {
      const isLoopStream = i % 3 === 1;
      const isDoneStream = i === 4;

      let pipeline = this.streamPipelines[0];
      if (isLoopStream) pipeline = this.streamPipelines[1];
      if (isDoneStream) pipeline = this.streamPipelines[2];

      const orbObj = this.createOrbMesh(i, pipeline, i * (1.0 / orbCount));
      this.workflowGroup.add(orbObj.group);
      this.orbs.push(orbObj);
    }

    // Anthropic Synapsen-Stream (Vertikal aufsteigende KI-Token-Impulse)
    this.aiTokens = [];
    const tokenCount = 4;
    for (let i = 0; i < tokenCount; i++) {
      const token = this.createAiToken(i, i * 0.25);
      this.workflowGroup.add(token.mesh);
      this.aiTokens.push(token);
    }
  }

  createOrbMesh(id, pipeline, progressOffset) {
    const group = new THREE.Group();

    // 1. Kern-Kugel (Pulsierendes Plasma)
    const coreGeom = new THREE.SphereGeometry(4.5, 16, 16);
    const coreMat = new THREE.MeshBasicMaterial({
      color: 0xffffff
    });
    const coreMesh = new THREE.Mesh(coreGeom, coreMat);
    group.add(coreMesh);

    // 2. Äußerer Halo Sprite
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

    // 3. Partikel-Trail (Schweif des kinetischen Protagonisten)
    const trailLength = 12;
    const trailGeom = new THREE.BufferGeometry();
    const trailPositions = new Float32Array(trailLength * 3);
    const trailColors = new Float32Array(trailLength * 3);

    for (let i = 0; i < trailLength; i++) {
      trailPositions[i * 3] = 0;
      trailPositions[i * 3 + 1] = 0;
      trailPositions[i * 3 + 2] = 0;

      const alpha = 1.0 - (i / trailLength);
      trailColors[i * 3] = 0.8 * alpha;
      trailColors[i * 3 + 1] = 0.9 * alpha;
      trailColors[i * 3 + 2] = 1.0 * alpha;
    }

    trailGeom.setAttribute('position', new THREE.BufferAttribute(trailPositions, 3));
    trailGeom.setAttribute('color', new THREE.BufferAttribute(trailColors, 3));

    const trailMat = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.85,
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
      segmentProgress: progressOffset,
      currentSegmentId: pipeline.segments[0],
      isTransformed: false
    };
  }

  createAiToken(id, offset) {
    const geom = new THREE.SphereGeometry(2.5, 12, 12);
    const mat = new THREE.MeshBasicMaterial({
      color: this.colors.brandGoldLight
    });
    const mesh = new THREE.Mesh(geom, mat);

    const spriteMat = new THREE.SpriteMaterial({
      map: this.orbTexture,
      color: this.colors.aiPurple,
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    });
    const sprite = new THREE.Sprite(spriteMat);
    sprite.scale.set(22, 22, 1);
    mesh.add(sprite);

    return {
      id,
      mesh,
      sprite,
      progress: offset
    };
  }

  buildHUDControls() {
    // Dark-Tech Minimalistic HUD Controls
    const hud = document.createElement('div');
    hud.id = 'workflow-3d-hud';
    hud.style.cssText = `
      position: absolute;
      bottom: 24px;
      right: 28px;
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(14, 17, 24, 0.75);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(184, 150, 46, 0.35);
      border-radius: 8px;
      padding: 8px 14px;
      font-family: 'Instrument Sans', system-ui, sans-serif;
      font-size: 11px;
      color: #D4B86A;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);
      user-select: none;
    `;

    hud.innerHTML = `
      <div style="display:flex;align-items:center;gap:6px;padding-right:8px;border-right:1px solid rgba(255,255,255,0.12)">
        <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e"></span>
        <span style="font-weight:600;letter-spacing:0.06em;color:#fff">LIVE 60FPS</span>
      </div>
      <button id="wf3d-btn-play" style="background:transparent;border:none;color:#fff;cursor:pointer;display:flex;align-items:center;gap:4px;font-size:11px;font-weight:600;padding:4px 8px;border-radius:4px;transition:background 0.2s">
        <span id="wf3d-icon-play">⏸ PAUSE</span>
      </button>
      <div style="display:flex;align-items:center;gap:4px">
        <button class="wf3d-spd" data-spd="0.5" style="background:transparent;border:1px solid rgba(212,184,106,0.3);color:#D4B86A;cursor:pointer;padding:2px 6px;border-radius:3px;font-size:10px">0.5x</button>
        <button class="wf3d-spd active" data-spd="1.0" style="background:#B8962E;border:1px solid #B8962E;color:#fff;cursor:pointer;padding:2px 6px;border-radius:3px;font-size:10px;font-weight:bold">1.0x</button>
        <button class="wf3d-spd" data-spd="2.0" style="background:transparent;border:1px solid rgba(212,184,106,0.3);color:#D4B86A;cursor:pointer;padding:2px 6px;border-radius:3px;font-size:10px">2.0x</button>
      </div>
      <button id="wf3d-btn-reset" title="Kamera zurücksetzen" style="background:transparent;border:none;color:rgba(255,255,255,0.6);cursor:pointer;padding:4px;font-size:11px;transition:color 0.2s">
        ↺ RESET
      </button>
    `;

    this.container.style.position = 'relative';
    this.container.appendChild(hud);

    // Event Bindings
    const playBtn = hud.querySelector('#wf3d-btn-play');
    const playIcon = hud.querySelector('#wf3d-icon-play');
    playBtn.addEventListener('click', () => {
      this.options.isPlaying = !this.options.isPlaying;
      playIcon.textContent = this.options.isPlaying ? '⏸ PAUSE' : '▶ PLAY';
      playBtn.style.color = this.options.isPlaying ? '#fff' : '#D4B86A';
    });

    hud.querySelectorAll('.wf3d-spd').forEach(btn => {
      btn.addEventListener('click', () => {
        hud.querySelectorAll('.wf3d-spd').forEach(b => {
          b.style.background = 'transparent';
          b.style.color = '#D4B86A';
          b.style.fontWeight = 'normal';
        });
        btn.style.background = '#B8962E';
        btn.style.color = '#fff';
        btn.style.fontWeight = 'bold';
        this.options.speed = parseFloat(btn.dataset.spd);
      });
    });

    hud.querySelector('#wf3d-btn-reset').addEventListener('click', () => {
      this.mouse.targetX = 0;
      this.mouse.targetY = 0;
      this.camera.position.copy(this.baseCameraPos);
      this.camera.lookAt(this.cameraTarget);
    });
  }

  bindEvents() {
    this.onWindowResize = () => {
      if (!this.container) return;
      const w = this.container.clientWidth;
      const h = this.container.clientHeight;
      this.camera.aspect = w / h;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(w, h);
    };
    window.addEventListener('resize', this.onWindowResize);

    // Mouse Parallax
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

    const baseSpeed = 0.38 * this.options.speed;

    // 1. Kinetic Protagonist Orbs
    this.orbs.forEach(orb => {
      orb.segmentProgress += baseSpeed * delta;

      // Segment-Übergang prüfen
      if (orb.segmentProgress >= 1.0) {
        orb.segmentProgress = 0.0;
        orb.segmentIndex = (orb.segmentIndex + 1) % orb.pipeline.segments.length;
        orb.currentSegmentId = orb.pipeline.segments[orb.segmentIndex];

        // Trigger Node Pulse bei Erreichen der Station
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

      // Aktuelle Kurve abfragen
      const conduit = this.conduits.find(c => c.id === orb.currentSegmentId);
      if (conduit) {
        const pos = conduit.curve.getPointAt(orb.segmentProgress);
        orb.group.position.copy(pos);

        // Transformation beim Durchqueren der Reasoning Engine:
        // Von Rohdaten (Cyan) zu High-Tier Stefan Wurzer Gold (#D4B86A / #FFE8A3)
        const isPostReasoning = [
          'p_reasoning_gate',
          'p_gate_action',
          'p_action_telemetry',
          'p_loop_return'
        ].includes(orb.currentSegmentId);

        if (isPostReasoning && !orb.isTransformed) {
          orb.isTransformed = true;
          orb.spriteMat.color.setHex(this.colors.synthesizedGold);
          orb.coreMesh.material.color.setHex(0xffffff);
        } else if (!isPostReasoning && orb.isTransformed) {
          orb.isTransformed = false;
          orb.spriteMat.color.setHex(this.colors.rawCyan);
        }

        // Orb Pulsieren
        const pulse = 1.0 + Math.sin(this.clock.getElapsedTime() * 8 + orb.id) * 0.18;
        orb.sprite.scale.set(38 * pulse, 38 * pulse, 1);

        // Trail Historie updaten
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

    // 2. Anthropic Vertikale Synapsen-Impulse
    const anthropicConduit = this.conduits.find(c => c.id === 'p_anthropic_reasoning');
    if (anthropicConduit) {
      this.aiTokens.forEach(token => {
        token.progress = (token.progress + delta * 0.65 * this.options.speed) % 1.0;
        const pos = anthropicConduit.curve.getPointAt(token.progress);
        token.mesh.position.copy(pos);

        // Skalierung mit zunehmender Höhe in die Reasoning Engine
        const s = 1.0 + token.progress * 0.5;
        token.mesh.scale.set(s, s, s);
      });
    }
  }

  animate() {
    this.animationFrameId = requestAnimationFrame(this.animate);

    const delta = this.clock.getDelta();
    const time = this.clock.getElapsedTime();

    // 1. Mouse Parallax Lerping
    this.mouse.x += (this.mouse.targetX - this.mouse.x) * 0.045;
    this.mouse.y += (this.mouse.targetY - this.mouse.y) * 0.045;

    this.camera.position.x = this.baseCameraPos.x + this.mouse.x * 65;
    this.camera.position.y = this.baseCameraPos.y - this.mouse.y * 45;
    this.camera.lookAt(this.cameraTarget);

    // 2. Nodes animieren (Pulsen abklingen lassen, zarte Schwebung)
    this.nodes.forEach(n => {
      // Dämpfung nach Impuls
      n.mesh.scale.lerp(n.baseScale, 0.08);
      const targetOpacity = n.cfg.isHero ? 0.85 : 0.45;
      n.edgeLines.material.opacity += (targetOpacity - n.edgeLines.material.opacity) * 0.08;

      // Ganz subtiles kosmisches Schweben
      n.mesh.position.y = n.cfg.pos.y + Math.sin(time * 1.5 + n.mesh.position.x * 0.02) * 1.5;
    });

    // 3. Kinetische Datenströme
    this.updateDataStream(delta);

    // 4. Ambient Partikel Drift
    if (this.ambientParticles) {
      this.ambientParticles.rotation.y = time * 0.015;
    }

    // 5. Focal Light Pulsieren
    if (this.coreLight) {
      this.coreLight.intensity = 2.2 + Math.sin(time * 3) * 0.4;
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
    const hud = document.getElementById('workflow-3d-hud');
    if (hud) hud.remove();
  }
}
