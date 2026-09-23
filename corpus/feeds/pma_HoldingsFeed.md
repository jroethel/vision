---
provenance: "docs/original/pma_HoldingsFeed.htm"
unit_type: "feed"
title: "Vision Upload Format: HoldingsFeed "
ingested: "2026-09-22"
entity: "Holding"
fields: [{"name": "acctId", "property": "account", "type": "String", "desc": "id of existing Portfolio or IndexAccount instance"}, {"name": "secId", "property": "security", "type": "String", "desc": "id of existing [Security](pma_SecurityMaster.md) instance", "ref": "pma_SecurityMaster"}, {"name": "date", "property": "date", "type": "Date", "desc": "date of the Holding"}, {"name": "mval", "property": "_totalMarketValue", "type": "Number", "desc": "market value of security held in account on date"}, {"name": "shares", "property": "_shares", "type": "Number", "desc": "shares (or units of security) held in account on date"}, {"name": "price", "property": "_accountingPrice", "type": "Number", "desc": "price used to compute market value of security"}, {"name": "totalCost", "property": "_totalCost", "type": "Number", "desc": "total cost of holding"}, {"name": "unitCost", "property": "_totalCost", "type": "Number", "desc": "unit cost of holdings"}, {"name": "adjustDate", "property": "_adjustmentDate", "type": "Date", "desc": "date holding is adjusted through"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "currency of the holding"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *HoldingsFeed*

**Category:** *TransactionFeed*
