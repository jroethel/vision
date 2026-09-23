---
provenance: "docs/original/pma_SplitsFeed.htm"
unit_type: "feed"
title: "Vision Upload Format: SplitsFeed "
ingested: "2026-09-22"
entity: "Security"
fields: [{"name": "entityId", "property": "-", "type": "String", "desc": "any valid security identifier"}, {"name": "date", "property": "-", "type": "Date", "desc": "date of split"}, {"name": "rate", "property": "rawSplitFactor", "type": "Number", "desc": "rate of split"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *SplitsFeed*

**Category:** *EntityExtenderFeed*

## Summary:

- The *SplitsFeed* feed is used to maintain the split adjustment history for securities. Split management is described in detail in the [*Portfolio Management Application Issues*](pmaIssues.htm#splits) document.

## Available Fields:

| Field | Security Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | \- | String | any valid security identifier |
| date | \- | Date | date of split |
| rate | rawSplitFactor | Number | rate of split |

## Special Processing Rules:

- The *entityId* must correspond to an existing **Security** instance. Any valid security alias can be used to identify the security.

- The *date* must be included and indicates the date of the split. It can be in any valid date format such as *19971215* or *12/15/97*.

- The *rate* field should contain the number of new shares received for one existing share. Stock splits and stock dividends can both be represented this way. A 2-for-1 stock split has a rate of 2 ; a 10% stock dividend has a rate of 1.1. A rate of NA or a negative value can be used to delete an existing split on a date.

- If your feed file supplies inverted rates, you can enable the inversion flag by saving the following code in the database:

          SplitsFeed enableSplitInversion;

  By default the inversion flag has been disabled.

- Once all raw split values have been updated by this feed, the **Security** message *rebuildAdjustmentFactor* is run to update the *adjustmentFactor* time series.

<span id="related"></span>

## Related Feeds:

- [*SecurityMaster*](pma_SecurityMaster.md): defines Security instances referenced by this feed
- [*SecurityAliases*](pma_SecurityAliases.md): loads cusip/sedol changes and adds other aliases that can serve as the *entityId* for a security.

## Sample Upload:

The following tab-delimited feed could be used to update splits.

     Interface ExternalFeedManager upload: "SplitsFeed" using:
         "entityId        date      rate
          00079410        19930205  1.50000 
          00079410        19960809  1.50000 
          00512510        19921201  2.00000 
          00512510        19950111  2.00000 
          00512510        19961112  2.00000 
         " ;

{% include doc-footer.htm copydates="1998-1999" %}
