---
provenance: "docs/original/sdmts.htm#Introduction"
unit_type: "general"
title: "Sets Do More Than Select"
ingested: "2026-09-22"
---

## Introduction

The first generation of database-centered applications -- maintaining an organization's operating data -- demanded database management systems tuned to handle large numbers of small, update-oriented transactions. The first generation of true database management technology -- relational data base systems -- was well matched to that class of problem. The normal forms of the relational model taught many good lessons in data analysis and structuring, the large amounts of simple data fit well into the tabular representation of relational data base management, and for the most part, the relatively simple data in these applications could be effectively queried using standard SQL query languages.

As the complexity of database-centered applications grows, a new set of database system requirements is emerging. The new generation of database-centered applications no longer focuses on operational data and transaction processing. Instead, it focuses on:

- managing and using complex relationships
- intelligent data acquisition
- decision support

These new applications do not fit well into a relational framework, primarily because relational database systems lack the ability to express many of the constraints, rules, and queries these new applications need. When relational implementations are tried, large parts of the application need to be written as custom programs in conventional programming languages, not in the database system.

This custom-programming strategy has significant costs in terms of both performance and productivity. These costs are compounded by the fact that many of these applications have a natural representation in the new technology of object-orientation. All of these factors have led to the emergence of object-oriented databases -- a technology that unifies the capabilities of database management and object-oriented programming systems.

Merging these two technologies creates a new technology that is more than the sum of its parts -- both in terms of the problems it can solve and the technical demands it imposes on its implementation. Some attempts to create this new technology have begun with object-oriented programming languages like C++ or Smalltalk, and augmented them with database-like capabilities such as persistence and sharing.

Unfortunately, programming languages and the techniques for optimizing them were never designed to scale to the size of a very large database. Other efforts started with relational frameworks and attempted to generalize the representational and query processing capabilities of these engines. While the set-orientation of a database engine is required for the system to scale, the classic techniques for optimizing and processing relational queries are not general enough to be of value to the full range of queries possible in these much more powerful information processing engines. To succeed, a new approach is required.

[Programming Language Techniques Do Not Scale](sdmts.htm#Programming%20Languages%20Do%20Not%20Scale)

[Relational Query Engines Are Not General Enough](sdmts.htm#Relational%20Query%20Engines%20Are%20Not%20General%20Enough)

[A New Paradigm For Object-Oriented Database Implementation](sdmts.htm#A%20New%20Paradigm%20For%20Data%20Base%20Programming)
