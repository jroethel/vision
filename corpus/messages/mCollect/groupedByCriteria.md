---
provenance: "docs/original/mCollect.htm#groupedByCriteria:"
unit_type: "message"
title: "groupedByCriteria:"
ingested: "2026-09-22"
class: "Collect"
---

<span id="groupedByCriteria:"></span>**groupedByCriteria:**

> **Synopsis:**
>
> > Collection groupedByCriteria: aBlockList
>
> **Description:**
>
> > Groups the recipient collection based on the criteria specified by supplied list of blocks. The resultant list contains one element for each combination of values present from processing the supplied blocks. Each element in the resultant list responds to the message 'keyList' which is the list of values associated with this group, one per supplied block. Each element in the resultant list responds to the message 'groupList' which returns the list of elements in the specific combination of block values. For example, Company masterList groupedByCriteria: \[ sector \] , \[ country \] returns a list of sector/country pairs. To display the name of each key and the group count, use: Company masterList groupedByCriteria: \[ sector \] , \[ country \] . do: \[ keyList do: \[ name print: 20 \] ; \#-- print keys groupList count printNL ; \#-- print count \] ;
>
> **Type:** Method          **Returns:** [Collection](../../classes/clCollect.md)
>
> **Parameters:**
>
> > 1 - List  

<img src="instdot.gif" data-align="middle" alt="o " />
