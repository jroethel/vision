---
provenance: "docs/original/clNA.htm#overview"
unit_type: "class"
title: "Vision Class: Undefined (NA) "
ingested: "2026-09-22"
---

## Overview

The **Undefined** class has a single instance that represents a value that is not available. This instance is named *NA*. Any object can be compared to the *NA* object using the messages *isNA* and *isntNA*. For example:

- *"x" isntNA print* ;
- *NA isNA print* ;
- *3 isNA print* ;
- *NA isntNA print* ;

The first two examples return and print the value *TRUE*. The last two examples return and print the value *FALSE*.

You cannot directly create new instances of the *Undefined* class. You can, however, [create subclasses](#subclass) of the *Undefined* class which have any number of instances.

The Undefined class is a direct subclass of Object:

      Object
         |
         Undefined
            |
            |-- NoValue

------------------------------------------------------------------------
