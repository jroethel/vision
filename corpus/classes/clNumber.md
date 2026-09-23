---
provenance: "docs/original/clNumber.htm#overview"
unit_type: "class"
title: "Vision Class: Number "
ingested: "2026-09-22"
---

## Overview

**Numbers** are objects that represent numerical values and respond to messages that compute mathematical results. The literal representation of a number is a sequence of digits that may be preceded by a minus sign and/or followed by a decimal point and another sequence of digits.

The classes *Integer*, *Double*, and *Float* are subclasses of the class *Number*. The class *Number* defines the general protocol for all numeric classes. Most numbers are either integers or doubles. The *Float* class is used for efficiency in certain cases. All arithmetic operations between numbers return instances of the class *Double*. It is not meaningful to create new instances of the *Number* classes.

The *Number* class is a direct subclass of the class *Ordinal*:

      Object
         |
         Ordinal
            |
            Number
               |
               |-- Double
               |
               |-- Float
               |
               |-- Integer

------------------------------------------------------------------------
