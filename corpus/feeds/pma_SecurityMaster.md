---
provenance: "docs/original/pma_SecurityMaster.htm"
unit_type: "feed"
title: "Vision Upload Format: securityMaster"
ingested: "2026-09-22"
entity: "Vision"
fields: [{"name": "entityId", "property": "code", "type": "String", "desc": "id of new or existing Security instance"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of existing [Currency](pma_CurrencyMaster.md) instance", "ref": "pma_CurrencyMaster"}, {"name": "companyId", "property": "company", "type": "String", "desc": "id of underlying Company instance which issued this security"}, {"name": "cusip", "property": "cusip", "type": "String", "desc": "8 or 9 character Cusip"}, {"name": "name", "property": "name", "type": "String", "desc": "security name"}, {"name": "sedol", "property": "sedol", "type": "String", "desc": "6 or 7 character Sedol"}, {"name": "ticker", "property": "ticker", "type": "String", "desc": "Ticker symbol"}, {"name": "type", "property": "type", "type": "String", "desc": "id of existing [SecurityType](pma_SecurityTypeMaster.md) instance", "ref": "pma_SecurityTypeMaster"}, {"name": "isin", "property": "isin", "type": "String", "desc": "isin id"}, {"name": "latestMarket CapUS", "property": "latestMarket CapUS", "type": "Number", "desc": "latest mcap available (in US$)"}, {"name": "sharesOut", "property": "_sharesOut", "type": "Number", "desc": "latest shares outstanding"}, {"name": "shortName", "property": "shortName", "type": "String", "desc": "short name"}, {"name": "sortCode", "property": "sortCode", "type": "String", "desc": "sort code"}, {"name": "valor", "property": "valor", "type": "String", "desc": "valor id"}, {"name": "terminateFlag", "property": "deletionDate", "type": "Date", "desc": "date the security became inactive"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *SecurityMaster*

**Category:** *MasterFeed*
