---
provenance: "docs/original/pma_CountryMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: CountryMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Country instance"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of existing [Corrency](pma_CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *CountryMaster*

**Category:** *MasterFeed*

## Summary:

- The *CountryMaster* feed is used to create and refresh basic information for **Country** instances.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Country instance |
| --- Suggested Fields --- |  |  |  |
| currencyId | baseCurrency | String | id of existing [Corrency](pma_CurrencyMaster.md) instance |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

<span id="related"></span>

## Related Feeds:

- [*CompanyToCountry*](pma_CompanyToCountry.md): manages company-country relationship
- [*EconFeed*](pma_EconFeed.md): loads economic data for country over time

## Sample Upload:

The following tab-delimited feed could be used to create **Country** instances and refresh basic information:

       Interface ExternalFeedManager upload: "CountryMaster" using:
       "EntityId    Name           Currency
        AT      Austria     ATS
        AU      Australia   AUD
        CA      Canada      CAD
        CH      Switzerland CHF
        US      United States   USD 
       "  ;

{% include doc-footer.htm copydates="1998" %}
