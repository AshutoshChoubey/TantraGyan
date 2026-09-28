/**
 * Tantra Gyan Vedic Astrology Book - Core Flip Engine
 * Controls realistic two-page book spreads, page turns, keyboard/touch navigation,
 * and page progress tracking.
 */

class BookEngine {
  constructor() {
    this.currentPage = 1;
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
  }

  init() {
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
    if (window.location.hash) {
      const match = window.location.hash.match(/#page-(\d+)/);
      if (match && parseInt(match[1])) {
        startPage = parseInt(match[1]);
      }
    } else {
      try {
        const saved = localStorage.getItem('tantra_book_page');
        if (saved) startPage = parseInt(saved);
      } catch (e) {}
    }

    startPage = Math.max(1, Math.min(this.totalPages, startPage));

    // Handle responsive spread mode
    this.updateSpreadMode();
    window.addEventListener('resize', () => {
      this.updateSpreadMode();
      this.render();
    });

    // Bind event listeners
    this.bindEvents();

    // Render initial page
    this.goToPage(startPage, false);
  }

  updateSpreadMode() {
    const forcedSingle = document.documentElement.classList.contains('single-mode-active');
    this.isDualPage = window.innerWidth > 1080 && !forcedSingle;
    const bookContainer = document.querySelector('.book-container');
    if (bookContainer) {
      if (this.isDualPage) {
        bookContainer.classList.add('dual-page-layout');
        bookContainer.classList.remove('single-page-layout');
      } else {
        bookContainer.classList.remove('dual-page-layout');
        bookContainer.classList.add('single-page-layout');
      }
    }
  }

  bindEvents() {
    if (this.prevBtn) {
      this.prevBtn.addEventListener('click', () => this.prevPage());
    }
    if (this.nextBtn) {
      this.nextBtn.addEventListener('click', () => this.nextPage());
    }

    if (this.slider) {
      this.slider.addEventListener('input', (e) => {
        const p = parseInt(e.target.value);
        this.goToPage(p, true);
      });
    }

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
      // Don't intercept if user is typing in search input
      if (e.target && e.target.tagName === 'INPUT') return;

      if (e.key === 'ArrowRight' || e.key === 'PageDown' || (e.key === ' ' && !e.shiftKey)) {
        e.preventDefault();
        this.nextPage();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || (e.key === ' ' && e.shiftKey)) {
        e.preventDefault();
        this.prevPage();
      } else if (e.key === 'Home') {
        e.preventDefault();
        this.goToPage(1);
      } else if (e.key === 'End') {
        e.preventDefault();
        this.goToPage(this.totalPages);
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

        // Decisive horizontal swipe: fast (< 500ms), at least 65px horizontal, predominantly horizontal
        if (timeDiff < 500 && Math.abs(diffX) > 65 && Math.abs(diffX) > Math.abs(diffY) * 1.8) {
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
    const step = this.isDualPage ? 2 : 1;
    if (this.currentPage + step <= this.totalPages) {
      this.flipAnimation('forward', () => {
        this.goToPage(this.currentPage + step, true, 'next');
      });
    } else if (this.currentPage < this.totalPages) {
      this.flipAnimation('forward', () => {
        this.goToPage(this.totalPages, true, 'next');
      });
    }
  }

  prevPage() {
    if (this.isAnimating) return;
    const step = this.isDualPage ? 2 : 1;
    if (this.currentPage - step >= 1) {
      this.flipAnimation('backward', () => {
        this.goToPage(this.currentPage - step, true, 'prev');
      });
    } else if (this.currentPage > 1) {
      this.flipAnimation('backward', () => {
        this.goToPage(1, true, 'prev');
      });
    }
  }

  flipAnimation(direction, callback) {
    this.isAnimating = true;
    const wrapper = document.querySelector('.book-pages-wrapper');
    if (wrapper) {
      const animClass = direction === 'forward' ? 'page-flip-anim-forward' : 'page-flip-anim-backward';
      wrapper.classList.add(animClass);
      setTimeout(() => {
        wrapper.classList.remove(animClass);
        callback();
        this.isAnimating = false;
      }, 250);
    } else {
      callback();
      this.isAnimating = false;
    }
  }

  goToPage(pageNum, playSound = false, soundDir = 'next') {
    if (pageNum < 1) pageNum = 1;
    if (pageNum > this.totalPages) pageNum = this.totalPages;

    // In dual-page mode, if on cover (page 1), show cover alone or with blank/preface
    // Keep page alignments natural: odd page on right or left
    if (this.isDualPage && pageNum > 1 && pageNum % 2 !== 0) {
      // align to even page for spread: e.g. 2 & 3, 4 & 5
      pageNum = pageNum - 1;
    }

    this.currentPage = pageNum;

    // Play synthesized realistic paper sound
    if (playSound && window.bookSound) {
      window.bookSound.playPageTurn(soundDir);
    }

    this.render();

    // Update URL hash and localStorage
    try {
      history.replaceState(null, null, `#page-${this.currentPage}`);
      localStorage.setItem('tantra_book_page', this.currentPage.toString());
    } catch (e) {}
  }

  render() {
    if (!this.pages.length) return;

    // Dual page mode
    if (this.isDualPage) {
      if (this.currentPage === 1) {
        // Front Cover spread: Left is inside front or intro, right is cover
        this.renderSinglePageContent(this.leftPageEl, this.pages[0], 1);
        if (this.pages[1]) {
          this.renderSinglePageContent(this.rightPageEl, this.pages[1], 2);
        } else {
          this.clearPage(this.rightPageEl);
        }
      } else {
        const leftIdx = this.currentPage - 1;
        const rightIdx = this.currentPage;

        if (this.pages[leftIdx]) {
          this.renderSinglePageContent(this.leftPageEl, this.pages[leftIdx], this.currentPage);
        } else {
          this.clearPage(this.leftPageEl);
        }

        if (this.pages[rightIdx]) {
          this.renderSinglePageContent(this.rightPageEl, this.pages[rightIdx], this.currentPage + 1);
        } else {
          this.clearPage(this.rightPageEl);
        }
      }
    } else {
      // Single Page Mode: Only render to right page container
      const idx = this.currentPage - 1;
      if (this.pages[idx]) {
        this.renderSinglePageContent(this.rightPageEl, this.pages[idx], this.currentPage);
      }
    }

    // Scroll page body back to top on page change
    if (this.leftPageEl) {
      const b1 = this.leftPageEl.querySelector('.page-body');
      if (b1) b1.scrollTop = 0;
    }
    if (this.rightPageEl) {
      const b2 = this.rightPageEl.querySelector('.page-body');
      if (b2) b2.scrollTop = 0;
    }

    // Update Slider and Counter
    if (this.slider) {
      this.slider.value = this.currentPage;
    }
    if (this.counter) {
      if (this.isDualPage && this.currentPage < this.totalPages) {
        this.counter.textContent = `Page ${this.currentPage}-${this.currentPage + 1} of ${this.totalPages}`;
      } else {
        this.counter.textContent = `Page ${this.currentPage} of ${this.totalPages}`;
      }
    }

    // Update reading progress bar
    if (this.progressFill) {
      const pct = Math.round((this.currentPage / this.totalPages) * 100);
      this.progressFill.style.width = `${pct}%`;
    }

    // Update Button Disabled States
    if (this.prevBtn) {
      this.prevBtn.disabled = this.currentPage <= 1;
    }
    if (this.nextBtn) {
      this.nextBtn.disabled = this.currentPage >= this.totalPages;
    }

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
      if (this.currentPage === 1) return [1, 2];
      const pages = [this.currentPage];
      if (this.currentPage + 1 <= this.totalPages) {
        pages.push(this.currentPage + 1);
      }
      return pages;
    }
    return [this.currentPage];
  }

  renderSinglePageContent(container, pageDataNode, pageNum) {
    if (!container || !pageDataNode) return;

    const chapterTitle = pageDataNode.getAttribute('data-chapter') || 'Tantra Gyan';
    const pageHeaderTitle = pageDataNode.getAttribute('data-title') || chapterTitle;
    const isFirstPage = pageNum <= 1;
    const isLastPage = pageNum >= this.totalPages;

    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-info">
          <span class="page-header-title">
            <span style="color:var(--accent-gold);">☸</span> ${chapterTitle}
          </span>
          <span class="page-header-subtitle">${pageHeaderTitle}</span>
        </div>
        <div class="page-nav-quick top-quick-nav">
          <button type="button" class="page-nav-pill prev-pill" onclick="if(window.bookEngine) window.bookEngine.prevPage();" title="पिछला पृष्ठ (Previous Page)" ${isFirstPage ? 'disabled style="opacity:0.3; pointer-events:none;"' : ''}>
            ‹ पिछला
          </button>
          <button type="button" class="page-nav-pill next-pill" onclick="if(window.bookEngine) window.bookEngine.nextPage();" title="अगला पृष्ठ (Next Page)" ${isLastPage ? 'disabled style="opacity:0.3; pointer-events:none;"' : ''}>
            अगला ›
          </button>
        </div>
      </div>
      <div class="page-body">
        ${pageDataNode.innerHTML}
      </div>
      <div class="page-footer">
        <span class="page-footer-title">${document.documentElement.lang === 'en' ? 'Complete Vedic Astrology Compendium Simplified' : 'वैदिक ज्योतिष महाग्रंथ सरलीकृत'}</span>
        <div class="page-nav-quick bottom-quick-nav">
          <button type="button" class="page-nav-pill prev-pill" onclick="if(window.bookEngine) window.bookEngine.prevPage();" title="पिछला पृष्ठ (Previous Page)" ${isFirstPage ? 'disabled style="opacity:0.3; pointer-events:none;"' : ''}>
            ‹ पिछला
          </button>
          <span class="page-number-display">Page ${pageNum}</span>
          <button type="button" class="page-nav-pill next-pill" onclick="if(window.bookEngine) window.bookEngine.nextPage();" title="अगला पृष्ठ (Next Page)" ${isLastPage ? 'disabled style="opacity:0.3; pointer-events:none;"' : ''}>
            अगला ›
          </button>
        </div>
      </div>
    `;
  }

  clearPage(container) {
    if (!container) return;
    container.innerHTML = `
      <div class="page-header">
        <span class="page-header-title">☸ Tantra Gyan</span>
      </div>
      <div class="page-body" style="display:flex; align-items:center; justify-content:center; opacity:0.3;">
        <p style="font-style:italic;">ॐ नमः शिवाय</p>
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
