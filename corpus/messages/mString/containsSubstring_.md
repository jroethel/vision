---
provenance: "docs/original/mString.htm#containsSubstring:"
unit_type: "message"
title: "containsSubstring:"
ingested: "2026-09-22"
class: "String"
---

<span id="containsSubstring:"></span>**containsSubstring:**

> **Synopsis:**
>
> > String containsSubstring: substring
>
> **Description:**
>
> > This message returns TRUE if substring is found in the recipient. Unlike  
> > the 'contains:' message, this form matches each character literally, so  
> > no wildcard characters are recognized. For example,  
> >   
> > "abc" contains: "^a"  
> >   
> > returns TRUE, but  
> >   
> > "abc" containsSubstring: "^a"  
> >   
> > returns FALSE.
>
> **Type:** Method          **Returns:** [Boolean](../../classes/clBoolean.md)
>
> **Parameters:**
>
> > 1 - String  

<img src="instdot.gif" data-align="middle" alt="o " />
