---
provenance: "docs/original/pma_AnalystEst.htm"
unit_type: "feed"
title: "Vision Upload Format: AnalystEst "
ingested: "2026-09-22"
entity: "AnalystEstimate"
fields: [{"name": "entityId", "property": "entity", "type": "String", "desc": "any valid company identifier"}, {"name": "date", "property": "date", "type": "Date", "desc": "date of data"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of currency for monetary data values"}, {"name": "adjustmentDate", "property": "adjsutmentDate", "type": "Date", "desc": "date through which data values are adjusted"}, {"name": "nextQuarterEnd", "property": "nextQuarterEnd", "type": "Date", "desc": "next fiscal quarter end date"}, {"name": "nextYearEnd", "property": "nextYearEnd", "type": "Date", "desc": "next fiscal year end date"}, {"name": "q1Est", "property": "_q1Est", "type": "Number", "desc": "estimate for next fiscal quarter"}, {"name": "q2Est", "property": "_q2Est", "type": "Number", "desc": "estimate for following fiscal quarter"}, {"name": "q3Est", "property": "_q3Est", "type": "Number", "desc": "estimate for following fiscal quarter"}, {"name": "q4Est", "property": "_q4Est", "type": "Number", "desc": "estimate for following fiscal quarter"}, {"name": "y1Est", "property": "_y1Est", "type": "Number", "desc": "estimate for next fiscal year end"}, {"name": "y2Est", "property": "_y2Est", "type": "Number", "desc": "estimate for following fiscal year end"}, {"name": "y3Est", "property": "_y3Est", "type": "Number", "desc": "estimate for following fiscal year end"}, {"name": "analyst", "property": "analyst", "type": "Number", "desc": "id of existing [Analyst](pma_AnalystMaster.md) instance", "ref": "pma_AnalystMaster"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *AnalystEst*

**Category:** *EntityExtenderFeed*
