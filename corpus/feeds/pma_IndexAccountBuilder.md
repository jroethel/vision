---
provenance: "docs/original/pma_IndexAccountBuilder.htm"
unit_type: "feed"
title: "Vision Upload Format: IndexAccountBuilder "
ingested: "2026-09-22"
entity: "IndexAccount"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of existing IndexAccount"}, {"name": "date", "property": "-", "type": "Date", "desc": "as of date for update"}, {"name": "universeId", "property": "universe", "type": "String", "desc": "id of existing Universe"}, {"name": "style", "property": "style", "type": "String", "desc": "Even or MCap indicator"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *IndexAccountBuilder*

**Category:** *EntityExtenderFeed*

## Summary:

- The *IndexAccountBuilder* feed is used to define a universe and weighting rule from which to derive the securities and shares used to create the holdings for one or more **IndexAccount** instances over time. The records supplied by this feed are used to update the **IndexAccount** time series properties *universe*.

  A number of [related feeds](#related%20feeds) are available to create new **Account** instances and to update other account-based information.

## Available Fields:

| Field | IndexAccount Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of existing IndexAccount |
| date | \- | Date | as of date for update |
| universeId | universe | String | id of existing Universe |
| --- Suggested Fields --- |  |  |  |
| style | style | String | Even or MCap indicator |

## Special Processing Rules:

- The *entityId* must correspond to an existing **IndexAccount**. The *universeId* must correspond to an existing **Universe**. The *date* field indicates the date for which the **Universe** members should be accessed and the **IndexAccount** holdings should be created. It can be supplied in any valid date format such as *19971215* or *12/15/97*.
- The *style* field indicates the rule for creating holdings from securities. The string *Even* indicates and even dollar amount should be invested in each security associated with the supplied universe. The string *MCap* (or anything else) indicates that the securities should be held in proportion to their market capitalization.
- The *securityList* time series property will be updated for each *entityId/date* combination included in this feed with an IndexedList of the **Security** instances found in the universe on the supplied date. The *universe* and *style* time series properties at **IndexAccount** are also updated as of this date.
- Holdings for the **IndexAccounts** referenced in this feed will be recreated on the date referenced using the style specified. The **IndexAccount** time series properties *\_totalMarketValue*, *\_totalMarketValueCash*, *\_totalMarketValueEquity*, *\_totalMarketValueFixed*, and *\_totalCost*, are computed as well as the holding properties *percentOfPort* and *percentOfEquity*.
- Note that **IndexAccount** holdings are **not** recreated if the members of the underlying universe are modified.

<span id="related feeds"></span>

## Related Feeds:

- [*IndexAccountMaster*](pma_IndexAccountMaster.md): creates IndexAccount instances
- [*HoldingsFeed*](pma_HoldingsFeed.md): loads holding records for one or more Portfolio or CompositeAccount instances for one or more time periods
- [*PortfolioMaster*](pma_PortfolioMaster.md): creates Portfolio instances
- [*AggAccountMaster*](pma_AggAccountMaster.md): creates AggAccount instances
- [*CompositeAccountMaster*](pma_CompositeAccountMaster.md): creates CompositeAccount instances
- [*PortfolioAggregates*](pma_PortfolioAggregates.md): defines Portfolio memberships in AggAccounts over time
- [*CompositeAccountMembers*](pma_CompositeAccountMembers.md): defines weighted combinations of Portfolio, AggAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time

## Sample Upload:

The following tab-delimited feed could be used to derive **IndexAccount** holdings from existing **Universe** memberships:

         Interface ExternalFeedManager upload: "IndexAccountBuilder" using:
         "entityId     date     universeId     style
          INDEX1       96       SP500          EVEN
          INDEX1       96       SP500          MCAP
         " ;

{% include doc-footer.htm copydates="1999" %}
