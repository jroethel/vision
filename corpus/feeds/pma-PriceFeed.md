---
provenance: "docs/original/pma_PriceFeed.htm"
unit_type: "feed"
title: "Vision Upload Format: PriceFeed"
ingested: "2026-09-22"
entity: "PriceRecord"
fields: [{"name": "entityId", "property": "entity", "type": "String", "desc": "any valid security identifier"}, {"name": "date", "property": "recordDate", "type": "Date", "desc": "date of the pricing data"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of currency in which the prices are provided"}, {"name": "adjustmentDate", "property": "adjustmentDate", "type": "Date", "desc": "date through which prices are adjusted (see notes below)"}, {"name": "ask", "property": "_ask", "type": "Number", "desc": "ask price for date"}, {"name": "bid", "property": "_bid", "type": "Number", "desc": "bid price for date"}, {"name": "close", "property": "recordValue", "type": "Number", "desc": "closing price for date"}, {"name": "high", "property": "_high", "type": "Number", "desc": "high price for date"}, {"name": "low", "property": "_low", "type": "Number", "desc": "low price for date"}, {"name": "open", "property": "_open", "type": "Number", "desc": "open price for date"}, {"name": "volume", "property": "_volume", "type": "Number", "desc": "trading volume for date"}, {"name": "yield", "property": "_yield", "type": "Number", "desc": "yield for date"}, {"name": "dailyReturn", "property": "_dailyReturn", "type": "Number", "desc": "daily return stored as a percent"}, {"name": "unitReturn", "property": "_unitReturn", "type": "Number", "desc": "daily return stored in units form"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *PriceFeed*

**Category:** *EntityExtenderFeed*
