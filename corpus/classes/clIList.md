---
provenance: "docs/original/clIList.htm#overview"
unit_type: "class"
title: "Vision Class: IndexedList"
ingested: "2026-09-22"
---

## Overview

The **IndexedList** class is an indirect subclass of the *Collection* class which is also a superclass of the classes [*List*](clList.md) and [*TimeSeries*](clTS.md). Instances of the class *IndexedList* consist of a collection of objects that are accessed either by a user-defined index or as a set. An *IndexedList* is updated by adding index-object pairs.

The *IndexedList* class has been optimized to organize and query large sets of data. A large number of the messages defined for this class have been written in Vision and can therefore be modified and expanded as needed. As always, you can define any number of new messages for the class.

The *IndexedList* class is a direct subclass of IndexedCollection:

        Object
           |
           Function
              |
              EnumeratedFunction
                 |
                 Collection
                    |
                    IndexedCollection
                       |
                       |-- IndexedList
                       |
                       |-- TimeSeries

------------------------------------------------------------------------
