---
provenance: "docs/original/pma_UniverseMembers.htm"
unit_type: "feed"
title: "Vision Upload Format: UniverseMembers "
ingested: "2026-09-22"
entity: "UniverseMembers"
fields: [{"name": "groupId", "property": "", "type": "String", "desc": "id of existing [Universe](pma_UniverseMaster.md) instance", "ref": "pma_UniverseMaster"}, {"name": "memberId", "property": "", "type": "String", "desc": "id of existing Entity instance appropriate for Universe"}, {"name": "date", "property": "", "type": "Date", "desc": "date of the membership"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *UniverseMembers*

**Category:** *MembershipFeed*

## Summary:

- The *UniverseMembers* feed is used to define the member **Entities** in a **Universe** over time. The records supplied by this feed are used to update the **Universe** time series property *list*.

  This class is described in detail in the [*Vision Class: Universe*](clUniverse.htm) document.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| groupId | String | id of existing [Universe](pma_UniverseMaster.md) instance |
| memberId | String | id of existing Entity instance appropriate for Universe |
| --- Suggested Fields --- |  |  |
| date | Date | date of the membership |

## Special Processing Rules:

- The *groupId* and *memberId* fields must be supplied. The *groupId* must correspond to an existing **Universe** instance. The *memberId* must correspond to an existing **Entity** instance of the class defined for the **Universe**.
- The *date* field is optional and should be supplied if you want to track membership changes in a universe over time. It can be supplied in any valid date format such as *19971215* or *12/15/97*. To specify an initial membership, use the date *10101* or the string *Default* as the value of the *date* field.
- The *list* time series property will be updated for each *groupId/date* combination included in this feed with an IndexedList of the appropriate entity instances specified by this feed. Because the memberships will replace the existing *list* for a date, you must specify all the members for each *groupId/date* included.

<span id="related"></span>

## Related Feeds:

- [*UniverseMaster*](pma_UniverseMaster.md): creates Universe instances

## Sample Upload:

The following tab-delimited feed could be used to define **Universe** memberships over time.

    Interface ExternalFeedManager upload: "UniverseMembers" using:
         "groupId     date       memberId
          SP500       19971031   45920010   
          SP500       19971031   37044210   
          SP500       19971031   88553510   
          SP500       19971031   00282410   
          SP500       19971031   00724F10   
          #---  ...
          SP500       19971130   45920010   
          SP500       19971130   37044210   
          SP500       19971130   88553510   
          SP500       19971130   00282410   
          SP500       19971130   00724F10   
          #---  ...
          DJT         Default    01165910
          DJT         Default    00176510
          DJT         Default    00202M10
          #---  ...
         " ;

{% include doc-footer.htm copydates="1998-1999" %}
