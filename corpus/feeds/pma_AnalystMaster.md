---
provenance: "docs/original/pma_AnalystMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: AnalystMaster"
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Analyst instance"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of existing [Currency](pma_CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *AnalystMaster*

**Category:** *MasterFeed*

## Summary:

- The *AnalystMaster* feed is used to create and refresh basic information for **Analyst** instances.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Analyst instance |
| --- Suggested Fields --- |  |  |  |
| currencyId | baseCurrency | String | id of existing [Currency](pma_CurrencyMaster.md) instance |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

<span id="related"></span>

## Related Feeds:

- [*CompanyToAnalyst*](pma_CompanyToAnalyst.md): manages company-analyst relationship over time
- [*AnalystEst*](pma_AnalystEst.md): loads analyst estimate information for companies

## Sample Upload:

The following tab-delimited feed could be used to create **Analyst** instances and refresh basic information:

       Interface ExternalFeedManager upload: "AnalystMaster" using:
       "EntityId        Name
        A1          Analyst 1
        A2          Analyst 2
        " ;

{% include doc-footer.htm copydates="1998" %}
