---
provenance: "docs/original/mSchema.htm#initializeDefaultInstance"
unit_type: "message"
title: "initializeDefaultInstance"
ingested: "2026-09-22"
class: "Schema"
---

<span id="initializeDefaultInstance"></span>**initializeDefaultInstance**

> **Synopsis:**
>
> > Schema ClassDescriptor initializeDefaultInstance
>
> **Description:**
>
> > This method is run as part of the 'initializeLocalAttributes' step of new class descriptor creation. If the class has a naming dictionary, it adds a reference to the newly created Class as "Default". If the new class shares the parent's naming dictionary, the name added to the dictionary concatenates the class name to the string "Default".
>
> **Type:** Method          **Returns:** Schema ClassDescriptor

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
