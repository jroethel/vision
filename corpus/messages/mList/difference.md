---
provenance: "docs/original/mList.htm#difference:"
unit_type: "message"
title: "difference:"
ingested: "2026-09-22"
class: "List"
---

<span id="difference:"></span>**difference:**

> **Synopsis:**
>
> > Collection difference: aList
>
> **Description:**
>
> > This message returns a list of two elements: the first element contains  
> > the list of elements that are in list 1 and not in list 2; the second  
> > element contains the list of elements that are in list 2 and not list 1.  
> > For example:  
> >   
> > !diffs \<- (1,2,3,4,5) difference: (3,4,5,6) ;  
> > "In 1 not 2" print ; diffs at: 1 . do: \[ print \] ; newLine print;  
> > "In 2 not 2" print ; diffs at: 2 . do: \[ print \] ;  
>
> **Type:** Method          **Returns:** [List](../../classes/clList.md)
>
> **Parameters:**
>
> > 1 - List  

<img src="instdot.gif" data-align="middle" alt="o " />
