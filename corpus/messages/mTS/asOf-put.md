---
provenance: "docs/original/mTS.htm#asOf:put:"
unit_type: "message"
title: "asOf:put:"
ingested: "2026-09-22"
class: "TS"
---

<span id="asOf:put:"></span>**asOf:put:**

> **Synopsis:**
>
> > TimeSeries asOf: aDate put: anObject
>
> **Description:**
>
> > Assigns supplied value into the time series as of the date supplied. The message creates a new time point in the time series if the date did not exist. Message only works with true time series, not methods (i.e., if formula is a method defined to compute a ratio of two numbers, the message can not be used to change the value of formula).
>
> **Type:** Method          **Returns:** [TimeSeries](../../classes/clTS.md)
>
> **Parameters:**
>
> > 1 - Date  
> > 2 - Object  

<img src="instdot.gif" data-align="middle" alt="o " />
