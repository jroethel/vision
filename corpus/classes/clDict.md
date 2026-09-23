---
provenance: "docs/original/clDict.htm#overview"
unit_type: "class"
title: "Vision Class: Dictionary "
ingested: "2026-09-22"
---

## Dictionary Overview

The subclasses of the class **Dictionary** are used to manage a set of names that return related objects. Dictionary classes do not have instances. All the messages defined for a particular Dictionary usually return objects of the same class. Operationally, a Dictionary is similar to the class [IndexedList](clIList.md) except that the index values are String objects when you work with a Dictionary.

The Dictionary class is a direct subclass of Object:

      Object
         |
         Dictionary
            |
            |-- Environment
            |
            |-- LocalDBDictionary
            |
            |-- Named
            |
            |-- SystemDictionary
            |
            |-- XRef

------------------------------------------------------------------------
