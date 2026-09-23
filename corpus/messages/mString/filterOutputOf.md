---
provenance: "docs/original/mString.htm#filterOutputOf:"
unit_type: "message"
title: "filterOutputOf:"
ingested: "2026-09-22"
class: "String"
---

<span id="filterOutputOf:"></span>**filterOutputOf:**

> **Synopsis:**
>
> > String filterOutputOf: aBlock
>
> **Description:**
>
> > Supplies the printed output associated with the execution of the  
> > supplied block as input to the recipient string as a Unix Command.  
> >   
> > For example:  
> >   
> > "format" filterOutputOf: \[ Named Company IBM displayReport \]  
> >   
> > will redirect the report through the format program as standard input  
> > (i.e., format \< report). By default, the results of executing this  
> > expression will be printed on your screen.
>
> **Type:** Primitive          **Returns:** [Object](../../classes/clObject.md)
>
> **Parameters:**
>
> > 1 - Block  

<img src="instdot.gif" data-align="middle" alt="o " />
