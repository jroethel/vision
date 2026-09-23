---
provenance: "docs/original/mpmaAccount.htm#createEvenDollarHoldingsAsOf:"
unit_type: "message"
title: "createEvenDollarHoldingsAsOf:"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="createEvenDollarHoldingsAsOf:"></span>**createEvenDollarHoldingsAsOf:**

> **Synopsis:**
>
> > IndexAccount createEvenDollarHoldingsAsOf: date
>
> **Description:**
>
> > Creates even dollar holdings for recipient as of supplied date using securities in 'memberList' as of that date. This method assumes that \$1,000 of each security is held. The '\_totalMarketValue' of each holding is therefore \$1,000 and the '\_shares' are set to 1000 / the security's price. Account totals are computed and 'percentOfPort' is updated for each holding.
>
> **Type:** Method          **Function:** Update          **Level:** Advanced
>
> **Returns:** NoValue
>
> **Parameters:**
>
> > 1 - Date  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
