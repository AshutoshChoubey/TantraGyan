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
    if (typeof window !== 'undefined' && window.location && window.location.hash) {
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

    // Render initial page without sound or animation
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
    if (this.isDualPage) {
      const currStart = (this.currentPage % 2 === 0) ? this.currentPage - 1 : this.currentPage;
      const targetStart = currStart + 2;
      if (targetStart <= this.totalPages) {
        this.flip3D('forward', targetStart);
      }
    } else {
      if (this.currentPage < this.totalPages) {
        this.flip3D('forward', this.currentPage + 1);
      }
    }
  }

  prevPage() {
    if (this.isAnimating) return;
    if (this.isDualPage) {
      const currStart = (this.currentPage % 2 === 0) ? this.currentPage - 1 : this.currentPage;
      const targetStart = currStart - 2;
      if (targetStart >= 1) {
        this.flip3D('backward', targetStart);
      }
    } else {
      if (this.currentPage > 1) {
        this.flip3D('backward', this.currentPage - 1);
      }
    }
  }

  /**
   * Executes a realistic physical 3D page turn
   * @param {string} direction - 'forward' or 'backward'
   * @param {number} targetPage - destination page number
   */
  flip3D(direction, targetPage) {
    if (this.isAnimating) return;
    this.isAnimating = true;

    // Trigger procedural audio instantly at the exact start of the turn
    if (window.bookSound) {
      window.bookSound.playPageTurn(direction === 'forward' ? 'next' : 'prev');
    }

    const wrapper = document.querySelector('.book-pages-wrapper');
    if (!wrapper) {
      this.currentPage = targetPage;
      this.render();
      this.onPageChanged();
      this.isAnimating = false;
      return;
    }

    // Clean up any lingering flipper nodes
    wrapper.querySelectorAll('.book-flipper-leaf, .flipper-under-shadow').forEach(el => el.remove());

    if (this.isDualPage) {
      this.performDualPageFlip(direction, targetPage, wrapper);
    } else {
      this.performSinglePageFlip(direction, targetPage, wrapper);
    }
  }

  performDualPageFlip(direction, targetPage, wrapper) {
    const currStart = (this.currentPage % 2 === 0) ? this.currentPage - 1 : this.currentPage;
    const currL = currStart;
    const currR = currStart + 1;

    const targetStart = (targetPage % 2 === 0) ? targetPage - 1 : targetPage;
    const targetL = targetStart;
    const targetR = targetStart + 1;

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
        this.renderSpread(targetL, targetR);
        this.onPageChanged();
        this.isAnimating = false;
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
        this.renderSpread(targetL, targetR);
        this.onPageChanged();
        this.isAnimating = false;
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
        this.onPageChanged();
        this.isAnimating = false;
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
        if (this.rightPageEl) {
          this.renderSinglePageContent(this.rightPageEl, this.pages[targetP - 1], targetP);
        }
        this.currentPage = targetP;
        this.onPageChanged();
        this.isAnimating = false;
      }, 520);
    }
  }

  goToPage(pageNum, playSound = false) {
    if (pageNum < 1) pageNum = 1;
    if (pageNum > this.totalPages) pageNum = this.totalPages;

    if (this.isDualPage) {
      const currStart = (this.currentPage % 2 === 0) ? this.currentPage - 1 : this.currentPage;
      const targetStart = (pageNum % 2 === 0) ? pageNum - 1 : pageNum;
      if (currStart === targetStart) {
        this.currentPage = pageNum;
        this.onPageChanged();
        return;
      }
      if (playSound && !this.isAnimating) {
        const dir = (targetStart > currStart) ? 'forward' : 'backward';
        this.flip3D(dir, targetStart);
        return;
      }
    } else {
      if (pageNum === this.currentPage) return;
      if (playSound && !this.isAnimating) {
        const dir = (pageNum > this.currentPage) ? 'forward' : 'backward';
        this.flip3D(dir, pageNum);
        return;
      }
    }

    this.currentPage = pageNum;
    this.render();
    this.onPageChanged();
  }

  render() {
    if (!this.pages.length) return;

    if (this.isDualPage) {
      const spreadStart = (this.currentPage % 2 === 0) ? this.currentPage - 1 : this.currentPage;
      this.renderSpread(spreadStart, spreadStart + 1);
    } else {
      if (this.rightPageEl && this.pages[this.currentPage - 1]) {
        this.renderSinglePageContent(this.rightPageEl, this.pages[this.currentPage - 1], this.currentPage);
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

    // Update Slider and Counter
    if (this.slider) {
      this.slider.value = this.currentPage;
    }
    if (this.counter) {
      if (this.isDualPage) {
        const spreadStart = (this.currentPage % 2 === 0) ? this.currentPage - 1 : this.currentPage;
        if (spreadStart < this.totalPages) {
          this.counter.textContent = `Page ${spreadStart}-${spreadStart + 1} of ${this.totalPages}`;
        } else {
          this.counter.textContent = `Page ${spreadStart} of ${this.totalPages}`;
        }
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

    // Update URL hash and localStorage
    try {
      history.replaceState(null, null, `#page-${this.currentPage}`);
      localStorage.setItem('tantra_book_page', this.currentPage.toString());
    } catch (e) {}

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
      const spreadStart = (this.currentPage % 2 === 0) ? this.currentPage - 1 : this.currentPage;
      const pages = [spreadStart];
      if (spreadStart + 1 <= this.totalPages) {
        pages.push(spreadStart + 1);
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

    const chapterTitle = node.getAttribute('data-chapter') || 'Tantra Gyan';
    const pageHeaderTitle = node.getAttribute('data-title') || chapterTitle;
    const isFirstPage = pageNum <= 1;
    const isLastPage = pageNum >= this.totalPages;
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
        ${node.innerHTML}
      </div>
      <div class="page-footer">
        <span class="page-footer-title">${footerTitle}</span>
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

  renderSinglePageContent(container, pageDataNode, pageNum) {
    if (!container) return;
    container.innerHTML = this.getPageHTML(pageNum);
  }

  clearPage(container) {
    if (!container) return;
    container.innerHTML = `
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
}

// Global book engine instance
window.bookEngine = new BookEngine();
