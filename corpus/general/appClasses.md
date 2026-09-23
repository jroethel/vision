---
provenance: "docs/original/appClasses.htm#overview"
unit_type: "general"
title: "Vision Design Methodology: Application Classes "
ingested: "2026-09-22"
---

## Overview

A number of **Abstract Classes** have been defined to organize different components of your Vision class hierarchy. Abstract classes are not normally instantiated directly; instead they serve to organize a set of subclasses that share some basic behavior. Built-in abstract classes include **Collection** which is the superclass of **List** and **TimeSeries** and **Ordinal** which is the superclass of **Number**, **Date**, and **String**.

It is useful to have a basic hierarchy for your application classes as well. Several abstract classes have been defined to help organize application classes:

- Entity
- DataRecord
- LinkRecord
- Bridge
- DataFeed
- DBEntity

Most applications will interact with the database via **Entity** instances. The other classes are used to store data or manage navigations from an entity to other parts of the database.

The organization provided by these classes is intended to serve as a guideline that can be applied as appropriate. These classes are all defined in Vision and can therefore be modified and expanded as needed by the database designer.

> 
>
> ------------------------------------------------------------------------
>
> **Note:**
>
> Some of the classes referenced in this document were added to the Vision bootstrap database as part of release 5.9.4. If your installation was bootstrapped prior to this, you may need to define the following:
>
>       Entity createSubclass: "Support" ;
>       Entity createSubclass: "Table" ;
>       Object createSubclass: "Bridge" ;
>       IncorporatorPrototype createSubclass: "DataFeed" ;
>
> ------------------------------------------------------------------------

------------------------------------------------------------------------
