---
provenance: "docs/original/pma_DivFeed.htm"
unit_type: "feed"
title: "Vision Upload Format: DivFeed"
ingested: "2026-09-22"
entity: "DivRecord"
fields: [{"name": "entityId", "property": "entity", "type": "String", "desc": "any valid security identifier"}, {"name": "date", "property": "date", "type": "Date", "desc": "ex-date of dividend data"}, {"name": "currencyId", "property": "baseCurrency", "type": "String", "desc": "id of currency in which dividends are provided"}, {"name": "adjustmentDate", "property": "adjustmentDate", "type": "Date", "desc": "date through which dividend is adjusted"}, {"name": "recordValue", "property": "recordValue", "type": "Number", "desc": "total cash dividends on ex-date"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *DivFeed*

**Category:** *EntityExtenderFeed*

## Summary:

- The *DivFeed* feed is used to create and update **DivRecord** instances for securities. This feed can include data for any number of securities for any number of dates. This class is used to track cash dividends paid by a security over time. The **DivRecord** class is described in detail in the [*Portfolio Management Application Issues*](pmaIssues.htm#prices) document.

## Available Fields:

| Field | DivRecord Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| entityId | entity | String | any valid security identifier |
| date | date | Date | ex-date of dividend data |
| currencyId | baseCurrency | String | id of currency in which dividends are provided |
| --- Suggested Fields --- |  |  |  |
| adjustmentDate | adjustmentDate | Date | date through which dividend is adjusted |
| recordValue | recordValue | Number | total cash dividends on ex-date |

## Special Processing Rules:

- The *entityId* must correspond to an existing **Security** instance. Any valid security alias can be used to identify the security.

- The *date* must be included and indicates the ex-date of the dividend. It can be in any valid date format such as *19971215* or *12/15/97*.

- The *currencyId* is used to identify the currency in which the dividend is supplied. This currency can be different from the security's base currency. By default, the dividend information is automatically converted into its security's base currency when it is accessed (in cases where the currencies are different). If the supplied *currencyId* does not map to an existing currency instance, the dividend record's *baseCurrency* is set to the default currency.

- The *adjustmentDate* is used to identify the date through which the data in the feed instance has been adjusted for splits. Normally, this date is the same as the record's date and this field need not be provided. When loading dividend history and/or corrections, the values may be supplied unadjusted (i.e., the values that existed on the ex-date) or adjusted (i.e., the values adjusted for any splits that have occurred since the ex-date. If the data is unadjusted, the *adjustmentDate* field is not needed or can contain the same value as the *date* field. If the data has been adjusted to reflect splits that have occurred since the record date, this field should indicate the date through which splits have been applied.

  Note that you do not need to resend data that has changed as the result of a split adjustment. Only true data corrections need to be supplied using this feed.

- The *recordValue* field should contain the total cash dividends paid by that security on that date.

<span id="related"></span>

## Related Feeds:

- [*SecurityMaster*](pma_%0ASecurityMaster.htm): defines Security instances referenced by this feed
- [*SecurityAliases*](pma_SecurityAliases.md): loads cusip/sedol changes and adds other aliases that can serve as the *entityId* for a security.

## Sample Upload:

The following tab-delimited feed could be used to create **DividendRecord** instances:

         Interface ExternalFeedManager upload: "DivFeed" using:
         "entityId     date          currencyId     recordValue
          45920010     05/07/1997    USD             0.20 
          45920010     08/07/1997    USD             0.20
          45920010     11/06/1997    USD             0.20
          37044210     05/13/1997    USD             0.50
          37044210     08/12/1997    USD             0.50
          37044210     11/10/1997    USD             0.50
         " ;

{% include doc-footer.htm copydates="2000" %}
