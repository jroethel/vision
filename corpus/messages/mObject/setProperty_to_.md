---
provenance: "docs/original/mObject.htm#setProperty:to:"
unit_type: "message"
title: "setProperty:to:"
ingested: "2026-09-22"
class: "Object"
---

<span id="setProperty:to:"></span>**setProperty:to:**

> **Synopsis:**
>
> > Object setProperty: p to: object
>
> **Description:**
>
> > This message is used to update a property in the recipient with the  
> > supplied object. The supplied property 'p' can be a string or a  
> > block containing the intensional form of the property to update.  
> > The block form is more efficient especially if this message is invoked  
> > from within a Collection operation. If 'p' refers to a fixed property,  
> > its value is set to the supplied object. If 'p' refers to a time series  
> > property, the property is updated as of the current evaluation date  
> > (i.e., ^date). This message returns the recipient object so you can  
> > stream multiple set messages to the same object. For example:  
> >   
> > object  
> > setProperty: \[ :property1 \] to: object1 .  
> > setProperty: \[ :property2 \] to: object2 .  
> > ;
>
> **Type:** Method          **Returns:** [Object](../../classes/clObject.md)
>
> **Parameters:**
>
> > 1 - Block  
> > 2 - Object  

<img src="instdot.gif" data-align="middle" alt="o " />
