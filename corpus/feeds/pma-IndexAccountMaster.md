---
provenance: "docs/original/pma_IndexAccountMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: IndexAccountMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing IndexAccount instance"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of existing [Currency](pma-CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *IndexAccountMaster*

**Category:** *MasterFeed*

## Summary:

- The *IndexAccountMaster* feed is used to create and refresh basic information for **IndexAccount** instances. An index account is an **Account** whose holdings are created starting with a list of securities that can be explicitly provided or derived from a **Universe**. The **IndexAccount** class is described in detail in the [*Portfolio Management Application Classes*](../classes/clpmaAccount/12.md) document. A number of [related feeds](#related%20feeds) are available to update and derive **IndexAccount** holdings and to update other account-based information.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing IndexAccount instance |
| --- Suggested Fields --- |  |  |  |
| currencyId | baseCurrency | String | id of existing [Currency](pma-CurrencyMaster.md) instance |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- The *entityId* is the unique id that permanently identifies the IndexAccount. When a new IndexAccount is created, this field is used to update the *code* property of the new instance. This id is also added to the **Named IndexAccount** naming dictionary. It is added to the **Named Account** dictionary if the id does not conflict with the id of an instance from a different subclass of **Account**. If a **Portfolio** instance is later created with the same id as an existing **IndexAccount**, the reference in the **Named Account** dictionary will return the **Portfolio** instance.
- To distinguish **IndexAccount** instances from instances of other **Account** subclasses that may be identified with the same id, a unique identifier is created by prepending the string *I\_* to the *entityId*. This id is used to update the *uniqueId* property of new **IndexAccount** instances and is added to the **Account** naming dictionary as well.
- The *currencyId* is used to identify the currency in which monetary values for the index account are displayed by default. This includes the *totalMarketValue* and the *totalMarketValueCash* values for the **IndexAccount** as well as the *totalMarketValue* for its individual holdings. The default value is US Dollars.

<span id="related feeds"></span>

## Related Feeds:

- [*HoldingsFeed*](pma-HoldingsFeed.md): loads holding records for one or more Portfolio or IndexAccount instances for one or more time periods
- [*IndexAccountBuilder*](pma-IndexAccountBuilder.md): creates holdings for one or more IndexAccount instances over time using existing Security Universe instances and a weighting rule
- [*PortfolioMaster*](pma-PortfolioMaster.md): creates Portfolio instances
- [*AggAccountMaster*](pma-AggAccountMaster.md): creates AggAccount instances
- [*PortfolioAggregates*](pma-PortfolioAggregates.md): defines Portfolio memberships in AggAccounts over time
- [*CompositeAccountMaster*](pma-CompositeAccountMaster.md): creates CompositeAccount instances
- [*CompositeAccountMembers*](pma-CompositeAccountMembers.md): defines weighted combinations of Portfolio, AggAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time

## Sample Upload:

The following tab-delimited feed could be used to create **IndexAccount** instances and refresh basic information:

       Interface ExternalFeedManager upload: "IndexAccountMaster" using:
       "entityId        name        ShortName
        INDEX1  Index Account 1     Index Acct 1
        INDEX2  Index Account 2     Index Acct 2
        "  ;

{% include doc-footer.htm copydates="1998" %}
