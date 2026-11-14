# CalFresh Guide for FLC Students

**Live:** https://folsomcartindex.com/calfresh/ · Part of [the Cart Index](../README.md)

## What it is and why it exists

Since June 1, 2026, students enrolled at least half-time in an associate's or bachelor's degree program at a California Community College, CSU, or UC campus meet CalFresh's student rule (CDSS All County Letter 26-25). Many eligible students never claim the aid, often because they don't know they qualify or because a dollar figure feels abstract.

This one-page guide explains the change, says who may qualify (and that income rules still apply and the county decides), and links straight to the application and to free help. Under the $306 figure, a small calculator shows any monthly amount as carts of the Cart Index's 14 Folsom staples at each tracked store, priced with the latest weekly Cart Index.

### Sources for the facts on the page

| Fact | Source |
|---|---|
| Up to $306 a month for one person from October 1, 2026 | USDA FNS, SNAP FY2027 cost-of-living adjustment; CDSS notice of the FFY 2027 CalFresh COLA |
| Student rule change, June 1, 2026 | CDSS All County Letter 26-25; [CDSS: CalFresh for college students](https://www.cdss.ca.gov/food-nutrition/calfresh/college-students) |
| Apply | [BenefitsCal](https://benefitscal.com/), California's official benefits application |
| Free help | [GetCalFresh](https://www.getcalfresh.org/); [Sacramento Food Bank & Family Services CalFresh outreach](https://www.sacramentofoodbank.org/calfresh): (916) 779-0052, text FOOD to 74544, calfresh@sacramentofoodbank.org; statewide CalFresh info line 1-877-847-3663 |

The page links to official rules instead of paraphrasing them in detail.

## How the cart calculator works

1. The page loads `../data/prices.csv`, the Cart Index data file, and keeps only rows with `phase` = `official`.
2. It picks the latest official week in which all three stores have all 14 items, and adds up each store's 14 prices to get one cart total per store, the same totals the index shows. The CSV already stores Safeway bread normalized from 22 oz to 20 oz and bananas priced per banana, so the page applies no adjustment of its own.
3. For the amount in the box (default $306), carts = amount ÷ cart total, at Walmart, Target, Safeway, and at the average of the three cart totals, rounded to one decimal.
4. It updates on its own each Monday when new prices are committed. Nothing in the Monday workflow changes. If the CSV cannot be loaded, the calculator shows no figures and links to the index instead.

The prices are each retailer's online prices for its Folsom store, under the Cart Index price-type rule (see the main README).

## The experiment (ended November 8, 2026)

From October 2 to November 8, 2026, each visitor was randomly shown one of two versions of the same information: version A led with "$306 a month," and version B led with "5 carts of groceries a month." The plan was committed before launch: **[experiment/PREREGISTRATION.md](experiment/PREREGISTRATION.md)**. Random assignment has been removed, and every visitor now sees the dollar version. The page as it ran is kept, unchanged and not served as a page, in [experiment/page-as-run.html.txt](experiment/page-as-run.html.txt), along with the analysis script, launch kit, and data files in [experiment/](experiment/).

## Privacy

- No cookies, no sign-in, no forms, and no personal information.
- The only analytics are [GoatCounter](https://www.goatcounter.com/), which counts page views and named events without storing personal data.
- The browser's `localStorage` keeps two small flags on the reader's own device, so the awareness answer and the calculator are counted only once (`calfresh_heard`, `calfresh_calc`). They never leave the device.
- Events: `calfresh/apply` and `calfresh/help` (one per click on Apply or a help link), `calfresh/heard-yes` or `calfresh/heard-no` (once per browser), and `calfresh/calc` (once per browser, the first time the calculator amount is changed). The experiment's event names (`exp/...`, `heard-yes`, `heard-no`) are no longer sent, so new data cannot mix with the experiment's data.

## Reproduce the experiment analysis

1. In GoatCounter (cartindex.goatcounter.com), go to Settings → Export and download the CSV export covering October 2 to November 8, 2026.
2. Run `python3 calfresh/experiment/analysis.py --from-export path/to/export.csv --write-md`. This rebuilds `results.csv` (dropping bots and out-of-window rows), runs the preregistered tests, and writes `results.md`.
3. Commit `results.csv` and `results.md`. Python 3.9+ standard library only; no packages needed.

## Limitations

- Clicks are not applications: the page can't see whether anyone applied or was approved.
- Browsers that block storage or GoatCounter are miscounted or not counted.
- The calculator uses one week of online prices at three stores, and $306 is a maximum: most households receive less.

## Changelog

The detailed log is in [CHANGELOG.md](CHANGELOG.md).

- **2026-11-14:** Experiment ended. Every visitor sees the dollar version; random assignment removed; cart calculator added; new `calfresh/` event names; `noindex` removed.
- **2026-10-01:** Corrected the Sept 28 Safeway cheddar price in the index data ($4.19 → $4.99); the grocery translation is now 5 carts with $25 to spare (was $26).
- **2026-10-01:** Experiment rebuilt and preregistered before launch: grocery version computed from the index, `?arm=` and `?ref=` added, Google Forms check-in removed, CDSS and statewide help links added, analysis script and launch kit added. Replaces the September 21 plan, which was never launched.
- **2026-09-21:** Guide published (unlisted, `noindex`).
