/**
 * Tantra Gyan Vedic Astrology Book - Hyper-Realistic Procedural Paper Sound Engine
 * Synthesizes authentic, crisp physical paper page-turn sound effects:
 * 1. Edge Separation & Surface Friction (crisp high-pass paper rustle)
 * 2. Aerodynamic Air Pocket & Parchment Flutter (resonant dual bandpass sweep)
 * 3. Soft Cushion Impact & Settle (low-frequency paper landing thump & air puff)
 * With organic randomized variance across every single turn.
 */

class BookSoundEngine {
  constructor() {
    this.audioCtx = null;
    this.isMuted = false;
    this.volume = 0.85;
    this.initialized = false;
    this.unlocked = false;
    this.variationIndex = 0;
    this.silentAudio = null;
    this.audioPool = {};

    // Check saved audio preference
    try {
      const savedMute = localStorage.getItem('tantra_book_muted');
      if (savedMute !== null) this.isMuted = savedMute === 'true';
      const savedVol = localStorage.getItem('tantra_book_volume');
      if (savedVol !== null) this.volume = parseFloat(savedVol);
    } catch (e) {
      console.warn('Storage not accessible for audio settings');
    }

    this.initAudioPool();

    // Auto-warm and unlock AudioContext and HTML5 audio on any user interaction across all mobile & desktop browsers
    const unlockHandler = () => {
      this.unlockAllAudio();
    };

    ['touchstart', 'touchend', 'click', 'pointerdown', 'keydown'].forEach(evt => {
      document.addEventListener(evt, unlockHandler, { passive: true });
      window.addEventListener(evt, unlockHandler, { passive: true });
    });
  }

  initAudioPool() {
    if (typeof window !== 'undefined' && window.BOOK_SOUND_DATA) {
      ['fwd', 'bwd', 'open', 'close'].forEach(key => {
        if (window.BOOK_SOUND_DATA[key]) {
          try {
            // Create a pool of 2 HTML5 audio elements per sound to allow overlapping turns
            this.audioPool[key] = [
              new Audio(window.BOOK_SOUND_DATA[key]),
              new Audio(window.BOOK_SOUND_DATA[key])
            ];
            this.audioPool[key].forEach(a => {
              a.preload = 'auto';
              a.volume = this.volume;
            });
          } catch (e) {
            console.warn('Audio pool initialization error:', e);
          }
        }
      });
    }
  }

  unlockAllAudio() {
    // 1. Prime HTML5 Audio Pool (unlocks iOS Safari audio playback restriction)
    if (!this.unlocked && this.audioPool) {
      this.unlocked = true;
      Object.keys(this.audioPool).forEach(key => {
        const list = this.audioPool[key];
        if (Array.isArray(list) && list[0]) {
          try {
            list[0].volume = 0;
            const p = list[0].play();
            if (p && typeof p.then === 'function') {
              p.then(() => {
                list[0].pause();
                list[0].currentTime = 0;
                list[0].volume = this.volume;
              }).catch(() => {});
            }
          } catch (e) {}
        }
      });
    }

    // 2. Unlock Web Audio Context
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!this.audioCtx && AudioContextClass) {
      try {
        this.audioCtx = new AudioContextClass();
        this.initialized = true;
      } catch (e) {}
    }

    if (this.audioCtx) {
      if (this.audioCtx.state === 'suspended') {
        this.audioCtx.resume().catch(() => {});
      }
    }
  }

  playNativeClip(soundName) {
    if (this.isMuted) return false;
    // Re-check pool in case sounds-data.js loaded after instance creation
    if (!this.audioPool[soundName] && typeof window !== 'undefined' && window.BOOK_SOUND_DATA) {
      this.initAudioPool();
    }
    const pool = this.audioPool ? this.audioPool[soundName] : null;
    if (pool && pool.length > 0) {
      let audioToPlay = pool.find(a => a.paused || a.ended);
      if (!audioToPlay) {
        audioToPlay = pool[0];
      }
      try {
        audioToPlay.currentTime = 0;
        audioToPlay.volume = this.volume;
        const playPromise = audioToPlay.play();
        if (playPromise !== undefined) {
          playPromise.catch(err => {
            // Autoplay policy or gesture required
          });
        }
        return true;
      } catch (e) {
        return false;
      }
    }
    return false;
  }

  init() {
    this.unlockAllAudio();
  }

  playPageTurn(direction = 'next') {
    if (this.isMuted) return;
    this.unlockAllAudio();

    const clipKey = direction === 'prev' ? 'bwd' : 'fwd';
    const isContextActive = this.audioCtx && this.audioCtx.state === 'running';

    // If Web Audio API isn't active/unlocked yet, play the pre-rendered smooth paper rustle clip
    if (!isContextActive) {
      this.playNativeClip(clipKey);
    }

    // Synthesized Web Audio API paper turn for rich layered spatial ambience
    if (!this.audioCtx) return;

    try {
      const now = Math.max(this.audioCtx.currentTime, 0.005);
      const duration = 0.52; // 520ms natural flip, matching 540ms/560ms 3D leaf turn

      // Organic variation factor (shifts pitch & filter characteristics slightly)
      this.variationIndex = (this.variationIndex + 1) % 3;
      const variations = [
        { freqMult: 1.0,  qMult: 1.0,  thudPitch: 75, frictionCutoff: 3400 },
        { freqMult: 1.08, qMult: 1.15, thudPitch: 82, frictionCutoff: 3800 },
        { freqMult: 0.94, qMult: 0.92, thudPitch: 68, frictionCutoff: 3100 }
      ];
      const curVar = variations[this.variationIndex];

      // ----------------------------------------------------------------------
      // 1. Noise Generator for Paper Texture & Fiber Friction
      // ----------------------------------------------------------------------
      const bufferSize = Math.floor(this.audioCtx.sampleRate * duration);
      const noiseBuffer = this.audioCtx.createBuffer(1, bufferSize, this.audioCtx.sampleRate);
      const output = noiseBuffer.getChannelData(0);
      let lastOut = 0.0;
      
      // Filtered Pink + White Noise with granular paper flutter
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        // Pink noise filter integration
        lastOut = (lastOut + (0.02 * white)) / 1.02;
        // Granular paper micro-flutter amplitude modulation (around 35Hz-45Hz)
        const t = i / this.audioCtx.sampleRate;
        const flutter = 0.74 + 0.26 * mathSin(2 * Math.PI * 38 * t + 0.7 * mathSin(2 * Math.PI * 12 * t));
        output[i] = (lastOut * 2.8 + white * 0.40) * flutter;
      }

      function mathSin(val) { return Math.sin(val); }

      const noiseSource = this.audioCtx.createBufferSource();
      noiseSource.buffer = noiseBuffer;

      // ----------------------------------------------------------------------
      // 2. Layer A: High-Frequency Edge Separation Rustle (0 to 140ms)
      // ----------------------------------------------------------------------
      const frictionFilter = this.audioCtx.createBiquadFilter();
      frictionFilter.type = 'highpass';
      frictionFilter.frequency.setValueAtTime(curVar.frictionCutoff, now);
      frictionFilter.Q.setValueAtTime(1.15, now);

      const frictionGain = this.audioCtx.createGain();
      frictionGain.gain.setValueAtTime(0.0001, now);
      // Gentle whisper ramp as leaf lifts
      frictionGain.gain.linearRampToValueAtTime(this.volume * 0.38, now + 0.08);
      frictionGain.gain.exponentialRampToValueAtTime(this.volume * 0.16, now + 0.20);
      frictionGain.gain.exponentialRampToValueAtTime(0.0001, now + 0.30);

      // ----------------------------------------------------------------------
      // 3. Layer B: Aerodynamic Resonant Body Swish & Air Displacement (0 to 500ms)
      // ----------------------------------------------------------------------
      const bodyFilter = this.audioCtx.createBiquadFilter();
      bodyFilter.type = 'bandpass';
      bodyFilter.Q.setValueAtTime(3.0 * curVar.qMult, now);

      if (direction === 'next') {
        // Page moves right to left: starts high, opens cavity, lowers pitch
        bodyFilter.frequency.setValueAtTime(2200 * curVar.freqMult, now);
        bodyFilter.frequency.exponentialRampToValueAtTime(1200 * curVar.freqMult, now + 0.25);
        bodyFilter.frequency.exponentialRampToValueAtTime(420 * curVar.freqMult, now + 0.48);
      } else {
        // Page moves left to right
        bodyFilter.frequency.setValueAtTime(650 * curVar.freqMult, now);
        bodyFilter.frequency.exponentialRampToValueAtTime(1600 * curVar.freqMult, now + 0.25);
        bodyFilter.frequency.exponentialRampToValueAtTime(460 * curVar.freqMult, now + 0.48);
      }

      const bodyGain = this.audioCtx.createGain();
      bodyGain.gain.setValueAtTime(0.0001, now);
      // Swells as page arches vertically across center (peaks around 250ms)
      bodyGain.gain.linearRampToValueAtTime(this.volume * 0.65, now + 0.12);
      bodyGain.gain.linearRampToValueAtTime(this.volume * 0.85, now + 0.25);
      bodyGain.gain.exponentialRampToValueAtTime(0.01, now + 0.46);
      bodyGain.gain.linearRampToValueAtTime(0.0001, now + 0.51);

      // ----------------------------------------------------------------------
      // 4. Layer C: Soft Paper Landing Impact & Air Puff (380ms to 520ms)
      // ----------------------------------------------------------------------
      const thudOsc = this.audioCtx.createOscillator();
      const thudGain = this.audioCtx.createGain();
      const thudFilter = this.audioCtx.createBiquadFilter();

      thudOsc.type = 'sine';
      thudFilter.type = 'lowpass';
      thudFilter.frequency.setValueAtTime(170, now + 0.38);

      thudOsc.frequency.setValueAtTime(curVar.thudPitch, now + 0.38);
      thudOsc.frequency.exponentialRampToValueAtTime(35, now + duration);

      thudGain.gain.setValueAtTime(0.0001, now);
      thudGain.gain.setValueAtTime(0.0001, now + 0.38);
      // Soft cushion arrival
      thudGain.gain.linearRampToValueAtTime(this.volume * 0.40, now + 0.44);
      thudGain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      const isMobileDevice = window.innerWidth <= 860 || /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

      // Directional Spatial Stereo Panning (Desktop only)
      let panner = null;
      if (!isMobileDevice && this.audioCtx.createStereoPanner) {
        try {
          panner = this.audioCtx.createStereoPanner();
          if (direction === 'next') {
            // Sweeps from Right (+0.35) across spine to Left (-0.35)
            panner.pan.setValueAtTime(0.35, now);
            panner.pan.linearRampToValueAtTime(-0.35, now + duration);
          } else {
            // Sweeps from Left (-0.35) across spine to Right (+0.35)
            panner.pan.setValueAtTime(-0.35, now);
            panner.pan.linearRampToValueAtTime(0.35, now + duration);
          }
        } catch (pe) {
          panner = null;
        }
      }

      // Master output limiter
      const masterGain = this.audioCtx.createGain();
      masterGain.gain.setValueAtTime(1.0, now);

      // Route Audio Graph
      noiseSource.connect(frictionFilter);
      frictionFilter.connect(frictionGain);
      frictionGain.connect(masterGain);

      noiseSource.connect(bodyFilter);
      bodyFilter.connect(bodyGain);
      bodyGain.connect(masterGain);

      thudOsc.connect(thudFilter);
      thudFilter.connect(thudGain);
      thudGain.connect(masterGain);

      if (panner) {
        masterGain.connect(panner);
        panner.connect(this.audioCtx.destination);
      } else {
        masterGain.connect(this.audioCtx.destination);
      }

      // Start sound sources
      noiseSource.start(now);
      noiseSource.stop(now + duration);
      thudOsc.start(now + 0.38);
      thudOsc.stop(now + duration);

    } catch (e) {
      console.warn('Web Audio playback error:', e);
    }
  }

  /**
   * Generates a sacred celestial harmonic aura resonance (108Hz / 432Hz)
   */
  playCosmicAura() {
    if (this.isMuted) return;
    this.init();
    if (!this.audioCtx) return;

    try {
      const now = this.audioCtx.currentTime;
      const duration = 1.4;
      
      const osc1 = this.audioCtx.createOscillator();
      const osc2 = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();
      const filter = this.audioCtx.createBiquadFilter();

      osc1.type = 'sine';
      osc1.frequency.setValueAtTime(108, now);
      osc1.frequency.exponentialRampToValueAtTime(162, now + duration * 0.6);
      osc1.frequency.exponentialRampToValueAtTime(108, now + duration);

      osc2.type = 'sine';
      osc2.frequency.setValueAtTime(432, now);
      osc2.frequency.exponentialRampToValueAtTime(436, now + duration * 0.4);
      osc2.frequency.exponentialRampToValueAtTime(432, now + duration);

      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(750, now);

      gain.gain.setValueAtTime(0.0001, now);
      gain.gain.linearRampToValueAtTime(this.volume * 0.28, now + 0.22);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      osc1.connect(filter);
      osc2.connect(filter);
      filter.connect(gain);
      gain.connect(this.audioCtx.destination);

      osc1.start(now);
      osc2.start(now);
      osc1.stop(now + duration);
      osc2.stop(now + duration);
    } catch (e) {
      console.warn('Cosmic audio error:', e);
    }
  }

  /**
   * Generates a deep, rich physical hardcover book opening sound with cosmic aura
   */
  playBookOpen() {
    if (this.isMuted) return;
    this.unlockAllAudio();

    const isContextActive = this.audioCtx && this.audioCtx.state === 'running';
    if (!isContextActive) {
      this.playNativeClip('open');
    }

    if (!this.audioCtx) return;

    try {
      const now = this.audioCtx.currentTime;
      const duration = 0.65;
      
      // Resonant leather/spine opening sweep
      const osc = this.audioCtx.createOscillator();
      const oscGain = this.audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(50, now);
      osc.frequency.exponentialRampToValueAtTime(115, now + 0.20);
      osc.frequency.exponentialRampToValueAtTime(42, now + duration);

      oscGain.gain.setValueAtTime(0.0001, now);
      oscGain.gain.linearRampToValueAtTime(this.volume * 0.42, now + 0.12);
      oscGain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      osc.connect(oscGain);
      oscGain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + duration);

      // Cosmic sacred overtone shimmer
      this.playCosmicAura();
    } catch (e) {
      console.warn('Audio open error:', e);
    }
  }

  /**
   * Generates a deep, satisfying hardcover book closing thud and snap
   */
  playBookClose() {
    if (this.isMuted) return;
    this.unlockAllAudio();

    const isContextActive = this.audioCtx && this.audioCtx.state === 'running';
    if (!isContextActive) {
      this.playNativeClip('close');
    }

    if (!this.audioCtx) return;

    try {
      const now = this.audioCtx.currentTime;
      const duration = 0.65;
      
      // Settling impact at close (around 460ms into the 650ms animation)
      const impactTime = now + 0.46;
      const thudOsc = this.audioCtx.createOscillator();
      const thudGain = this.audioCtx.createGain();
      thudOsc.type = 'triangle';
      thudOsc.frequency.setValueAtTime(88, impactTime);
      thudOsc.frequency.exponentialRampToValueAtTime(35, impactTime + 0.18);

      thudGain.gain.setValueAtTime(0.0001, impactTime);
      thudGain.gain.linearRampToValueAtTime(this.volume * 0.62, impactTime + 0.02);
      thudGain.gain.exponentialRampToValueAtTime(0.0001, impactTime + 0.18);

      thudOsc.connect(thudGain);
      thudGain.connect(this.audioCtx.destination);
      thudOsc.start(impactTime);
      thudOsc.stop(impactTime + 0.18);
    } catch (e) {
      console.warn('Audio close error:', e);
    }
  }

  toggleMute() {
    this.isMuted = !this.isMuted;
    try {
      localStorage.setItem('tantra_book_muted', this.isMuted.toString());
    } catch (e) {}

    if (this.isMuted && this.audioPool) {
      Object.keys(this.audioPool).forEach(key => {
        const list = this.audioPool[key];
        if (Array.isArray(list)) {
          list.forEach(a => {
            try {
              a.pause();
              a.currentTime = 0;
            } catch (e) {}
          });
        }
      });
    }
    return this.isMuted;
  }

  setVolume(vol) {
    this.volume = Math.max(0, Math.min(1, vol));
    try {
      localStorage.setItem('tantra_book_volume', this.volume.toString());
    } catch (e) {}

    if (this.audioPool) {
      Object.keys(this.audioPool).forEach(key => {
        const list = this.audioPool[key];
        if (Array.isArray(list)) {
          list.forEach(a => {
            a.volume = this.volume;
          });
        }
      });
    }
  }
}

// Global instance ready for UI binding
window.bookSound = new BookSoundEngine();
