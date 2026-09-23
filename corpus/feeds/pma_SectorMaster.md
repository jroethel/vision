---
provenance: "docs/original/pma_SectorMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: SectorMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Sector instance"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *SectorMaster*

**Category:** *MasterFeed*

## Summary:

- The *SectorMaster* feed is used to create and refresh basic information for **Sector** instances.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Sector instance |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

<span id="related"></span>

## Related Feeds:

- [*IndustryToSector*](pma_IndustryToSector.md): manages industry-sector relationship

## Sample Upload:

The following tab-delimited feed could be used to create **Sector** instances and refresh basic information:

       Interface ExternalFeedManager upload: "SectorMaster" using:
       "EntityId    Name           
        NOND    Consumer non-durables
        DURB    Consumer durables
        SERV    Consumer services
        RETL    Retail trade
        TECH    Technology
       "  ;

{% include doc-footer.htm copydates="1998" %}
