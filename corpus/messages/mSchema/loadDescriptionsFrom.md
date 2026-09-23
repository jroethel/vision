---
provenance: "docs/original/mSchema.htm#loadDescriptionsFrom:"
unit_type: "message"
title: "loadDescriptionsFrom:"
ingested: "2026-09-22"
class: "Schema"
---

<span id="loadDescriptionsFrom:"></span>**loadDescriptionsFrom:**

> **Synopsis:**
>
> > Schema MessageImplementationDescriptor loadDescriptionsFrom: file
>
> **Description:**
>
> > Loads descriptive information from a tab-delimited file containing the following fields: class, message, keyType, returns, container, tvFlag, description, parameter1, ..., parameterN. The information is updated for the MessageImplementationDescriptor associated with the supplied class/message. The 'keyType' can be Full, Partial, or blank. The 'returns' field contains the class of the object returned by the message. The 'container' field contains Object, List, IndexedList, or TimeSeries, and indicates the form in which the result is returned. If the field is blank, the default is that values are returned as a scalar Object. If a collection of objects is returned, you should set the return field to one of the collection classes. The 'tvFlag' field can be used to indicate that a method is time varying. If this field is blank or the message type is not a method, this flag is derived from the database. The 'description' field sets the description for the message. The parameter fields can be used to indicate the types of inputs for binary and keyword messages (one field per keyword) and can also be used to indicate the index type for objects that return an IndexedList container.
>
> **Type:** Method          **Returns:** NoValue
>
> **Parameters:**
>
> > 1 - String  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
