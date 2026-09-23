---
provenance: "docs/original/mTS.htm#<-"
unit_type: "message"
title: "<-"
ingested: "2026-09-22"
class: "TS"
---

<span id="<-"></span>**\<-**

> **Synopsis:**
>
> > TimeSeries \<- anObject
>
> **Description:**
>
> > Assigns the value provided as of the default date into the recipient. This operations does NOT create new points in the time series; it updates the point on or before the default date. If there is no point on or before the default, the value is stored at the date 1/1/1. \<- only works with true time series, not methods (i.e., if formula is a method defined to compute a ratio of two numbers, the \<- message can not be used to change the value of formula).
>
> **Type:** Method          **Returns:** [TimeSeries](../../classes/clTS.md)
>
> **Parameters:**
>
> > 1 - Object  

<img src="instdot.gif" data-align="middle" alt="o " />
