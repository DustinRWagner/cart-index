# The Cart Index 🛒

**A hyperlocal grocery price index for Folsom, California — the same 14-item basket, priced every Monday at four Folsom stores from each retailer's own published prices. Fully open-source.**

The BLS publishes CPI for the Sacramento–Roseville–Folsom metro **every other month**, at the metro level. The Cart Index measures food prices **in Folsom, weekly, store by store**, and publishes every observation. It answers two questions no official statistic answers:

1. **What is grocery inflation in Folsom, this week?**
2. **Which store has the cheapest full cart right now — and what is switching worth per year?**

Live site: `https://YOUR-USERNAME.github.io/cart-index/` (custom domain optional — see setup)

---

## The four tracked stores

Chosen to span the full price spectrum, all inside Folsom city limits, all with store-specific prices published on their own websites (so the basket can be priced remotely, the same way, every week):

| Store | Address | Tier | Where prices come from |
|---|---|---|---|
| Walmart Supercenter | 1018 Riley St | Discount anchor | walmart.com (set store: Folsom) |
| Target | 430 Blue Ravine Rd | Mass / value | target.com (set store: Folsom) |
| Safeway | 1850 Prairie City Rd | Mainstream national | safeway.com (set store: Prairie City Rd) |
| Bel Air | 2760 E Bidwell St | Regional / premium | shop.raleys.com (set store: Bel Air Folsom) |

### Stores deliberately excluded (and why — this is part of the methodology)

- **WinCo Foods (200 Blue Ravine Rd)** — likely the lowest-priced grocer in Folsom, but WinCo publishes no online prices at all. Excluding it means this index **understates how cheap the cheapest option in Folsom really is**; that limitation is disclosed everywhere. If in-person collection ever becomes possible, WinCo is the first store to add.
- **Trader Joe's** — nearly all private-label; a fixed comparable basket can't be constructed across stores.
- **Grocery Outlet** — opportunistic, rotating inventory; a fixed basket can't be tracked week to week.
- **Whole Foods (Palladio)** — doesn't carry several national-brand anchor items in the basket.
- **Costco** — membership pricing and bulk pack sizes aren't comparable to standard retail units.

### Conflict-of-interest disclosure (required reading)

The founder works part-time at **Raley's #410 (25025 Blue Ravine Rd, Folsom)**. For that reason:
- The Raley's-family data point is **Bel Air on E Bidwell St — a different store**, never store #410.
- Every price used is the retailer's **own publicly published online price**. Zero internal information (costs, planned price changes, systems access) is used — ever.
- This disclosure appears on the site, in this README, and in any media conversation. Check the employee handbook / ask a manager before launch; if the employer prefers, the Bel Air data point can be anonymized or replaced with the E Bidwell Raley's under the same rules.

## The basket (14 items, precisely defined)

Every item exists at all four stores in a comparable form. National brands are used where exact SKU-level comparability matters; store brands where the commodity itself is the standard.

| # | Item (exact definition) | Unit | Category |
|---|---|---|---|
| 1 | Whole milk, store brand | 1 gal | Dairy & Eggs |
| 2 | Large white eggs, grade A, store brand (cheapest conventional) | dozen | Dairy & Eggs |
| 3 | Tillamook medium cheddar | 8 oz | Dairy & Eggs |
| 4 | Boneless skinless chicken breast, store brand tray | per lb | Meat & Poultry |
| 5 | Ground beef 80/20, store brand | per lb | Meat & Poultry |
| 6 | Bananas, conventional | per lb | Produce |
| 7 | Baby carrots, store brand | 1 lb bag | Produce |
| 8 | Romaine hearts | 3 ct | Produce |
| 9 | Cheerios (plain) | 18 oz | Pantry |
| 10 | Jif creamy peanut butter | 16 oz | Pantry |
| 11 | Barilla spaghetti | 16 oz | Pantry |
| 12 | White sandwich bread, store brand | ~20 oz loaf | Pantry |
| 13 | Coca-Cola | 2 L | Beverages |
| 14 | Starbucks Pike Place, ground | 12 oz | Beverages |

**Fallback rules (write these down once, follow them forever):**
- Out of stock online → leave the price blank for that store-week and note it in the commit message. Never substitute silently.
- Package size changes (shrinkflation!) → record the new size in the commit message and keep tracking; a size change *is* a finding worth a post.
- Only the **regular listed price** is recorded. Sale/member prices go in the commit note, not the data.

## Methodology

- **Measurement definition:** the price shown on each retailer's own website/app with the named Folsom store selected (pickup mode), recorded every Monday morning in a fixed store order.
- **Honest caveat, stated up front:** some retailers' online prices can differ from their in-store shelf prices (Safeway says so explicitly). That biases the *level* of a cart total, but the **index measures change over time using the identical instrument every week** — which is what makes week-over-week and cumulative inflation numbers meaningful. Consistency of instrument > perfection of instrument. Say exactly this when asked.
- **Weighted Laspeyres index**, base week = 100, BLS food-at-home-style category weights (editable in `CONFIG.WEIGHTS` in `index.html`): Meat & Poultry 0.25, Pantry 0.22, Dairy & Eggs 0.20, Produce 0.20, Beverages 0.13.

  `Index_t = 100 × Σ_c  w_c × ( Σ prices in category c at week t ÷ Σ prices in category c at week 0 )`

- **Cheapest full cart:** raw 14-item basket total per store per week; the spread drives the savings calculator.

### Why this is NOT web-scraped (interviewers will ask; here's the answer)

Automated scraping of grocery sites (a) violates most retailers' terms of service, (b) is technically fragile behind anti-bot systems, and (c) would be a terrible look for a project whose entire value is credibility — especially run by a grocery employee. Instead, the human reads 56 published prices into a spreadsheet once a week (~30–40 minutes), and **everything downstream is automated**: the site recomputes the index, the charts, the cheapest cart, and the savings math in the browser on every visit, from the CSV alone. Manual where integrity matters, automated everywhere else.

## Weekly workflow (30–40 min, fully remote, zero coding)

1. Monday morning, open the four sites with the Folsom stores selected. Same store order every week.
2. Enter the 56 prices into your tracking sheet (a Google Sheet with one row per item-store works well; export CSV) — or type them straight into GitHub (step 3).
3. On github.com, open `data/prices.csv` → pencil icon (**Edit in place**) → paste the new week's rows at the bottom → **Commit changes**. That's the entire "coding." The live site updates itself within a minute or two.
4. Post the Monday number (see `GET_IT_NOTICED.md`).

## "But isn't this just a GitHub thing?" — No.

GitHub here plays two invisible roles: it stores the data publicly (which is what makes the index auditable and credible), and **GitHub Pages turns the repo into a real public website** with a normal URL. Visitors never see GitHub, never need an account, never know it's involved. And with a ~$12/year custom domain (e.g. `folsomcartindex.com`), the address on your LinkedIn, your applications, and the local paper is a clean brand — not a github.io link.

### Setup (~20 minutes, once)

1. Create a free GitHub account → **New repository** → name it `cart-index`, set Public → **uploading an existing file** → drag in `index.html`, `README.md`, `GET_IT_NOTICED.md`, and the `data` folder → Commit.
2. Repo **Settings → Pages → Source: Deploy from a branch → main / (root) → Save.** Two minutes later the site is live at `https://YOUR-USERNAME.github.io/cart-index/`.
3. Open `index.html` in the repo → pencil icon → set `CONFIG.GITHUB_URL` to your repo's URL → Commit.
4. Optional custom domain: buy `folsomcartindex.com` (Namecheap/Cloudflare, ~$12/yr) → repo Settings → Pages → Custom domain → follow the DNS instructions shown.
5. Do collection #1, replace the contents of `data/prices.csv` (keep the header row). The "simulated sample data" badge disappears automatically.

## Repo structure & data schema

```
cart-index/
├── index.html          # the entire dashboard (CONFIG at the top of the <script>)
├── GET_IT_NOTICED.md   # the launch & promotion playbook
├── data/
│   └── prices.csv      # ⚠ currently SIMULATED SAMPLE DATA — replace with week 1
└── README.md
```

```csv
date,store,item,category,unit,price
2026-07-06,Walmart - Riley St,Cheerios,Pantry,18 oz,5.49
```
`date` = the Monday of collection (`YYYY-MM-DD`) · `category` must match a `CONFIG.WEIGHTS` key · no commas inside fields.

## Impact metrics — log these in an IMPACT.md from day one

Consecutive weeks published (the streak is the story) · total price observations (14 × 4 × weeks) · this-week and cumulative spread ("families following the cheapest-cart signal have saved $X") · divergence vs. the BLS Sacramento-area food-at-home CPI at each bimonthly release · site visitors, repo stars/forks · media and civic touchpoints · other cities recruited.

## Roadmap

Overlay the BLS Sacramento CPI series on the chart at each release → single-item deep dives when something moves (the egg index, the coffee index) → one-paragraph Monday commentary (a free writing portfolio) → recruit one student in another city to fork it (the first student-run multi-city grocery price network) → semester-end working paper: *Weekly Hyperlocal Grocery Price Dynamics in Folsom, CA*, brought into the statistical economics course.

---

*Independent student research. Not affiliated with, endorsed by, or informed by any retailer. All prices are the retailers' own publicly published prices for their Folsom stores.*
