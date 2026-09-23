---
provenance: "docs/original/mCollect.htm#normalize:by:by:"
unit_type: "message"
title: "normalize:by:by:"
ingested: "2026-09-22"
class: "Collect"
---

<span id="normalize:by:by:"></span>**normalize:by:by:**

> **Synopsis:**
>
> > Collection normalize: aBlock by: bBlock by: cBlock
>
> **Description:**
>
> > Groups the recipient by the criteria in bBlock and cBlock and generates a  
> > normalized value for each element relative to its group. The result object  
> > is the original collection extended by the variable 'norm'. For example:  
> > Company masterList  
> > normalize: \[ sales \] by: \[ country \] by: \[ industry \]  
>
> **Type:** Method          **Returns:** [Collection](../../classes/clCollect.md)
>
> **Parameters:**
>
> > 1 - Block  
> > 2 - Block  

<img src="instdot.gif" data-align="middle" alt="o " />
