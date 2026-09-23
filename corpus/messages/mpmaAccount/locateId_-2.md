---
provenance: "docs/original/mpmaAccount.htm#locateId:"
unit_type: "message"
title: "locateId:"
ingested: "2026-09-22"
class: "pmaAccount"
---

<span id="locateId:"></span>**locateId:**

> **Synopsis:**
>
> > Account locateId: id
>
> **Description:**
>
> > Returns the Account object associated with the supplied id. If the message is sent directly to 'Account', the naming dictionary search order starts with Named Account, followed by Named Portfolio, Named AggAccount, Named IndexAccount, and Named CompositeAccount. If the message is set to a subclass of 'Account', just that subclass' naming dictionary is used.
>
> **Type:** Method          **Function:** Access          **Level:** Basic
>
> **Returns:** [Account](../../classes/clpmaAccount.md)
>
> **Parameters:**
>
> > 1 - String  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
