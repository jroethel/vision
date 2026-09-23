---
provenance: "docs/original/clString.htm#overview"
unit_type: "class"
title: "Vision Class: String "
ingested: "2026-09-22"
---

## Overview

**Strings** are objects that represent sequences of characters. Strings respond to messages that format, parse, and perform comparisons with other strings. The literal representation of a string is a sequence of characters delimited by double quotes. For example:

- "xyz"
- "a"
- "The Vision language is fun"

Any character may be included in a string. If you need to include a double quote in the string, it must be *escaped* using the '\\ character to avoid confusion with the string delimiters. For example:

      "He said, \"The Vision language is fun\" "

returns the string:

      He said, "The Vision language is fun"

The *String* class is a direct subclass of the class *Ordinal*:

      Object
         |
         Ordinal
            |
            String

------------------------------------------------------------------------
