---
provenance: "docs/original/pma_CurrencyMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: CurrencyMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Currency instance"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "conversion", "property": "conversion", "type": "Number", "desc": "-"}, {"name": "underlyingCurrency", "property": "underlyingCurrency", "type": "String", "desc": "main currency for exchange rate storage"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *CurrencyMaster*

**Category:** *MasterFeed*

## Summary:

- The *CurrencyMaster* feed is used to create and refresh basic information for **Currency** instances. Instances of this class represent currencies in which monetary transactions are performed. The **Currency** class is described in detail in the [*Vision Class: Currency*](../classes/clCurrency.md) document. A number of [related feeds](#related%20feeds) are also available.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Currency instance |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| conversion | conversion | Number | \- |
| underlyingCurrency | underlyingCurrency | String | main currency for exchange rate storage |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- Monetary values are sometimes expressed as a fraction or multiple of a base currency. For example, data may be expressed in pence instead of pounds. When you define a currency such as *pence*, you also want to establish a relationship to its parent currency, the *pound*. The *underlyingCurrency* field is used to define the parent currency. The *conversion* field is used to specify the unit of exchange needed to covert the currency to its parent. In the *pence-to-pound* scenario, this value would be 100 (100 pence to the pound). Exchange rate information is only maintained for the parent currency. See [*Creating Related Currencies*](../classes/clCurrency/3.md) for more information.

<span id="related feeds"></span>

## Related Feeds:

- [*ExchangeRateFeed*](pma_ExchangeRateFeed.md): loads exchange rate information over time

## Sample Upload:

The following tab-delimited feed could be used to create **Currency** instances and refresh basic information:

       Interface ExternalFeedManager upload: "CurrencyMaster" using:
       "Id      Name           underlyingCurrency       conversion
        USD     US Dollar      
        CAD     Canadian Dollar 
        GBP     British Pound
        BPN     British Pence       GBP         100
       "  ;

{% include doc-footer.htm copydates="1998" %}
