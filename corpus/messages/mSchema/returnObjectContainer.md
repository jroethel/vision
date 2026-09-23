---
provenance: "docs/original/mSchema.htm#returnObjectContainer"
unit_type: "message"
title: "returnObjectContainer"
ingested: "2026-09-22"
class: "Schema"
---

<span id="returnObjectContainer"></span>**returnObjectContainer**

> **Synopsis:**
>
> > Schema MessageImplementationDescriptor returnObjectContainer
>
> **Description:**
>
> > This property contains the class descriptor for the type of container returned by this message. Objects can be returned as a single scalar value, in which case the return object container is Object. Some messages return collections of values, in which case the return object container will be List, IndexedList, or TimeSeries. A message that returns a TimeSeries should not be confused with a time series property or a method that varies over time. Time varying messages will produce different results if they are evaluated as of different dates but do not actually return a TimeSeries object. A message that returns a TimeSeries container is actually returning a TimeSeries object which responds to all the TimeSeries messages.
>
> **Type:** FixedProperty          **Returns:** Schema ClassDescriptor

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
