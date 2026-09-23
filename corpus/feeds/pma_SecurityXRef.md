---
provenance: "docs/original/pma_SecurityXRef.htm"
unit_type: "feed"
title: "Vision Upload Format: SecurityXRef "
ingested: "2026-09-22"
entity: "SecurityXRef"
fields: [{"name": "entityId", "property": "", "type": "String", "desc": "any valid security identifier"}, {"name": "sourceId", "property": "", "type": "String", "desc": "valid identifier of an IdSource"}, {"name": "symbol", "property": "", "type": "String", "desc": "the symbol supplied by this source for this security"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *SecurityXRef*

**Category:** *XRefFeed*

## Summary:

- The *SecurityXRef* feed is used to load alternative identifiers for a **Security**. Alternative identifiers are stored in [cross reference dictionaries (*XRef's*](../classes/clDict/5.md)) defined for the **Security** class. XRef's provide a convenient way to track identifiers that are uniquely assigned by a specific source but may overlap with identifiers assigned by other sources. Depending on the source, this feed may also update the identifier in the primary naming dictionary as well. The related feed, [*Security Aliases*](pma_SecurityAliases.md), adds ids to the primary naming dictionary only.

## Available Fields:

| Field | Type | Description |
|:--:|:--:|:--:|
| --- Required Fields --- |  |  |
| entityId | String | any valid security identifier |
| sourceId | String | valid identifier of an IdSource |
| symbol | String | the symbol supplied by this source for this security |

## Special Processing Rules:

- The *entityId* must correspond to an existing **Security** instance. Any primary security alias can be used to identify the security.
- The *sourceId* must correspond to an existing **IdSource** instance.
- Each *symbol* is added to the **XRef** dictionary defined by the supplied *sourceID* and associated with the security defined by the supplied *entityId*. If the source is flagged as a primary source, the symbol is also added to the **Named Security** dictionary.
- When the *symbol* for an entity/source changes, the old value is deleted from the cross reference unless the source is flagged to retain old values. If the source is flagged as a primary identifier, the old value is deleted from the **Named Security** dictionary, unless the source is flagged to retain old values.
- If the supplied *symbol* is already defined for another security, that security's value is reset to  *NA*. If the symbol is supplied as a blank or *NA* value, the symbol is deleted from the cross reference and the associated property value is reset to *NA*.
- If multiple *symbols* are supplied for an *entityId/SourceId* combination, only the first occurrence is used. If the same *sourceId/symbol* combination is supplied for more than one *entityId*, only the first occurrence is used.

<span id="related"></span>

## Related Feeds:

- [*SecurityMaster*](pma_SecurityMaster.md): defines Security instances referenced by this feed
- [*IdSourceMaster*](pma_IdSourceMaster.md): defines IdSource instances referenced by this feed
- [*SecurityAliases*](pma_SecurityAliases.md): defines aliases independent of source

## Sample Upload:

The following tab-delimited feed could be used to update security cross references:

       Interface ExternalFeedManager upload: "SecurityXRef" using:
         "entityId      sourceId      symbol
          1             CUSIP         16161010
          2             CUSIP         69846210
          3             TICKERUS      XYZ
         " ;

{% include doc-footer.htm copydates="1998" %}
