---
provenance: "docs/original/pma_EconFeed.htm"
unit_type: "feed"
title: "Vision Upload Format: EconFeed "
ingested: "2026-09-22"
entity: "EconomicData"
fields: [{"name": "entityId", "property": "entity", "type": "String", "desc": "any valid country identifier"}, {"name": "date", "property": "date", "type": "Date", "desc": "date of data"}, {"name": "gnp", "property": "gnp", "type": "Number", "desc": "Gross National Production"}, {"name": "cpi", "property": "cpi", "type": "Number", "desc": "Consumer Price Index"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *EconFeed*

**Category:** *EntityExtenderFeed*

## Summary:

- The *EconFeed* feed is used to create and update **EconomicData** data record instances for countries. A single **EconomicData** record is created for each **Country**; time series properties are defined for this record and can be updated at whatever frequency is appropriate for the series. The data is accessed via the property *econData* defined for the **Country** class.

  This feed can include data for any number of countries for any number of dates and can be used to set initial values for properties and/or change existing values.

  This class is described in the [*Portfolio Management Application Supplemental Classes*](pmaSupp.htm#Econ) document.

## Available Fields:

| Field | EconomicData Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | entity | String | any valid country identifier |
| date | date | Date | date of data |
| --- Suggested Fields --- |  |  |  |
| gnp | gnp | Number | Gross National Production |
| cpi | cpi | Number | Consumer Price Index |

## Special Processing Rules:

- The *entityId* must correspond to an existing **Country** instance. Any valid country alias can be used to identify the country.
- The *date* is used to update any of the fields associated with time series properties. It can be in any valid date format such as *9705* or *5/31/97*.
- A country's **EconomicData** record is attached to the country via the fixed property *econData*. The individual properties associated with the record are defined to vary over time. A single upload should include fields that vary over time with the same frequency.

<span id="related"></span>

## Related Feeds:

- [*CountryMaster*](pma-CountryMaster.md): defines Country instances referenced by this feed

## Sample Upload:

The following tab-delimited feed could be used to create and update **EconomicData** instances:

      Interface ExternalFeedManager upload: "EconFeed" using:
         "entityId     date       gnp      cpi
          US           95         1234.56  987.65
          US           96         2345.67  876.54
          CA           95         111.22   33.44
          CA           96         222.33   44.55
         " ;

{% include doc-footer.htm copydates="1998" %}
