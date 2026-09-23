---
provenance: "docs/original/mpmaAccount.htm#buildHoldings"
unit_type: "message"
title: "buildHoldings"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="buildHoldings"></span>**buildHoldings**

> **Synopsis:**
>
> > CompositeAccount buildHoldings
>
> **Description:**
>
> > Creates holdings from the holdings associated with the accounts in recipient's 'componentList' as of the evalution date. The shares and market values are computed using the weight stored for the component. For example, if Account XYZ is a component with a weight of 50, 50% of each holding in Account XYZ will be included in the rcipient. Note that the weights are used to determine the number of shares and market value for each holding and need not add up to 100.
>
> **Type:** Method (time varying)          **Function:** Update          **Level:** DBA
>
> **Returns:** NoValue

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
