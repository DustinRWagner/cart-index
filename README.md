# The Cart Index

**A hyperlocal grocery price index for Folsom, California. The same 14-item basket, priced every Monday at three Folsom stores from each retailer's own published prices. Fully open source.**

The Bureau of Labor Statistics publishes no Consumer Price Index for the Sacramento area at any frequency. The nearest official benchmarks are the West region food-at-home CPI (monthly) and the San Francisco area CPI (every other month), both far coarser than a single city. The Cart Index measures food prices in Folsom, weekly, store by store, and publishes every observation. It answers two questions no official statistic answers:

1. **What is grocery inflation in Folsom, this week?**
2. **Which store has the cheapest full cart right now, and what is switching worth per year?**

Live site: `https://dustinrwagner.github.io/cart-index/` (custom domain optional; see setup)

---

## The three tracked stores

Chosen to span the price spectrum, all inside Folsom, all with store-specific prices published on their own websites, so the basket can be priced remotely, the same way, every week:

| Store | Address | Tier | Where prices come from |
|---|---|---|---|
| Walmart Supercenter | 1018 Riley St | Discount anchor | walmart.com (store set to Folsom) |
| Target | 430 Blue Ravine Rd | Mass / value | target.com (store set to Folsom) |
| Safeway | 1850 Prairie City Rd | Mainstream national | safeway.com (store set to Prairie City Rd) |

### Stores deliberately excluded, and why (this is part of the methodology)

- **Raley's and Bel Air** (the region's hometown chains): excluded to avoid a potential conflict of interest for the author. This leaves the premium regional tier unrepresented, which is disclosed as a panel limitation.
- **WinCo Foods (200 Blue Ravine Rd)**: likely the lowest-priced grocer in Folsom, but WinCo publishes no online prices at all. Excluding it means this index understates how cheap the cheapest option in Folsom really is; that limitation is disclosed. If in-person collection ever becomes possible, WinCo is the first store to add.
- **Trader Joe's**: nearly all private label; a fixed comparable basket cannot be constructed across stores.
- **Grocery Outlet**: opportunistic, rotating inventory; a fixed basket cannot be tracked week to week.
- **Whole Foods (Palladio)**: does not carry several national-brand anchor items in the basket.
- **Costco**: membership pricing and bulk pack sizes are not comparable to standard retail units.

## The basket (14 items, precisely defined)

Every item exists at all three stores in a comparable form. National brands are used where exact SKU-level comparability matters; store brands where the commodity itself is the standard.

| # | Item (exact definition) | Unit | Category |
|---|---|---|---|
| 1 | Whole milk, store brand | 1 gal | Dairy & Eggs |
| 2 | Large white eggs, grade A, store brand (cheapest conventional) | dozen | Dairy & Eggs |
| 3 | Tillamook medium cheddar | 8 oz | Dairy & Eggs |
| 4 | Boneless skinless chicken breast (spec below) | per lb | Meat & Poultry |
| 5 | Ground beef 80/20 (spec below) | per lb | Meat & Poultry |
| 6 | Bananas, conventional (spec below) | per banana | Produce |
| 7 | Baby carrots, store brand | 1 lb bag | Produce |
| 8 | Romaine hearts | 3 ct | Produce |
| 9 | Cheerios (plain) | 18 oz | Pantry |
| 10 | Jif creamy peanut butter | 16 oz | Pantry |
| 11 | Barilla spaghetti | 16 oz | Pantry |
| 12 | White sandwich bread, store brand (spec below) | 20 oz loaf | Pantry |
| 13 | Coca-Cola | 2 L | Beverages |
| 14 | Starbucks Pike Place, ground | 12 oz | Beverages |

### Meat item specification (authoritative; effective 2026-08-24)

Meat is where unwritten collection rules break an index, because the cheapest per-pound option is almost always a large value pack or chub whose bulk discount varies week to week. Recording it confounds pack economics with price change. This index therefore prices the standard retail unit a typical basket shopper buys:

**Item 4, chicken breast.** Store-brand or store-labeled, conventional (not organic, not air-chilled, not "no antibiotics ever" or other premium lines), fresh (not frozen), boneless skinless breast, in the retailer's large or value-pack tray. Record the per-pound price.

Why the value-pack tier: Walmart offers no conventional store-brand fresh boneless skinless breast in any size below a family pack; its only smaller option is a premium antibiotic-free line. Target and Safeway offer both standard and value packs. The value-pack tier is therefore the only tier stocked at all three stores, and holding product tier constant across stores matters more than holding pack size constant, because per-pound pricing already normalizes quantity. Tracked products: Walmart Freshness Guaranteed boneless skinless chicken breasts (large tray); Target Good & Gather Fresh All Natural boneless & skinless chicken breast value pack (2.5-5.25 lb); Safeway boneless skinless chicken breast value pack (3.5 lb).

**Item 5, ground beef.** Store-brand, conventional, 80% lean / 20% fat, in the 1 lb tray. Products labeled "ground chuck" qualify only if the label also states 80/20. Record the per-pound price. Never a chub, roll, or loaf; never a value or family pack; never Angus, grass-fed, organic, or other premium lines. All three stores stock a qualifying 1 lb tray: Walmart All Natural 80/20 Ground Beef Chuck (1 lb tray); Target Good & Gather Fresh All Natural 80/20 Ground Beef (1 lb); Safeway Signature SELECT 80% Lean 20% Fat Ground Beef (1 lb).

**Pack-size comparability, disclosed.** Chicken is priced from value packs whose sizes differ by store (roughly 2.5 to 6 lb). Part of any cross-store chicken gap therefore reflects pack economics rather than store pricing, which affects the level of a cart comparison. It does not affect the index, which measures change over time using the same product at the same store every week.

**Once selected, the product is fixed.** The rules above choose each product once. Every subsequent week, re-price that same product, even if a different item is cheaper that week. Product URLs are saved and reused. The rules are re-run only if a tracked product is discontinued.

**If a tracked product is unavailable** in a given week, apply the out-of-stock rule below. Do not substitute a different pack size or tier.

### Produce and packaged-item measurement notes (effective 2026-08-24)

**Item 6, bananas.** Priced per banana (per each) at all three stores. Target displays only a per-each price for bananas, so per-each is the unit directly observable at every store, and it requires no assumption about banana weight. Record the displayed price of one conventional banana.

**Item 12, white sandwich bread.** Safeway's store-brand loaf is 22 oz where Walmart's and Target's are 20 oz. The recorded Safeway price is normalized to a 20 oz equivalent: the observed loaf price divided by 22, multiplied by 20. This keeps the basket quantity identical across stores while starting from the observed shelf price. If any store changes its loaf size, the same per-ounce normalization to 20 oz applies, with the change noted in the commit message.

### Price-type rule (applies to every item)

The recorded price is the price displayed on the retailer's own website for the selected Folsom store, including free loyalty-program pricing where the retailer displays it by default (Safeway for U, which any shopper can join at no cost). Clip-to-activate digital coupons and paid-membership prices are never used. The rule follows CPI practice: record the price generally available to consumers, applied with the identical instrument every week.

### Fallback rules (written once, followed forever)

- Out of stock online: carry forward the item's prior-week price for that store (standard price-index imputation) and note the imputation in the commit message. Never substitute a different product, and never leave a blank row.
- Package size changes (shrinkflation): record the new size in the commit message and keep tracking. A size change is itself a finding worth a post.
- Any deviation from this document gets a dated entry in the site's revision log. The protocol is only amended in writing, never silently.

## Pilot phase and official series

Collections for the seven Mondays of 2026-07-06 through 2026-08-17 predate this written protocol. During that period the meat items were not selected under a fixed specification, so those observations are not like-for-like week to week. They are published in full in `data/prices.csv`, flagged `pilot` in the `phase` column, and are excluded from the index. The pilot panel also included a fourth store, Bel Air, removed for the conflict-of-interest reason stated above; its 98 pilot observations remain published at `archive/belair.csv`, with the panel change recorded in the site's revision log. The index displayed on this site before 2026-08-21, computed from all pilot data with base week 2026-07-06, is superseded and is not comparable to the official series. The official series begins with the first collection under this protocol on Monday, 2026-08-24, which is the base week (= 100). The site's revision log records this history.

## Methodology

- **Measurement definition:** the price shown on each retailer's own website with the named Folsom store selected (pickup mode), recorded every Monday morning in a fixed store order, under the price-type rule above.
- **Honest caveat, stated up front:** retailers' online prices can differ from in-store shelf prices, and Safeway's displayed prices reflect its free membership program. That affects the level of a cart total. The index, however, measures change over time using the identical instrument every week, which is what makes week-over-week and cumulative inflation numbers meaningful. Consistency of instrument over perfection of instrument. Say exactly this when asked.
- **Weighted Laspeyres index**, base week = 100, BLS-style food-at-home category weights (editable in `CONFIG.WEIGHTS` in `index.html`): Meat & Poultry 0.25, Pantry 0.22, Dairy & Eggs 0.20, Produce 0.20, Beverages 0.13.

  `Index_t = 100 x Sum_c  w_c x ( Sum of category-c prices at week t / Sum of category-c prices at base week )`

- **Cheapest full cart:** raw 14-item basket total per store per week; the spread drives the savings calculator.

### Why this is not web-scraped (interviewers will ask; here is the answer)

Automated scraping of grocery sites (a) violates most retailers' terms of service, (b) is technically fragile behind anti-bot systems, and (c) would be a poor look for a project whose entire value is credibility. Instead, a human reads 42 published prices into the data file once a week (about 30 minutes), and everything downstream is automated: the site recomputes the index, the charts, the cheapest cart, and the savings math in the browser on every visit, from the CSV alone. Manual where integrity matters, automated everywhere else.

## Weekly workflow (about 30 minutes, fully remote, zero coding)

1. Monday morning, open the three sites with the Folsom stores selected. Same store order every week.
2. Record the 42 prices under the item spec and price-type rule above.
3. On github.com, open `data/prices.csv`, click the pencil icon (edit in place), paste the new week's 42 rows at the bottom with `official` in the `phase` column, and commit. The live site updates itself within a minute or two.
4. Post the Monday number (see `GET_IT_NOTICED.md`).

## "But isn't this just a GitHub thing?" No.

GitHub plays two invisible roles: it stores the data publicly, which is what makes the index auditable, and GitHub Pages turns the repo into a real public website with a normal URL. Visitors never see GitHub. With an optional custom domain (about $12/year, for example `folsomcartindex.com`), the address on applications and in the local paper is a clean brand rather than a github.io link.

### Setup (about 20 minutes, once)

1. Create a free GitHub account, then New repository, name it `cart-index`, set Public, upload `index.html`, `og-image.png`, `README.md`, `GET_IT_NOTICED.md`, and the `data` folder, and commit.
2. Repo Settings, Pages, Source: Deploy from a branch, main / (root), Save. The site is live at `https://YOUR-USERNAME.github.io/cart-index/` within minutes.
3. In `index.html`, set `GH_USER`, `GH_REPO`, `GH_BRANCH`, `SITE_URL`, and `CONTACT_EMAIL` at the top of the CONFIG block. (This copy of the repo is already configured.)
4. Optional custom domain: buy the domain, then repo Settings, Pages, Custom domain, and follow the DNS instructions shown.

## Repo structure and data schema

```
cart-index/
├── index.html          # the entire dashboard (CONFIG at the top of the <script>)
├── og-image.png        # social link preview image
├── GET_IT_NOTICED.md   # the launch and promotion playbook
├── data/
│   └── prices.csv      # every panel observation, pilot and official
├── archive/
│   └── belair.csv      # pilot observations from the store removed at launch
└── README.md
```

```csv
date,store,item,category,unit,price,phase
2026-08-24,Walmart - Riley St,Cheerios,Pantry,18 oz,4.47,official
```

`date` is the Monday of collection (`YYYY-MM-DD`). `category` must match a `CONFIG.WEIGHTS` key. `phase` is `official` for index rows or `pilot` for pre-protocol rows. No commas inside fields.

## Impact metrics (log these in an IMPACT.md from day one)

Consecutive Mondays collected since 2026-07-06, and official weeks published (the streak is the story). Total price observations (14 x 3 x weeks, plus the 294 published pilot observations). This-week and cumulative cheapest-cart spread. Divergence from the BLS West region food-at-home CPI at each monthly release. Site visitors, repo stars and forks. Media and civic touchpoints. Other cities recruited.

## Roadmap

Overlay the BLS West region food-at-home series on the chart at each monthly release. Single-item deep dives when something moves (the egg index, the coffee index). One-paragraph Monday commentary as a free writing portfolio. Recruit one student in another city to fork it, the first student-run multi-city grocery price network. Semester-end working paper, *Weekly Hyperlocal Grocery Price Dynamics in Folsom, CA*, brought into the statistical economics course.

---

*Independent student research. Not affiliated with, endorsed by, or informed by any retailer. All prices are the retailers' own publicly published prices for their Folsom stores.*
