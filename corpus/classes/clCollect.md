---
provenance: "docs/original/clCollect.htm#overview"
unit_type: "class"
title: "Vision Class: Collection"
ingested: "2026-09-22"
---

## Overview

The **Collection** class is an abstract class that is used to organize classes in the hierarchy whose instances represent sets of objects. The major subclasses of *Collection* are: [*List*](clList.md), [*IndexedList*](clIList.md), and [*TimeSeries*](clTS.md).

Instances of the class **List** represent collections of objects that are accessed either by position or as a set. Instances of the class **IndexedList** represent collections of objects that are accessed by a user-defined index or as a set. Instances of the class **TimeSeries** represent collections of objects that are accessed by date or as a set. The elements in a collection do not need to be from the same class.

The *Collection* class is an indirect subclass of Object:

      Object
         |
         Function
            |
            EnumeratedFunction
               |
               Collection
                  |
                  IndexedCollection
                  |   |-- IndexedList
                  |   |-- TimeSeries
                  |
                  SequencedCollection
                      |-- List

The *Collecton* classes have been optimized to organize and query large sets of data. A large number of the messages defined for these classes have been written in Vision and can therefore be modified and expanded as needed. As always, you can define any number of new messages for these classes.

------------------------------------------------------------------------
