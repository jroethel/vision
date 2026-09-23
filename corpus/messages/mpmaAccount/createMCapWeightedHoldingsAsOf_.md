---
provenance: "docs/original/mpmaAccount.htm#createMCapWeightedHoldingsAsOf:"
unit_type: "message"
title: "createMCapWeightedHoldingsAsOf:"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="createMCapWeightedHoldingsAsOf:"></span>**createMCapWeightedHoldingsAsOf:**

> **Synopsis:**
>
> > IndexAccount createMCapWeightedHoldingsAsOf: date
>
> **Description:**
>
> > Creates market-cap-weighted holdings for recipient as of supplied date using securities in 'memberList' as of that date. This method assumes that you hold the total market value of each holding is equal to the security's market capitalization. The '\_shares' are set to this market value / the security's price. Account totals are computed and 'percentOfPort' is updated for each holding. This method assumes that the 'marketCap' method has been defined for security. All market cap values are accessed in the base currency of the recipient.
>
> **Type:** Method          **Function:** Update          **Level:** Advanced
>
> **Returns:** NoValue
>
> **Parameters:**
>
> > 1 - Date  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
