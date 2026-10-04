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
    this.volume = 0.75;
    this.initialized = false;
    this.variationIndex = 0;

    // Check saved audio preference
    try {
      const savedMute = localStorage.getItem('tantra_book_muted');
      if (savedMute !== null) this.isMuted = savedMute === 'true';
      const savedVol = localStorage.getItem('tantra_book_volume');
      if (savedVol !== null) this.volume = parseFloat(savedVol);
    } catch (e) {
      console.warn('Storage not accessible for audio settings');
    }

    // Auto-warm AudioContext on first touch/click anywhere on document
    const unlockAudio = () => {
      this.init();
      document.removeEventListener('pointerdown', unlockAudio);
      document.removeEventListener('keydown', unlockAudio);
    };
    document.addEventListener('pointerdown', unlockAudio, { passive: true });
    document.addEventListener('keydown', unlockAudio, { passive: true });
  }

  init() {
    if (!this.initialized) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        this.audioCtx = new AudioContextClass();
        this.initialized = true;
      }
    }
    if (this.audioCtx && this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
  }

  /**
   * Generates a realistic physical paper page turn sound
   * @param {string} direction - 'next' or 'prev'
   */
  playPageTurn(direction = 'next') {
    if (this.isMuted) return;
    this.init();
    if (!this.audioCtx) return;

    try {
      const now = this.audioCtx.currentTime;
      const duration = 0.52; // 520ms natural flip, matching 540ms 3D leaf turn

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
        // Granular paper micro-flutter amplitude modulation (around 32Hz-55Hz)
        const t = i / this.audioCtx.sampleRate;
        const flutter = 0.72 + 0.28 * Math.sin(2 * Math.PI * 38 * t + Math.sin(2 * Math.PI * 11 * t));
        output[i] = (lastOut * 2.8 + white * 0.45) * flutter;
      }

      const noiseSource = this.audioCtx.createBufferSource();
      noiseSource.buffer = noiseBuffer;

      // ----------------------------------------------------------------------
      // 2. Layer A: High-Frequency Edge Separation Rustle (0 to 140ms)
      // ----------------------------------------------------------------------
      const frictionFilter = this.audioCtx.createBiquadFilter();
      frictionFilter.type = 'highpass';
      frictionFilter.frequency.setValueAtTime(curVar.frictionCutoff, now);
      frictionFilter.Q.setValueAtTime(1.2, now);

      const frictionGain = this.audioCtx.createGain();
      frictionGain.gain.setValueAtTime(0.001, now);
      // Fast tactile grab & lift attack
      frictionGain.gain.linearRampToValueAtTime(this.volume * 0.45, now + 0.025);
      // Gentle flutter decay
      frictionGain.gain.exponentialRampToValueAtTime(this.volume * 0.15, now + 0.12);
      frictionGain.gain.exponentialRampToValueAtTime(0.001, now + 0.22);

      // ----------------------------------------------------------------------
      // 3. Layer B: Aerodynamic Resonant Body Swish & Air Displacement (0 to 450ms)
      // ----------------------------------------------------------------------
      const bodyFilter = this.audioCtx.createBiquadFilter();
      bodyFilter.type = 'bandpass';
      bodyFilter.Q.setValueAtTime(3.2 * curVar.qMult, now);

      if (direction === 'next') {
        // Page moves right to left: starts high, opens cavity, lowers pitch
        bodyFilter.frequency.setValueAtTime(2100 * curVar.freqMult, now);
        bodyFilter.frequency.exponentialRampToValueAtTime(1150 * curVar.freqMult, now + 0.24);
        bodyFilter.frequency.exponentialRampToValueAtTime(420 * curVar.freqMult, now + 0.46);
      } else {
        // Page moves left to right
        bodyFilter.frequency.setValueAtTime(650 * curVar.freqMult, now);
        bodyFilter.frequency.exponentialRampToValueAtTime(1600 * curVar.freqMult, now + 0.22);
        bodyFilter.frequency.exponentialRampToValueAtTime(460 * curVar.freqMult, now + 0.46);
      }

      const bodyGain = this.audioCtx.createGain();
      bodyGain.gain.setValueAtTime(0.001, now);
      bodyGain.gain.linearRampToValueAtTime(this.volume * 0.75, now + 0.07);
      bodyGain.gain.linearRampToValueAtTime(this.volume * 0.85, now + 0.22);
      bodyGain.gain.exponentialRampToValueAtTime(0.01, now + 0.46);
      bodyGain.gain.linearRampToValueAtTime(0.0001, now + 0.50);

      // ----------------------------------------------------------------------
      // 4. Layer C: Soft Paper Landing Impact & Air Puff (380ms to 520ms)
      // ----------------------------------------------------------------------
      const thudOsc = this.audioCtx.createOscillator();
      const thudGain = this.audioCtx.createGain();
      const thudFilter = this.audioCtx.createBiquadFilter();

      thudOsc.type = 'sine';
      thudFilter.type = 'lowpass';
      thudFilter.frequency.setValueAtTime(180, now + 0.36);

      thudOsc.frequency.setValueAtTime(curVar.thudPitch, now + 0.36);
      thudOsc.frequency.exponentialRampToValueAtTime(36, now + duration);

      thudGain.gain.setValueAtTime(0.0001, now);
      thudGain.gain.setValueAtTime(0.0001, now + 0.36);
      // Soft cushion arrival
      thudGain.gain.linearRampToValueAtTime(this.volume * 0.42, now + 0.40);
      thudGain.gain.exponentialRampToValueAtTime(0.001, now + duration);

      // Directional Spatial Stereo Panning (Opposite stereo trajectory)
      let panner = null;
      if (this.audioCtx.createStereoPanner) {
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
      thudOsc.start(now + 0.36);
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
      gain.gain.linearRampToValueAtTime(this.volume * 0.28, now + 0.25);
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
    this.init();
    if (!this.audioCtx) return;

    try {
      const now = this.audioCtx.currentTime;
      const duration = 0.65;
      
      // Resonant leather/spine opening sweep
      const osc = this.audioCtx.createOscillator();
      const oscGain = this.audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(50, now);
      osc.frequency.exponentialRampToValueAtTime(115, now + 0.22);
      osc.frequency.exponentialRampToValueAtTime(42, now + duration);

      oscGain.gain.setValueAtTime(0.001, now);
      oscGain.gain.linearRampToValueAtTime(this.volume * 0.42, now + 0.12);
      oscGain.gain.exponentialRampToValueAtTime(0.001, now + duration);

      osc.connect(oscGain);
      oscGain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + duration);

      // Cosmic sacred overtone shimmer
      this.playCosmicAura();

      // Organic paper rustle layer
      this.playPageTurn('next');
    } catch (e) {
      console.warn('Audio open error:', e);
    }
  }

  /**
   * Generates a deep, satisfying hardcover book closing thud and snap
   */
  playBookClose() {
    if (this.isMuted) return;
    this.init();
    if (!this.audioCtx) return;

    try {
      const now = this.audioCtx.currentTime;
      const duration = 0.65;
      
      // Initial swing paper whoosh
      this.playPageTurn('prev');

      // Heavy settling impact at close (around 460ms into the 650ms animation)
      const impactTime = now + 0.46;
      const thudOsc = this.audioCtx.createOscillator();
      const thudGain = this.audioCtx.createGain();
      thudOsc.type = 'triangle';
      thudOsc.frequency.setValueAtTime(90, impactTime);
      thudOsc.frequency.exponentialRampToValueAtTime(35, impactTime + 0.18);

      thudGain.gain.setValueAtTime(0.001, impactTime);
      thudGain.gain.linearRampToValueAtTime(this.volume * 0.65, impactTime + 0.02);
      thudGain.gain.exponentialRampToValueAtTime(0.001, impactTime + 0.18);

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
    return this.isMuted;
  }

  setVolume(vol) {
    this.volume = Math.max(0, Math.min(1, vol));
    try {
      localStorage.setItem('tantra_book_volume', this.volume.toString());
    } catch (e) {}
  }
}

// Global instance ready for UI binding
window.bookSound = new BookSoundEngine();
