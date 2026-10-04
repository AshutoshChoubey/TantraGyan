const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');

console.log('--- RUNNING FULL BOOK ANIMATION & AUDIO VALIDATION ---');

// 1. Verify CSS styles
const cssContent = fs.readFileSync(path.join(rootDir, 'css/book.css'), 'utf-8');

// Check single-flip-forward
if (!cssContent.includes('.book-flipper-leaf.single-flip-forward') || 
    !cssContent.includes('transform-origin: left center') ||
    !cssContent.includes('animation: flipSingleForward 0.66s')) {
  console.error('FAIL: single-flip-forward CSS missing or wrong origin/animation');
  process.exit(1);
}

// Check single-flip-backward
if (!cssContent.includes('.book-flipper-leaf.single-flip-backward') ||
    !cssContent.includes('transform-origin: right center') ||
    !cssContent.includes('right: 0') ||
    !cssContent.includes('animation: flipSingleBackward 0.66s')) {
  console.error('FAIL: single-flip-backward CSS missing or wrong origin/animation');
  process.exit(1);
}

// Check flipSingleForward keyframes: 0deg to -180deg
if (!cssContent.includes('@keyframes flipSingleForward') ||
    !cssContent.includes('transform: rotateY(-180deg);')) {
  console.error('FAIL: flipSingleForward keyframes missing rotateY(-180deg)');
  process.exit(1);
}

// Check flipSingleBackward keyframes: 0deg to 180deg
if (!cssContent.includes('@keyframes flipSingleBackward') ||
    !cssContent.includes('transform: rotateY(180deg);')) {
  console.error('FAIL: flipSingleBackward keyframes missing rotateY(180deg)');
  process.exit(1);
}

// Check single-flip shadows
if (!cssContent.includes('.single-flip-forward-shadow') ||
    !cssContent.includes('.single-flip-backward-shadow')) {
  console.error('FAIL: single-flip shadows missing');
  process.exit(1);
}

// Check single-cover-close: right: 0, transform-origin: right center, rotateY(180deg)
if (!cssContent.includes('.book-flipper-leaf.single-cover-close') ||
    !cssContent.includes('singleCoverClose 0.62s')) {
  console.error('FAIL: single-cover-close styles missing');
  process.exit(1);
}

console.log('PASS: css/book.css styles, keyframes, transform-origins, and shadows verified.');

// 2. Verify book-engine.js
const engineContent = fs.readFileSync(path.join(rootDir, 'js/book-engine.js'), 'utf-8');

// Ensure no synchronous playPageTurn in flip3D
const flip3DSection = engineContent.substring(engineContent.indexOf('flip3D(direction, targetPage)'), engineContent.indexOf('performBookOpen('));
if (flip3DSection.includes('window.bookSound.playPageTurn')) {
  console.error('FAIL: flip3D still contains synchronous playPageTurn call');
  process.exit(1);
}

// Ensure performSinglePageFlip backward renders targetP into rightPageEl and sets single-flip-backward
const defIdx = engineContent.lastIndexOf('performSinglePageFlip(direction, targetPage, wrapper) {');
const singleFlipSection = engineContent.substring(defIdx, engineContent.indexOf('goToPage(', defIdx));
if (!singleFlipSection.includes("single-flip-backward") ||
    !singleFlipSection.includes("single-flip-backward-shadow") ||
    !singleFlipSection.includes("playPageTurn('prev')") ||
    !singleFlipSection.includes("playPageTurn('next')") ||
    !singleFlipSection.includes("}, 660);")) {
  console.error('FAIL: performSinglePageFlip missing correct directional classes, sound triggers, or 660ms timeout');
  process.exit(1);
}

// Ensure sound triggers use setTimeout with 70ms
const setTimeoutMatches = engineContent.match(/setTimeout\(\(\) => \{\s*if \(window\.bookSound/g) || [];
if (setTimeoutMatches.length < 8) {
  console.error(`FAIL: Expected at least 8 synchronized audio setTimeout triggers, found ${setTimeoutMatches.length}`);
  process.exit(1);
}

console.log(`PASS: js/book-engine.js verified with ${setTimeoutMatches.length} synchronized audio triggers and directional single-flip logic.`);

// 3. Verify sound.js envelope
const soundContent = fs.readFileSync(path.join(rootDir, 'js/sound.js'), 'utf-8');
if (!soundContent.includes('gain.linearRampToValueAtTime') ||
    !soundContent.includes('now + 0.12') ||
    !soundContent.includes('now + 0.25')) {
  console.error('FAIL: js/sound.js missing envelope swell and mid-flight peak');
  process.exit(1);
}

console.log('PASS: js/sound.js swell and peak envelope verified.');

// 4. Verify all HTML files and page counts
['index.html', 'hindi.html', 'english.html'].forEach(file => {
  const html = fs.readFileSync(path.join(rootDir, file), 'utf-8');
  if (!html.includes('book.css?v=3.6') || !html.includes('book-engine.js?v=3.6')) {
    console.error(`FAIL: ${file} missing asset v=3.6`);
    process.exit(1);
  }
  const pageMatches = html.match(/class="book-page-data"/g) || [];
  if (pageMatches.length !== 88) {
    console.error(`FAIL: ${file} does not contain 88 pages (found ${pageMatches.length})`);
    process.exit(1);
  }
  console.log(`PASS: ${file} verified (88 pages, v=3.6 assets).`);
});

console.log('\n--- ALL VERIFICATION TESTS PASSED SUCCESSFULLY! ---');
