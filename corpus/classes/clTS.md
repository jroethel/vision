---
provenance: "docs/original/clTS.htm#overview"
unit_type: "class"
title: "Vision Class: TimeSeries"
ingested: "2026-09-22"
---

## Overview

**TimeSeries** objects are used to track information for a particular data item over time. Some items, such as company sales and earnings may be tracked at regular intervals. Other information, such as ratings, will change at irregular intervals over time. The *TimeSeries* class has been designed to work effectively in all these cases.

The *TimeSeries* class is an indirect subclass of the *Collection* class which is also a superclass of the classes [*List*](clList.md) and [*IndexedList*](clIList.md). Instances of the class *TimeSeries* consist of a collection of objects that are accessed either by date or as a set. A *TimeSeries* is updated by adding date-object pairs.

The *TimeSeries* class has been optimized to organize and query large sets of data. A large number of the messages defined for this class have been written in Vision and can therefore be modified and expanded as needed. As always, you can define any number of new messages for the class.

The *TimeSeries* class is a direct subclass of IndexedCollection:

        Object
           |
           Function
              |
              EnumeratedFunction
                 |
                 Collection
                    |
                    IndexedCollection
                       |-- IndexedList
                       |-- TimeSeries

------------------------------------------------------------------------
