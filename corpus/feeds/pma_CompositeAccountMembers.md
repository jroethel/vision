---
provenance: "docs/original/pma_CompositeAccountMembers.htm"
unit_type: "feed"
title: "Vision Upload Format: CompositeAccountMembers "
ingested: "2026-09-22"
entity: "CompositeAccountMembers"
fields: [{"name": "groupId", "property": "", "type": "String", "desc": "id of existing [CompositeAccount](pma_CompositeAccountMaster.md) instance", "ref": "pma_CompositeAccountMaster"}, {"name": "memberId", "property": "", "type": "String", "desc": "id of existing Account instance"}, {"name": "date", "property": "", "type": "Date", "desc": "date of the membership"}, {"name": "weight", "property": "", "type": "Number", "desc": "percentage of member's holdings to include in composite"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *CompositeAccountMembers*

**Category:** *MembershipFeed*

## Summary:

- The *CompositeAccountMembers* feed is used to define the weighted combinations of Portfolio, AggAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time. The records supplied by this feed are used to update the **CompositeAccount** time series property *componentList*. Whenever a membership is updated, the holdings for the **CompositeAccount** are recreated for that date.

  A number of [related feeds](#related%20feeds) are available to create new **Account** instances and to update other account-based information.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| groupId | String | id of existing [CompositeAccount](pma_CompositeAccountMaster.md) instance |
| memberId | String | id of existing Account instance |
| date | Date | date of the membership |
| weight | Number | percentage of member's holdings to include in composite |

## Special Processing Rules:

- The *groupId* and *memberId* fields must be supplied. The *groupId* must correspond to an existing **CompositeAccount** instance. The *memberId* must correspond to an existing **Portfolio**, **AggAccount**, **IndexAccount**, or **CompositeAccount** instance.
- The *date* field indicates the date for which the composite holdings should be created using the supplied membership. It can be supplied in any valid date format such as *19971215* or *12/15/97*.
- The *weight* field indicates the percentage of the component account to use in constructing this composite. Component weights need not add up to 100.
- The *componentList* time series property will be updated for each *groupId/date* combination included in this feed with an IndexedList of **CompositeAccount Component** instances. Because the memberships will replace the existing *componentList* for a date, you must specify all the components for each *groupId/date* included.
- Holdings for the **CompositeAccounts** referenced in this feed will be recreated on the date referenced. The **CompositeAccount** time series properties *\_totalMarketValue*, *\_totalMarketValueCash*, *\_totalMarketValueEquity*, *\_totalMarketValueFixed*, and *\_totalCost*, are computed as well as the holding properties *percentOfPort* and *percentOfEquity*.
- Note that **CompositeAccount** holdings are **not** recreated if the holdings associated with any of its component accounts are updated.

<span id="related feeds"></span>

## Related Feeds:

- [*CompositeAccountMaster*](pma_CompositeAccountMaster.md): creates CompositeAccount instances
- [*PortfolioMaster*](pma_PortfolioMaster.md): creates Portfolio instances
- [*AggAccountMaster*](pma_AggAccountMaster.md): creates AggAccount instances
- [*IndexAccountMaster*](pma_IndexAccountMaster.md): creates IndexAccount instances
- [*HoldingsFeed*](pma_HoldingsFeed.md): loads holding records for one or more Portfolio or CompositeAccount instances for one or more time periods
- [*PortfolioAggregates*](pma_PortfolioAggregates.md): defines Portfolio memberships in AggAccounts over time
- [*IndexAccountBuilder*](pma_IndexAccountBuilder.md): creates holdings for one or more IndexAccount instances over time using existing Security Universe instances and a weighting rule

## Sample Upload:

The following tab-delimited feed could be used to define **CompositeAccount** memberships over time.

      Interface ExternalFeedManager upload: "CompositeAccountMembers" using:
      "date  groupId     memberId     weight

       #- create a composite representing 50% of PORT1's holdings
       97    COMP1       PORT1        50

       #- create a composite represent equal amounts of 4 accounts
       #- in 95, unequal amounts in 96
       95    COMP2       PORT7      25
       95    COMP2       AGG1       25
       95    COMP2       INDEX7     25
       95    COMP2       COMP1      25
       96    COMP2       PORT7      33
       96    COMP2       AGG1       33
       96    COMP2       INDEX7     33
       96    COMP2       COMP1      1
      " ;

{% include doc-footer.htm copydates="1998-1999" %}
