// Ubah daftar kosakata Markdown menjadi PDF A4 dengan Playwright (Chromium).
// Pakai: NODE_PATH=$(npm root -g) node kosakata/build-pdf.js kosakata/kosakata-bab-01-25.md
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const files = process.argv.slice(2);
if (files.length === 0) {
  console.error('Pakai: node build-pdf.js <file.md> [...]');
  process.exit(1);
}
const css = fs.readFileSync(path.join(__dirname, 'style.css'), 'utf8');

(async () => {
  const browser = await chromium.launch();
  for (const md of files) {
    const src = fs.readFileSync(md, 'utf8');
    const body = execFileSync('npx', ['--yes', 'marked@12.0.2', '--gfm'], { input: src, encoding: 'utf8' });
    const title = (src.match(/^# (.*)$/m) || [])[1] || '';
    const page = await browser.newPage();
    await page.setContent(
      `<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>${title}</title>` +
        `<style>${css}</style></head><body>${body}</body></html>`,
      { waitUntil: 'load' }
    );
    // Bab pertama langsung di bawah judul; bab berikutnya mulai di halaman baru.
    await page.evaluate(() => {
      const h = document.querySelector('h2');
      if (h) h.classList.add('awal');
    });
    const out = md.replace(/\.md$/, '.pdf');
    await page.pdf({ path: out, format: 'A4', preferCSSPageSize: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: '<div style="font-size:8pt;width:100%;text-align:center;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
    await page.close();
    console.log('PDF:', out);
  }
  await browser.close();
})();
