---
provenance: "docs/original/mNA.htm#elseIf:then:"
unit_type: "message"
title: "elseIf:then:"
ingested: "2026-09-22"
class: "NA"
---

<span id="elseIf:then:"></span>**elseIf:then:**

> **Synopsis:**
>
> > Undefined elseIf: condition then: object
>
> **Description:**
>
> > When sent to NA, evaluates supplied object if boolean is TRUE, otherwise  
> > returns ^self. For example:  
> > v isNumber  
> > ifTrue: \[ list at: v asInteger \] .  
> > elseIf: v isString  
> > then: \[ dictionary at: v \] .  
> > elseIf: list isList  
> > then: \[ list at: 1 \] .  
> > else: \[ "Unknown object type" \]  
>
> **Type:** Method          **Returns:** [Object](../../classes/clObject.md)
>
> **Also Defined At:**  
> \| [Object](../mObject/elseIf-then.md) \|

<img src="instdot.gif" data-align="middle" alt="o " />
