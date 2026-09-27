/**
 * Tantra Gyan Vedic Astrology Book - User Interface Controller
 * Manages Table of Contents, Theme Switching, Dual/Single Page mode,
 * Bilingual/Language filtering, Font scaling, Fullscreen, and Real-time Search.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Sound and Engine
  if (window.bookEngine) {
    window.bookEngine.init();
  }

  // 1. Theme Management
  const themeBtn = document.getElementById('btn-theme-toggle');
  const themes = ['parchment', 'dark', 'light'];
  let currentThemeIdx = 0;

  try {
    const savedTheme = localStorage.getItem('tantra_book_theme');
    if (savedTheme && themes.includes(savedTheme)) {
      currentThemeIdx = themes.indexOf(savedTheme);
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeButtonLabel(savedTheme);
    }
  } catch (e) {}

  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      currentThemeIdx = (currentThemeIdx + 1) % themes.length;
      const nextTheme = themes[currentThemeIdx];
      document.documentElement.setAttribute('data-theme', nextTheme);
      updateThemeButtonLabel(nextTheme);
      try {
        localStorage.setItem('tantra_book_theme', nextTheme);
      } catch (e) {}
    });
  }

  function updateThemeButtonLabel(t) {
    if (!themeBtn) return;
    if (t === 'dark') {
      themeBtn.innerHTML = '<span>🌌</span> <span>रात्रि</span>';
      themeBtn.title = 'Switch to Light Theme';
    } else if (t === 'light') {
      themeBtn.innerHTML = '<span>📄</span> <span>श्वेत</span>';
      themeBtn.title = 'Switch to Parchment Theme';
    } else {
      themeBtn.innerHTML = '<span>📜</span> <span>भोजपत्र</span>';
      themeBtn.title = 'Switch to Dark Theme';
    }
  }

  // 2. Language Mode Switcher (Hindi / English / Bilingual)
  const langBtns = document.querySelectorAll('.lang-btn');
  try {
    const savedLang = localStorage.getItem('tantra_book_lang') || 'bilingual';
    setLanguageMode(savedLang);
  } catch (e) {}

  langBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = btn.getAttribute('data-lang');
      setLanguageMode(mode);
    });
  });

  function setLanguageMode(mode) {
    document.documentElement.setAttribute('data-lang-mode', mode);
    langBtns.forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-lang') === mode);
    });
    try {
      localStorage.setItem('tantra_book_lang', mode);
    } catch (e) {}
  }

  // 3. Dual Page Spread vs Single Page Mode Toggle
  const layoutBtn = document.getElementById('btn-layout-toggle');
  if (layoutBtn) {
    layoutBtn.addEventListener('click', () => {
      const isSingle = document.documentElement.classList.toggle('single-mode-active');
      layoutBtn.innerHTML = isSingle ? '<span>📄</span> <span>एकल पृष्ठ</span>' : '<span>📖</span> <span>दो पृष्ठ</span>';
      layoutBtn.title = isSingle ? 'Switch to Two-Page Spread' : 'Switch to Single Page View';
      if (window.bookEngine) {
        window.bookEngine.updateSpreadMode();
        window.bookEngine.render();
      }
    });
  }

  // 4. Sound Mute Toggle
  const soundBtn = document.getElementById('btn-sound-toggle');
  if (soundBtn && window.bookSound) {
    updateSoundBtnState();
    soundBtn.addEventListener('click', () => {
      window.bookSound.toggleMute();
      updateSoundBtnState();
      // Play brief test rustle if unmuting
      if (!window.bookSound.isMuted) {
        window.bookSound.playPageTurn('next');
      }
    });
  }

  function updateSoundBtnState() {
    if (!soundBtn || !window.bookSound) return;
    if (window.bookSound.isMuted) {
      soundBtn.innerHTML = '<span>🔇</span>';
      soundBtn.title = 'Unmute Page Turn Sound';
      soundBtn.style.opacity = '0.6';
    } else {
      soundBtn.innerHTML = '<span>🔊</span>';
      soundBtn.title = 'Mute Page Turn Sound';
      soundBtn.style.opacity = '1';
    }
  }

  // 5. Font Scale Controls
  let currentFontScale = 1.0;
  const fontDecBtn = document.getElementById('btn-font-dec');
  const fontIncBtn = document.getElementById('btn-font-inc');

  if (fontDecBtn) {
    fontDecBtn.addEventListener('click', () => {
      if (currentFontScale > 0.85) {
        currentFontScale -= 0.05;
        document.documentElement.style.setProperty('--font-scale', `${currentFontScale}rem`);
      }
    });
  }

  if (fontIncBtn) {
    fontIncBtn.addEventListener('click', () => {
      if (currentFontScale < 1.35) {
        currentFontScale += 0.05;
        document.documentElement.style.setProperty('--font-scale', `${currentFontScale}rem`);
      }
    });
  }

  // 6. Fullscreen Toggle
  const fullscreenBtn = document.getElementById('btn-fullscreen');
  if (fullscreenBtn) {
    fullscreenBtn.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          console.warn('Fullscreen request failed:', err);
        });
        fullscreenBtn.innerHTML = '<span>↙</span>';
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
          fullscreenBtn.innerHTML = '<span>⛶</span>';
        }
      }
    });
  }

  // 7. Table of Contents (TOC) Modal
  const tocBtn = document.getElementById('btn-toc-toggle');
  const tocOverlay = document.getElementById('toc-overlay');
  const tocCloseBtn = document.getElementById('toc-close-btn');

  if (tocBtn && tocOverlay) {
    tocBtn.addEventListener('click', () => {
      tocOverlay.classList.add('active');
    });

    if (tocCloseBtn) {
      tocCloseBtn.addEventListener('click', () => {
        tocOverlay.classList.remove('active');
      });
    }

    tocOverlay.addEventListener('click', (e) => {
      if (e.target === tocOverlay) {
        tocOverlay.classList.remove('active');
      }
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && tocOverlay.classList.contains('active')) {
        tocOverlay.classList.remove('active');
      }
    });

    // Delegate TOC Item Clicks
    const tocItems = tocOverlay.querySelectorAll('.toc-item');
    tocItems.forEach(item => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const targetPage = parseInt(item.getAttribute('data-goto'));
        if (targetPage && window.bookEngine) {
          window.bookEngine.goToPage(targetPage, true);
          tocOverlay.classList.remove('active');
        }
      });
    });
  }

  // 8. Real-time Search Engine across all pages
  const searchInput = document.getElementById('book-search');
  const searchCounter = document.getElementById('search-counter');
  let searchTimeout = null;

  if (searchInput && searchCounter) {
    searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      const query = e.target.value.trim().toLowerCase();

      if (!query || query.length < 2) {
        searchCounter.textContent = '';
        return;
      }

      searchTimeout = setTimeout(() => {
        performSearch(query);
      }, 300);
    });

    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const query = searchInput.value.trim().toLowerCase();
        if (query.length >= 2) {
          performSearch(query, true);
        }
      }
    });
  }

  function performSearch(query, jumpToFirst = false) {
    const rawPages = document.querySelectorAll('.book-page-data');
    let matchCount = 0;
    let firstMatchingPage = null;

    rawPages.forEach((pageEl, idx) => {
      const pageText = pageEl.textContent.toLowerCase();
      if (pageText.includes(query)) {
        matchCount++;
        if (firstMatchingPage === null) {
          firstMatchingPage = idx + 1;
        }
      }
    });

    if (matchCount > 0) {
      searchCounter.textContent = `${matchCount} pgs`;
      if (jumpToFirst && firstMatchingPage && window.bookEngine) {
        window.bookEngine.goToPage(firstMatchingPage, true);
      }
    } else {
      searchCounter.textContent = '0 found';
    }
  }
});
