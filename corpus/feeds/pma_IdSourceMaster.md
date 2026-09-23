---
provenance: "docs/original/pma_IdSourceMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: IdSourceMaster "
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing IdSource instance"}, {"name": "name", "property": "name", "type": "String", "desc": "descriptive name"}, {"name": "xrefName", "property": "xrefName", "type": "String", "desc": "name of XRef (if different from code)"}, {"name": "xrefProperty", "property": "xrefProperty", "type": "String", "desc": "name of property (if different from code)"}, {"name": "primaryFlag", "property": "primaryFlag", "type": "Boolean", "desc": "track source at Named as well"}, {"name": "retainOldFlag", "property": "retainOldFlag", "type": "Boolean", "desc": "keep old values in cross reference"}, {"name": "numericCode", "property": "numericCode", "type": "Number", "desc": "numeric code"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *IdSourceMaster*

**Category:** *MasterFeed*

## Summary:

- The *IdSourceMaster* feed is used to create and refresh basic information for **IdSource** instances. **IdSources** are used to define standard sources of entity identification schemas. Alternative identifiers are stored in [cross reference dictionaries (*XRef's*)](../classes/clDict/5.md) defined for an **Entity** class. XRef's provide a convenient way to track identifiers that are uniquely assigned by a specific source but may overlap with identifiers assigned by other sources.

## Available Fields:

| Field | Vision Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | code | String | id of new or existing IdSource instance |
| --- Suggested Fields --- |  |  |  |
| name | name | String | descriptive name |
| xrefName | xrefName | String | name of XRef (if different from code) |
| xrefProperty | xrefProperty | String | name of property (if different from code) |
| primaryFlag | primaryFlag | Boolean | track source at Named as well |
| retainOldFlag | retainOldFlag | Boolean | keep old values in cross reference |
| --- Other Fields --- |  |  |  |
| numericCode | numericCode | Number | numeric code |
| shortName | shortName | String | short name |
| sortCode | sortCode | String | sort code |

## Special Processing Rules:

- The *xrefName* is used to identify the name of the **XRef** dictionary that will be used to store aliases supplied by this source; by default, this value will be the same as the instance's *code*.
- The *xrefProperty* is used to identify the name of the property to be defined at the **entity** class which will hold the current value of the identifier supplied by this source.
- The *primaryFlag* can be set to *Yes (True)* or *No (False)* to indicate that the source should be viewed as a primary supplier of identifiers. Identifiers for primary sources are tracked in the local cross reference and the entity's shared naming dictionary. By default, a source is not flagged as primary.
- The *retainOldFlag* can be set to *Yes (True)* or *No (False)* to indicate that the old values of the identifier should be maintained as aliases in the cross reference. If set to true, an old identifier can be used to access the underlying entity instance until it is reassigned by the source to reference a different entity. By default, a source is not flagged to retain old values.

<span id="related"></span>

## Related Feeds:

- [*SecurityXRef*](pma_SecurityXRef.md): loads cross reference ids by source

## Sample Upload:

The following tab-delimited feed could be used to create **IdSource** instances and refresh basic information:

       Interface ExternalFeedManager upload: "IdSourceMaster" using:
       "Id        Name       primaryFlag   xrefName   xrefProperty  retainOldFlag
        CUSIP     Cusip      Yes           Cusip      cusip         Yes
        SEDOL     Sedol      Yes           Sedol      sedol         Yes
        TICKERUS  US Ticker  Yes           TickerUS   ticker        No
        RIC       Reuters    No            Ric        ricCode       No
        ISIN      Isin       Yes           Isin       isin          No
        Valor     Valor      No            Valor      valor         No 
       " ;

{% include doc-footer.htm copydates="1998" %}
