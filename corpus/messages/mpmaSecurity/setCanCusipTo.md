---
provenance: "docs/original/mpmaSecurity.htm#setCanCusipTo:"
unit_type: "message"
title: "setCanCusipTo:"
ingested: "2026-09-22"
class: "pmaSecurity"
---

<span id="setCanCusipTo:"></span>**setCanCusipTo:**

> **Synopsis:**
>
> > Security setCanCusipTo: string
>
> **Description:**
>
> > Sets the recipient's 'canCusip' to supplied string. If the current 'code' is the same as the old 'canCusip', it is reset to the supplied string as well. The string is added as an alias to the Named Security and Named Company dictionaries (with a prepended 'c') and to the XRef CanCusip (as an 8 and 9 character id).
>
> **Type:** Method          **Function:** Update          **Level:** DBA
>
> **Returns:** [Security](clpmaSecurity.htm)
>
> **Parameters:**
>
> > 1 - String  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
