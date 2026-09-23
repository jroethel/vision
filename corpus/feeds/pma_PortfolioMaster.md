---
provenance: "docs/original/pma_PortfolioMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: PortfolioMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Portolio instance"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of existing [Currency](pma_CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *PortfolioMaster*

**Category:** *MasterFeed*

## Summary:

- The *PortfolioMaster* feed is used to create and refresh basic information for **Portfolio** instances. Portfolios usually represent real accounts whose holdings are supplied from an accounting system. The **Portfolio** class is described in detail in the [*Portfolio Management Application Classes*](../classes/clpmaAccount/8.md) document. A number of [related fields](#related%20feeds) are available to create **Portfolio** holdings and to update other account-based information.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Portolio instance |
| --- Suggested Fields --- |  |  |  |
| currencyId | baseCurrency | String | id of existing [Currency](pma_CurrencyMaster.md) instance |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

The *entityId* is the unique id that permanently identifies the Portfolio. When a new Portfolio is created, this field is used to update the *code* property of the new instance. This id is also added to the **Named Portfolio** and **Named Account** naming dictionaries. If a non-portfolio instance with this id is already defined in the **Named Account** dictionary, this reference is replaced with the reference to the new **Portfolio** instance.

To distinguish **Portfolio** instances from instances of other **Account** subclasses that may be identified with the same id, a unique identifier is created by prepending the string *P\_* to the *entityId*. This id is used to update the *uniqueId* property of new **Portfolio** instances and is added to the **Account** naming dictionary as well.

The *currencyId* is used to identify the currency in which monetary values for the portfolio are displayed by default. This includes the *totalMarketValue* and the *totalMarketValueCash* values for the **Portfolio** as well as the *totalMarketValue* for its individual holdings. The default value is US Dollars.

<span id="related feeds"></span>

## Related Feeds:

- [*HoldingsFeed*](pma_HoldingsFeed.md): loads holding records for one or more Portfolio or IndexAccount instances for one or more time periods
- [*AggAccountMaster*](pma_AggAccountMaster.md): creates AggAccount instances
- [*PortfolioAggregates*](pma_PortfolioAggregates.md): defines Portfolio memberships in AggAccounts over time
- [*CompositeAccountMaster*](pma_CompositeAccountMaster.md): creates CompositeAccount instances
- [*CompositeAccountMembers*](pma_CompositeAccountMembers.md): defines weighted combinations of Portfolio, AggAccount, IndexAccount, and/or other CompositeAccount instances that make up a composite over time
- [*IndexAccountMaster*](pma_IndexAccountMaster.md): creates IndexAccount instances
- [*IndexAccountBuilder*](pma_IndexAccountBuilder.md): creates holdings for one or more IndexAccount instances over time using existing Security Universe instances and a weighting rule

## Sample Upload:

The following tab-delimited feed could be used to create **Portfolio** instances and refresh basic information:

       Interface ExternalFeedManager upload: "PortfolioMaster" using:
       "entityId         Name                         ShortName
        PORT1            EQUITY INCOME FUND           EI FUND
        PORT2            GROWTH FUND                  GR FUND 
       "  ;

{% include doc-footer.htm copydates="1998" %}
