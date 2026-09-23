---
provenance: "docs/original/mpmaAccount.htm#createWeightedHoldingsAsOf:using:"
unit_type: "message"
title: "createWeightedHoldingsAsOf:using:"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="createWeightedHoldingsAsOf:using:"></span>**createWeightedHoldingsAsOf:using:**

> **Synopsis:**
>
> > IndexAccount createWeightedHoldingsAsOf: date using: acct
>
> **Description:**
>
> > Creates holdings extended by various statistics for recipient as of supplied date using securities in 'memberList' as of that date. This method assumes that you own the same number of shares that the supplied account has. The extension includes the property 'mvalEvenDollar' which is set to 1000, 'mvalMCapWeighted' which is set to the security's price (in recipient's base currency) \* the security's 'sharesOut' value, and 'mvalMVWeighted' which is set to the security's price \* the shares held in supplied account. The extension propeties 'pctEvenDollar', 'pctMCapWeighted', and 'pctMValWeighted' are computed relative to this list of holdings.
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
