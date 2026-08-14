# Bonus pack site — Hawaii by Land and Sea 2027

Three pages. Static HTML, no build step, no dependencies.

```
index.html     the bonus pack landing page  <- your QR code points here
review.html    redirects to your Amazon review page
updates.html   the living corrections page
files/         the downloadable files
```

---

## The one rule

**The QR code in your printed book points at YOUR page, never at Amazon.**

Print is permanent. A redirect is not. Publish the book, get your ASIN, edit one
line here, and every copy ever printed now works. This is why you do not need the
ASIN before uploading.

---

## Deploy in five minutes

### GitHub Pages (simplest, free)

1. Create a new public repo, e.g. `hawaii-2027`
2. Upload these files to the root of it
3. Settings → Pages → Source: `main`, folder `/ (root)` → Save
4. Live in about a minute at
   `https://YOURNAME.github.io/hawaii-2027/`

### Vercel (also free, custom domain is easier)

1. vercel.com → New Project → import the repo, or drag the folder in
2. Framework preset: **Other**. No build command. Output directory: leave blank
3. Deploy

Either works. If you own a domain, point it at the deployment and use a short
path like `yoursite.com/hawaii`, which prints better under a QR code.

---

## After you publish the book

1. Find your **ASIN** in the KDP Bookshelf, or in the product URL:
   `amazon.com/dp/B0XXXXXXXX` — that code is the ASIN.
2. Open `review.html`. Replace `REPLACE_WITH_YOUR_ASIN` in **both** places.
3. Commit. Done. Nothing in the printed book changes.

The review link uses Amazon's direct review form:
`https://www.amazon.com/review/create-review?asin=YOUR_ASIN`
That opens the write-a-review box rather than the product page, which removes a
step and measurably improves how many people finish.

---

## The QR codes

Generate two, both **static**, not tracked or dynamic. A dynamic QR depends on a
third-party service that can start charging or shut down, and your book is in
print for years.

| Goes in | Points at |
|---|---|
| Bonus pack page | `https://yoursite.com/hawaii/` |
| Review page | `https://yoursite.com/hawaii/review.html` |

QR Code Monkey is fine. Settings that matter:

- **Error correction: H.** Survives printing and scuffing.
- **Black on white.** No gradients, no logo in the middle.
- **Download as SVG or PNG at 1000px+.**
- Place at **1.2 inches square minimum** with clear white space around it.

**Scan the printed proof, not the screen.** A QR that works on a monitor can fail
on paper at small sizes. This is the single most common QR mistake in self
publishing.

---

## Keeping the update page alive

Update the "Last checked" date on `updates.html` every couple of months even if
nothing changed. A recent date is what tells a reader the page is maintained, and
that is the whole reason it beats a competitor's static book.

When something does change, copy the commented-out template block in
`updates.html`, fill it in, and put it at the top.

Things worth watching:
- The cruise green fee appeal, which was unresolved at the time of printing
- Reservation windows and prices at Haleakalā, Hāʻena, Hanauma Bay, Diamond Head
- Kīlauea eruption status and park closures
- West Maui reopening progress
- Any change to state or county lodging tax rates
