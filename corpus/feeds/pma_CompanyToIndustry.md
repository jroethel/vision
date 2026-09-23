---
provenance: "docs/original/pma_CompanyToIndustry.htm"
unit_type: "feed"
title: "Vision Upload Format: CompanyToIndustry "
ingested: "2026-09-22"
entity: "CompanyToIndustry"
fields: [{"name": "groupId", "property": "", "type": "String", "desc": "id of existing [Industry](pma_IndustryMaster.md) instance", "ref": "pma_IndustryMaster"}, {"name": "memberId", "property": "", "type": "String", "desc": "id of existing [Company](pma_CompanyMaster.md) instance", "ref": "pma_CompanyMaster"}, {"name": "date", "property": "", "type": "Date", "desc": "date of the membership"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *CompanyToIndustry*

**Category:** *MembershipFeed*

## Summary:

- The *CompanyToIndustry* feed is used to track a company's industry over time and to cross reference the companies included in each industry over time. The records supplied by this feed are used to update the **Company** time series property *industry* and the **Industry** time series property *memberList*.

  This relationship is described in the [*Portfolio Management Application Core Classes*](pmaClasses.htm#Memberships) document.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| groupId | String | id of existing [Industry](pma_IndustryMaster.md) instance |
| memberId | String | id of existing [Company](pma_CompanyMaster.md) instance |
| --- Suggested Fields --- |  |  |
| date | Date | date of the membership |

## Special Processing Rules:

- The *groupId* and *memberId* fields must be supplied. The *groupId* must correspond to an existing **Industry** instance. The *memberId* must correspond to an existing **Company** instance.
- The *date* field is optional and should be supplied if you want to track industry changes over time. It can be supplied in any valid date format such as *19971215* or *12/15/97*. To specify an initial membership, use the date *10101* or the string *Default* as the value of the *date* field.
- The *industry* time series property at **Company** will be updated as of the supplied *date* with the **Industry** indicated by the supplied *groupId*. The *memberList* time series property at **Industry** will be updated for each **Industry/date** combination affected by this feed.
- To indicate that the company no longer has an industry (if the company is acquired for example), use the string *Default* as the value of *groupId* field.
- This feed is designed as an *append-style* update. You only need to supply records for dates on which a company's industry has changed.

<span id="related"></span>

## Related Feeds:

- [*IndustryMaster*](pma_IndustryMaster.md): creates Industry instances
- [*CompanyMaster*](pma_CompanyMaster.md): creates Company instances

## Sample Upload:

The following tab-delimited feed could be used to define *company-industry* memberships over time.

      Interface ExternalFeedMaster upload: "CompanyToIndustry" using:
        "memberId     groupId     date
         00036110     560         Default
         00036110     120         19951231
         00079410     740         Default
         00079410     120         19931231
         00079410     Default     19960115
         00163T10     140         Default
        " ;

{% include doc-footer.htm copydates="1998-1999" %}
