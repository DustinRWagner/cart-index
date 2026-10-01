# CalFresh Guide for FLC Students

**Live:** https://folsomcartindex.com/calfresh/ · Part of [the Cart Index](../README.md)

## What it is and why it exists

Since June 1, 2026, students enrolled at least half-time in an associate's or bachelor's degree program at a California Community College, CSU, or UC campus meet CalFresh's student rule (CDSS All County Letter 26-25). Many eligible students never claim the aid, often because they don't know they qualify or because a dollar figure feels abstract.

This one-page guide explains the change, says who may qualify (and that income rules still apply and the county decides), and links straight to the application and to free help. It also shows the aid as real Folsom groceries, priced with the weekly Cart Index, so $306 looks like five full carts of groceries instead of an abstract number.

### Sources for the facts on the page

| Fact | Source |
|---|---|
| Up to $306 a month for one person from October 1, 2026 | USDA FNS, SNAP FY2027 cost-of-living adjustment; CDSS notice of the FFY 2027 CalFresh COLA |
| Student rule change, June 1, 2026 | CDSS All County Letter 26-25; [CDSS: CalFresh for college students](https://www.cdss.ca.gov/food-nutrition/calfresh/college-students) |
| Apply | [BenefitsCal](https://benefitscal.com/), California's official benefits application |
| Free help | [GetCalFresh](https://www.getcalfresh.org/); [Sacramento Food Bank & Family Services CalFresh outreach](https://www.sacramentofoodbank.org/calfresh): (916) 779-0052, text FOOD to 74544, calfresh@sacramentofoodbank.org; statewide CalFresh info line 1-877-847-3663 |

The page links to official rules instead of paraphrasing them in detail.

## How the grocery translation is computed

1. The page loads `../data/prices.csv`, the Cart Index data file, and keeps only rows with `phase` = `official`.
2. For the chosen week, it adds up the 14 basket items at each store to get one cart total per store, then averages the three totals.
3. Full carts = floor($306 ÷ average cart). Left over = $306 − full carts × average cart, rounded to the dollar.
4. **Which week:** during the experiment (through November 8, 2026) the page uses the week of September 28, 2026, so every reader sees the same message. After that it uses the latest official week, so it updates on its own each Monday when new prices are committed. Nothing in the Monday workflow changes.

Week of September 28, 2026: Walmart $49.57, Target $52.76, Safeway $65.49; average **$55.94**. $306 ÷ $55.94 = 5.47 → **5 full carts**, $279.70, with **$26.30** left over (shown as $26).

Only whole carts are counted, so the figure never overstates what the aid buys. The prices are each retailer's online prices for its Folsom store, under the Cart Index price-type rule (see the main README).

## The experiment

Each visitor is randomly shown one of two versions of the same information: version A leads with "$306 a month," and version B leads with "5 carts of groceries a month" and shows $306 in smaller text. The outcome is the share of visitors who click to apply or get help. The full plan was committed before launch: **[experiment/PREREGISTRATION.md](experiment/PREREGISTRATION.md)**. Results: [experiment/results.md](experiment/results.md). Launch kit: [experiment/LAUNCH.md](experiment/LAUNCH.md).

## Privacy

- No cookies, no sign-in, no forms, and no personal information.
- The only analytics are [GoatCounter](https://www.goatcounter.com/), which counts page views and named events without storing personal data.
- The browser's `localStorage` keeps four small values on the reader's own device: the assigned version (`cf_version`), the link tag that brought them (`cf_ref`), and flags so each event is counted only once. These values never leave the device except as the anonymous event names below.
- Events: `exp/<A|B>/<view|any|apply|help>/<ref>`, plus `heard-yes` or `heard-no` for the awareness question.

## Reproduce the analysis

1. In GoatCounter (cartindex.goatcounter.com), go to Settings → Export and download the CSV export covering October 2 to November 8, 2026.
2. Run `python3 calfresh/experiment/analysis.py --from-export path/to/export.csv --write-md`. This rebuilds `results.csv` (dropping bots and out-of-window rows), runs the preregistered tests, and writes `results.md`.
3. Commit `results.csv` and `results.md`. Python 3.9+ standard library only; no packages needed.

## Testing

- `?arm=A` or `?arm=B` forces a version. A red "Test mode" bar appears, and nothing is stored or sent.
- `?ref=TAG` attributes a visit to a channel. Only the first visit's tag is kept.

## Limitations

- Clicks are not applications: the page can't see whether anyone applied or was approved.
- Small sample: only large differences are detectable, so the result is a pilot (see the power note in the preregistration).
- A person who uses two devices counts twice. Browsers that block storage or GoatCounter are miscounted or not counted.
- Which subreddits allow the post is not random. Only the version is randomized.
- The grocery translation uses one week of online prices at three stores, and $306 is a maximum: most households receive less.

## Changelog

The detailed log is in [CHANGELOG.md](CHANGELOG.md).

- **2026-10-01:** Experiment rebuilt and preregistered before launch: grocery version computed from the index, `?arm=` and `?ref=` added, Google Forms check-in removed, CDSS and statewide help links added, analysis script and launch kit added. Replaces the September 21 plan, which was never launched.
- **2026-09-21:** Guide published (unlisted, `noindex`).
