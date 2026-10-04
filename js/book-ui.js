/**
 * Tantra Gyan Vedic Astrology Book - User Interface Controller
 * Features:
 * - Table of Contents (TOC) Modal
 * - Saved Bookmarks System (Modal, Toolbar Button, Silk Ribbon, LocalStorage)
 * - Real-time Search Engine with Results Dropdown, Snippets & In-Page Highlights
 * - Non-intrusive Animated Toast Notifications
 * - Theme Switcher (Parchment, Dark, Light)
 * - Bilingual / Hindi / English Language Mode Filter
 * - Two-Page Spread vs Single Page View Toggle
 * - Web Audio API Page-Turn Sound Mute Toggle
 * - Font Scale & Fullscreen Controls
 */

class BookUIController {
  constructor() {
    this.searchIndex = [];
    this.activeSearchQuery = '';
    this.bookmarks = [];
    this.toastTimeout = null;
    this.searchTimeout = null;
    this.isInitialized = false;
  }

  init() {
    if (this.isInitialized) return;
    this.isInitialized = true;

    // 1. Initialize Engine & Sound
    if (window.bookEngine) {
      window.bookEngine.init();
    }

    // 2. Initialize Bookmarks
    this.initBookmarks();

    // 3. Initialize Search Engine
    this.initSearch();

    // 4. Initialize Themes
    this.initTheme();

    // 5. Initialize Language Mode Switcher
    this.initLanguageMode();

    // 6. Initialize Spread / Single Layout Toggle
    this.initLayoutToggle();

    // 7. Initialize Sound Controls
    this.initSoundToggle();

    // 8. Initialize Font Scaling & Fullscreen
    this.initFontAndFullscreen();

    // 9. Initialize Table of Contents Modal
    this.initTOC();

    // 10. Initialize Mobile Settings Drawer Modal (⚙️)
    this.initSettingsDrawer();

    // Initial update of bookmark UI state
    this.updateBookmarkUI();
  }

  // ============================================================================
  // 1. Toast Notification System (Replaces browser alert)
  // ============================================================================
  showToast(message, duration = 3000) {
    const toast = document.getElementById('book-toast');
    if (!toast) return;
    toast.innerHTML = message;
    toast.classList.add('show');
    clearTimeout(this.toastTimeout);
    this.toastTimeout = setTimeout(() => {
      toast.classList.remove('show');
    }, duration);
  }

  // ============================================================================
  // 2. Bookmark System
  // ============================================================================
  initBookmarks() {
    // Load existing bookmarks
    try {
      const stored = localStorage.getItem('tantra_saved_bookmarks');
      if (stored) {
        this.bookmarks = JSON.parse(stored);
      } else {
        // Migrate legacy single bookmark if exists
        const legacy = localStorage.getItem('tantra_book_saved_bookmark');
        if (legacy) {
          const p = parseInt(legacy);
          if (p && !isNaN(p)) {
            this.bookmarks = [{
              page: p,
              chapter: 'Saved Page',
              title: `Page ${p}`,
              date: new Date().toLocaleDateString('hi-IN', { day: 'numeric', month: 'short' })
            }];
            this.saveBookmarks();
          }
        }
      }
    } catch (e) {
      this.bookmarks = [];
    }

    const bookmarkOverlay = document.getElementById('bookmark-overlay');
    const bookmarkBtn = document.getElementById('btn-bookmark-toggle');
    const bookmarkCloseBtn = document.getElementById('bookmark-close-btn');
    const bookmarkCurrentBtn = document.getElementById('btn-bookmark-current');

    // Toggle Modal
    if (bookmarkBtn && bookmarkOverlay) {
      bookmarkBtn.addEventListener('click', () => {
        this.openBookmarkModal();
      });
    }

    if (bookmarkCloseBtn && bookmarkOverlay) {
      bookmarkCloseBtn.addEventListener('click', () => {
        bookmarkOverlay.classList.remove('active');
      });
    }

    if (bookmarkOverlay) {
      bookmarkOverlay.addEventListener('click', (e) => {
        if (e.target === bookmarkOverlay) {
          bookmarkOverlay.classList.remove('active');
        }
      });
    }

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && bookmarkOverlay && bookmarkOverlay.classList.contains('active')) {
        bookmarkOverlay.classList.remove('active');
      }
    });

    // Bookmark Current Page Button inside Modal
    if (bookmarkCurrentBtn) {
      bookmarkCurrentBtn.addEventListener('click', () => {
        const currentPage = window.bookEngine ? window.bookEngine.currentPage : 1;
        this.toggleBookmark(currentPage);
      });
    }
  }

  saveBookmarks() {
    try {
      localStorage.setItem('tantra_saved_bookmarks', JSON.stringify(this.bookmarks));
    } catch (e) { }
  }

  isPageBookmarked(pageNum) {
    return this.bookmarks.some(b => b.page === pageNum);
  }

  toggleBookmark(pageNum) {
    if (!pageNum) pageNum = 1;
    const exists = this.isPageBookmarked(pageNum);

    if (exists) {
      this.bookmarks = this.bookmarks.filter(b => b.page !== pageNum);
      this.saveBookmarks();
      this.showToast(`🗑️ पृष्ठ ${pageNum} बुकमार्क से हटाया गया (Page ${pageNum} removed)`);
    } else {
      // Find chapter & title
      let title = `Page ${pageNum}`;
      let chapter = 'Tantra Gyan';
      const pageNode = document.getElementById(`page-data-${pageNum}`);
      if (pageNode) {
        chapter = pageNode.getAttribute('data-chapter') || chapter;
        title = pageNode.getAttribute('data-title') || title;
      }

      this.bookmarks.push({
        page: pageNum,
        chapter: chapter,
        title: title,
        date: new Date().toLocaleDateString('hi-IN', { day: 'numeric', month: 'short' })
      });
      // Sort by page number
      this.bookmarks.sort((a, b) => a.page - b.page);
      this.saveBookmarks();
      this.showToast(`🔖 पृष्ठ ${pageNum} बुकमार्क में सहेज लिया गया (Page ${pageNum} bookmarked!)`);

      if (window.bookSound && !window.bookSound.isMuted) {
        window.bookSound.playPageTurn('next');
      }
    }

    this.updateBookmarkUI();
  }

  openBookmarkModal() {
    const bookmarkOverlay = document.getElementById('bookmark-overlay');
    if (!bookmarkOverlay) return;
    this.renderBookmarkList();
    this.updateBookmarkCurrentBtn();
    bookmarkOverlay.classList.add('active');
  }

  updateBookmarkCurrentBtn() {
    const bookmarkCurrentBtn = document.getElementById('btn-bookmark-current');
    if (!bookmarkCurrentBtn || !window.bookEngine) return;

    const visiblePages = window.bookEngine.getCurrentVisiblePages();
    const isCurrentBookmarked = visiblePages.some(p => this.isPageBookmarked(p));
    const targetPage = visiblePages[0] || window.bookEngine.currentPage;

    if (isCurrentBookmarked) {
      bookmarkCurrentBtn.classList.add('is-bookmarked');
      bookmarkCurrentBtn.innerHTML = `<span>🗑️</span> <span>पृष्ठ ${targetPage} को बुकमार्क से हटाएं</span>`;
    } else {
      bookmarkCurrentBtn.classList.remove('is-bookmarked');
      bookmarkCurrentBtn.innerHTML = `<span>➕</span> <span>वर्तमान पृष्ठ (P.${targetPage}) बुकमार्क करें</span>`;
    }
  }

  updateBookmarkUI() {
    if (!window.bookEngine) return;
    const visiblePages = window.bookEngine.getCurrentVisiblePages();
    const isCurrentBookmarked = visiblePages.some(p => this.isPageBookmarked(p));

    // 1. Update Silk Ribbon on spine
    const ribbon = document.querySelector('.silk-bookmark');
    if (ribbon) {
      ribbon.classList.toggle('bookmarked', isCurrentBookmarked);
      ribbon.title = isCurrentBookmarked
        ? 'वर्तमान पृष्ठ बुकमार्क से हटाएं (Click to remove bookmark)'
        : 'वर्तमान पृष्ठ बुकमार्क करें (Click to bookmark page)';
    }

    // 2. Update Bookmark Count Badge in Toolbar & Settings Drawer
    const countBadge = document.getElementById('bookmark-count-badge');
    if (countBadge) {
      countBadge.textContent = this.bookmarks.length.toString();
      countBadge.style.display = this.bookmarks.length > 0 ? 'inline-block' : 'none';
    }
    const settingsCountBadge = document.getElementById('settings-bookmark-badge');
    if (settingsCountBadge) {
      settingsCountBadge.textContent = this.bookmarks.length.toString();
      settingsCountBadge.style.display = this.bookmarks.length > 0 ? 'inline-block' : 'none';
    }

    // 3. Update Modal Button
    this.updateBookmarkCurrentBtn();

    // 4. If modal is currently active, refresh list
    const bookmarkOverlay = document.getElementById('bookmark-overlay');
    if (bookmarkOverlay && bookmarkOverlay.classList.contains('active')) {
      this.renderBookmarkList();
    }
  }

  renderBookmarkList() {
    const listEl = document.getElementById('bookmark-list');
    if (!listEl) return;

    if (this.bookmarks.length === 0) {
      listEl.innerHTML = `
        <div class="bookmark-empty-state">
          <div class="bookmark-empty-icon">🔖</div>
          <p><strong>कोई बुकमार्क नहीं सहेजा गया है</strong></p>
          <p style="font-size:0.82rem; margin-top:0.4rem; color:var(--text-muted);">
            पढ़ते समय ऊपर '🔖 बुकमार्क' या मध्य में लटकती लाल रेशमी रिबन (Silk Ribbon) पर क्लिक करके किसी भी पृष्ठ को सहेज सकते हैं।
          </p>
        </div>
      `;
      return;
    }

    listEl.innerHTML = this.bookmarks.map(b => `
      <div class="bookmark-item">
        <div class="bookmark-item-left">
          <span class="bookmark-page-badge">P.${b.page}</span>
          <div class="bookmark-item-info">
            <span class="bookmark-item-title">${this.escapeHtml(b.title)}</span>
            <span class="bookmark-item-date">${this.escapeHtml(b.chapter)} • ${b.date || ''}</span>
          </div>
        </div>
        <div class="bookmark-item-actions">
          <button type="button" class="bookmark-btn-open" data-page="${b.page}" title="Open Page ${b.page}">📖 खोलें</button>
          <button type="button" class="bookmark-btn-del" data-page="${b.page}" title="Remove Bookmark">🗑️ हटाएं</button>
        </div>
      </div>
    `).join('');

    // Attach click events
    listEl.querySelectorAll('.bookmark-btn-open').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const p = parseInt(btn.getAttribute('data-page'));
        if (p && window.bookEngine) {
          window.bookEngine.goToPage(p, true);
          const bookmarkOverlay = document.getElementById('bookmark-overlay');
          if (bookmarkOverlay) bookmarkOverlay.classList.remove('active');
        }
      });
    });

    listEl.querySelectorAll('.bookmark-btn-del').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const p = parseInt(btn.getAttribute('data-page'));
        if (p) {
          this.toggleBookmark(p);
        }
      });
    });
  }

  // ============================================================================
  // 3. Real-time Search Engine with Results Dropdown & In-Page Highlights
  // ============================================================================
  initSearch() {
    // Build Page Index from DOM
    const rawPages = document.querySelectorAll('.book-page-data');
    this.searchIndex = Array.from(rawPages).map((el, i) => {
      const pageNum = parseInt(el.getAttribute('data-page')) || (i + 1);
      const chapter = el.getAttribute('data-chapter') || '';
      const title = el.getAttribute('data-title') || '';
      const text = el.textContent.replace(/\s+/g, ' ').trim();
      return { pageNum, chapter, title, text, el };
    });

    const searchInput = document.getElementById('book-search');
    const searchCounter = document.getElementById('search-counter');
    const searchClearBtn = document.getElementById('search-clear-btn');
    const searchDropdown = document.getElementById('search-dropdown');
    const searchDropdownClose = document.getElementById('search-dropdown-close');

    if (!searchInput) return;

    // Ensure hidden initially
    if (searchClearBtn) searchClearBtn.style.display = 'none';
    if (searchCounter) {
      searchCounter.textContent = '';
      searchCounter.style.display = 'none';
    }
    if (searchDropdown) searchDropdown.style.display = 'none';

    // Real-time input typing with debounce
    searchInput.addEventListener('input', (e) => {
      clearTimeout(this.searchTimeout);
      const query = e.target.value.trim();

      if (searchClearBtn) {
        searchClearBtn.style.display = e.target.value.length > 0 ? 'flex' : 'none';
      }

      if (!query || query.length < 2) {
        if (searchCounter) {
          searchCounter.textContent = '';
          searchCounter.style.display = 'none';
        }
        if (searchDropdown) searchDropdown.style.display = 'none';
        this.activeSearchQuery = '';
        this.clearPageHighlights();
        return;
      }

      this.searchTimeout = setTimeout(() => {
        this.executeSearch(query);
      }, 200);
    });

    // Enter Key
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const query = searchInput.value.trim();
        if (query.length >= 2) {
          this.executeSearch(query, true);
        }
      } else if (e.key === 'Escape') {
        if (searchDropdown) searchDropdown.style.display = 'none';
      }
    });

    // Clear Button
    if (searchClearBtn) {
      searchClearBtn.addEventListener('click', () => {
        searchInput.value = '';
        searchClearBtn.style.display = 'none';
        if (searchCounter) {
          searchCounter.textContent = '';
          searchCounter.style.display = 'none';
        }
        if (searchDropdown) searchDropdown.style.display = 'none';
        this.activeSearchQuery = '';
        this.clearPageHighlights();
        searchInput.focus();
      });
    }

    // Toggle Dropdown when clicking on the counter badge
    if (searchCounter) {
      searchCounter.addEventListener('click', () => {
        const query = searchInput.value.trim();
        if (query.length >= 2) {
          this.executeSearch(query);
        }
      });
    }

    const header = document.querySelector('.app-header');
    const searchCloseMobileBtn = document.getElementById('search-close-mobile-btn');

    const expandSearchMobile = () => {
      if (window.innerWidth <= 860 && header) {
        header.classList.add('search-expanded');
      }
    };

    const collapseSearchMobile = () => {
      if (header) {
        header.classList.remove('search-expanded');
      }
      if (searchDropdown) {
        searchDropdown.style.display = 'none';
      }
    };

    this.collapseSearchMobile = collapseSearchMobile;

    // Mobile Search Trigger Pill Click
    const mobileSearchTrigger = document.getElementById('mobile-search-trigger');
    if (mobileSearchTrigger) {
      mobileSearchTrigger.addEventListener('click', (e) => {
        e.stopPropagation();
        if (header && header.classList.contains('search-expanded')) {
          collapseSearchMobile();
        } else {
          expandSearchMobile();
          setTimeout(() => {
            if (searchInput) searchInput.focus();
          }, 50);
        }
      });
    }

    // Expand mobile search on focus or click
    searchInput.addEventListener('focus', expandSearchMobile);
    searchInput.addEventListener('click', expandSearchMobile);

    // Mobile Close Button
    if (searchCloseMobileBtn) {
      searchCloseMobileBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        searchInput.value = '';
        if (searchClearBtn) searchClearBtn.style.display = 'none';
        if (searchCounter) {
          searchCounter.textContent = '';
          searchCounter.style.display = 'none';
        }
        if (searchDropdown) searchDropdown.style.display = 'none';
        this.activeSearchQuery = '';
        this.clearPageHighlights();
        collapseSearchMobile();
        searchInput.blur();
      });
    }

    // Close Dropdown Button
    if (searchDropdownClose && searchDropdown) {
      searchDropdownClose.addEventListener('click', () => {
        searchDropdown.style.display = 'none';
      });
    }

    // Click Outside to Close Search Dropdown & Collapse Mobile Search
    document.addEventListener('click', (e) => {
      const container = document.getElementById('search-box-container');
      if (container && !container.contains(e.target)) {
        if (searchDropdown) searchDropdown.style.display = 'none';
        if (window.innerWidth <= 860 && !searchInput.value.trim()) {
          collapseSearchMobile();
        }
      }
    });
  }

  normalizeSearchQuery(str) {
    if (!str) return '';
    return str.toLowerCase().trim();
  }

  buildSearchRegex(query) {
    const q = query.trim();
    const escaped = this.escapeRegex(q);

    // Hindi variants equivalence:
    // If searching "चंद्र" or "चन्द्र", match both
    let pattern = escaped;
    if (/च[ंन][्द]र|चंद्र|चन्द्र/i.test(q)) {
      pattern = '(?:चंद्र|चन्द्र|चन्द्रा|चन्द)';
    } else if (/सूर्[यय]|सूर्य|सुर्य/i.test(q)) {
      pattern = '(?:सूर्य|सुर्य)';
    } else if (/सिंह|सींह/i.test(q)) {
      pattern = '(?:सिंह|सींह)';
    }

    return new RegExp(`(${pattern})`, 'gi');
  }

  executeSearch(query, jumpToFirst = false) {
    const regex = this.buildSearchRegex(query);
    const searchCounter = document.getElementById('search-counter');
    const searchDropdown = document.getElementById('search-dropdown');
    const searchResultsList = document.getElementById('search-results-list');
    const searchDropdownTitle = document.getElementById('search-dropdown-title');

    const matches = [];

    this.searchIndex.forEach((item) => {
      const fullSearchable = `${item.title} ${item.chapter} ${item.text}`;
      if (regex.test(fullSearchable)) {
        matches.push(item);
      }
      regex.lastIndex = 0; // reset regex state
    });

    this.activeSearchQuery = query;

    // Update Counter display (Clear, informative Hindi/English counter)
    if (searchCounter) {
      if (matches.length > 0) {
        searchCounter.textContent = `${matches.length} परिणाम`;
        searchCounter.title = `${matches.length} matching pages found. Click to view results list.`;
        searchCounter.style.display = 'inline-flex';
      } else {
        searchCounter.textContent = '0 परिणाम';
        searchCounter.title = 'No matches found.';
        searchCounter.style.display = 'inline-flex';
      }
    }

    // Render Dropdown
    if (searchDropdown && searchResultsList) {
      if (searchDropdownTitle) {
        searchDropdownTitle.textContent = `🔍 परिणाम: ${matches.length} पृष्ठ मिले ('${query}')`;
      }

      if (matches.length === 0) {
        searchResultsList.innerHTML = `
          <div class="search-no-results">
            ‘${this.escapeHtml(query)}’ के लिए कोई परिणाम नहीं मिला।<br>
            <span style="font-size:0.78rem; color:var(--text-muted); display:inline-block; margin-top:0.3rem;">
              कृपया अन्य शब्द (जैसे Moon, सूर्य, नक्षत्र, राजयोग) से खोजें।
            </span>
          </div>
        `;
      } else {
        searchResultsList.innerHTML = matches.map(m => {
          const snippet = this.generateSnippet(m.text, regex);
          return `
            <div class="search-result-item" data-page="${m.pageNum}" tabindex="0">
              <div class="search-result-top">
                <span class="search-page-badge">पृष्ठ ${m.pageNum}</span>
                <span class="search-chapter-name">${this.escapeHtml(m.chapter)}</span>
              </div>
              <div class="search-page-title">${this.escapeHtml(m.title)}</div>
              <div class="search-snippet">${snippet}</div>
            </div>
          `;
        }).join('');

        // Delegate click on each result item
        searchResultsList.querySelectorAll('.search-result-item').forEach(item => {
          item.addEventListener('click', () => {
            const targetPage = parseInt(item.getAttribute('data-page'));
            if (targetPage && window.bookEngine) {
              window.bookEngine.goToPage(targetPage, true);
              this.highlightActiveSearchInPage();
              searchDropdown.style.display = 'none';
              if (window.innerWidth <= 860 && typeof this.collapseSearchMobile === 'function') {
                this.collapseSearchMobile();
              }
            }
          });
        });
      }

      searchDropdown.style.display = 'block';
    }

    // If Jump to First (e.g. on Enter key)
    if (jumpToFirst && matches.length > 0 && window.bookEngine) {
      const firstPage = matches[0].pageNum;
      window.bookEngine.goToPage(firstPage, true);
      this.highlightActiveSearchInPage();
      this.showToast(`🔍 पृष्ठ ${firstPage} पर ले जाया गया (${matches.length} परिणाम मिले)`);
      if (searchDropdown) searchDropdown.style.display = 'none';
      if (window.innerWidth <= 860 && typeof this.collapseSearchMobile === 'function') {
        this.collapseSearchMobile();
      }
    }
  }

  generateSnippet(text, regex) {
    regex.lastIndex = 0;
    const match = regex.exec(text);
    if (!match) {
      return this.escapeHtml(text.slice(0, 95)) + '...';
    }

    const idx = match.index;
    const matchLen = match[0].length;
    const start = Math.max(0, idx - 35);
    const end = Math.min(text.length, idx + matchLen + 55);

    const prefix = start > 0 ? '...' : '';
    const suffix = end < text.length ? '...' : '';
    const rawSnippet = text.slice(start, end);

    regex.lastIndex = 0;
    const highlighted = this.escapeHtml(rawSnippet).replace(regex, '<mark class="search-kw">$1</mark>');
    return `${prefix}${highlighted}${suffix}`;
  }

  highlightActiveSearchInPage() {
    if (!this.activeSearchQuery || this.activeSearchQuery.length < 2) return;
    this.clearPageHighlights();

    const regex = this.buildSearchRegex(this.activeSearchQuery);
    const pageBodies = document.querySelectorAll('.page-sheet .page-body');

    pageBodies.forEach(body => {
      this.walkAndHighlight(body, regex);
    });
  }

  walkAndHighlight(element, regex) {
    if (!element) return;
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
    const textNodes = [];
    let node;

    while ((node = walker.nextNode())) {
      const parent = node.parentElement;
      if (
        node.nodeValue.trim().length > 0 &&
        parent &&
        parent.tagName !== 'MARK' &&
        parent.tagName !== 'SCRIPT' &&
        parent.tagName !== 'STYLE' &&
        !parent.classList.contains('page-search-mark')
      ) {
        textNodes.push(node);
      }
    }

    textNodes.forEach(tNode => {
      regex.lastIndex = 0;
      if (regex.test(tNode.nodeValue)) {
        regex.lastIndex = 0;
        const span = document.createElement('span');
        span.className = 'highlight-wrapper';
        span.innerHTML = this.escapeHtml(tNode.nodeValue).replace(regex, '<mark class="page-search-mark">$1</mark>');
        if (tNode.parentNode) {
          tNode.parentNode.replaceChild(span, tNode);
        }
      }
    });
  }

  clearPageHighlights() {
    document.querySelectorAll('.page-search-mark').forEach(m => {
      const parent = m.parentNode;
      if (parent) {
        parent.replaceChild(document.createTextNode(m.textContent), m);
        parent.normalize();
      }
    });
  }

  // ============================================================================
  // 4. Themes
  // ============================================================================
  initTheme() {
    const themeBtn = document.getElementById('btn-theme-toggle');
    const themes = ['parchment', 'dark', 'light'];
    let currentThemeIdx = 0;

    try {
      const savedTheme = localStorage.getItem('tantra_book_theme');
      if (savedTheme && themes.includes(savedTheme)) {
        currentThemeIdx = themes.indexOf(savedTheme);
        document.documentElement.setAttribute('data-theme', savedTheme);
        this.updateThemeButtonLabel(savedTheme);
      }
    } catch (e) { }

    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        currentThemeIdx = (currentThemeIdx + 1) % themes.length;
        const nextTheme = themes[currentThemeIdx];
        document.documentElement.setAttribute('data-theme', nextTheme);
        this.updateThemeButtonLabel(nextTheme);
        try {
          localStorage.setItem('tantra_book_theme', nextTheme);
        } catch (e) { }
      });
    }
  }

  updateThemeButtonLabel(t) {
    const themeBtn = document.getElementById('btn-theme-toggle');
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
    this.syncSettingsDrawerLabels();
  }

  // ============================================================================
  // 5. Language Mode Switcher (Seamlessly Switches Between File Editions)
  // ============================================================================
  initLanguageMode() {
    const langBtns = document.querySelectorAll('.lang-btn');

    // Determine active edition from filename or HTML attribute
    const currentPath = window.location.pathname;
    const currentFile = currentPath.substring(currentPath.lastIndexOf('/') + 1) || 'index.html';

    let activeMode = 'bilingual';
    if (currentFile.includes('hindi')) {
      activeMode = 'hindi';
    } else if (currentFile.includes('english')) {
      activeMode = 'english';
    } else {
      activeMode = document.documentElement.getAttribute('data-lang-mode') || 'bilingual';
    }

    this.setLanguageMode(activeMode);

    langBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const targetMode = btn.getAttribute('data-lang');
        const currentPage = (window.bookEngine && window.bookEngine.currentPage) ? window.bookEngine.currentPage : 1;

        let targetFile = 'index.html';
        if (targetMode === 'hindi') {
          targetFile = 'hindi.html';
        } else if (targetMode === 'english') {
          targetFile = 'english.html';
        } else {
          targetFile = 'index.html';
        }

        const path = window.location.pathname;
        const thisFile = path.substring(path.lastIndexOf('/') + 1) || 'index.html';

        if (thisFile !== targetFile) {
          try {
            localStorage.setItem('tantra_book_page', currentPage.toString());
            localStorage.setItem('tantra_book_lang', targetMode);
          } catch (err) { }
          window.location.href = `${targetFile}#page-${currentPage}`;
        } else {
          this.setLanguageMode(targetMode);
        }
      });
    });
  }

  setLanguageMode(mode) {
    document.documentElement.setAttribute('data-lang-mode', mode);
    document.querySelectorAll('.lang-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-lang') === mode);
    });
    document.querySelectorAll('.settings-opt-btn').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-lang') === mode);
    });
    try {
      localStorage.setItem('tantra_book_lang', mode);
    } catch (e) { }
  }

  // ============================================================================
  // 6. Layout Toggle
  // ============================================================================
  initLayoutToggle() {
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
  }

  // ============================================================================
  // 7. Sound Toggle
  // ============================================================================
  initSoundToggle() {
    const soundBtn = document.getElementById('btn-sound-toggle');
    if (soundBtn && window.bookSound) {
      this.updateSoundBtnState();
      soundBtn.addEventListener('click', () => {
        window.bookSound.toggleMute();
        this.updateSoundBtnState();
        if (!window.bookSound.isMuted) {
          window.bookSound.playPageTurn('next');
          this.showToast('🔊 पृष्ठ पलटने की ध्वनि सक्रिय (Sound On)');
        } else {
          this.showToast('🔇 ध्वनि म्यूट (Sound Muted)');
        }
      });
    }
  }

  updateSoundBtnState() {
    const soundBtn = document.getElementById('btn-sound-toggle');
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

  // ============================================================================
  // 8. Font Scaling & Fullscreen
  // ============================================================================
  initFontAndFullscreen() {
    let currentFontScale = 1.0;
    try {
      const savedScale = localStorage.getItem('tg_font_scale');
      if (savedScale) {
        currentFontScale = parseFloat(savedScale) || 1.0;
        document.documentElement.style.setProperty('--font-scale', `${currentFontScale}rem`);
      }
    } catch (e) {
      console.warn('Could not read font scale from localStorage:', e);
    }

    const fontDecBtn = document.getElementById('btn-font-dec');
    const fontIncBtn = document.getElementById('btn-font-inc');

    if (fontDecBtn) {
      fontDecBtn.addEventListener('click', () => {
        if (currentFontScale > 0.85) {
          currentFontScale = Math.round((currentFontScale - 0.05) * 100) / 100;
          document.documentElement.style.setProperty('--font-scale', `${currentFontScale}rem`);
          try { localStorage.setItem('tg_font_scale', currentFontScale); } catch (e) { }
        }
      });
    }

    if (fontIncBtn) {
      fontIncBtn.addEventListener('click', () => {
        if (currentFontScale < 1.40) {
          currentFontScale = Math.round((currentFontScale + 0.05) * 100) / 100;
          document.documentElement.style.setProperty('--font-scale', `${currentFontScale}rem`);
          try { localStorage.setItem('tg_font_scale', currentFontScale); } catch (e) { }
        }
      });
    }

    // Fullscreen Toggle for Desktop Toolbar
    const fullscreenBtns = document.querySelectorAll('#btn-fullscreen');
    const updateFsIcons = (isFs) => {
      const icon = isFs
        ? '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14h6m0 0v6m0-6L3 21m17-7h-6m0 0v6m0-6l7 7M10 4v6m0 0H4m6 0L3 3m10 7h6m-6 0V4m0 6l7-7"/></svg>'
        : '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>';
      fullscreenBtns.forEach(b => {
        b.innerHTML = icon;
        b.title = isFs ? 'Exit Fullscreen' : 'Toggle Fullscreen';
      });
    };

    fullscreenBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const isFs = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement;
        if (!isFs) {
          const docEl = document.documentElement;
          if (docEl.requestFullscreen) {
            docEl.requestFullscreen().catch(err => console.warn('Fullscreen request failed:', err));
          } else if (docEl.webkitRequestFullscreen) {
            docEl.webkitRequestFullscreen();
          } else if (docEl.webkitEnterFullscreen) {
            docEl.webkitEnterFullscreen();
          } else if (docEl.msRequestFullscreen) {
            docEl.msRequestFullscreen();
          }
        } else {
          if (document.exitFullscreen) {
            document.exitFullscreen().catch(err => console.warn('Exit fullscreen failed:', err));
          } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
          } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
          }
        }
      });
    });

    ['fullscreenchange', 'webkitfullscreenchange', 'mozfullscreenchange', 'MSFullscreenChange'].forEach(evt => {
      document.addEventListener(evt, () => {
        const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);
        updateFsIcons(isFs);
        this.syncSettingsDrawerLabels();
      });
    });
  }

  // ============================================================================
  // 9. Table of Contents Modal
  // ============================================================================
  initTOC() {
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
  }

  // ============================================================================
  // 10. Mobile Settings Drawer Modal (⚙️)
  // ============================================================================
  initSettingsDrawer() {
    const settingsToggleBtn = document.getElementById('btn-settings-toggle');
    const settingsOverlay = document.getElementById('settings-overlay');
    const settingsCloseBtn = document.getElementById('settings-close-btn');

    if (settingsToggleBtn && settingsOverlay) {
      settingsToggleBtn.addEventListener('click', () => {
        if (typeof this.collapseSearchMobile === 'function') {
          this.collapseSearchMobile();
        }
        settingsOverlay.classList.add('active');
        this.syncSettingsDrawerLabels();
      });

      if (settingsCloseBtn) {
        settingsCloseBtn.addEventListener('click', () => {
          settingsOverlay.classList.remove('active');
        });
      }

      settingsOverlay.addEventListener('click', (e) => {
        if (e.target === settingsOverlay) {
          settingsOverlay.classList.remove('active');
        }
      });

      // Quick Action: TOC
      const settingsTocBtn = document.getElementById('settings-btn-toc');
      if (settingsTocBtn) {
        settingsTocBtn.addEventListener('click', () => {
          settingsOverlay.classList.remove('active');
          const tocBtn = document.getElementById('btn-toc-toggle');
          if (tocBtn) tocBtn.click();
        });
      }

      // Quick Action: Bookmarks
      const settingsBookmarkBtn = document.getElementById('settings-btn-bookmark');
      if (settingsBookmarkBtn) {
        settingsBookmarkBtn.addEventListener('click', () => {
          settingsOverlay.classList.remove('active');
          const bmBtn = document.getElementById('btn-bookmark-toggle');
          if (bmBtn) bmBtn.click();
        });
      }

      // Quick Action: Theme Toggle
      const settingsThemeBtn = document.getElementById('settings-btn-theme');
      if (settingsThemeBtn) {
        settingsThemeBtn.addEventListener('click', () => {
          const mainThemeBtn = document.getElementById('btn-theme-toggle');
          if (mainThemeBtn) {
            mainThemeBtn.click();
            this.syncSettingsDrawerLabels();
          }
        });
      }

      // Quick Action: Layout Toggle
      const settingsLayoutBtn = document.getElementById('settings-btn-layout');
      if (settingsLayoutBtn) {
        settingsLayoutBtn.addEventListener('click', () => {
          const mainLayoutBtn = document.getElementById('btn-layout-toggle');
          if (mainLayoutBtn) {
            mainLayoutBtn.click();
            this.syncSettingsDrawerLabels();
          }
        });
      }

      // Quick Action: Sound Toggle
      const settingsSoundBtn = document.getElementById('settings-btn-sound');
      if (settingsSoundBtn) {
        settingsSoundBtn.addEventListener('click', () => {
          const mainSoundBtn = document.getElementById('btn-sound-toggle');
          if (mainSoundBtn) {
            mainSoundBtn.click();
            this.syncSettingsDrawerLabels();
          }
        });
      }

      // Quick Action: Fullscreen inside Settings Modal
      const settingsFsBtn = document.getElementById('settings-btn-fullscreen');
      if (settingsFsBtn) {
        settingsFsBtn.addEventListener('click', () => {
          const docEl = document.documentElement;
          const isFs = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement;

          if (!isFs) {
            if (docEl.requestFullscreen) {
              docEl.requestFullscreen().catch(err => {
                this.showToast('ℹ️ इस डिवाइस/ब्राउज़र में वेब फुलस्क्रीन समर्थित नहीं है।');
              });
            } else if (docEl.webkitRequestFullscreen) {
              docEl.webkitRequestFullscreen();
            } else {
              this.showToast('ℹ️ iPhone Safari वेब फुलस्क्रीन समर्थित नहीं करता। पूर्ण स्क्रीन अनुभव हेतु Share → "Add to Home Screen" करें।', 4000);
            }
          } else {
            if (document.exitFullscreen) {
              document.exitFullscreen().catch(err => console.warn(err));
            } else if (document.webkitExitFullscreen) {
              document.webkitExitFullscreen();
            }
          }
          this.syncSettingsDrawerLabels();
        });
      }

      // Quick Action: Font Zoom
      const settingsFontDec = document.getElementById('settings-font-dec');
      const settingsFontInc = document.getElementById('settings-font-inc');
      if (settingsFontDec) {
        settingsFontDec.addEventListener('click', () => {
          const dec = document.getElementById('btn-font-dec');
          if (dec) dec.click();
        });
      }
      if (settingsFontInc) {
        settingsFontInc.addEventListener('click', () => {
          const inc = document.getElementById('btn-font-inc');
          if (inc) inc.click();
        });
      }

      // Settings Language Option Buttons
      const settingsLangBtns = document.querySelectorAll('.settings-opt-btn');
      settingsLangBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          const targetLang = btn.getAttribute('data-lang');
          const matchingToolbarBtn = document.querySelector(`.lang-btn[data-lang="${targetLang}"]`);
          if (matchingToolbarBtn) {
            settingsOverlay.classList.remove('active');
            matchingToolbarBtn.click();
          }
        });
      });
    }
  }

  syncSettingsDrawerLabels() {
    const langMode = document.documentElement.getAttribute('data-lang-mode') || 'bilingual';
    const isPureHindi = (langMode === 'hindi');

    // Sync Theme Label
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'parchment';
    const themeLabel = document.getElementById('settings-theme-label');
    if (themeLabel) {
      if (isPureHindi) {
        if (currentTheme === 'dark') themeLabel.textContent = 'रात्रि';
        else if (currentTheme === 'light') themeLabel.textContent = 'श्वेत';
        else themeLabel.textContent = 'भोजपत्र';
      } else {
        if (currentTheme === 'dark') themeLabel.textContent = 'Night';
        else if (currentTheme === 'light') themeLabel.textContent = 'Day';
        else themeLabel.textContent = 'Parchment';
      }
    }

    // Sync Layout Label
    const isSingle = document.documentElement.classList.contains('single-mode-active');
    const layoutLabel = document.getElementById('settings-layout-label');
    if (layoutLabel) {
      if (isPureHindi) {
        layoutLabel.textContent = isSingle ? 'एकल पृष्ठ' : 'दो पृष्ठ';
      } else {
        layoutLabel.textContent = isSingle ? 'Single Page' : 'Two Pages';
      }
    }

    // Sync Sound Label
    const soundLabel = document.getElementById('settings-sound-label');
    if (soundLabel && window.bookSound) {
      if (isPureHindi) {
        soundLabel.textContent = window.bookSound.isMuted ? 'म्यूट' : 'चालू';
      } else {
        soundLabel.textContent = window.bookSound.isMuted ? 'Off' : 'On';
      }
    }

    // Sync Fullscreen Label
    const fsLabel = document.getElementById('settings-fs-label');
    if (fsLabel) {
      const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);
      if (isPureHindi) {
        fsLabel.textContent = isFs ? 'बंद करें' : 'चालू करें';
      } else {
        fsLabel.textContent = isFs ? 'Exit' : 'Enter';
      }
    }

    // Sync Bookmark Badge
    const bmBadge = document.getElementById('settings-bookmark-badge');
    const saved = this.getBookmarks ? this.getBookmarks() : (this.bookmarks || []);
    if (bmBadge) {
      if (saved.length > 0) {
        bmBadge.textContent = saved.length.toString();
        bmBadge.style.display = 'inline-block';
      } else {
        bmBadge.style.display = 'none';
      }
    }

    // Sync Language Buttons
    const currentLang = document.documentElement.getAttribute('data-lang-mode') || 'bilingual';
    document.querySelectorAll('.settings-opt-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === currentLang);
    });
  }

  escapeHtml(text) {
    if (!text) return '';
    return text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
}

// Global UI instance initialized upon DOM loading
window.bookUI = new BookUIController();

function bootBookUI() {
  if (window.bookUI && !window.bookUI.isInitialized) {
    window.bookUI.init();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', bootBookUI);
} else {
  // Document is already interactive or complete
  bootBookUI();
}

window.addEventListener('load', bootBookUI);
