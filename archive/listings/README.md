# Source listing archive

Dated screen captures of every price listing behind `data/prices.csv`.

**Adopted 2026-09-23. Effective with the collection of Monday, 2026-09-28.** This folder is empty until that date.

## Layout

One folder per collection date:

```
archive/listings/
└── 2026-09-28/
    ├── walmart_milk.jpg
    ├── walmart_eggs.jpg
    ├── ...
    ├── target_milk.jpg
    ├── ...
    └── safeway_coffee.jpg
```

42 images per week: three stores times fourteen items.

## Naming

`store_itemid.jpg`, where `store` is `walmart`, `target`, or `safeway`, and `itemid` matches the `item_id` column in `data/prices.csv`:

`milk`, `eggs`, `cheddar`, `chicken`, `beef`, `bread`, `bananas`, `carrots`, `romaine`, `spaghetti`, `cheerios`, `peanutbutter`, `coke`, `coffee`

Any row in the price file locates its own evidence from `date` + `store` + `item_id`.

## What each capture shows

The product page as displayed for the named Folsom store, with the product name, the package size, and the price visible. Captures are committed in the same commit as that week's prices, so a price and the evidence behind it carry one timestamp recorded by GitHub rather than by the author.

## Coverage

The five official weeks of 2026-08-24 through 2026-09-21 were collected before this rule and have no captures. That gap is recorded in the site's revision log. No published price was changed when the rule was adopted.
