---
provenance: "docs/original/mpmaSecurity.htm#adjustmentFactor"
unit_type: "message"
title: "adjustmentFactor"
ingested: "2026-09-22"
class: "pmaSecurity"
---

<span id="adjustmentFactor"></span>**adjustmentFactor**

> **Synopsis:**
>
> > Security adjustmentFactor
>
> **Description:**
>
> > Cumulative adjustment factor. This property has an initial value of 1.0. Each time a split occurs, a new point representing the product of the new raw factor and the last adjustment factor is stored in this property as of the ex-date. To properly use the adjustment factor, you access values as of the two dates involved, the adjustment date and the current date. The ratio of these factors gives you the correct adjustment.
>
> **Type:** TimeSeriesProperty          **Function:** Data          **Level:** Basic
>
> **Returns:** [Number](../../classes/clNumber.md)

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
