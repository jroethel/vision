---
provenance: "docs/original/pmaStarting.htm#starter"
unit_type: "general"
title: "Vision Portfolio Management Application: Getting Started"
ingested: "2026-09-22"
---

## Assembling Starter Files

To start each system, you will minimally want to prepare the following data feeds: *SecurityTypeMaster*, *SecurityMaster*, *PortfolioMaster*, and *HoldingsFeed*.

Assume the data for *SecurityTypeMaster* looks like the following:

    Id name              unitCalc     AssetCategory

    0   Cash & Equiv      1        Cash
    1   Common Stock      1        Equity
    2   Preferred Stock   1        Equity

This feed will be saved as *sectype.txt*.

Assume the data for *SecurityMaster* looks like the following:

    id      name                  ticker   type   latestMarketCapUS
                    
    00195710   AT&T CORP COM         T    1      55447562.63
    00811710   AETNA INC COM         AET      1      14458498.5
    20449310   COMPAQ COMPUTER CORP  CPQ      1      26578000

This feed will be saved as *sec.txt*.

Assume the data for *PortfolioMaster* looks like the following:

    id   name
        
    102 INSYTE GROWTH FUND
    232 INSYTE INCOME FUND
    332 INSYTE GROWTH & INCOME FUND
    532 INSYTE PENSION

This feed will be saved as *portfolio.txt*.

Assume the data for *HoldingsFeed* looks like the following:

    date acctId  secId      shares   mval
                    
    971215  102 00195710   8823     49422.22
    971215  102 00811710   6111     42122.11
    971215  232 00811710   7700     444444.4
    971215  232 20449310   7001     424344.4
    971215  332 20449310   7800     497741.4
    971215  332 00195710   7100     463321.4

This feed will be saved as *holdings.txt*.

More information about [Feed Formats](pmaFeeds/2.md) and [Starter Feeds](pmaFeeds/5.md) is available.

------------------------------------------------------------------------
