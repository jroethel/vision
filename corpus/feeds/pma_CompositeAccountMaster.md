---
provenance: "docs/original/pma_CompositeAccountMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: CompositeAccountMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing CompositeAccount instance"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of existing [Currency](pma_CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *CompositeAccountMaster*

**Category:** *MasterFeed*

## Summary:

- The *CompositeAccountMaster* feed is used to create and refresh basic information for **CompositeAccount** instances. A composite account is an **Account** whose holdings are created as a weighted combination of the holdings in the set of Portfolio, IndexAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time. The **CompositeAccount** class is described in detail in the [*Portfolio Management Application Classes*](../classes/clpmaAccount/14.md) document. A number of [related feeds](#related%20feeds) are available to specify **CompositeAccount** membership weights and to update other account-based information.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing CompositeAccount instance |
| --- Suggested Fields --- |  |  |  |
| currencyId | baseCurrency | String | id of existing [Currency](pma_CurrencyMaster.md) instance |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- The *entityId* is the unique id that permanently identifies the CompositeAccount. When a new CompositeAccount is created, this field is used to update the *code* property of the new instance. This id is also added to the **Named CompositeAccount** naming dictionary. It is added to the **Named Account** dictionary if the id does not conflict with the id of an instance from a different subclass of **Account**. If a **Portfolio** instance is later created with the same id as an existing **CompositeAccount**, the reference in the **Named Account** dictionary will return the **Portfolio** instance.
- To distinguish **CompositeAccount** instances from instances of other **Account** subclasses that may be identified with the same id, a unique identifier is created by prepending the string *C\_* to the *entityId*. This id is used to update the *uniqueId* property of new **CompositeAccount** instances and is added to the **Account** naming dictionary as well.
- The *currencyId* is used to identify the currency in which monetary values for the composite account are displayed by default. This includes the *totalMarketValue* and the *totalMarketValueCash* values for the **CompositeAccount** as well as the *totalMarketValue* for its individual holdings. The default value is US Dollars.

<span id="related feeds"></span>

## Related Feeds:

- [*CompsiteAccountMembers*](pma_CompositeAccountMembers.md): defines weighted combinations of Portfolio, AggAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time
- [*PortfolioMaster*](pma_PortfolioMaster.md): creates Portfolio instances
- [*HoldingsFeed*](pma_HoldingsFeed.md): loads holding records for one or more Portfolio or CompositeAccount instances for one or more time periods
- [*AggAccountMaster*](pma_AggAccountMaster.md): creates AggAccount instances
- [*PortfolioAggregates*](pma_PortfolioAggregates.md): defines Portfolio memberships in AggAccounts over time
- [*IndexAccountMaster*](pma_IndexAccountMaster.md): creates IndexAccount instances
- [*IndexAccountBuilder*](pma_IndexAccountBuilder.md): creates holdings for one or more IndexAccount instances over time using existing Security Universe instances and a weighting rule

## Sample Upload:

The following tab-delimited feed could be used to create **CompositeAccount** instances and refresh basic information:

      Interface ExternalFeedManager upload: "CompositeAccountMaster" using:
       "entityId    name                ShortName
        COMP1   Composite Account 1 Composite Acct 1
        COMP2   Composite Account 2 Composite Acct 2
        "  ;

{% include doc-footer.htm copydates="1998" %}
