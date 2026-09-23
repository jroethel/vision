---
provenance: "docs/original/mpmaSecurity.htm#setCompanyTo:"
unit_type: "message"
title: "setCompanyTo:"
ingested: "2026-09-22"
class: "pmaSecurity"
---

<span id="setCompanyTo:"></span>**setCompanyTo:**

> **Synopsis:**
>
> > Security setCompanyTo: comp
>
> **Description:**
>
> > Set company for recipient. Note that security/company pairs that are created together with 'createAndLink:' will have identical 'code' value and should not be reset because you will lose aliases at the company. The recipient's aliases that are associated with the original company are deleted from this company and added to the supplied company. If the supplied company does not refer to a primary security, its 'primarySecurity' is set to recipient.
>
> **Type:** Method          **Function:** Update          **Level:** DBA
>
> **Returns:** [Security](clpmaSecurity.htm)
>
> **Parameters:**
>
> > 1 - Company  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
