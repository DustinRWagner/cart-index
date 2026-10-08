# Launch Kit: Sharing the CalFresh Guide on Reddit

You post everything yourself. Nothing here is automated. Post no earlier than **October 2, 2026** (the data window opens then). The window closes **November 8, 2026**, so aim to have every post up in the first two weeks.

## Before the first post

- [ ] On every browser and phone you use, open `https://folsomcartindex.com/calfresh/#toggle-goatcounter` once. GoatCounter's script then asks whether to stop counting this browser; confirm it. Then open the page normally and check that no new `exp/...` event appears in the dashboard.
- [ ] Check both versions with `?arm=A` and `?arm=B` (they send nothing; a red "Test mode" bar confirms it).
- [ ] Confirm that GitHub Pages shows the committed preregistration at `calfresh/experiment/PREREGISTRATION.md`, including the Oct 6 deviation entry.
- [ ] Paste one link into a private chat or Reddit's post preview and check the preview text: it should say "CalFresh for college students" and "Free guide for California college students…", with no dollar amount or carts.

## Where to post, in order

Fit is about the readers, not the size. Membership sizes and rules change, so check each one yourself before posting. Every tag below is already in [`refs.csv`](refs.csv), which assigns its audience tier for the analysis.

**Tier 1, local. Post these first, one or two per day.**

| Subreddit | Link |
|---|---|
| r/folsom | https://folsomcartindex.com/calfresh/?ref=r-folsom |
| r/Sacramento | https://folsomcartindex.com/calfresh/?ref=r-sacramento |
| r/SacState | https://folsomcartindex.com/calfresh/?ref=r-sacstate |
| r/UCDavis | https://folsomcartindex.com/calfresh/?ref=r-ucdavis |
| An FLC or Los Rios subreddit, if one exists and is active (check first) | https://folsomcartindex.com/calfresh/?ref=r-flc |

**Tier 2, statewide. Post after Tier 1 is done.**

| Subreddit | Link |
|---|---|
| r/California | https://folsomcartindex.com/calfresh/?ref=r-california |
| r/CalFresh | https://folsomcartindex.com/calfresh/?ref=r-calfresh |
| r/berkeley | https://folsomcartindex.com/calfresh/?ref=r-berkeley |
| r/UCSD | https://folsomcartindex.com/calfresh/?ref=r-ucsd |
| r/UCI | https://folsomcartindex.com/calfresh/?ref=r-uci |
| r/ucla | https://folsomcartindex.com/calfresh/?ref=r-ucla |

**Oct 8 posts** (campus subreddits, statewide tier):

| Subreddit | Link |
|---|---|
| r/berkeley | https://folsomcartindex.com/calfresh/?ref=r-berkeley |
| r/UCSD | https://folsomcartindex.com/calfresh/?ref=r-ucsd |
| r/ucla | https://folsomcartindex.com/calfresh/?ref=r-ucla |
| r/UCSantaBarbara | https://folsomcartindex.com/calfresh/?ref=r-ucsb |

**Later, optional (city subs; expect low volume)** (local tier):

| Subreddit | Link |
|---|---|
| r/Roseville | https://folsomcartindex.com/calfresh/?ref=r-roseville |
| r/ElkGrove | https://folsomcartindex.com/calfresh/?ref=r-elkgrove |
| r/Stockton | https://folsomcartindex.com/calfresh/?ref=r-stockton |
| r/Davis | https://folsomcartindex.com/calfresh/?ref=r-davis |

**Tier 3, national. Only under the Oct 25 rule below.**

| Subreddit | Link |
|---|---|
| r/povertyfinance | https://folsomcartindex.com/calfresh/?ref=r-povertyfinance |

**The Oct 25 rule (preregistered as a deviation on Oct 6, 2026):** on October 25, 2026, run `python3 analysis.py` after importing the GoatCounter export. Post to Tier 3 only if **fewer than 300 visitors per version** have been recorded. Look only at the visitor counts, not the click rates. If both versions already have 300 or more, do not post to Tier 3.

**Other channels** (tier "other"): https://folsomcartindex.com/calfresh/?ref=discord · ?ref=facebook · ?ref=linkedin · ?ref=flyer.

**Don't make up a new tag on the spot.** A tag missing from `refs.csv` is counted as tier "other". To post somewhere new, first add its tag and tier to `refs.csv`, commit it, and log it in PREREGISTRATION.md's Deviations section, all before posting. Tags must be lowercase letters, numbers, or hyphens, 30 characters at most. Anything else is recorded as `direct`.

## Posting notes

- **Use text posts, not link posts.** Put the link inside the body.
- **Message the moderators first** wherever the rules mention self-promotion, using the draft below. Wait for a reply. If there is no reply in 3 days, do not post there.
- **One or two subreddits per day.** Post once per subreddit. Do not repost or cross-post the same link to the same subreddit.
- **Use only that subreddit's own `?ref=` link** from the tables above.
- **Answer comments in the first hour.** If someone asks about their own eligibility, point them to GetCalFresh or the county; don't make the call yourself.
- **Never use alternate accounts or ask for upvotes.**
- If anyone asks why the page differs from what a friend saw: **"It randomly shows one of two layouts to learn which is clearer."**
- The post copy below deliberately never mentions $306 or carts. Keep it that way in comments too, so readers see their own version first.
- Record each post in [`posts.csv`](posts.csv) the same day.

## Message to moderators (draft)

> Hi, I'm Dustin, an economics student at Folsom Lake College. I made a free, non-commercial one-page guide for California college students on CalFresh eligibility, with the official student rules and a direct link to apply. Would it be OK to share it here as a text post? It has no ads and collects no personal information. To learn which layout is clearer, the page randomly shows one of two versions of the same information. Thanks for considering it.

## Post copy

**Local title (Tier 1), pick one:**

1. Most college students who qualify for CalFresh never apply. I made a free guide to check if you do.
2. Sacramento-area students: you might qualify for monthly grocery money and not know it

**Statewide title (Tier 2):**

California college students: most who qualify for CalFresh never apply. Free guide to check if you do.

**National title (Tier 3 only):**

California college students only: most who qualify for CalFresh never apply. Free guide to check if you do.

**Body (all tiers):**

> I'm a Folsom Lake College student. CalFresh (California's version of food stamps) gives eligible college students money for groceries every month, but most students who qualify never apply, often because they assume it isn't for them.
>
> I put together a free one-page guide with the official student eligibility info and a direct link to apply:
>
> [link with this subreddit's ref tag]
>
> No sign-up, no ads, no personal info collected. If it helps one person eat better this semester, that's the whole point.

## Log

The post log is [`posts.csv`](posts.csv): one row per post with `date,subreddit,ref,status,notes`, where status is `live`, `removed`, `planned`, or `pending` (submitted but held for moderator review). Add a row when you plan a post and update its status the same day it goes up or comes down. `analysis.py` reads it and reports visitors per ref with each post's status.

## Counting reach for your essay

- **Subreddits shared on** = rows in `posts.csv` marked `live` (posts that stayed up). Don't count posts that were removed.
- **Readers from live posts** = the "total visitors from live posts" line printed by `python3 analysis.py`.
- **Readers in the first [period]** = sum of `visitors` in `results.csv` from your first post date through the end of that period. These are unique browsers that loaded the page, after bots, test visits, and your own visits are excluded. Run `python3 analysis.py` after importing the GoatCounter export to get the totals.
