---
provenance: "docs/original/mString.htm#asCSVRecords"
unit_type: "message"
title: "asCSVRecords"
ingested: "2026-09-22"
class: "String"
---

<span id="asCSVRecords"></span>**asCSVRecords**

> **Synopsis:**
>
> > String asCSVRecords
>
> **Description:**
>
> > Converts a comma-separated-value format file to a list of strings,  
> > with each element responding to the message 'fields', which returns  
> > a list of the comma-separted values. Embedded commas in the original  
> > file are preserved. For example, if the file 'sample.dat' contains:  
> > key1, description1, value1  
> > key2, "description 2 with , character", value2  
> > then:  
> > "sample.dat" asCSVRecords  
> > do: \[ "Field 1: " print ; fields at: 1 . printNL ;  
> > "Field 2: " print ; fields at: 2 . printNL ;  
> > "Field 3: " print ; fields at: 3 . printNL ;  
> > \] ;  
> >   
> > displays:  
> >   
> > Field 1: key1  
> > Field 2: description1  
> > Field 3: value1  
> > Field 1: key2  
> > Field 2: description 2 with , character  
> > Field 3: value2  
>
> **Type:** Method          **Returns:** [List](../../classes/clList.md)

<img src="instdot.gif" data-align="middle" alt="o " />
