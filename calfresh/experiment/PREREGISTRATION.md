# Preregistration: Dollars vs. Groceries on the FLC CalFresh Guide

- **Author:** Dustin Wagner
- **Date:** October 1, 2026
- **Page:** https://folsomcartindex.com/calfresh/
- **Record:** the timestamp of the commit that adds this file is the preregistration record. It is committed before the guide is shared anywhere. After launch, this file changes only in the dated **Deviations** section at the end.
- **Replaces:** the earlier plan in [`../PREREGISTRATION.md`](../PREREGISTRATION.md) (committed September 21, 2026). That plan's data window opened October 1, but the guide had not been shared and no data had been collected under it. It is kept unchanged in the repository for the record. The replacement is logged in [`../CHANGELOG.md`](../CHANGELOG.md).

## 1. Background

Many students who are eligible for CalFresh never claim it. Since June 1, 2026, students enrolled at least half-time in an associate's or bachelor's degree program at a California Community College, CSU, or UC campus meet CalFresh's student rule (CDSS All County Letter 26-25). The maximum monthly benefit for one person is $306 from October 1, 2026 (federal fiscal year 2027 cost-of-living adjustment).

A dollar amount is abstract. The Cart Index prices the same 14 groceries every Monday at three Folsom stores, so the benefit can also be shown as real local groceries. This experiment asks whether that framing makes readers more likely to take the next step.

## 2. Hypothesis

Visitors shown the grocery framing (version B) click "apply" or "get help" at a higher rate than visitors shown the dollar framing (version A).

The test is two-sided: a difference in either direction will be reported.

This test compares two presentations of the same aid. It does not measure whether anyone applied, was approved, or received benefits, and it does not measure the guide's effect on enrollment.

## 3. The two versions

The page, its facts, and its links are identical in both versions except for the framing of the benefit at the top of the page and on the receipt graphic beside it.

- **Version A (dollars):** a large "$306 per month, max," and "CalFresh gives up to $306 a month for groceries for a single person." The receipt reads "MONTHLY MAX, 1 PERSON $306.00."
- **Version B (groceries):** a large "5 carts of groceries a month, max," and "CalFresh can cover up to five full carts of the same 14 Folsom staples every month, with $25 to spare," followed by the list of the 14 items, the average cart cost ($56.21), the store names, and the price week (Sep 28, 2026). The receipt reads "MONTHLY MAX, 1 PERSON 5 CARTS."
- **Decision: version B also shows the dollar figure, in smaller text** ("That is up to $306 a month for one person."), below the grocery translation. Reason: $306 is the official figure a reader needs in order to check it against the county's own information, and leaving it out of one version would make the versions differ in facts, not just framing. Version B therefore *leads* with groceries; it does not hide dollars. Version A does not mention the grocery translation.

**How the grocery number is computed.** From `data/prices.csv`, official rows only, week of Monday, September 28, 2026: the 14-item basket costs $49.57 at Walmart, $52.76 at Target, and $66.29 at Safeway. The average is $56.21. $306 ÷ $56.21 = 5.44, so $306 buys **5 full carts** (5 × $56.21 = $281.03) with **$24.97** left over, shown rounded to $25. (These figures include the October 1 correction of the Safeway cheddar price for that week, made before launch; see CHANGELOG.md.) Only whole carts are counted, so the translation never overstates what the aid buys.

**The number is fixed for the whole experiment.** The page computes it from the CSV. Until the end of the data window it uses the September 28 week, so every version-B visitor sees the same message. After the window closes, it automatically follows the latest official week.

## 4. Unit, randomization, and assignment

- **Unit of analysis:** one browser ("visitor").
- **Randomization:** on a browser's first visit, JavaScript assigns version A or B with probability 0.5 each (`Math.random() < 0.5`). The assignment is stored in `localStorage` (key `cf_version`), so a returning visitor sees the same version.
- **Referrer:** the `?ref=` tag on the link that first brought a browser to the page (for example `?ref=r-folsom`) is stored in `localStorage` (key `cf_ref`) and attached to all of that browser's events. A visit without a tag is recorded as `direct`.
- **Test override:** `?arm=A` or `?arm=B` forces a version. In that mode the page stores nothing, sends no events, and does not record a pageview.

## 5. Measurement

All measurement uses GoatCounter (cartindex.goatcounter.com), which sets no cookies and collects no personal information. No other analytics or trackers are used.

Each event is recorded at most once per browser:

| Event path | Fires when |
|---|---|
| `exp/<A or B>/view/<ref>` | First visit (the denominator) |
| `exp/<A or B>/any/<ref>` | First click on the Apply button or any help link |
| `exp/<A or B>/apply/<ref>` | First click on "Apply on BenefitsCal" |
| `exp/<A or B>/help/<ref>` | First click on any help link: GetCalFresh; Sacramento Food Bank & Family Services phone, text, or email; the statewide CalFresh info line |

Links that do not count as an outcome: the GetCalFresh income-limit link under "Who may qualify," the CDSS student-rules link, the Cart Index links, and the footer links. An awareness question ("Before today, had you heard about this change?") appears in both versions and is recorded as `heard-yes` or `heard-no`. It is reported descriptively only.

## 6. Outcomes

- **Primary:** the share of visitors in each version with at least one apply or help click: `any` ÷ `view`.
- **Secondary:**
  1. Apply-only rate: `apply` ÷ `view`, per version.
  2. Results by referrer: views and click rates per version for each `?ref=` tag.
  3. Help-only rate: `help` ÷ `view`, per version. This one is reported descriptively.

## 7. Data window and stopping rule

- **Opens:** October 2, 2026, 12:00 a.m. Pacific. Nothing will be posted before then.
- **Closes:** **Sunday, November 8, 2026, 11:59 p.m. Pacific.**
- The window ends on that date regardless of interim numbers. No early stop, no extension, and no significance testing before it closes.
- Results are computed November 9 to 15 and published by **November 16, 2026**.

## 8. Analysis

Run by [`analysis.py`](analysis.py) on [`results.csv`](results.csv).

- **Test:** two-proportion z-test with pooled standard error, two-sided, α = 0.05.
  z = (p_B − p_A) / √( p̂(1 − p̂)(1/n_A + 1/n_B) ), where p̂ = (x_A + x_B) / (n_A + n_B).
- **Small cells:** if any of the four cells (clickers and non-clickers in each version) is under 10, the p-value comes from Fisher's exact test (two-sided) instead. Both are printed, and the one this rule selects is the one reported.
- **Reported:** both rates with n; the difference p_B − p_A with a 95% confidence interval (unpooled Wald); and the relative lift p_B / p_A − 1 with a 95% confidence interval (log risk-ratio method). If either version has zero clicks, the relative lift is reported as undefined.
- The same procedure is applied to the apply-only secondary outcome. Results by referrer are descriptive, with no tests.

## 9. Exclusions

- **My own visits:** my browsers are excluded through GoatCounter's "ignore my visits" setting before launch. While it is on, the page sends no pageviews or events.
- **Test overrides:** `?arm=` visits send nothing, so they cannot enter the data.
- **Obvious bots:** GoatCounter drops known bots and automated browsers. Rows flagged as bots in the GoatCounter export are removed.
- **Outside the window:** any event before October 2 or after November 8, 2026 (Pacific) is removed.

No other exclusions will be made.

## 10. Power note (why this is a pilot)

At a click rate near 5%, with 80% power and α = 0.05, the smallest detectable difference is:

| Visitors per version | Detectable difference | That is |
|---|---|---|
| 150 | 7.1 points (5% → 12.1%) | +141% relative |
| 300 | 5.0 points (5% → 10.0%) | +100% |
| 500 | 3.9 points (5% → 8.9%) | +77% |
| 1,000 | 2.7 points (5% → 7.7%) | +55% |

Even at roughly 1,000 visitors per version, only large effects can be detected, and local-subreddit traffic will likely be smaller. **The result will be reported as a pilot either way.** A non-significant result is not evidence that the framings perform the same.

## 11. Known limitations

- **Clicks are not applications.** The page cannot see whether anyone applied or was approved.
- **Blocked storage:** a browser that blocks `localStorage` is reassigned on each load and can be counted more than once. Browsers with ad blockers that block GoatCounter are not counted in either version.
- **Same person, more than one device:** one person on a phone and a laptop counts as two visitors and may see both versions.
- **Channels are not randomized:** which subreddits allow the post, and when, is not under the experiment's control. Only the version is randomized, so the comparison between versions is unaffected.
- **The grocery translation uses one week's prices,** online prices for three stores, including Safeway's displayed prices under the Cart Index price-type rule.

## 12. Commitment to publish

The result will be published by November 16, 2026, whatever it shows: positive, negative, or null. Only aggregate counts will be published, in `results.csv`, `results.md`, and on the page.

## Deviations

Any change after launch is added here with its date, what changed, why, and what data it affects.

- **Oct 6, 2026, before any public posts:** (1) Broadened audience wording from FLC students to California college students, labeled the Sacramento County food bank contact, stated that the student rule applies at California community colleges, CSU, and UC (replacing "at FLC"; CDSS ACL 26-25, as in section 1), and added neutral link-preview metadata; changes are identical in both versions and do not alter the framing being tested. (2) Because version B's grocery framing uses Folsom prices while version A's dollar figure is universal, traffic is grouped into audience tiers (local, statewide, national, other) defined in refs.csv. The primary analysis is unchanged. Added: per-tier descriptive results, and a sensitivity analysis restricted to local and statewide traffic. (3) National subreddits will be used only if, by Oct 25, 2026, there are fewer than 300 visitors per version; any such posts use their own ref tag. (4) Known limitation: version B places more text above the Apply button, which may affect clicks on mobile independent of framing.
- **Oct 7, 2026, before any posts to these communities:** added ref tags r-csus, r-davis, r-roseville, r-elkgrove, r-stockton (local) and r-ucsb, r-ucr, r-ucsc, r-sjsu, r-sdsu, r-csulb, r-calpoly (statewide) to the existing tiers in refs.csv. Tier definitions, the primary analysis, and the Oct 25 national-posting rule are unchanged.
- **Oct 8, 2026:** Campus subreddit posts were removed or filtered by moderators (r/berkeley removed; r/UCLA and r/UCSantaBarbara filtered pending review). Statewide California subreddits were added earlier than the October 25 decision point originally planned, to reach adequate sample size before the fixed November 8 close. The primary analysis, the outcome measure, and the stopping rule are unchanged. The pre-specified sensitivity analysis restricted to local and statewide traffic now carries more weight, since the grocery version is priced in Folsom while the dollar version is location-neutral.
