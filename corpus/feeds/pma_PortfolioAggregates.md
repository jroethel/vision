---
provenance: "docs/original/pma_PortfolioAggregates.htm"
unit_type: "feed"
title: "Vision Upload Format: PortfolioAggregates "
ingested: "2026-09-22"
entity: "PortfolioAggregates"
fields: [{"name": "groupId", "property": "", "type": "String", "desc": "id of existing [AggAccount](pma_AggAccountMaster.md) instance", "ref": "pma_AggAccountMaster"}, {"name": "memberId", "property": "", "type": "String", "desc": "id of existing [Portfolio](pma_PortfolioMaster.md) instance", "ref": "pma_PortfolioMaster"}, {"name": "date", "property": "", "type": "Date", "desc": "date of the membership"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *PortfolioAggregates*

**Category:** *MembershipFeed*

## Summary:

- The *PortfolioAggregates* feed is used to define the member **Portfolios** in an **AggAccount** over time. The records supplied by this feed are used to update the **AggAccount** time series property *memberList*. Whenever a membership is updated, the holdings for the **AggAccount** are recreated for each date that any of the member **Portfolios** has holdings.

  A number of [related feeds](#related%20feeds) are available to create new **Portfolio** and **AggAccount** instances and to update other account-based information.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| groupId | String | id of existing [AggAccount](pma_AggAccountMaster.md) instance |
| memberId | String | id of existing [Portfolio](pma_PortfolioMaster.md) instance |
| --- Suggested Fields --- |  |  |
| date | Date | date of the membership |

## Special Processing Rules:

- The *groupId* and *memberId* fields must be supplied. The *groupId* must correspond to an existing **AggAccount** instance. The *memberId* must correspond to an existing **Portfolio** instance.
- The *date* field is optional and should be supplied if you want to track membership changes over time. It can be supplied in any valid date format such as *19971215* or *12/15/97*. To specify an initial membership, use the date *10101* or the string *Default* as the value of the *date* field.
- The *memberList* time series property will be updated for each *groupId/date* combination included in this feed with an IndexedList of the **Portfolio** instances specified in this feed. Because the memberships will replace the existing *memberList* for a date, you must specify all the portfolios for each *groupId/date* included.
- Holdings for the **AggAccounts** referenced in this feed will be recreated for one or more dates. Starting with each date for which the membership was updated, new holdings are created for the **AggAccount** for any date where any of the member **Portfolios** has holdings. When holdings are recreated, the **AggAccount** time series properties *\_totalMarketValue*, *\_totalMarketValueCash*, *\_totalMarketValueEquity*, *\_totalMarketValueFixed*, and *\_totalCost*, are computed as well as the holding properties *percentOfPort* and *percentOfEquity*.

<span id="related feeds"></span>

## Related Feeds:

- [*AggAccountMaster*](pma_AggAccountMaster.md): creates AggAccount instances
- [*PortfolioMaster*](pma_PortfolioMaster.md): creates Portfolio instances
- [*HoldingsFeed*](pma_HoldingsFeed.md): loads holding records for one or more Portfolio or CompositeAccount instances for one or more time periods
- [*CompositeAccountMaster*](pma_CompositeAccountMaster.md): creates CompositeAccount instances
- [*CompositeAccountMembers*](pma_CompositeAccountMembers.md): defines weighted combinations of Portfolio, AggAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time
- [*IndexAccountMaster*](pma_IndexAccountMaster.md): creates IndexAccount instances
- [*IndexAccountBuilder*](pma_IndexAccountBuilder.md): creates holdings for one or more IndexAccount instances over time using existing Security Universe instances and a weighting rule

## Sample Upload:

The following tab-delimited feed could be used to define **AggAccount** memberships over time.

         Interface ExternalFeedManager upload: "PortfolioAggregates" using:
         "groupId     memberId     date

          #-  define AGG1 to have 3 members since earliest possible date
          AGG1        PORT1        Default
          AGG1        PORT2        Default
          AGG1        PORT3        Default

          #- define AGG2 to have 2 members in 95 and a third added in 96
          AGG2        PORT2        1/1/95
          AGG2        PORT7        1/1/95
          AGG2        PORT2        1/1/96
          AGG2        PORT7        1/1/96
          AGG2        PORT4        1/1/96
         " ;

{% include doc-footer.htm copydates="1999" %}
