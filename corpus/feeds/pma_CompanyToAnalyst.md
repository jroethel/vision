---
provenance: "docs/original/pma_CompanyToAnalyst.htm"
unit_type: "feed"
title: "Vision Upload Format: CompanyToAnalyst"
ingested: "2026-09-22"
entity: "CompanyToAnalyst"
fields: [{"name": "groupId", "property": "", "type": "String", "desc": "id of existing [Analyst](pma_AnalystMaster.md) instance", "ref": "pma_AnalystMaster"}, {"name": "memberId", "property": "", "type": "String", "desc": "id of existing [Company](pma_CompanyMaster.md) instance", "ref": "pma_CompanyMaster"}, {"name": "date", "property": "", "type": "Date", "desc": "date of the membership"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *CompanyToAnalyst*

**Category:** *MembershipFeed*

## Summary:

- The *CompanyToAnalyst* feed is used to track a company's analyst over time and to cross reference the companies followed by each analyst over time. The records supplied by this feed are used to update the **Company** time series property *analyst* and the **Analyst** time series property *memberList*.

  This relationship is described in the [*Portfolio Management Application Supplemental Core Classes*](pmaSupp.htm#Analyst) document.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| groupId | String | id of existing [Analyst](pma_AnalystMaster.md) instance |
| memberId | String | id of existing [Company](pma_CompanyMaster.md) instance |
| --- Suggested Fields --- |  |  |
| date | Date | date of the membership |

## Special Processing Rules:

- The *groupId* and *memberId* fields must be supplied. The *groupId* must correspond to an existing **Analyst** instance. The *memberId* must correspond to an existing **Company** instance.
- The *date* field is optional and should be supplied if you want to track analyst changes over time. It can be supplied in any valid date format such as *19971215* or *12/15/97*. To specify an initial membership, use the date *10101* or the string *Default* as the value of the *date* field.
- The *analyst* time series property at **Company** will be updated as of the supplied *date* with the **Analyst** indicated by the supplied *groupId*. The *memberList* time series property at **Analyst** will be updated for each **Analyst/date** combination affected by this feed.
- To indicate that the company no longer has an analyst use the string *Default* as the value of *groupId* field.
- This feed is designed as an *append-style* update. You only need to supply records for dates on which a company's analyst has changed.

<span id="related"></span>

## Related Feeds:

- [*AnalystMaster*](pma_AnalystMaster.md): creates Analyst instances
- [*CompanyMaster*](pma_CompanyMaster.md): creates Company instances

## Sample Upload:

The following tab-delimited feed could be used to define *company-analyst* memberships over time.

    Interface ExternalFeedMaster upload: "CompanyToAnalyst" using:
         "memberId     groupId     date
          00036110     A1         Default
          00036110     A2         19951231
          00079410     A2         Default
          00079410     A3         19931231
          00079410     Default    19960115
          00163T10     A3         Default
         " ;

{% include doc-footer.htm copydates="1998-1999" %}
