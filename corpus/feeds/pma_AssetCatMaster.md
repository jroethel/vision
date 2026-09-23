---
provenance: "docs/original/pma_AssetCatMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: AssetCatMaster"
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing AssetCategory instance"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *AssetCatMaster*

**Category:** *MasterFeed*

## Summary:

- The *AssetCatMaster* feed is used to create and refresh basic information for **AssetCategory** instances. This class is described in more detail in the [*Portfolio Management Application Classes*](../classes/clpmaCompany/9.md) document.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing AssetCategory instance |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

<span id="related"></span>

## Related Feeds:

- [*SecurityTypeMaster*](pma_SecurityTypeMaster.md): updates SecurityType instances with assetCategory

## Sample Upload:

The following tab-delimited feed could be used to create **AssetCategory** instances and refresh basic information:

      Interface ExternalFeedManager upload:  "AssetCatMaster" using:
      "EntityId     Name
       Equity       Equity
       Fixed        Fixed Income
       Cash         Cash & Equivalents
       Other        Other Assets   
       "  ;

{% include doc-footer.htm copydates="1998" %}
