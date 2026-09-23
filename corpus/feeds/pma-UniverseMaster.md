---
provenance: "docs/original/pma_UniverseMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: UniverseMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Universe instance"}, {"name": "memberType", "property": "memberType", "type": "String", "desc": "id of existing Entity class"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *UniverseMaster*

**Category:** *MasterFeed*

## Summary:

- The *UniverseMaster* feed is used to create and refresh basic information for **Universe** instances. A **Universe** is used to name and track lists of related entities over time. This class is described in detail in the [*Vision Class: Universe*](../classes/clUniverse.md) document. A number of [related feeds](#related%20feeds) are also available.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing Universe instance |
| memberType | memberType | String | id of existing Entity class |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- The *memberType* should reference an existing Entity class that represents the type of entity to be tracked by this universe.

<span id="related feeds"></span>

## Related Feeds:

- [*UniverseMembers*](pma-UniverseMembers.md): updates memberships for universes over time

## Sample Upload:

The following tab-delimited feed could be used to create **Universe** instances and refresh basic information:

       Interface ExternalFeedManager upload: "UniverseMaster" using:
       "Id       Name                        MemberType
        SP500    Standard & Poors 500        Security
        DJ30     Dow Jones 30 Industrials    Security
       "  ;

{% include doc-footer.htm copydates="1998" %}
