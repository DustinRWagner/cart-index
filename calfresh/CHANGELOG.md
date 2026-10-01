# Changelog: FLC CalFresh Guide

Every change to the page, the method, or the data after the preregistration commit is recorded here, newest first. Each entry gives the date, what changed, why, and any data affected.

## 2026-10-01

- **Index data corrected before launch.** The Sept 28 Safeway cheddar price in `data/prices.csv` was $4.19, which was Target's price entered on the Safeway row; the correct Safeway price is $4.99 (see the Cart Index revision log). Version B's fixed translation is now 5 full carts with $25 to spare (average cart $56.21), not $26 (average $55.94). The number of carts is unchanged. This was corrected before the guide was shared and before the data window opens.
- **Preregistration replaced before launch.** The September 21 plan (`PREREGISTRATION.md`) set a data window opening October 1. The guide had not been shared anywhere, and the only visits were the author's own tests, so no data existed under that plan. It is replaced by `experiment/PREREGISTRATION.md`, committed today, before launch. The old file is kept, with a note at the top. What changed: window Oct 2 to Nov 8 (was Oct 1 to Nov 13); version B now leads with the grocery translation (whole 14-item carts, week of Sep 28) and shows $306 in smaller text (was one added sentence, "5.3 times," week of Sep 21); outcomes are now counted per referrer; Fisher's exact test applies when a cell is under 10; the earlier rule of at least 150 visitors per version is replaced by reporting every result as a pilot.
- Page: `?arm=A` / `?arm=B` test override (no storage, no events); `?ref=` replaces `?src=` for channel tags; events renamed `exp/<version>/<view|any|apply|help>/<ref>`, each once per browser.
- Page: Google Forms check-in removed. The guide now collects nothing outside GoatCounter.
- Page: added links to the CDSS college-student rules page and the statewide CalFresh info line (1-877-847-3663), which counts as a help link. Added the footer note on the two versions.

## 2026-09-21

- Guide published at https://folsomcartindex.com/calfresh/ (calfresh/index.html). Unlisted, with a noindex tag, and not linked from the homepage.
- Events and `?src=` channel tags tested on a phone. All test visits fall before the October 1 data window and are excluded.
