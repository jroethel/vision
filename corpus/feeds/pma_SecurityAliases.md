---
provenance: "docs/original/pma_SecurityAliases.htm"
unit_type: "feed"
title: "Vision Upload Format: SecurityAliases "
ingested: "2026-09-22"
entity: "SecurityAliases"
fields: [{"name": "alias1", "property": "", "type": "String", "desc": "any valid security identifier"}, {"name": "alias2", "property": "", "type": "String", "desc": "alias to add to security"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *SecurityAliases*

**Category:** *AliasFeed*

## Summary:

- The *SecurityAliases* feed is used to load cusip/sedol changes for a security as well as any other desired aliases. Alias management is described in detail in the [*Portfolio Management Application Issues*](pmaIssues.htm#ids) document.

## Available Fields:

|          Field          |  Type  |          Description          |
|:-----------------------:|:------:|:-----------------------------:|
| --- Required Fields --- |        |                               |
|         alias1          | String | any valid security identifier |
|         alias2          | String |   alias to add to security    |

## Special Processing Rules:

- The first alias that matches an existing security is used to identify the security. All other values supplied as tab-delimited fields on the same record are added as aliases to this security.
- If none of the identifiers provided in the record match an existing security, an error is noted in the exception report and no aliases are posted.

<span id="related"></span>

## Related Feeds:

- [*SecurityMaster*](pma_SecurityMaster.md): defines Security instances referenced by this feed

## Sample Upload:

The following tab-delimited feed could be used to update security aliases. The first field should contain the id of an existing security; you can follow this with one or more ids to add as aliases for the security. The header line should be included, but the header values are ignored:

       Interface ExternalFeedManager upload: "SecurityAliases" using:
         "oldId         newId
          16161010      16161A10
          69792610      69846210
          54567410      54570010
          61844710      61844A10
         " ;

{% include doc-footer.htm copydates="1999" %}
