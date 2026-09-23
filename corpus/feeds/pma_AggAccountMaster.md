---
provenance: "docs/original/pma_AggAccountMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: AggAccountMaster"
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing AggAccount instance"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "currencyId", "property": "baseCurrancy", "type": "String", "desc": "id of existing [Currency](pma_CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *AggAccountMaster*

**Category:** *MasterFeed*

## Summary:

- The *AggAccountMaster* feed is used to create and refresh basic information for **AggAccount** instances. An aggregate account is an **Account** whose holdings are created by combining the holdings for a list of member portfolios. The **AggAccount** class is described in detail in the [*Portfolio Management Application Classes*](clpmaAccount.htm#agg) document. A number of [related feeds](#related%20feeds) are available to specify **AggAccount** memberships and to update other account-based information.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing AggAccount instance |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| currencyId | baseCurrancy | String | id of existing [Currency](pma_CurrencyMaster.md) instance |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- The *entityId* is the unique id that permanently identifies the AggAccount. When a new AggAccount is created, this field is used to update the *code* property of the new instance. This id is also added to the **Named AggAccount** naming dictionary. It is added to the **Named Account** dictionary if the id does not conflict with the id of an instance from a different subclass of **Account**. If a **Portfolio** instance is later created with the same id as an existing **AggAccount**, the reference in the **Named Account** dictionary will return the **Portfolio** instance.
- To distinguish **AggAccount** instances from instances of other **Account** subclasses that may be identified with the same id, a unique identifier is created by prepending the string *A\_* to the *entityId*. This id is used to update the *uniqueId* property of new **AggAccount** instances and is added to the **Account** naming dictionary as well.
- The *currencyId* is used to identify the currency in which monetary values for the aggregate account are displayed by default. This includes the *totalMarketValue* and the *totalMarketValueCash* values for the **AggAccount** as well as the *totalMarketValue* for its individual holdings. The default value is US Dollars.

<span id="related feeds"></span>

## Related Feeds:

- [*PortfolioAggregates*](pma_PortfolioAggregates.md): defines Portfolio memberships in AggAccounts over time
- [*PortfolioMaster*](pma_PortfolioMaster.md): creates Portfolio instances
- [*HoldingsFeed*](pma_HoldingsFeed.md): loads holding records for one or more time periods
- [*CompositeAccountMaster*](pma_CompositeAccountMaster.md): creates CompositeAccount instances
- [*CompositeAccountMembers*](pma_CompositeAccountMembers.md): defines weighted combinations of Portolio, AggAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time
- [*IndexAccountMaster*](pma_IndexAccountMaster.md): creates IndexAccount instances
- [*IndexAccountBuilder*](pma_IndexAccountBuilder.md): creates holdings for one or more IndexAccount instances over time using existing Security Universe instances and a weighting rule

## Sample Upload:

The following tab-delimited feed could be used to create **AggAccount** instances and refresh basic information:

      Interface ExternalFeedManager upload: "AggAccountMaster" using:
      "entityId       Name                        ShortName
       AGG1           Aggregate Account 1         Agg Acct 1
       AGG2        Aggregate Account 2         Agg Acct 2
       "  ;

{% include doc-footer.htm copydates="1998" %}
