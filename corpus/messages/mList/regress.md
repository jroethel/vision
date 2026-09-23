---
provenance: "docs/original/mList.htm#regress:"
unit_type: "message"
title: "regress:"
ingested: "2026-09-22"
class: "List"
---

<span id="regress:"></span>**regress:**

> **Synopsis:**
>
> > Collection regress: list2
>
> **Description:**
>
> > Performs a standard linear regression between the recipient collection  
> > (the dependent variable) and the supplied parameter (the independent  
> > variable). The returned object responds to the messages 'beta', 'alpha',  
> > 'pearson', 'rsq', and 'stdErr'. If either collection contains non-numeric  
> > values or the two collections are not the same size, the returned values will  
> > be NA. For example:  
> >   
> > (2,3,9,1,8,7,5) regress: (6,5,11,7,5,4,4) .  
> > do: \[ beta print ; alpha print ;  
> > pearson print ; rsq print ; stdErr printNL ;  
> > \] ;  
> >   
> > runs the regression and displays the results of the various computations.
>
> **Type:** Method          **Returns:** [Object](../../classes/clObject.md)
>
> **Parameters:**
>
> > 1 - Collection  

<img src="instdot.gif" data-align="middle" alt="o " />
