# Preregistration: FLC CalFresh Guide Message Test

Author: Dustin Wagner
Page: https://folsomcartindex.com/calfresh/
Committed before any data collection. The commit timestamp in this repository is the record that this plan existed before the data window opened.

## 1. Hypothesis

Showing the CalFresh maximum as local groceries (version B) produces a higher click-through rate to apply or get help than showing the dollar amount alone (version A).

The test compares two messages. It does not measure whether the project raised CalFresh enrollment overall, because there is no control group and no county enrollment data.

## 2. The two versions

Both versions are identical except for one sentence. Version A states the benefit as up to $306 a month for one person. Version B adds this sentence, in the same paragraph and the same style as the $306 sentence:

> At Folsom prices, that buys a 14-item basket of staples like milk, eggs, chicken, and bread 5.3 times a month (Cart Index, week of Sep 21, 2026).

How 5.3 was derived: the average Cart Index basket cost across the three stores in the week of Sep 21, 2026 was $57.32 (Walmart $50.11, Target $52.96, Safeway $68.89). $306 divided by $57.32 is 5.3. This number is fixed for the full data window and will not be updated with later weeks' prices.

## 3. Unit and assignment

- Unit: one browser.
- Assignment: on a first visit, the page assigns version A or B at random, 50/50, and stores the result in the browser (localStorage key `cf_version`). Return visits show the same version.
- If browser storage is blocked, the page assigns a version again on each load. This is a known limitation.

## 4. Primary outcome

Click-through rate per version:

- Version A: `act-A` events divided by `view-A` events
- Version B: `act-B` events divided by `view-B` events

Event definitions:

| Event | Fires when | How often |
|---|---|---|
| `view-A`, `view-B` | A version is assigned on a first visit | Once per browser |
| `act-A`, `act-B` | The first click on Apply or on any help link | Once per browser |

"Help links" are GetCalFresh and the Sacramento Food Bank & Family Services phone, text, and email links. The income-limit link under "Who may qualify" does not count as an action. The check-in link does not count as an action.

## 5. Analysis

Two-sided two-proportion z-test at α = 0.05, using the pooled rate:

z = (p_B − p_A) / sqrt( p × (1 − p) × (1/n_A + 1/n_B) ), where p = (x_A + x_B) / (n_A + n_B)

Here x is act events and n is view events for each version.

Also reported: both click-through rates, the difference (B minus A), and a 95% interval for the difference using the unpooled standard error, with n for each version.

## 6. Sample size rule

- 150 or more visitors per version by the end of the window: report the z-test, p-value, and 95% interval.
- Fewer than 150 per version: report the two rates as a directional pilot, with no claims of statistical significance.

At 150 per version, the test has about 83% power to detect a difference between 20% and 35% click-through. At 100 per version, about 66%.

## 7. Data window

October 1, 2026, 12:00 a.m. through November 13, 2026, 11:59 p.m., Pacific time. Any visits or events before October 1 are excluded.

## 8. Exclusions

- Test-mode visits (`?test=1`), which send no events.
- The author's own devices and browsers, blocked from GoatCounter before the window opens.
- Forced-version links (`?v=A`, `?v=B`) are used only together with test mode.

## 9. Integrity check

After the first 100 views, a split between `view-A` and `view-B` worse than 60/40 is treated as a sign that assignment is broken. It will be fixed and logged in CHANGELOG.md with the date and the affected data.

## 10. Secondary measures

These are reported descriptively, with no significance tests:

- Share who hadn't heard of the rule change: `heard-no` divided by (`heard-yes` + `heard-no`), reported with that total. Each fires once per browser when the visitor answers "Before today, had you heard about this change?"
- Detail clicks: `apply-A`, `apply-B`, `help-A`, `help-B`, and `checkin`, which fire on every click.
- Visits by channel, from the `?src=` tag on each link. In GoatCounter, each tag appears both as its own page row and under Top referrers.
- Anonymous check-in form answers: where the visitor saw the guide, whether they applied, the result, and the approximate monthly amount.

## 11. Known limits

- Outreach channels were not randomized. Only the message version was.
- Check-in answers are self-reported and anonymous, so they cannot be verified.
- Visitors with ad blockers that block GoatCounter are not counted in either version.
- Channel and version are counted separately, so visits by channel cannot be split by version without the raw export.

## 12. Changes after this commit

Any change to the page, the method, or the data after this commit is recorded as a dated entry in CHANGELOG.md, with the reason and the data affected.

## 13. What gets published

On November 16, 2026: weekly totals and summary results only. Individual check-in answers are never published.
