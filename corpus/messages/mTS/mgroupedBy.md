---
provenance: "docs/original/mTS.htm#mgroupedBy:"
unit_type: "message"
title: "mgroupedBy:"
ingested: "2026-09-22"
class: "TS"
---

<span id="mgroupedBy:"></span>**mgroupedBy:**

> **Synopsis:**
>
> > Collection mgroupedBy: aBlock
>
> **Description:**
>
> > Groups the recipient list using result of block, where supplied block should  
> > generate a list as its result. Elements in the original list will be  
> > included in one or more groupLists. For example, if instances of the class  
> > EntityCategory respond to the message 'entities' with the list of entities  
> > included in the instance, then the expression:  
> >   
> > EntityCategory masterList mgroupedBy: \[ entities \]  
> >   
> > returns a list of the entities included in any EntityCategory where each  
> > element of this new list responds to the 'groupList' message with the  
> > list of EntityCategories that include the element.
>
> **Type:** Method          **Returns:** [List](../../classes/clList.md)
>
> **Parameters:**
>
> > 1 - Block  

<img src="instdot.gif" data-align="middle" alt="o " />
