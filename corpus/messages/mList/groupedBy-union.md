---
provenance: "docs/original/mList.htm#groupedBy:union:"
unit_type: "message"
title: "groupedBy:union:"
ingested: "2026-09-22"
class: "List"
---

<span id="groupedBy:union:"></span>**groupedBy:union:**

> **Synopsis:**
>
> > Collection groupedBy: block union: list
>
> **Description:**
>
> > Groups the recipient collection based on the criteria specified by supplied blocks. The resultant list contains one element for each value that is included in supplied list OR that results from applying the supplied block to the recipient collection. For example, companyList groupedBy: \[ country \] union: Country masterList will return a list with one entry for each Country including countries not represented in 'companyList' (where groupList count will be 0.
>
> **Type:** Method          **Returns:** [Collection](../../classes/clCollect.md)
>
> **Parameters:**
>
> > 1 - List  

<img src="instdot.gif" data-align="middle" alt="o " />
