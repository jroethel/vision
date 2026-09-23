---
provenance: "docs/original/pma_CompanyToCountry.htm"
unit_type: "feed"
title: "Vision Upload Format: CompanyToCountry"
ingested: "2026-09-22"
entity: "CompanyToCountry"
fields: [{"name": "groupId", "property": "", "type": "String", "desc": "id of existing [Country](pma_CountryMaster.md) instance", "ref": "pma_CountryMaster"}, {"name": "memberId", "property": "", "type": "String", "desc": "id of existing [Company](pma_CompanyMaster.md) instance", "ref": "pma_CompanyMaster"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *CompanyToCountry*

**Category:** *MembershipFeed*

## Summary:

- The *CompanyToCountry* feed is used to define a company's country and to cross reference the companies included in each country. The records supplied by this feed are used to update the **Company** property *country* and the **Country** property *memberList*.

  This relationship is described in the [*Portfolio Management Application Core Classes*](clpmaCompany.htm#feeds) document.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| groupId | String | id of existing [Country](pma_CountryMaster.md) instance |
| memberId | String | id of existing [Company](pma_CompanyMaster.md) instance |

## Special Processing Rules:

- The *groupId* and *memberId* fields must be supplied. The *groupId* must correspond to an existing **Country** instance. The *memberId* must correspond to an existing **Company** instance.
- The *country* property at **Company** will be updated with the **Country** indicated by the supplied *groupId*. The *memberList* property at **Country** will be updated for each **Country** affected by this feed.
- To indicate that the company no longer has a country (if the company is acquired for example), use the string *Default* as the value of *groupId* field.
- This feed is designed as an *append-style* update. You only need to supply records that assign initial country values or that change existing ones.
- If a country is assigned to a company that does not have a value for its base currency, the base currency associated with the country is assigned to the company's *baseCurrency* property.

<span id="related"></span>

## Related Feeds:

- [*CountryMaster*](pma_CountryMaster.md): creates Country instances
- [*CompanyMaster*](pma_CompanyMaster.md): creates Company instances

## Sample Upload:

The following tab-delimited feed could be used to define *company-country* membership over time.

      Interface ExternalFeedManager upload: "CompanyToCountry" using:
        "memberId     groupId
         00036110     US    
         00079410     US    
         00194110     CA    
         00443110     MX    
         01310410     US    
         01371610     CA    
        " ;

{% include doc-footer.htm copydates="1998" %}
