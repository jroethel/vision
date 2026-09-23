---
provenance: "docs/original/mSchema.htm#createNamingDictionaryAt:"
unit_type: "message"
title: "createNamingDictionaryAt:"
ingested: "2026-09-22"
class: "Schema"
---

<span id="createNamingDictionaryAt:"></span>**createNamingDictionaryAt:**

> **Synopsis:**
>
> > Schema ClassDescriptor createNamingDictionaryAt: dictionary
>
> **Description:**
>
> > This method is used to create a naming dictionary for the class if one  
> > does not already exist. The parameter should itself be a dictionary  
> > that is used to name references to other dictionaries (e.g., Named).  
> > This method creates a new instance of this dictionary, assigns it to  
> > the 'namingDictionary' property at the class descriptor, and defines  
> > the class descriptor's code at the supplied dictionary to return this  
> > new dictionary. Current instances in the class are then added to  
> > the dictionary. For example, to create a dictionary for MyClass at Named  
> > use:  
> >   
> > MyClass classDescriptor createNamingDictionaryAt: Named ;  
> >   
> > If MyClass had an instance with code "my1", the expression:  
> >   
> > Named MyClass my1  
> >   
> > would access this instance. All new instances would automatically get  
> > cross-referenced in this naming dictionary.
>
> **Type:** Method          **Returns:** Schema ClassDescriptor
>
> **Parameters:**
>
> > 1 - Dictionary  

<img src="instdot.gif" data-align="middle" data-border="0" alt="o " />
