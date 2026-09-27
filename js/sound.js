/**
 * Tantra Gyan Vedic Astrology Book - Procedural Web Audio Sound Engine
 * Synthesizes authentic, crisp physical paper page-turn sound effects
 * without any external audio files or network dependencies.
 */

class BookSoundEngine {
  constructor() {
    this.audioCtx = null;
    this.isMuted = false;
    this.volume = 0.65;
    this.initialized = false;
    
    // Check saved audio preference
    try {
      const savedMute = localStorage.getItem('tantra_book_muted');
      if (savedMute !== null) this.isMuted = savedMute === 'true';
      const savedVol = localStorage.getItem('tantra_book_volume');
      if (savedVol !== null) this.volume = parseFloat(savedVol);
    } catch (e) {
      console.warn('Storage not accessible for audio settings');
    }
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
   * Generates a realistic paper flip sound
   * @param {string} direction - 'next' or 'prev'
   */
  playPageTurn(direction = 'next') {
    if (this.isMuted) return;
    this.init();
    if (!this.audioCtx) return;

    try {
      const now = this.audioCtx.currentTime;
      const duration = 0.35; // 350ms natural flip

      // 1. Noise buffer for paper texture & friction
      const bufferSize = this.audioCtx.sampleRate * duration;
      const noiseBuffer = this.audioCtx.createBuffer(1, bufferSize, this.audioCtx.sampleRate);
      const output = noiseBuffer.getChannelData(0);
      let lastOut = 0.0;
      
      // Pink / Brown noise synthesis for realistic paper fiber friction
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        output[i] = (lastOut + (0.02 * white)) / 1.02;
        lastOut = output[i];
        output[i] *= 3.5; // Gain boost
      }

      const noiseSource = this.audioCtx.createBufferSource();
      noiseSource.buffer = noiseBuffer;

      // 2. Dynamic Bandpass filter to simulate page moving through air
      const filter = this.audioCtx.createBiquadFilter();
      filter.type = 'bandpass';
      filter.Q.setValueAtTime(2.2, now);

      if (direction === 'next') {
        filter.frequency.setValueAtTime(1400, now);
        filter.frequency.exponentialRampToValueAtTime(700, now + duration * 0.7);
        filter.frequency.exponentialRampToValueAtTime(350, now + duration);
      } else {
        filter.frequency.setValueAtTime(800, now);
        filter.frequency.exponentialRampToValueAtTime(1300, now + duration * 0.6);
        filter.frequency.exponentialRampToValueAtTime(450, now + duration);
      }

      // 3. Amplitude envelope: fast swish attack, fluttering body, soft paper drop release
      const gainNode = this.audioCtx.createGain();
      gainNode.gain.setValueAtTime(0.001, now);
      // Fast attack
      gainNode.gain.linearRampToValueAtTime(this.volume * 0.8, now + 0.04);
      // Subtle paper flutter midpoint
      gainNode.gain.linearRampToValueAtTime(this.volume * 0.95, now + 0.12);
      // Decay & soft settle
      gainNode.gain.exponentialRampToValueAtTime(0.01, now + duration);

      // 4. Subtle low-frequency thud for book page resting down
      const thudOsc = this.audioCtx.createOscillator();
      const thudGain = this.audioCtx.createGain();
      thudOsc.type = 'sine';
      thudOsc.frequency.setValueAtTime(95, now + 0.18);
      thudOsc.frequency.exponentialRampToValueAtTime(40, now + duration);
      
      thudGain.gain.setValueAtTime(0.001, now);
      thudGain.gain.setValueAtTime(0.001, now + 0.17);
      thudGain.gain.linearRampToValueAtTime(this.volume * 0.35, now + 0.20);
      thudGain.gain.exponentialRampToValueAtTime(0.001, now + duration);

      // Connect nodes
      noiseSource.connect(filter);
      filter.connect(gainNode);
      gainNode.connect(this.audioCtx.destination);

      thudOsc.connect(thudGain);
      thudGain.connect(this.audioCtx.destination);

      // Start and schedule stop
      noiseSource.start(now);
      noiseSource.stop(now + duration);
      thudOsc.start(now + 0.17);
      thudOsc.stop(now + duration);

    } catch (e) {
      console.warn('Web Audio playback error:', e);
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
