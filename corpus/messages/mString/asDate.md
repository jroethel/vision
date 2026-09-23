---
provenance: "docs/original/mString.htm#asDate"
unit_type: "message"
title: "asDate"
ingested: "2026-09-22"
class: "String"
---

<span id="asDate"></span>**asDate**

> **Synopsis:**
>
> > String asDate
>
> **Description:**
>
> > Converts the recipient String into a Date object. The recipient  
> > can contain a value in one of the following forms:  
> > "yy", "yymm", "yymmdd", "yyyymmdd"  
> > "m/d/y" where m is 1-12; d is 1-31; y is yy or yyyy  
> > "m-d-y" where m is 1-12; d is 1-31; y is yy or yyyy  
> > "+ \# offset", where \# is integer and offset is a DateOffset  
> > "- \# offset", where \# is integer and offset is a DateOffset  
> > "today"  
> > "yesterday"  
> >   
> > The 'offset' formats add/subtract the offset from the current value of '^date'.  
> > For example:  
> > "961231" asDate --\> 12/31/96  
> > "1/3/95" asDate --\> 1/3/95  
> > "+ 3 days" --\> current date + 3 days  
> > "today" --\> today's date  
>
> **Type:** Method          **Returns:** [Date](../../classes/clDate.md)
>
> **Also Defined At:**  
> \| [Date](../mDate/asDate.md) \| [DateOffset](../mOffset/asDate.md) \| [Number](../mNumber/asDate.md) \| [Undefined](../mNA/asDate.md) \|

<img src="instdot.gif" data-align="middle" alt="o " />
