---
provenance: "docs/original/mList.htm#collectListElementsFrom:"
unit_type: "message"
title: "collectListElementsFrom:"
ingested: "2026-09-22"
class: "List"
---

<span id="collectListElementsFrom:"></span>**collectListElementsFrom:**

> **Synopsis:**
>
> > Collection collectListElementsFrom: aBlock
>
> **Description:**
>
> > Evaluates the statements provided in supplied block for each element in the list and produces a new list containing these elements. Used to combine a list of lists. The supplied block must evaluate to a list. For example, the expression: 5 sequence collectListElementsFrom: \[ ^self sequence \] returns the list elements 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5
>
> **Type:** Method          **Returns:** [List](../../classes/clList.md)
>
> **Parameters:**
>
> > 1 - Block  

<img src="instdot.gif" data-align="middle" alt="o " />
