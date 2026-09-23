---
provenance: "docs/original/mString.htm#as:"
unit_type: "message"
title: "as:"
ingested: "2026-09-22"
class: "String"
---

<span id="as:"></span>**as:**

> **Synopsis:**
>
> > String as: type
>
> **Description:**
>
> > Converts the recipient String to an instance of the class indicated by the parameter, if possible. If the type is a string that is not the default String, the supplied type will be evaluated to determine its class. The implementation of 'convertFrom:' defined for that class will be used to convert the string to the correct class. The version at Object looks the string up in the class' default naming dictionary if it exists. If the recipient String contains the ',' character, this method returns a list of objects of the supplied type. Any String that cannot be converted to the supplied class returns NA.
>
> **Type:** Method          **Returns:** [Object](../../classes/clObject.md)
>
> **Also Defined At:**  
> \| [Undefined](../mNA/as.md) \|

<img src="instdot.gif" data-align="middle" alt="o " />
