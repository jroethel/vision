---
provenance: "docs/original/mObject.htm#basicSend:"
unit_type: "message"
title: "basicSend:"
ingested: "2026-09-22"
class: "Object"
---

<span id="basicSend:"></span>**basicSend:**

> **Synopsis:**
>
> > Object basicSend: aBlock
>
> **Description:**
>
> > Evaluates all statements inside supplied block in the context of the recipient object. Identical to 'do:' message except 'do:' returns recipient object and 'basicSend:' returns the result of evaluating the block. At Object, the messages 'basicSend:' and 'send:' perform identical functions. By convention, the 'basicSend:' message is not redefined by subclasses.
>
> **Type:** Primitive          **Returns:** [Object](../../classes/clObject.md)
>
> **Parameters:**
>
> > 1 - Block  

<img src="instdot.gif" data-align="middle" alt="o " />
