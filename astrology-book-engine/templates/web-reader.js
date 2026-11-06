/**
 * Tantra Gyan Astrology Book Engine - Client-Side Interactive Web Reader
 * Powered by Paged.js polyfill with zero backend dependency.
 */

document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const loadingOverlay = document.getElementById("paged-loading-overlay");
  const pageIndicator = document.getElementById("page-indicator");
  const chapterSelect = document.getElementById("reader-chapter-select");
  const btnPrev = document.getElementById("btn-prev-page");
  const btnNext = document.getElementById("btn-next-page");
  const btnSpreadToggle = document.getElementById("btn-spread-toggle");
  const btnThemeToggle = document.getElementById("btn-theme-toggle");
  const btnZoomIn = document.getElementById("btn-zoom-in");
  const btnZoomOut = document.getElementById("btn-zoom-out");
  const btnFullscreen = document.getElementById("btn-fullscreen");
  const stage = document.querySelector(".reader-stage-container");

  let currentPageIndex = 0;
  let totalPages = 0;
  let zoomLevel = 1.0;

  // Initialize Paged.js hooks
  if (typeof Paged !== "undefined") {
    class ReaderHandler extends Paged.Handler {
      constructor(chunker, polisher, caller) {
        super(chunker, polisher, caller);
      }

      afterPageLayout(pageElement, page, breakToken, chunker) {
        // Track pages as they are built
        totalPages = chunker.pages.length;
        if (pageIndicator) {
          pageIndicator.textContent = `Page 1 of ${totalPages}`;
        }
      }

      afterRendered(pages) {
        totalPages = pages.length;
        if (pageIndicator) {
          pageIndicator.textContent = `1 / ${totalPages}`;
        }
        if (loadingOverlay) {
          loadingOverlay.style.opacity = "0";
          setTimeout(() => {
            loadingOverlay.style.display = "none";
          }, 400);
        }
        setupChapterSync();
        scrollToPage(0);
      }
    }
    Paged.registerHandlers(ReaderHandler);
  } else {
    // If not using Paged.js directly
    if (loadingOverlay) {
      loadingOverlay.style.display = "none";
    }
  }

  // Navigation Logic
  function getAllPages() {
    return document.querySelectorAll(".pagedjs_page");
  }

  function scrollToPage(index) {
    const pages = getAllPages();
    if (!pages || pages.length === 0) return;

    if (index < 0) index = 0;
    if (index >= pages.length) index = pages.length - 1;

    currentPageIndex = index;
    pages[index].scrollIntoView({ behavior: "smooth", block: "start", inline: "center" });

    if (pageIndicator) {
      pageIndicator.textContent = `${index + 1} / ${pages.length}`;
    }
  }

  function nextPage() {
    const step = body.classList.contains("mode-spread") ? 2 : 1;
    scrollToPage(currentPageIndex + step);
  }

  function prevPage() {
    const step = body.classList.contains("mode-spread") ? 2 : 1;
    scrollToPage(currentPageIndex - step);
  }

  if (btnNext) btnNext.addEventListener("click", nextPage);
  if (btnPrev) btnPrev.addEventListener("click", prevPage);

  // Keyboard Shortcuts
  window.addEventListener("keydown", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") return;

    switch (e.key) {
      case "ArrowRight":
      case "PageDown":
        e.preventDefault();
        nextPage();
        break;
      case "ArrowLeft":
      case "PageUp":
        e.preventDefault();
        prevPage();
        break;
      case "Home":
        e.preventDefault();
        scrollToPage(0);
        break;
      case "End":
        e.preventDefault();
        scrollToPage(totalPages - 1);
        break;
      case "f":
      case "F":
        toggleFullscreen();
        break;
    }
  });

  // Chapter Jump Sync
  function setupChapterSync() {
    if (!chapterSelect) return;
    chapterSelect.addEventListener("change", (e) => {
      const targetId = e.target.value;
      if (!targetId) return;

      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        // Find parent pagedjs_page
        const pageEl = targetEl.closest(".pagedjs_page");
        if (pageEl) {
          const allPages = Array.from(getAllPages());
          const pIndex = allPages.indexOf(pageEl);
          if (pIndex !== -1) {
            scrollToPage(pIndex);
          }
        } else {
          targetEl.scrollIntoView({ behavior: "smooth" });
        }
      }
    });
  }

  // Spread Mode Toggle
  if (btnSpreadToggle) {
    btnSpreadToggle.addEventListener("click", () => {
      if (body.classList.contains("mode-spread")) {
        body.classList.remove("mode-spread");
        body.classList.add("mode-single");
        btnSpreadToggle.innerHTML = `<span>📄</span> <span>Single</span>`;
      } else {
        body.classList.remove("mode-single");
        body.classList.add("mode-spread");
        btnSpreadToggle.innerHTML = `<span>📖</span> <span>Spread</span>`;
      }
      scrollToPage(currentPageIndex);
    });
  }

  // Theme Toggle: Parchment -> Dark -> White
  const themes = ["theme-dark", "theme-parchment", "theme-white"];
  let currentThemeIdx = 0;

  if (btnThemeToggle) {
    btnThemeToggle.addEventListener("click", () => {
      body.classList.remove(themes[currentThemeIdx]);
      currentThemeIdx = (currentThemeIdx + 1) % themes.length;
      body.classList.add(themes[currentThemeIdx]);

      const labels = ["🌙 Dark", "📜 Parchment", "☀️ White"];
      btnThemeToggle.innerHTML = `<span>🎨</span> <span>${labels[currentThemeIdx]}</span>`;
    });
  }

  // Zoom Controls
  function applyZoom() {
    const container = document.querySelector(".pagedjs_pages");
    if (container) {
      container.style.transform = `scale(${zoomLevel})`;
    }
  }

  if (btnZoomIn) {
    btnZoomIn.addEventListener("click", () => {
      if (zoomLevel < 1.6) {
        zoomLevel += 0.1;
        applyZoom();
      }
    });
  }

  if (btnZoomOut) {
    btnZoomOut.addEventListener("click", () => {
      if (zoomLevel > 0.6) {
        zoomLevel -= 0.1;
        applyZoom();
      }
    });
  }

  // Fullscreen Toggle
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
      }
    }
  }

  if (btnFullscreen) {
    btnFullscreen.addEventListener("click", toggleFullscreen);
  }
});
