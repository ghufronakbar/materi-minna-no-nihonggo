// Ubah file soal Markdown menjadi PDF A4 dengan Playwright (Chromium).
// Cadangan untuk build-pdf.sh di lingkungan tanpa Google Chrome Mac, misalnya sesi cloud.
// Pakai: NODE_PATH=$(npm root -g) node soal/build-pdf-playwright.js soal/bab-15
//        NODE_PATH=$(npm root -g) node soal/build-pdf-playwright.js soal/bab-15/tes-kotoba-bab-15.md
// Butuh: Node.js (npx) dan paket playwright beserta Chromium-nya.
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('Pakai: node build-pdf-playwright.js <folder-bab atau file.md>');
  process.exit(1);
}

const files = fs.statSync(args[0]).isDirectory()
  ? fs.readdirSync(args[0]).filter((f) => f.endsWith('.md')).map((f) => path.join(args[0], f))
  : args;
const css = fs.readFileSync(path.join(__dirname, 'style.css'), 'utf8');

(async () => {
  const browser = await chromium.launch();
  for (const md of files) {
    const body = execFileSync('npx', ['--yes', 'marked@12.0.2', '--gfm', '-i', md], { encoding: 'utf8' });
    const title = (fs.readFileSync(md, 'utf8').match(/^# (.*)$/m) || [])[1] || '';
    const page = await browser.newPage();
    await page.setContent(
      `<!doctype html><html lang="id"><head><meta charset="utf-8"><title>${title}</title>` +
        `<style>${css}</style></head><body>${body}</body></html>`,
      { waitUntil: 'load' }
    );
    const out = md.replace(/\.md$/, '.pdf');
    await page.pdf({ path: out, format: 'A4', preferCSSPageSize: true });
    await page.close();
    console.log('PDF:', out);
  }
  await browser.close();
})();
