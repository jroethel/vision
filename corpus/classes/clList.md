---
provenance: "docs/original/clList.htm#overview"
unit_type: "class"
title: "Vision Class: List"
ingested: "2026-09-22"
---

## Overview

The **List** class is an indirect subclass of the *Collection* class which is also a superclass of the [*IndexedList*](clIList.md) and [*TimeSeries*](clTS.md) classes. Instances of the class *List* consist of a collection of objects that are accessed either by position or as a set. A *List* is updated by appending objects to its end.

The *List* class has been optimized to organize and query large sets of data. A large number of the messages defined for this class have been written in Vision and can therefore be modified and expanded as needed. As always, you can define any number of new messages for the class.

The *List* class is a direct subclass of *SequencedCollection*:

      Object
         |
         Function
            |
            EnumeratedFunction
               |
               Collection
                  |
                  SequencedCollection
                     |
                     |-- List

------------------------------------------------------------------------
