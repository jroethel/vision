---
provenance: "docs/original/mTS.htm#asOf:assign:"
unit_type: "message"
title: "asOf:assign:"
ingested: "2026-09-22"
class: "TS"
---

<span id="asOf:assign:"></span>**asOf:assign:**

> **Synopsis:**
>
> > TimeSeries asOf: aDate assign: aValue
>
> **Description:**
>
> > Assigns supplied value into the time series as of the supplied date. This operation does NOT create new points in the time series; it updates the first date on or before the supplied date that already exists in the time series. Message only works with true time series, not methods (i.e., if formula is a method defined to compute a ratio of two numbers, the message can not be used to change the value of formula).
>
> **Type:** Method          **Returns:** [TimeSeries](../../classes/clTS.md)
>
> **Parameters:**
>
> > 1 - Date  
> > 2 - Object  

<img src="instdot.gif" data-align="middle" alt="o " />
