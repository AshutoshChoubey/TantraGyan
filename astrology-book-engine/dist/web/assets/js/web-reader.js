/**
 * Tantra Gyan Modern Rich-Text Book Reader Client Engine
 * Instant Zero-Lag Rendering • Interactive Spreads • Typography Controls
 */

document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const stage = document.getElementById("reader-stage");
  const chapterSelect = document.getElementById("reader-chapter-select");
  const btnPrev = document.getElementById("btn-prev-page");
  const btnNext = document.getElementById("btn-next-page");
  const btnSpreadToggle = document.getElementById("btn-spread-toggle");
  const btnThemeToggle = document.getElementById("btn-theme-toggle");
  const btnZoomIn = document.getElementById("btn-zoom-in");
  const btnZoomOut = document.getElementById("btn-zoom-out");
  const btnFullscreen = document.getElementById("btn-fullscreen");

  const sheets = Array.from(document.querySelectorAll(".book-sheet"));
  let currentSheetIdx = 0;
  let currentFontSizePt = 11;

  // Chapter Jump Sync
  if (chapterSelect) {
    chapterSelect.addEventListener("change", (e) => {
      const targetId = e.target.value;
      if (!targetId) return;

      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        targetEl.scrollIntoView({ behavior: "smooth", block: "start" });
        currentSheetIdx = sheets.indexOf(targetEl);
      }
    });
  }

  // Navigation Logic
  function scrollToSheet(idx) {
    if (idx < 0) idx = 0;
    if (idx >= sheets.length) idx = sheets.length - 1;
    currentSheetIdx = idx;
    sheets[idx].scrollIntoView({ behavior: "smooth", block: "start" });

    // Sync select dropdown
    const sheetId = sheets[idx].id;
    if (chapterSelect && sheetId) {
      chapterSelect.value = sheetId;
    }
  }

  function nextSection() {
    scrollToSheet(currentSheetIdx + 1);
  }

  function prevSection() {
    scrollToSheet(currentSheetIdx - 1);
  }

  if (btnNext) btnNext.addEventListener("click", nextSection);
  if (btnPrev) btnPrev.addEventListener("click", prevSection);

  // Keyboard Shortcuts
  window.addEventListener("keydown", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") return;

    switch (e.key) {
      case "ArrowRight":
      case "PageDown":
        e.preventDefault();
        nextSection();
        break;
      case "ArrowLeft":
      case "PageUp":
        e.preventDefault();
        prevSection();
        break;
      case "Home":
        e.preventDefault();
        scrollToSheet(0);
        break;
      case "End":
        e.preventDefault();
        scrollToSheet(sheets.length - 1);
        break;
      case "f":
      case "F":
        toggleFullscreen();
        break;
    }
  });

  // Spread Mode Toggle
  if (btnSpreadToggle) {
    btnSpreadToggle.addEventListener("click", () => {
      const label = btnSpreadToggle.querySelector(".btn-label");
      if (body.classList.contains("mode-spread")) {
        body.classList.remove("mode-spread");
        body.classList.add("mode-single");
        if (label) label.textContent = "Single Column";
      } else {
        body.classList.remove("mode-single");
        body.classList.add("mode-spread");
        if (label) label.textContent = "Two Pages";
      }
    });
  }

  // Theme Cycling
  const themes = ["theme-parchment", "theme-dark", "theme-white"];
  let themeIndex = 0;

  if (btnThemeToggle) {
    btnThemeToggle.addEventListener("click", () => {
      body.classList.remove(themes[themeIndex]);
      themeIndex = (themeIndex + 1) % themes.length;
      body.classList.add(themes[themeIndex]);

      const labels = ["📜 Parchment", "🌙 Dark", "☀️ White"];
      const label = btnThemeToggle.querySelector(".btn-label");
      if (label) label.textContent = labels[themeIndex];
    });
  }

  // Font Zoom
  if (btnZoomIn) {
    btnZoomIn.addEventListener("click", () => {
      if (currentFontSizePt < 18) {
        currentFontSizePt += 1;
        document.documentElement.style.setProperty("--book-font-size", `${currentFontSizePt}pt`);
      }
    });
  }

  if (btnZoomOut) {
    btnZoomOut.addEventListener("click", () => {
      if (currentFontSizePt > 9) {
        currentFontSizePt -= 1;
        document.documentElement.style.setProperty("--book-font-size", `${currentFontSizePt}pt`);
      }
    });
  }

  // Fullscreen
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
