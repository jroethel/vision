---
provenance: "docs/original/mpmaAccount.htm#createEvenShareHoldingsAsOf:"
unit_type: "message"
title: "createEvenShareHoldingsAsOf:"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="createEvenShareHoldingsAsOf:"></span>**createEvenShareHoldingsAsOf:**

> **Synopsis:**
>
> > IndexAccount createEvenShareHoldingsAsOf: date
>
> **Description:**
>
> > Creates even share holdings for recipient as of supplied date using securities in 'memberList' as of that date. This method assumes that 1,000 shares of each security is held. The '\_shares' of each holding are set to 1000.00 and the '\_totalMarketValue' is computed as 'price \* shares' using the security's price. Account totals are computed and 'percentOfPort' is updated for each holding.
>
> **Type:** Method          **Function:** Update          **Level:** Advanced
>
> **Returns:** NoValue
>
> **Parameters:**
>
> > 1 - Date  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
