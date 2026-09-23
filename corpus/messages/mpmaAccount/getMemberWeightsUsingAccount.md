---
provenance: "docs/original/mpmaAccount.htm#getMemberWeightsUsingAccount:"
unit_type: "message"
title: "getMemberWeightsUsingAccount:"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="getMemberWeightsUsingAccount:"></span>**getMemberWeightsUsingAccount:**

> **Synopsis:**
>
> > IndexAccount getMemberWeightsUsingAccount: acct
>
> **Description:**
>
> > Returns list of securities in 'memberList' as of evaluation date extended by the properties 'mvalEvenDollar' which stores the value 1000, 'pctEvenDollar' which stores the percent of index in this security based on even dollar market values, 'mvalMCapWeighted' which stores the security's 'price' \* the security's 'sharesOut' in the recipient's currency, 'pctMCapWeighted' which stores the percent of index in this security based on market cap values, 'mvalMValWeighted' which stores the market value based on the number shares of this security in the supplied account as of the evaluation date, and 'pctMValWeighted' which stores the percent of index in this security based on the supplied accounts' market value.
>
> **Type:** Method (time varying)          **Function:** Data          **Level:** Basic
>
> **Returns:** List of [Security](clpmaSecurity.htm)
>
> **Parameters:**
>
> > 1 - Account  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
