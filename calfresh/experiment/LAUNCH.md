# Launch Kit: Sharing the CalFresh Guide on Reddit

You post everything yourself. Nothing here is automated. Post no earlier than **October 2, 2026** (the data window opens then). The window closes **November 8, 2026**, so aim to have every post up in the first two weeks.

## Before the first post

- [ ] On every browser and phone you use, open `https://folsomcartindex.com/calfresh/#toggle-goatcounter` once. GoatCounter's script then asks whether to stop counting this browser; confirm it. Then open the page normally and check that no new `exp/...` event appears in the dashboard.
- [ ] Check both versions with `?arm=A` and `?arm=B` (they send nothing; a red "Test mode" bar confirms it).
- [ ] Confirm that GitHub Pages shows the committed preregistration at `calfresh/experiment/PREREGISTRATION.md`.

## Candidate subreddits to evaluate

Membership sizes and rules change. Check each one yourself before posting. Fit is about the readers, not the size.

| Subreddit | Why it might fit | Check |
|---|---|---|
| r/Folsom | Local to the Cart Index and FLC | Self-promotion rules; whether local resources posts are welcome |
| r/Sacramento | Largest regional audience; CalFresh is administered by Sacramento County | Strict rules on links and self-promotion are common; message mods first |
| r/FolsomLakeCollege (if it exists and is active) | Exactly the students the guide is for | Is it active? Who moderates it? |
| r/RanchoCordova, r/ElDoradoHills, r/Roseville | Nearby towns where FLC students live | Activity level; local-resource rules |
| r/CommunityCollege | Students in California community colleges, though nationwide | The guide is California-only; say so in the title |
| r/CalFresh (if it exists and is active) | People already looking into CalFresh | Whether outside links are allowed |
| r/UCDavis, r/SacState | Nearby students. The June 2026 rule also covers CSU and UC, but the page is written for FLC | Only post if moderators agree it is useful despite the FLC framing |

## Checklist for each subreddit

- [ ] Read the sidebar rules and any pinned "self-promotion" or "resources" policy.
- [ ] Check whether the subreddit requires a minimum account age or karma.
- [ ] **Message the moderators first** (use "Message the mods"), with the draft below and the link. Wait for a reply before posting. If there is no reply in 3 days, do not post there.
- [ ] Use only that subreddit's `?ref=` link from the table below.
- [ ] Post once. Do not repost or cross-post the same link to the same subreddit.
- [ ] Reply to comments honestly. If someone asks about eligibility for their situation, point them to GetCalFresh or the county; don't make the call yourself.
- [ ] Record the outcome in the log below the same day.

## Message to moderators (draft)

> Hi, I'm Dustin, an economics student at Folsom Lake College. I run the Cart Index (folsomcartindex.com), a free weekly grocery price index for Folsom. I made a free, non-commercial guide for students on the June 2026 CalFresh rule change, which now lets many community college students qualify. Would it be OK to share it here? It has no ads and collects no personal information. To learn which presentation is clearer, the page randomly shows one of two versions of the same information. Thanks for considering it.

## Post draft

**Title:** Free guide: since June 2026, many FLC / community college students now qualify for CalFresh (grocery aid)

> I'm a student at Folsom Lake College and I run the Cart Index, a free weekly grocery price index for Folsom. I made a short, free guide to the CalFresh student rule change. Since June 1, 2026, students enrolled at least half-time in an associate's or bachelor's degree program at a California community college, CSU, or UC meet CalFresh's student rule. Income and other rules still apply, and the county makes the decision.
>
> The guide links straight to the official application (BenefitsCal) and to free help (GetCalFresh, Sacramento Food Bank & Family Services).
>
> [link for this subreddit]
>
> It's non-commercial: no ads, no sign-up, no personal information collected. One note: to learn which presentation is clearer, the page randomly shows one of two versions of the same information. The plan for that comparison is public on GitHub, and I'll post the result whatever it shows.

## One link per subreddit

Use the exact link for each place. Tags must be lowercase letters, numbers, or hyphens.

| Subreddit | Link |
|---|---|
| r/Folsom | https://folsomcartindex.com/calfresh/?ref=r-folsom |
| r/Sacramento | https://folsomcartindex.com/calfresh/?ref=r-sacramento |
| r/FolsomLakeCollege | https://folsomcartindex.com/calfresh/?ref=r-folsomlakecollege |
| r/RanchoCordova | https://folsomcartindex.com/calfresh/?ref=r-ranchocordova |
| r/ElDoradoHills | https://folsomcartindex.com/calfresh/?ref=r-eldoradohills |
| r/Roseville | https://folsomcartindex.com/calfresh/?ref=r-roseville |
| r/CommunityCollege | https://folsomcartindex.com/calfresh/?ref=r-communitycollege |
| r/CalFresh | https://folsomcartindex.com/calfresh/?ref=r-calfresh |
| r/UCDavis | https://folsomcartindex.com/calfresh/?ref=r-ucdavis |
| r/SacState | https://folsomcartindex.com/calfresh/?ref=r-sacstate |
| Any other place | https://folsomcartindex.com/calfresh/?ref=other-NAME |

## Log

"Readers" = visitors recorded for that `ref` (the `exp/A/view/<ref>` plus `exp/B/view/<ref>` events in GoatCounter, or the by-referrer table from `analysis.py`). Fill this in when the window closes.

| Date posted | Subreddit | Link (ref) | Mods messaged | Approved / removed | Readers (to Nov 8) |
|---|---|---|---|---|---|
| | | | | | |

## Counting reach for your essay

- **Subreddits shared on** = rows above marked "approved" (posts that stayed up). Don't count posts that were removed.
- **Readers in the first [period]** = sum of `visitors` in `results.csv` from your first post date through the end of that period. These are unique browsers that loaded the page, after bots, test visits, and your own visits are excluded. Run `python3 analysis.py` after importing the GoatCounter export to get the totals.
