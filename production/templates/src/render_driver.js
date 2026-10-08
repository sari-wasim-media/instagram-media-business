// Screenshot driver for render_piece.py — one Chromium, many frames.
// Reads a job JSON: { frames: [ { html, width, height, shots: [ { t, png } ] } ] }
// For every shot it freezes all CSS animations at time t (seconds) and writes a PNG.
// Local production aid: it reads and writes files only; it touches nothing outside this machine.
const fs = require("fs");
const { chromium } = require("playwright");

(async () => {
  const job = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
  const browser = await chromium.launch();
  try {
    for (const f of job.frames) {
      const page = await browser.newPage({ viewport: { width: f.width, height: f.height }, deviceScaleFactor: 1 });
      await page.goto("file://" + f.html, { waitUntil: "load" });
      await page.evaluate(() => document.fonts.ready);
      for (const s of f.shots) {
        await page.evaluate((ms) => {
          for (const a of document.getAnimations()) { a.pause(); a.currentTime = ms; }
        }, s.t * 1000);
        await page.screenshot({ path: s.png, clip: { x: 0, y: 0, width: f.width, height: f.height } });
      }
      await page.close();
    }
  } finally {
    await browser.close();
  }
})().catch((e) => { console.error(e); process.exit(1); });
