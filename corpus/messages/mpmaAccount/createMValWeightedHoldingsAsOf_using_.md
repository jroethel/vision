---
provenance: "docs/original/mpmaAccount.htm#createMValWeightedHoldingsAsOf:using:"
unit_type: "message"
title: "createMValWeightedHoldingsAsOf:using:"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="createMValWeightedHoldingsAsOf:using:"></span>**createMValWeightedHoldingsAsOf:using:**

> **Synopsis:**
>
> > IndexAccount createMValWeightedHoldingsAsOf: date using: acct
>
> **Description:**
>
> > Creates holdings for recipient as of supplied date using securities in 'memberList' as of that date based on the market value of the security in the supplied Account. This method assumes that you own the same number of shares that the supplied account has. If the supplied account does not own the security, the shares value in the recipient's holding will be 0. The '\_totalMarketValue' is computed as 'price \* shares' using the security's price. Account totals are computed and 'percentOfPort' is updated for each holding.
>
> **Type:** Method          **Function:** Update          **Level:** Advanced
>
> **Returns:** NoValue
>
> **Parameters:**
>
> > 1 - Date  
> > 2 - Account  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
