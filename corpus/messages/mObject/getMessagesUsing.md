---
provenance: "docs/original/mObject.htm#getMessagesUsing:"
unit_type: "message"
title: "getMessagesUsing:"
ingested: "2026-09-22"
class: "Object"
---

<span id="getMessagesUsing:"></span>**getMessagesUsing:**

> **Synopsis:**
>
> > Object getMessagesUsing: aString
>
> **Description:**
>
> > This method returns a list of message implementation descriptors whose method definitions contain the supplied string. All messages defined in the recipient's inheritance path are considered (i.e., super classes and subclasses). The returned list is sorted by message, then class descriptor within message. The parameter can utilize the standard Unix regular expression syntax for partial matches.
>
> **Type:** Method          **Returns:** [List](../../classes/clList.md)
>
> **Parameters:**
>
> > 1 - String  

<img src="instdot.gif" data-align="middle" alt="o " />
