---
provenance: "docs/original/mDate.htm#convertFrom:"
unit_type: "message"
title: "convertFrom:"
ingested: "2026-09-22"
class: "Date"
---

<span id="convertFrom:"></span>**convertFrom:**

> **Synopsis:**
>
> > Date convertFrom: string
>
> **Description:**
>
> > This message converts the supplied string to an instance of the recipient's class if applicable, returning NA otherwise. The definition at Object will lookup the string in the class' naming dictionary, if defined. The version at String returns the recipient stripped of any extensions. The versions at Number, Integer, Double, and Float convert the recipient to a numeric value if possible. The version at Date converts the recipient to a Date using the 'asDate' message defined at String. The version at Boolean returns TRUE if the recipient contains an upper/lower case combination of 'true' and FALSE if the recipient contains an upper/lower case combination of 'false'. The version at block returns a block containing the string as a message. This message is called by the 'as:' message at String.
>
> **Type:** Method          **Returns:** [Object](../../classes/clObject.md)
>
> **Also Defined At:**  
> \| [Block](../mBlock/convertFrom_.md) \| [Boolean](../mBoolean/convertFrom_.md) \| [Number](../mNumber/convertFrom_.md) \| [Object](../mObject/convertFrom_.md) \| [String](../mString/convertFrom_.md) \| [Undefined](../mNA/convertFrom_.md) \|

<img src="instdot.gif" data-align="middle" alt="o " />
