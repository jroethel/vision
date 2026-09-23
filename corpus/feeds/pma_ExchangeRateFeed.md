---
provenance: "docs/original/pma_ExchangeRateFeed.htm"
unit_type: "feed"
title: "Vision Upload Format: ExchangeRateFeed"
ingested: "2026-09-22"
entity: "Currency"
fields: [{"name": "entityId", "property": "-", "type": "String", "desc": "any valid currency identifier"}, {"name": "date", "property": "-", "type": "Date", "desc": "date of exchange rate"}, {"name": "usExchange", "property": "usExchange", "type": "Number", "desc": "rate of exchange to us currency"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *ExchangeRateFeed*

**Category:** *EntityExtenderFeed*

## Summary:

- The *ExchangeRateFeed* feed is used to update currency exchange rates over time. The time series *usExchange* tracks daily exchange rates to convert a specific currency into US Dollars. Exchange rates are stored as the number of foreign currency units that are equivalent to one US Dollar.

  The **Currency** class and currency conversions are described in detail in the [*Vision Class: Currency*](../classes/clCurrency.md) document.

## Available Fields:

| Field | Currency Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | \- | String | any valid currency identifier |
| date | \- | Date | date of exchange rate |
| usExchange | usExchange | Number | rate of exchange to us currency |

## Special Processing Rules:

- The *entityId* must correspond to an existing **Currency** instance.
- The *date* must be included and indicates the date of the exchange. It can be in any valid date format such as *19971215* or *12/15/97*.
- The *usExchange* field should contain the number of units in the currency associated with *entityId* that are equivalent to one US Dollar.
- The exchange rates for the eleven Euro countries are automatically updated (legacy fixed rate to EUR \* daily EUR to US rate) when EUR *usExchange* rates are included for the supplied date.

<span id="related"></span>

## Related Feeds:

- [*CurrencyMaster*](pma_CurrencyMaster.md): defines Currency instances referenced by this feed

## Sample Upload:

The following tab-delimited feed could be used to update currency exchange rates.

    terface ExternalFeedManager upload: "ExchangeRateFeed" using:
         "entityId        date      usExchange
          CAD             19971128  1.4234  
          CAD             19971201  1.4238  
          CAD             19971202  1.4219  
          ARS             19971128  0.9996  
          ARS             19971201  0.9999  
          ARS             19971202  0.9999  
          ATS             19971128 12.4142  
          ATS             19971201 12.5080  
          ATS             19971202 12.4888  
         " ;

{% include doc-footer.htm copydates="2000" %}
