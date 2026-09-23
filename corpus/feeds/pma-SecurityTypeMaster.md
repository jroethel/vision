---
provenance: "docs/original/pma_SecurityTypeMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: SecurityTypeMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing SecurityType instance"}, {"name": "assetCategory", "property": "assetCategory", "type": "String", "desc": "id of existing [AssetCategory](pma-AssetCatMaster.md) instance", "ref": "pma_AssetCatMaster"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "unitCalc", "property": "unitCalc", "type": "1.00", "desc": "multiplier for market value calcs"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *SecurityTypeMaster*

**Category:** *MasterFeed*

## Summary:

- The *SecurityTypeMaster* feed is used to create and refresh basic information for **SecurityType** instances. This class is described in more detail in the [*Portfolio Management Application Classes*](pmaClasses.htm#SecurityType) document. The field *unitCalc* has been moved from Required Fields to Suggested Fields.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing SecurityType instance |
| assetCategory | assetCategory | String | id of existing [AssetCategory](pma-AssetCatMaster.md) instance |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| unitCalc | unitCalc | 1.00 | multiplier for market value calcs |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- The *assetCategory* and *unitCalc* values are used as part of the holdings generation process for portfolios. See the [*HoldingFeed*](pma-HoldingsFeed.md) document for more information.

<span id="related"></span>

## Related Feeds:

- [*AssestCatMaster*](pma-AssetCatMaster.md): defines AssetCategory instances by SecurityType

## Sample Upload:

The following tab-delimited feed could be used to create **SecurityType** instances and refresh basic information:

       Interface ExternalFeedManager upload: "SecurityTypeMaster" using:
       "Id   Name              UnitCalc     AssetCategory
        0    Cash & Equiv       1.00     Cash
        1    Common Stock       1.00         Equity
        2    Corporate Bond    10.00         Fixed
        3    Gvt Bond          10.00         Fixed
        4    Option           100.00         Other 
       " ;

w {% include doc-footer.htm copydates="1998" %}
