---
provenance: "docs/original/pma_IndustryToSector.htm"
unit_type: "feed"
title: "Vision Upload Format: IndustryToSector "
ingested: "2026-09-22"
entity: "IndustryToSector"
fields: [{"name": "groupId", "property": "", "type": "String", "desc": "id of existing [Sector](pma_SectorMaster.md) instance", "ref": "pma_SectorMaster"}, {"name": "memberId", "property": "", "type": "String", "desc": "id of existing [Industry](pma_IndustryMaster.md) instance", "ref": "pma_IndustryMaster"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *IndustryToSector*

**Category:** *MembershipFeed*

## Summary:

- The *IndustryToSector* feed is used to define an industry's sector and to cross reference the industries included in each sector. The records supplied by this feed are used to update the **Industry** property *sector* and the **Sector** property *memberList*.

  This relationship is described in the [*Portfolio Management Application Core Classes*](pmaClasses.htm#Memberships) document.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| groupId | String | id of existing [Sector](pma_SectorMaster.md) instance |
| memberId | String | id of existing [Industry](pma_IndustryMaster.md) instance |

## Special Processing Rules:

- The *groupId* and *memberId* fields must be supplied. The *groupId* must correspond to an existing **Sector** instance. The *memberId* must correspond to an existing **Industry** instance.
- The *sector* property at **Industry** will be updated with the **Sector** indicated by the supplied *groupId*. The *memberList* property at **Sector** will be updated for each **Sector** affected by this feed.
- To indicate that the industry should not be included in any sector, use the string *Default* as the value of *groupId* field.
- This feed is designed as an *append-style* update. You only need to supply records that assign initial sector values or that change existing ones.

<span id="related"></span>

## Related Feeds:

- [*SectorMaster*](pma_SectorMaster.md): creates Sector instances
- [*IndustryMaster*](pma_IndustryMaster.md): creates Industry instances

## Sample Upload:

The following tab-delimited feed could be used to define *industry-sector* memeberships over time.

    Interface ExternalFeedManager upload: "IndustryToSector" using:
         "groupId     memberId
          NOND        110
          NOND        120
          NOND        130
          DURB        210
          DURB        220
          DURB        230
         " ;

{% include doc-footer.htm copydates="1998" %}
