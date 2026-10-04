/**
 * Tantra Gyan Vedic Astrology Book - Core 3D Flip Engine
 * Features:
 * - True 3D physical book page turning animation with perspective, paper curl & lighting
 * - Dual-page desktop spread and single-page mobile/tablet mode
 * - Perfectly synchronized procedural physical paper sound effects
 * - Smooth touch swipe, keyboard, slider, and TOC navigation
 */

class BookEngine {
  constructor() {
    this.currentPage = null;
    this.totalPages = 0;
    this.isDualPage = window.innerWidth > 1080;
    this.isAnimating = false;
    this.pages = [];

    // UI Elements
    this.leftPageEl = null;
    this.rightPageEl = null;
    this.prevBtn = null;
    this.nextBtn = null;
    this.slider = null;
    this.counter = null;
    this.progressFill = null;
    this.isInitialized = false;
  }

  init() {
    if (this.isInitialized) return;
    this.isInitialized = true;

    // Collect all page elements defined in DOM
    const rawPages = document.querySelectorAll('.book-page-data');
    this.pages = Array.from(rawPages);
    this.totalPages = this.pages.length;

    this.leftPageEl = document.getElementById('left-page-container');
    this.rightPageEl = document.getElementById('right-page-container');
    this.prevBtn = document.getElementById('btn-prev-page');
    this.nextBtn = document.getElementById('btn-next-page');
    this.slider = document.getElementById('page-slider');
    this.counter = document.getElementById('page-counter-badge');
    this.progressFill = document.getElementById('reading-progress-fill');

    if (this.slider) {
      this.slider.max = this.totalPages;
    }

    // Check saved page or URL hash
    let startPage = 1;
    if (typeof window !== 'undefined' && window.location && window.location.hash) {
      const match = window.location.hash.match(/#page-(\d+)/);
      if (match && parseInt(match[1], 10)) {
        startPage = parseInt(match[1], 10);
      }
    } else {
      try {
        const saved = localStorage.getItem('tantra_book_page');
        if (saved) {
          const p = parseInt(saved, 10);
          if (!isNaN(p) && p >= 1) startPage = p;
        }
      } catch (e) { }
    }

    startPage = Math.max(1, Math.min(this.totalPages || 1, startPage));

    // Handle responsive spread mode
    this.updateSpreadMode();
    window.addEventListener('resize', () => {
      this.updateSpreadMode();
      this.render();
    });

    // Bind event listeners
    this.bindEvents();

    // Render initial page with 100% guarantee across all devices
    this.currentPage = startPage;
    this.render();
    this.onPageChanged();
  }

  updateSpreadMode() {
    const forcedSingle = document.documentElement.classList.contains('single-mode-active');
    this.isDualPage = window.innerWidth > 1080 && !forcedSingle;
    this.updateSpreadLayoutClasses();
  }

  updateSpreadLayoutClasses() {
    const bookContainer = document.querySelector('.book-container');
    if (!bookContainer) return;
    bookContainer.classList.remove('dual-page-layout', 'single-page-layout', 'cover-closed-front', 'cover-closed-back');

    if (!this.isDualPage) {
      bookContainer.classList.add('single-page-layout');
      if (this.currentPage === 1) {
        bookContainer.classList.add('cover-closed-front');
      } else if (this.currentPage === this.totalPages) {
        bookContainer.classList.add('cover-closed-back');
      }
      return;
    }

    if (this.currentPage === 1) {
      bookContainer.classList.add('cover-closed-front');
    } else if (this.currentPage === this.totalPages) {
      bookContainer.classList.add('cover-closed-back');
    } else {
      bookContainer.classList.add('dual-page-layout');
    }
  }

  bindEvents() {
    if (this.prevBtn) {
      this.prevBtn.addEventListener('click', () => this.prevPage());
    }
    if (this.nextBtn) {
      this.nextBtn.addEventListener('click', () => this.nextPage());
    }

    // Clicking anywhere on closed cover opens the book
    const bookContainer = document.querySelector('.book-container');
    if (bookContainer) {
      bookContainer.addEventListener('click', (e) => {
        if (this.isAnimating) return;
        if (bookContainer.classList.contains('cover-closed-front')) {
          if (!e.target.closest('button, a, input, select, .silk-bookmark, .tool-btn, .page-nav-pill')) {
            this.nextPage();
          }
        } else if (bookContainer.classList.contains('cover-closed-back')) {
          if (!e.target.closest('button, a, input, select, .silk-bookmark, .tool-btn, .page-nav-pill')) {
            this.prevPage();
          }
        }
      });
    }

    // Direct page element clicks as backup
    if (this.rightPageEl) {
      this.rightPageEl.addEventListener('click', (e) => {
        const bc = document.querySelector('.book-container');
        if (bc && bc.classList.contains('cover-closed-front')) {
          if (!e.target.closest('button, a, input, select, .silk-bookmark, .tool-btn, .page-nav-pill')) {
            this.nextPage();
          }
        }
      });
    }
    if (this.leftPageEl) {
      this.leftPageEl.addEventListener('click', (e) => {
        const bc = document.querySelector('.book-container');
        if (bc && bc.classList.contains('cover-closed-back')) {
          if (!e.target.closest('button, a, input, select, .silk-bookmark, .tool-btn, .page-nav-pill')) {
            this.prevPage();
          }
        }
      });
    }

    if (this.slider) {
      this.slider.addEventListener('input', (e) => {
        const p = parseInt(e.target.value, 10);
        this.goToPage(p, true);
      });
    }

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
      // Don't intercept if user is typing in search input
      if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) return;

      if (e.key === 'ArrowRight' || e.key === 'PageDown' || (e.key === ' ' && !e.shiftKey)) {
        e.preventDefault();
        this.nextPage();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || (e.key === ' ' && e.shiftKey)) {
        e.preventDefault();
        this.prevPage();
      } else if (e.key === 'Home') {
        e.preventDefault();
        this.goToPage(1, true);
      } else if (e.key === 'End') {
        e.preventDefault();
        this.goToPage(this.totalPages, true);
      }
    });

    // Touch swipe navigation for tablets and mobile (Strictly protected against table scrolling)
    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartTime = 0;
    let isTableTouch = false;
    const stage = document.querySelector('.main-stage');
    if (stage) {
      stage.addEventListener('touchstart', (e) => {
        if (!e.changedTouches || !e.changedTouches.length) return;
        const target = e.target;
        // If touch began inside any table, table container, or scrollable area, disable page flip
        isTableTouch = !!(target && target.closest('.astro-table-container, .table-container, table, pre, code, .table-scroll-hint, button, input, select, a, .tool-btn, .page-nav-pill'));
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
        touchStartTime = Date.now();
      }, { passive: true });

      stage.addEventListener('touchend', (e) => {
        // If touch began on or inside a table or interactive control, NEVER flip page
        if (isTableTouch) {
          isTableTouch = false;
          return;
        }
        if (!e.changedTouches || !e.changedTouches.length) return;
        const target = e.target;
        if (target && target.closest('.astro-table-container, .table-container, table, pre, code, .table-scroll-hint, button, input, select, a, .tool-btn, .page-nav-pill')) {
          return;
        }

        const diffX = e.changedTouches[0].screenX - touchStartX;
        const diffY = e.changedTouches[0].screenY - touchStartY;
        const timeDiff = Date.now() - touchStartTime;

        // Decisive horizontal swipe: fast (< 500ms), at least 60px horizontal, predominantly horizontal
        if (timeDiff < 500 && Math.abs(diffX) > 60 && Math.abs(diffX) > Math.abs(diffY) * 1.6) {
          if (diffX < 0) {
            this.nextPage();
          } else {
            this.prevPage();
          }
        }
      }, { passive: true });
    }

    // Silk bookmark click to toggle bookmark
    const bookmark = document.querySelector('.silk-bookmark');
    if (bookmark) {
      bookmark.addEventListener('click', () => {
        if (window.bookUI && typeof window.bookUI.toggleBookmark === 'function') {
          window.bookUI.toggleBookmark(this.currentPage);
        }
      });
    }
  }

  nextPage() {
    if (this.isAnimating) return;
    if (!this.isDualPage) {
      if (this.currentPage < this.totalPages) {
        this.flip3D('forward', this.currentPage + 1);
      }
      return;
    }

    // Dual-page mode navigation
    if (this.currentPage <= 1) {
      // From closed Front Cover, open to first inside spread [2, 3]
      this.flip3D('forward', 2);
    } else if (this.currentPage >= this.totalPages) {
      // Already at closed Back Cover
      return;
    } else {
      const currL = (this.currentPage % 2 === 0) ? this.currentPage : this.currentPage - 1;
      const nextL = currL + 2;
      if (nextL >= this.totalPages) {
        // Close book to Back Cover
        this.flip3D('forward', this.totalPages);
      } else {
        this.flip3D('forward', nextL);
      }
    }
  }

  prevPage() {
    if (this.isAnimating) return;
    if (!this.isDualPage) {
      if (this.currentPage > 1) {
        this.flip3D('backward', this.currentPage - 1);
      }
      return;
    }

    // Dual-page mode navigation
    if (this.currentPage <= 1) {
      return;
    } else if (this.currentPage >= this.totalPages) {
      // Reopen from Back Cover to last inside spread [totalPages - 2, totalPages - 1] (e.g. [86, 87])
      this.flip3D('backward', this.totalPages - 2);
    } else {
      const currL = (this.currentPage % 2 === 0) ? this.currentPage : this.currentPage - 1;
      const prevL = currL - 2;
      if (prevL < 2) {
        // Close book to Front Cover
        this.flip3D('backward', 1);
      } else {
        this.flip3D('backward', prevL);
      }
    }
  }

  clearAnimLock() {
    if (this._animWatchdog) {
      clearTimeout(this._animWatchdog);
      this._animWatchdog = null;
    }
    this.isAnimating = false;
  }

  /**
   * Executes a realistic physical 3D page turn
   * @param {string} direction - 'forward' or 'backward'
   * @param {number} targetPage - destination page number
   */
  flip3D(direction, targetPage) {
    if (this.isAnimating) return;
    this.isAnimating = true;

    // Safety watchdog: recover engine if animation callback is delayed or stalled
    if (this._animWatchdog) clearTimeout(this._animWatchdog);
    this._animWatchdog = setTimeout(() => {
      if (this.isAnimating) {
        console.warn('Flip watchdog triggered - auto-recovering book animation lock');
        this.clearAnimLock();
        const w = document.querySelector('.book-pages-wrapper');
        if (w) {
          w.querySelectorAll('.book-flipper-leaf, .flipper-under-shadow').forEach(el => el.remove());
        }
        this.render();
        this.onPageChanged();
      }
    }, 700);

    const wrapper = document.querySelector('.book-pages-wrapper');
    if (!wrapper) {
      this.currentPage = targetPage;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
      return;
    }

    // Clean up any lingering flipper nodes
    wrapper.querySelectorAll('.book-flipper-leaf, .flipper-under-shadow').forEach(el => el.remove());

    if (this.isDualPage) {
      // 1. Opening Book from Front Cover (Page 1 -> Spread 2-3)
      if (this.currentPage === 1 && direction === 'forward') {
        this.performBookOpen(targetPage, wrapper);
        return;
      }

      // 2. Closing Book to Front Cover (Spread 2-3 -> Page 1)
      if (targetPage === 1 && direction === 'backward') {
        this.performBookCloseFront(wrapper);
        return;
      }

      // 3. Closing Book to Back Cover (Spread -> Page 88)
      if (targetPage >= this.totalPages && direction === 'forward') {
        this.performBookCloseBack(wrapper);
        return;
      }

      // 4. Re-opening Book from Back Cover (Page 88 -> Spread)
      if (this.currentPage >= this.totalPages && direction === 'backward') {
        this.performBookOpenBack(targetPage, wrapper);
        return;
      }

      // Standard interior dual-page flip
      if (window.bookSound) {
        window.bookSound.playPageTurn(direction === 'forward' ? 'next' : 'prev');
      }
      this.performDualPageFlip(direction, targetPage, wrapper);
    } else {
      // Single Page Mode (Mobile / Tablet)
      // 1. Opening Book from Front Cover (Page 1 -> Page 2)
      if (this.currentPage === 1 && direction === 'forward') {
        this.performSingleCoverOpen(targetPage, wrapper);
        return;
      }

      // 2. Closing Book to Front Cover (Page 2 -> Page 1)
      if (targetPage === 1 && direction === 'backward') {
        this.performSingleCoverClose(wrapper);
        return;
      }

      // 3. Closing Book to Back Cover (Page 87 -> Page 88)
      if (targetPage >= this.totalPages && direction === 'forward') {
        this.performSingleCoverCloseBack(wrapper);
        return;
      }

      // 4. Reopening Book from Back Cover (Page 88 -> Page 87)
      if (this.currentPage >= this.totalPages && direction === 'backward') {
        this.performSingleCoverOpenBack(targetPage, wrapper);
        return;
      }

      // Standard single page flip
      if (window.bookSound) {
        window.bookSound.playPageTurn(direction === 'forward' ? 'next' : 'prev');
      }
      this.performSinglePageFlip(direction, targetPage, wrapper);
    }
  }

  /**
   * Real 3D physical hardcover book opening (Front Cover -> Inside Spread)
   * Single, clean, majestic hardcover swing with no duplicate page flashes
   */
  performBookOpen(targetPage, wrapper) {
    const bookContainer = document.querySelector('.book-container');
    if (window.bookSound && window.bookSound.playBookOpen) {
      window.bookSound.playBookOpen();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('next');
    }

    // Step 1: Transition container into dual-page opening state
    if (bookContainer) {
      bookContainer.classList.remove('cover-closed-front', 'cover-closed-back', 'cosmic-manifest');
      bookContainer.classList.add('dual-page-layout', 'book-opening');
    }

    // Step 2: Underneath the lifting cover:
    // Left desk page is kept completely empty/hidden during the 3D cover swing
    if (this.leftPageEl) {
      this.clearPage(this.leftPageEl);
    }
    // Right desk page immediately reveals Page 3 as the cover lifts off it
    if (this.rightPageEl) {
      this.renderSinglePageContent(this.rightPageEl, this.pages[2], 3);
    }

    // Step 3: 3D Heavy Cover Leaf (swings from 0deg on right to -180deg on left)
    // Front face: Page 1 (Front Cover)
    // Back face: Page 2 (Inside Cover / Mangalacharan)
    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf book-cover-flipper book-open-forward';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet right-page">
        ${this.getPageHTML(1)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet left-page">
        ${this.getPageHTML(2)}
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    const shadow = document.createElement('div');
    shadow.className = 'flipper-under-shadow book-open-shadow';

    wrapper.appendChild(shadow);
    wrapper.appendChild(flipper);

    setTimeout(() => {
      // Step 4: Cover has landed at -180deg on the left desk
      if (this.leftPageEl) {
        this.renderSinglePageContent(this.leftPageEl, this.pages[1], 2);
      }
      flipper.remove();
      shadow.remove();
      if (bookContainer) {
        bookContainer.classList.remove('book-opening');
      }
      this.currentPage = targetPage;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 650);
  }

  /**
   * Real 3D physical hardcover book closing (Inside Spread -> Front Cover)
   * Clean single reverse swing shut into the floating closed cover
   */
  performBookCloseFront(wrapper) {
    const bookContainer = document.querySelector('.book-container');
    if (window.bookSound && window.bookSound.playBookClose) {
      window.bookSound.playBookClose();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('prev');
    }

    if (bookContainer) {
      bookContainer.classList.add('book-closing-front');
    }

    // Step 1: Left desk page lifts with the cover leaf, so clear left container
    if (this.leftPageEl) {
      this.clearPage(this.leftPageEl);
    }
    // Right container remains displaying Page 3 until covered

    // Step 2: 3D Cover Leaf swings from -180deg on left to 0deg on right
    // Front face: Page 2 (Inside Cover)
    // Back face: Page 1 (Front Cover)
    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf book-cover-flipper book-close-backward';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet left-page">
        ${this.getPageHTML(2)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet right-page">
        ${this.getPageHTML(1)}
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    const shadow = document.createElement('div');
    shadow.className = 'flipper-under-shadow book-close-shadow';

    wrapper.appendChild(shadow);
    wrapper.appendChild(flipper);

    setTimeout(() => {
      // Step 3: Cover has landed closed over the right desk
      flipper.remove();
      shadow.remove();
      if (bookContainer) {
        bookContainer.classList.remove('dual-page-layout', 'book-closing-front');
        bookContainer.classList.add('cover-closed-front');
      }
      this.currentPage = 1;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 650);
  }

  /**
   * Real 3D physical book closing to Back Cover
   */
  performBookCloseBack(wrapper) {
    const bookContainer = document.querySelector('.book-container');
    if (window.bookSound && window.bookSound.playBookClose) {
      window.bookSound.playBookClose();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('next');
    }

    if (bookContainer) {
      bookContainer.classList.add('book-closing-back');
    }

    // Right desk lifts with the leaf
    if (this.rightPageEl) {
      this.clearPage(this.rightPageEl);
    }

    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf book-cover-flipper book-close-forward';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet right-page">
        ${this.getPageHTML(this.totalPages - 1)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet left-page">
        ${this.getPageHTML(this.totalPages)}
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    const shadow = document.createElement('div');
    shadow.className = 'flipper-under-shadow book-open-shadow';

    wrapper.appendChild(shadow);
    wrapper.appendChild(flipper);

    setTimeout(() => {
      flipper.remove();
      shadow.remove();
      if (bookContainer) {
        bookContainer.classList.remove('dual-page-layout', 'book-closing-back');
        bookContainer.classList.add('cover-closed-back');
      }
      this.currentPage = this.totalPages;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 650);
  }

  /**
   * Real 3D physical book reopening from Back Cover
   */
  performBookOpenBack(targetPage, wrapper) {
    const bookContainer = document.querySelector('.book-container');
    if (window.bookSound && window.bookSound.playBookOpen) {
      window.bookSound.playBookOpen();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('prev');
    }

    if (bookContainer) {
      bookContainer.classList.remove('cover-closed-front', 'cover-closed-back');
      bookContainer.classList.add('dual-page-layout', 'book-opening-back');
    }

    const targetL = this.totalPages - 2;
    const targetR = this.totalPages - 1;

    if (this.leftPageEl) {
      this.clearPage(this.leftPageEl);
    }
    if (this.rightPageEl) {
      this.renderSinglePageContent(this.rightPageEl, this.pages[targetR - 1], targetR);
    }

    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf book-cover-flipper book-open-backward';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet left-page">
        ${this.getPageHTML(this.totalPages)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet right-page">
        ${this.getPageHTML(targetL)}
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    const shadow = document.createElement('div');
    shadow.className = 'flipper-under-shadow book-close-shadow';

    wrapper.appendChild(shadow);
    wrapper.appendChild(flipper);

    setTimeout(() => {
      if (this.leftPageEl) {
        this.renderSinglePageContent(this.leftPageEl, this.pages[targetL - 1], targetL);
      }
      flipper.remove();
      shadow.remove();
      if (bookContainer) {
        bookContainer.classList.remove('book-opening-back');
      }
      this.currentPage = targetPage;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 650);
  }

  /**
   * Single-page (mobile) book cover opening animation
   */
  performSingleCoverOpen(targetPage, wrapper) {
    if (window.bookSound && window.bookSound.playBookOpen) {
      window.bookSound.playBookOpen();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('next');
    }

    if (this.rightPageEl) {
      this.renderSinglePageContent(this.rightPageEl, this.pages[targetPage - 1], targetPage);
    }

    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf single-cover-open';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet">
        ${this.getPageHTML(1)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet">
        <div class="page-sheet-back-parchment"></div>
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    wrapper.appendChild(flipper);

    setTimeout(() => {
      flipper.remove();
      this.currentPage = targetPage;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 620);
  }

  /**
   * Single-page (mobile) book cover closing animation
   */
  performSingleCoverClose(wrapper) {
    if (window.bookSound && window.bookSound.playBookClose) {
      window.bookSound.playBookClose();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('prev');
    }

    if (this.rightPageEl) {
      this.renderSinglePageContent(this.rightPageEl, this.pages[0], 1);
    }

    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf single-cover-close';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet">
        ${this.getPageHTML(2)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet">
        ${this.getPageHTML(1)}
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    wrapper.appendChild(flipper);

    setTimeout(() => {
      flipper.remove();
      this.currentPage = 1;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 620);
  }

  /**
   * Single-page (mobile) closing to Back Cover
   */
  performSingleCoverCloseBack(wrapper) {
    if (window.bookSound && window.bookSound.playBookClose) {
      window.bookSound.playBookClose();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('next');
    }

    if (this.rightPageEl) {
      this.renderSinglePageContent(this.rightPageEl, this.pages[this.totalPages - 1], this.totalPages);
    }

    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf single-cover-open';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet">
        ${this.getPageHTML(this.totalPages - 1)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet">
        ${this.getPageHTML(this.totalPages)}
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    wrapper.appendChild(flipper);

    setTimeout(() => {
      flipper.remove();
      this.currentPage = this.totalPages;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 620);
  }

  /**
   * Single-page (mobile) reopening from Back Cover
   */
  performSingleCoverOpenBack(targetPage, wrapper) {
    if (window.bookSound && window.bookSound.playBookOpen) {
      window.bookSound.playBookOpen();
    } else if (window.bookSound) {
      window.bookSound.playPageTurn('prev');
    }

    if (this.rightPageEl) {
      this.renderSinglePageContent(this.rightPageEl, this.pages[targetPage - 1], targetPage);
    }

    const flipper = document.createElement('div');
    flipper.className = 'book-flipper-leaf single-cover-close';
    flipper.innerHTML = `
      <div class="flipper-face flipper-face-front page-sheet">
        ${this.getPageHTML(this.totalPages)}
        <div class="flipper-lighting-layer"></div>
      </div>
      <div class="flipper-face flipper-face-back page-sheet">
        ${this.getPageHTML(targetPage)}
        <div class="flipper-lighting-layer"></div>
      </div>
    `;

    wrapper.appendChild(flipper);

    setTimeout(() => {
      flipper.remove();
      this.currentPage = targetPage;
      this.render();
      this.onPageChanged();
      this.clearAnimLock();
    }, 620);
  }

  performDualPageFlip(direction, targetPage, wrapper) {
    const currL = (this.currentPage % 2 === 0) ? this.currentPage : this.currentPage - 1;
    const currR = currL + 1;

    const targetL = (targetPage % 2 === 0) ? targetPage : targetPage - 1;
    const targetR = targetL + 1;

    if (direction === 'forward') {
      // The turning sheet is the Right Page (currR), flipping over to Left (targetL)
      // Underneath, right container immediately reveals targetR
      if (this.rightPageEl) {
        this.renderSinglePageContent(this.rightPageEl, this.pages[targetR - 1], targetR);
      }

      // Create 3D Flipper Leaf
      const flipper = document.createElement('div');
      flipper.className = 'book-flipper-leaf dual-flip-forward';
      flipper.innerHTML = `
        <div class="flipper-face flipper-face-front page-sheet right-page">
          ${this.getPageHTML(currR)}
          <div class="flipper-lighting-layer"></div>
        </div>
        <div class="flipper-face flipper-face-back page-sheet left-page">
          ${this.getPageHTML(targetL)}
          <div class="flipper-lighting-layer"></div>
        </div>
      `;

      const shadow = document.createElement('div');
      shadow.className = 'flipper-under-shadow dual-flip-forward-shadow';

      wrapper.appendChild(shadow);
      wrapper.appendChild(flipper);

      setTimeout(() => {
        flipper.remove();
        shadow.remove();
        this.currentPage = targetPage;
        this.render();
        this.onPageChanged();
        this.clearAnimLock();
      }, 540);

    } else {
      // Backward: The turning sheet is the Left Page (currL), flipping over to Right (targetR)
      // Underneath, left container immediately reveals targetL
      if (this.leftPageEl) {
        this.renderSinglePageContent(this.leftPageEl, this.pages[targetL - 1], targetL);
      }

      // Create 3D Flipper Leaf
      const flipper = document.createElement('div');
      flipper.className = 'book-flipper-leaf dual-flip-backward';
      flipper.innerHTML = `
        <div class="flipper-face flipper-face-front page-sheet left-page">
          ${this.getPageHTML(currL)}
          <div class="flipper-lighting-layer"></div>
        </div>
        <div class="flipper-face flipper-face-back page-sheet right-page">
          ${this.getPageHTML(targetR)}
          <div class="flipper-lighting-layer"></div>
        </div>
      `;

      const shadow = document.createElement('div');
      shadow.className = 'flipper-under-shadow dual-flip-backward-shadow';

      wrapper.appendChild(shadow);
      wrapper.appendChild(flipper);

      setTimeout(() => {
        flipper.remove();
        shadow.remove();
        this.currentPage = targetPage;
        this.render();
        this.onPageChanged();
        this.clearAnimLock();
      }, 540);
    }
  }

  performSinglePageFlip(direction, targetPage, wrapper) {
    const currP = this.currentPage;
    const targetP = targetPage;

    if (direction === 'forward') {
      // Underneath, right container immediately reveals target page
      if (this.rightPageEl) {
        this.renderSinglePageContent(this.rightPageEl, this.pages[targetP - 1], targetP);
      }

      const flipper = document.createElement('div');
      flipper.className = 'book-flipper-leaf single-flip-forward';
      flipper.innerHTML = `
        <div class="flipper-face flipper-face-front page-sheet">
          ${this.getPageHTML(currP)}
          <div class="flipper-lighting-layer"></div>
        </div>
        <div class="flipper-face flipper-face-back page-sheet">
          <div class="page-sheet-back-parchment"></div>
          <div class="flipper-lighting-layer"></div>
        </div>
      `;

      wrapper.appendChild(flipper);

      setTimeout(() => {
        flipper.remove();
        this.currentPage = targetP;
        this.render();
        this.onPageChanged();
        this.clearAnimLock();
      }, 520);

    } else {
      const flipper = document.createElement('div');
      flipper.className = 'book-flipper-leaf single-flip-backward';
      flipper.innerHTML = `
        <div class="flipper-face flipper-face-front page-sheet">
          ${this.getPageHTML(targetP)}
          <div class="flipper-lighting-layer"></div>
        </div>
        <div class="flipper-face flipper-face-back page-sheet">
          <div class="page-sheet-back-parchment"></div>
          <div class="flipper-lighting-layer"></div>
        </div>
      `;

      wrapper.appendChild(flipper);

      setTimeout(() => {
        flipper.remove();
        this.currentPage = targetP;
        this.render();
        this.onPageChanged();
        this.clearAnimLock();
      }, 520);
    }
  }

  goToPage(pageNum, playSound = false) {
    if (pageNum < 1) pageNum = 1;
    if (pageNum > this.totalPages) pageNum = this.totalPages;

    if (this.isDualPage) {
      if (this.currentPage === 1 && pageNum === 1) return;
      if (this.currentPage === this.totalPages && pageNum === this.totalPages) return;
      if (this.currentPage >= 2 && this.currentPage < this.totalPages && pageNum >= 2 && pageNum < this.totalPages) {
        const currL = (this.currentPage % 2 === 0) ? this.currentPage : this.currentPage - 1;
        const targetL = (pageNum % 2 === 0) ? pageNum : pageNum - 1;
        if (currL === targetL) {
          this.currentPage = pageNum;
          this.onPageChanged();
          return;
        }
      }
      if (playSound && !this.isAnimating) {
        const dir = (pageNum > (this.currentPage || 1)) ? 'forward' : 'backward';
        this.flip3D(dir, pageNum);
        return;
      }
    } else {
      if (pageNum === this.currentPage) return;
      if (playSound && !this.isAnimating) {
        const dir = (pageNum > (this.currentPage || 1)) ? 'forward' : 'backward';
        this.flip3D(dir, pageNum);
        return;
      }
    }

    this.currentPage = pageNum;
    this.render();
  }

  render() {
    if (!this.pages || !this.pages.length) return;
    this.updateSpreadLayoutClasses();

    if (this.isDualPage) {
      if (this.currentPage === 1) {
        // Closed Front Cover: page 1 on right container, left container hidden
        if (this.rightPageEl) {
          this.renderSinglePageContent(this.rightPageEl, this.pages[0], 1);
        }
        if (this.leftPageEl) {
          this.clearPage(this.leftPageEl);
        }
      } else if (this.currentPage === this.totalPages) {
        // Closed Back Cover: last page on left container, right container hidden
        if (this.leftPageEl) {
          this.renderSinglePageContent(this.leftPageEl, this.pages[this.totalPages - 1], this.totalPages);
        }
        if (this.rightPageEl) {
          this.clearPage(this.rightPageEl);
        }
      } else {
        // Open two-page spread [leftNum, rightNum]
        const leftNum = (this.currentPage % 2 === 0) ? this.currentPage : this.currentPage - 1;
        const rightNum = leftNum + 1;
        this.renderSpread(leftNum, rightNum);
      }
    } else {
      // Single Page Mode
      const activeNum = this.currentPage || 1;
      if (this.rightPageEl && this.pages[activeNum - 1]) {
        this.renderSinglePageContent(this.rightPageEl, this.pages[activeNum - 1], activeNum);
      }
      if (this.leftPageEl) {
        this.clearPage(this.leftPageEl);
      }
    }
    this.onPageChanged();
  }

  renderSpread(leftNum, rightNum) {
    if (this.leftPageEl) {
      if (leftNum >= 1 && leftNum <= this.totalPages) {
        this.renderSinglePageContent(this.leftPageEl, this.pages[leftNum - 1], leftNum);
      } else {
        this.clearPage(this.leftPageEl);
      }
    }
    if (this.rightPageEl) {
      if (rightNum >= 1 && rightNum <= this.totalPages) {
        this.renderSinglePageContent(this.rightPageEl, this.pages[rightNum - 1], rightNum);
      } else {
        this.clearPage(this.rightPageEl);
      }
    }
  }

  onPageChanged() {
    // Scroll page body back to top on page change
    if (this.leftPageEl) {
      const b1 = this.leftPageEl.querySelector('.page-body');
      if (b1) b1.scrollTop = 0;
    }
    if (this.rightPageEl) {
      const b2 = this.rightPageEl.querySelector('.page-body');
      if (b2) b2.scrollTop = 0;
    }

    // Update Slider
    if (this.slider) {
      this.slider.value = this.currentPage;
    }

    // Update Counter badge (Compact font/text so it fits beside buttons on a single line)
    if (this.counter) {
      const langMode = document.documentElement.getAttribute('data-lang-mode') || 'bilingual';
      const isPureHindi = (langMode === 'hindi');

      if (this.isDualPage) {
        if (this.currentPage === 1) {
          this.counter.textContent = isPureHindi ? `मुखपृष्ठ • Cover (१ / ${this.totalPages})` : `Cover • 1 / ${this.totalPages}`;
        } else if (this.currentPage >= this.totalPages) {
          this.counter.textContent = isPureHindi ? `समापन • Back (${this.totalPages} / ${this.totalPages})` : `Back Cover • ${this.totalPages} / ${this.totalPages}`;
        } else {
          const leftNum = (this.currentPage % 2 === 0) ? this.currentPage : this.currentPage - 1;
          const rightNum = Math.min(leftNum + 1, this.totalPages);
          this.counter.textContent = isPureHindi ? `पृष्ठ ${leftNum}–${rightNum} / ${this.totalPages}` : `Pages ${leftNum}–${rightNum} / ${this.totalPages}`;
        }
      } else {
        if (this.currentPage === 1) {
          this.counter.textContent = isPureHindi ? `मुखपृष्ठ • Cover (१ / ${this.totalPages})` : `Cover • 1 / ${this.totalPages}`;
        } else if (this.currentPage >= this.totalPages) {
          this.counter.textContent = isPureHindi ? `समापन • Back (${this.totalPages} / ${this.totalPages})` : `Back Cover • ${this.totalPages} / ${this.totalPages}`;
        } else {
          this.counter.textContent = isPureHindi ? `पृष्ठ ${this.currentPage} / ${this.totalPages}` : `Page ${this.currentPage} / ${this.totalPages}`;
        }
      }
    }

    // Update reading progress bar
    if (this.progressFill) {
      const pct = Math.round((this.currentPage / this.totalPages) * 100);
      this.progressFill.style.width = `${pct}%`;
    }

    // Update Button Disabled States (All 4 Bottom Navigation Buttons)
    const atStart = this.currentPage <= 1;
    const atEnd = this.currentPage >= this.totalPages;
    if (this.prevBtn) this.prevBtn.disabled = atStart;
    if (this.nextBtn) this.nextBtn.disabled = atEnd;

    const btnFirstBottom = document.getElementById('btn-first-bottom');
    if (btnFirstBottom) btnFirstBottom.disabled = atStart;
    const btnPrevBottom = document.getElementById('btn-prev-bottom');
    if (btnPrevBottom) btnPrevBottom.disabled = atStart;
    const btnNextBottom = document.getElementById('btn-next-bottom');
    if (btnNextBottom) btnNextBottom.disabled = atEnd;
    const btnLastBottom = document.getElementById('btn-last-bottom');
    if (btnLastBottom) btnLastBottom.disabled = atEnd;

    // Update URL hash and localStorage
    try {
      history.replaceState(null, null, `#page-${this.currentPage}`);
      localStorage.setItem('tantra_book_page', this.currentPage.toString());
    } catch (e) { }

    // Notify BookUI to refresh bookmark state and search highlights
    if (window.bookUI && typeof window.bookUI.updateBookmarkUI === 'function') {
      window.bookUI.updateBookmarkUI();
    }
    if (window.bookUI && typeof window.bookUI.highlightActiveSearchInPage === 'function') {
      window.bookUI.highlightActiveSearchInPage();
    }
  }

  getCurrentVisiblePages() {
    if (this.isDualPage) {
      if (this.currentPage === 1) return [1];
      if (this.currentPage === this.totalPages) return [this.totalPages];
      const leftNum = (this.currentPage % 2 === 0) ? this.currentPage : this.currentPage - 1;
      const pages = [leftNum];
      if (leftNum + 1 <= this.totalPages) {
        pages.push(leftNum + 1);
      }
      return pages;
    }
    return [this.currentPage];
  }

  getPageHTML(pageNum) {
    if (pageNum < 1 || pageNum > this.totalPages) {
      return `
        <div class="page-header">
          <span class="page-header-title">☸ Tantra Gyan</span>
        </div>
        <div class="page-body" style="display:flex; align-items:center; justify-content:center; opacity:0.35;">
          <p style="font-style:italic; font-family:var(--font-heading);">ॐ नमः शिवाय</p>
        </div>
        <div class="page-footer">
          <span></span>
          <span class="page-number-display"></span>
        </div>
      `;
    }

    const node = this.pages[pageNum - 1];
    if (!node) return '';

    // Cover Pages (Front Cover = 1, Back Cover = totalPages) do NOT have running header/footer
    if (pageNum === 1 || pageNum === this.totalPages) {
      return `
        <div class="page-body cover-page-wrapper">
          ${node.innerHTML}
        </div>
      `;
    }

    const chapterTitle = node.getAttribute('data-chapter') || 'Tantra Gyan';
    const pageHeaderTitle = node.getAttribute('data-title') || chapterTitle;
    const footerTitle = document.documentElement.lang === 'en'
      ? 'Complete Vedic Astrology Compendium Simplified'
      : 'वैदिक ज्योतिष महाग्रंथ सरलीकृत';

    return `
      <div class="page-header">
        <div class="page-header-info">
          <span class="page-header-title">
            <span style="color:var(--accent-gold);">☸</span> ${chapterTitle}
          </span>
          <span class="page-header-subtitle">${pageHeaderTitle}</span>
        </div>
      </div>
      <div class="page-body">
        ${node.innerHTML}
      </div>
      <div class="page-footer">
        <span class="page-footer-title">${footerTitle}</span>
        <span class="page-number-display">Page ${pageNum} of ${this.totalPages}</span>
      </div>
    `;
  }

  renderSinglePageContent(container, pageDataNode, pageNum) {
    if (!container) return;
    container.innerHTML = this.getPageHTML(pageNum);
  }

  checkAndRepairSpread() {
    if (!this.pages || !this.pages.length) return;
    if (this.isDualPage) {
      if (this.currentPage === 1) {
        const hasRight = !!(this.rightPageEl && this.rightPageEl.querySelector('.page-body'));
        if (!hasRight) this.render();
      } else if (this.currentPage === this.totalPages) {
        const hasLeft = !!(this.leftPageEl && this.leftPageEl.querySelector('.page-body'));
        if (!hasLeft) this.render();
      } else {
        const hasLeft = !!(this.leftPageEl && this.leftPageEl.querySelector('.page-body'));
        const hasRight = !!(this.rightPageEl && this.rightPageEl.querySelector('.page-body'));
        if (!hasLeft || !hasRight) this.render();
      }
    } else {
      const hasRight = !!(this.rightPageEl && this.rightPageEl.querySelector('.page-body'));
      if (!hasRight) this.render();
    }
  }

  clearPage(container) {
    if (!container) return;
    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-info">
          <span class="page-header-title" style="opacity:0.4;">☸ Tantra Gyan</span>
        </div>
      </div>
      <div class="page-body" style="display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; opacity:0.6; min-height:0;">
        <p style="font-style:italic; font-family:var(--font-heading); font-size:1.15rem; color:var(--accent-gold);">ॐ नमः शिवाय</p>
      </div>
      <div class="page-footer">
        <span></span>
        <span class="page-number-display"></span>
      </div>
    `;
  }
}

// Global book engine instance
window.bookEngine = new BookEngine();

// Auto-boot BookEngine across all browsers and environments
function bootBookEngine() {
  if (window.bookEngine && !window.bookEngine.isInitialized) {
    window.bookEngine.init();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', bootBookEngine);
} else {
  // Document is already interactive or complete
  bootBookEngine();
}

window.addEventListener('load', () => {
  bootBookEngine();
  if (window.bookEngine) {
    window.bookEngine.checkAndRepairSpread();
  }
});

window.addEventListener('pageshow', () => {
  if (window.bookEngine) {
    window.bookEngine.checkAndRepairSpread();
  }
});
