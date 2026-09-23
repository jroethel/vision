---
provenance: "docs/original/mpmaLinkRecord.htm#initializeCashFrom:"
unit_type: "message"
title: "initializeCashFrom:"
ingested: "2026-09-22"
class: "pmaLinkRecord"
---

<span id="initializeCashFrom:"></span>**initializeCashFrom:**

> **Synopsis:**
>
> > Holding initializeCashFrom: list
>
> **Description:**
>
> > Updates the '\_totalMarketValue', '\_shares', and '\_totalCost' properties in recipients using the total 'totalMarketValue' of the supplied list if non-NA, otherwise using the total 'shares' of the supplied list if non-NA, otherwise using the total 'totalCost' of the supplied list. The recipient is assumed to be a holding in a cash security and the supplied is list is assumed to respond to the 'totalMarketValue', 'shares', and 'totalCost' messages.
>
> **Type:** Method          **Function:** Update          **Level:** DBA
>
> **Returns:** [Holding](../../classes/clpmaAccount.md)
>
> **Parameters:**
>
> > 1 - List  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
