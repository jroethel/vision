---
provenance: "docs/original/pma_CompanyMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: CompanyMaster"
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Company instance"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of existing [Currency](pma_CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "analyst", "property": "analyst", "type": "String", "desc": "id of existing [Analyst](pma_AnalystMaster.md) instance", "ref": "pma_AnalystMaster"}, {"name": "country", "property": "country", "type": "String", "desc": "id of existing [Country](pma_CountryMaster.md) instance", "ref": "pma_CountryMaster"}, {"name": "fiscalYearEnd", "property": "fiscalYearEnd", "type": "Integer", "desc": "fiscal year end month"}, {"name": "industry", "property": "industry", "type": "String", "desc": "id of existing [Industry](pma_IndustryMaster.md) instance", "ref": "pma_IndustryMaster"}, {"name": "primaryCompany", "property": "_primaryCompany", "type": "String", "desc": "id of parent company"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *CompanyMaster*

**Category:** *MasterFeed*

## Summary:

- The *CompanyMaster* feed is used to create and refresh basic information for **Company** instances. Companies represent the actual corporate entity. One or more **Security** instances may be associated with a specific company. Fundamental company information is usually stored with the companies; pricing, dividend, and split related information is usually stored with the securities. The **Company** class is described in detail in the [*Portfolio Management Application Classes*](../classes/clpmaCompany/9.md) document. A number of [related feeds](pma_CompanyMaster.htm#related%20feeds) are also available.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Company instance |
| --- Suggested Fields --- |  |  |  |
| currencyId | baseCurrency | String | id of existing [Currency](pma_CurrencyMaster.md) instance |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| analyst | analyst | String | id of existing [Analyst](pma_AnalystMaster.md) instance |
| country | country | String | id of existing [Country](pma_CountryMaster.md) instance |
| fiscalYearEnd | fiscalYearEnd | Integer | fiscal year end month |
| industry | industry | String | id of existing [Industry](pma_IndustryMaster.md) instance |
| primaryCompany | \_primaryCompany | String | id of parent company |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- The *entityId* can be a unique id assigned by your organization (or your company master source) that permanently identifies the company. The aliases associated with any security for that company are also valid as the identifier (e.g., the cusip or sedol of a security issued by the company).
- The *currencyId* is used to identify the currency in which monetary values for the company are displayed by default. This currency may differ from the currencies of the securities for that company.
- *primaryCompany* can be used to set a parent company when it is different from the company (e.g., GMH's primaryCompany is GM).

<span id="related feeds"></span>

## Related Feeds:

- [*SecurityMaster*](pma_SecurityMaster.md): defines Security instances which reference companies
- [*FundamentalA*](pma_FundamentalA.md): loads company annual fundamentals over time
- [*FundamentalQ*](pma_FundamentalQ.md): loads company quarterly fundamentals over time
- [*FundamentalM*](pma_FundamentalM.md): loads company monthly fundamentals over time
- [*CompanyToCountry*](pma_CompanyToCountry.md): manages company-country relationship
- [*CompanyToIndustry*](pma_CompanyToIndustry.md): manages company-industry relationship over time
- [*CompanyToAnalyst*](pma_CompanyToAnalyst.md): manages company-analyst relationship over time

## Sample Upload:

The following tab-delimited feed could be used to create **Company** instances and refresh basic information:

       Interface ExternalFeedManager upload: "CompanyMaster" using:
       "Id      Name        fiscalYearEnd
        00036110    AAR CORP         5
        00079410    ACC CORP         12
        00095710    ABM INDUSTRIES       10 
       "  ;

{% include doc-footer.htm copydates="2000" %}
