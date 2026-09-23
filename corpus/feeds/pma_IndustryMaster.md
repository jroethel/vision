---
provenance: "docs/original/pma_IndustryMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: IndustryMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Industry instance"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "Numeric code"}, {"name": "sector", "property": "sector", "type": "String", "desc": "id of existing [Sector](pma_SectorMaster.md) instance", "ref": "pma_SectorMaster"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *IndustryMaster*

**Category:** *MasterFeed*

## Summary:

- The *IndustryMaster* feed is used to create and refresh basic information for **Industry** instances.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Industry instance |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | Numeric code |
| sector | sector | String | id of existing [Sector](pma_SectorMaster.md) instance |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

<span id="related"></span>

## Related Feeds:

- [*CompanyToIndustry*](pma_CompanyToIndustry.md): manages company-industry relationship over time
- [*IndustryToSector*](pma_IndustryToSector.md): manages industry-sector relationship

## Sample Upload:

The following tab-delimited feed could be used to create **Industry** instances and refresh basic information:

       Interface ExternalFeedManager upload: "IndustryMaster" using:
       "EntityId    Name           
        110     Beverages
        120     Cosmetics
        130     Alcoholic Beverages
        140     Tobacco Products
        150     Grocery Products
        160     Apparel
        190     Other Consumer Non-durables
       "  ;

{% include doc-footer.htm copydates="1998" %}
