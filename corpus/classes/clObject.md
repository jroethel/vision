---
provenance: "docs/original/clObject.htm#overview"
unit_type: "class"
title: "Vision Class: Object "
ingested: "2026-09-22"
---

## Overview

The **Object** class is a direct or indirect super class of all other classes in the database. Any message defined at *Object* is applicable to all objects. Any subclass can redefine the behavior of a message defined at the *Object* class. You do not normally create instances of the class *Object* directly. When you create instances in another class, a new instance is created in each of that class' super classes including *Object*.

The major subclasses of *Object* are:

      Object
          Boolean
          DateRange
          Dictionary
          Entity
          Function
              Block
              IndexedList
              List
              TimeSeries
          Ordinal
              Date
              Number
              String
          ToolKit
              OpenVision
              Schema
              UserInterface
         Undefined

------------------------------------------------------------------------
