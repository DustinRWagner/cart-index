# Changelog: FLC CalFresh Guide

Every change to the page, the method, or the data after the preregistration commit is recorded here, newest first. Each entry gives the date, what changed, why, and any data affected.

## 2026-10-08

Logged as a deviation in `experiment/PREREGISTRATION.md`.

- **Ref tags added.** `experiment/refs.csv` gains r-losangeles, r-bayarea, r-sanfrancisco, r-sandiego (statewide). r-california was already listed and is unchanged. Reason: campus posts were removed or held by moderators, and these subreddits add California traffic before the fixed November 8 close. Tier definitions, the data window, the stopping rule, randomization, and the primary analysis are unchanged. The page needed no change: each tag passes its 1-to-30-character a-z, 0-9, hyphen check.
- **Post log.** `experiment/posts.csv`: r/berkeley is now `removed`; r/ucla and r/UCSantaBarbara are `pending` (filtered for moderator review at submission). `pending` is a new allowed status in `analysis.py` and `experiment/LAUNCH.md`; it only affects the descriptive post-status report.

## 2026-10-07

Before any posts to these communities. Logged as a deviation in `experiment/PREREGISTRATION.md`.

- **Ref tags added.** `experiment/refs.csv` gains r-csus, r-davis, r-roseville, r-elkgrove, r-stockton (local) and r-ucsb, r-ucr, r-ucsc, r-sjsu, r-sdsu, r-csulb, r-calpoly (statewide), in the existing tiers. Tier definitions, the primary analysis, and the Oct 25 national-posting rule are unchanged. The page needed no change: it already accepts any tag of 1 to 30 characters of a-z, 0-9, or hyphens, and records anything else as `direct`.
- **Post log.** `experiment/posts.csv` records each post's date, subreddit, ref, and status (live, removed, planned). It replaces the table in `experiment/LAUNCH.md`.
- **Analysis (descriptive additions only).** `analysis.py` now reports visitors per ref with each ref's post status, total visitors from live posts, and the counts of `heard-yes` and `heard-no` answers (`--from-export` now also writes `experiment/heard.csv`). These answer events carry no ref tag, so the counts cover all traffic and cannot be limited to the local and statewide tiers. The primary analysis is unchanged.
- **Launch plan.** `experiment/LAUNCH.md` lists the Oct 8 campus posts (r/berkeley, r/UCSD, r/ucla, r/UCSantaBarbara) and optional later city subreddits (r/Roseville, r/ElkGrove, r/Stockton, r/Davis).

## 2026-10-06

Before any public posts. Logged as a deviation in `experiment/PREREGISTRATION.md`.

- **Audience broadened (both versions identically).** Masthead, eyebrow, heading, and receipt subtitle now address California college students instead of FLC students; the footer credits a Folsom Lake College student. "At FLC" in the student-rule sentence replaced with "at a California community college, CSU, or UC," and the same qualifier added to the "Who may qualify" card, matching CDSS ACL 26-25 (section 1 of the preregistration). The rule itself is unchanged; without the qualifier, students at private or out-of-state colleges could have read it as covering them. The Sacramento Food Bank & Family Services contact is labeled "In Sacramento County"; GetCalFresh and the statewide line (1-877-847-3663) remain the options for everyone. The tested framing (the $306 / 5-carts block and the receipt's monthly-max line) is unchanged.
- **Neutral link previews.** Title, description, og:title, and og:description no longer mention FLC and contain no dollar amounts or cart counts; added `twitter:card=summary`. No og:image.
- **`?ref=` validation.** Tags are lowercased and must be 1 to 30 characters of a-z, 0-9, or hyphens; anything else is recorded as `direct` (previously invalid characters were stripped and tags cut at 40). First-visit-only behavior is unchanged.
- **Audience tiers.** `experiment/refs.csv` maps each ref to a tier (local, statewide, national, other); unlisted refs count as other. Reason: version B's grocery framing uses Folsom prices, while version A's dollar figure is universal.
- **Analysis.** Primary analysis unchanged (all eligible traffic in the window, pooled). Added a pre-specified sensitivity analysis (same test, local + statewide tiers only), a visitors-per-tier table in `results.md`, and `--by-tier` descriptive results.
- **Launch plan.** National subreddits only if, by Oct 25, 2026, there are fewer than 300 visitors per version, each with its own ref tag. Known limitation recorded: version B places more text above the Apply button on mobile.

## 2026-10-01

- **Index data corrected before launch.** The Sept 28 Safeway cheddar price in `data/prices.csv` was $4.19, which was Target's price entered on the Safeway row; the correct Safeway price is $4.99 (see the Cart Index revision log). Version B's fixed translation is now 5 full carts with $25 to spare (average cart $56.21), not $26 (average $55.94). The number of carts is unchanged. This was corrected before the guide was shared and before the data window opens.
- **Preregistration replaced before launch.** The September 21 plan (`PREREGISTRATION.md`) set a data window opening October 1. The guide had not been shared anywhere, and the only visits were the author's own tests, so no data existed under that plan. It is replaced by `experiment/PREREGISTRATION.md`, committed today, before launch. The old file is kept, with a note at the top. What changed: window Oct 2 to Nov 8 (was Oct 1 to Nov 13); version B now leads with the grocery translation (whole 14-item carts, week of Sep 28) and shows $306 in smaller text (was one added sentence, "5.3 times," week of Sep 21); outcomes are now counted per referrer; Fisher's exact test applies when a cell is under 10; the earlier rule of at least 150 visitors per version is replaced by reporting every result as a pilot.
- Page: `?arm=A` / `?arm=B` test override (no storage, no events); `?ref=` replaces `?src=` for channel tags; events renamed `exp/<version>/<view|any|apply|help>/<ref>`, each once per browser.
- Page: Google Forms check-in removed. The guide now collects nothing outside GoatCounter.
- Page: added links to the CDSS college-student rules page and the statewide CalFresh info line (1-877-847-3663), which counts as a help link. Added the footer note on the two versions.

## 2026-09-21

- Guide published at https://folsomcartindex.com/calfresh/ (calfresh/index.html). Unlisted, with a noindex tag, and not linked from the homepage.
- Events and `?src=` channel tags tested on a phone. All test visits fall before the October 1 data window and are excluded.
