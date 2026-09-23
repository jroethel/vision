---
provenance: "docs/original/tinats.htm#Introduction"
unit_type: "general"
title: "Time Is Not A Time-Series"
ingested: "2026-09-22"
---

## Introduction

Representing time-varying data in a database has long been a problem. While it has always been possible to build structures tagged with time fields, the database tools for maintaining and analyzing time-varying data have left much to be desired.

In the days of relational databases, there were few choices except to use the database system as a simple data repository. Most, if not all, of the analysis and query logic associated with time-varying data needed to be implemented in application programs. The deficiency of the relational systems was their inability to create new data types that could hold time-varying collections of data. If the operation couldn't be done using select, project, join, and cartesian product, it couldn't be done in the relational system.

With the advent of object-oriented technology in general, and object-oriented database systems in particular, the obvious problem of the relational systems appears to be solved. Because object-oriented database systems can implement new data types that are directly usable by the database system, it is now possible to define new types of collections -- such as time-series -- that model time-varying collections of data. Presumably, these new data types can include the operations needed to maintain, select, and aggregate their contents based on the needs of the application builder.

Based on this new-found capability, there is now a perception that the only thing to do is provide a starter set of classes. Our ten years of experience in designing and using Vision<sup>TM</sup> -- our commercial, temporal, object-oriented database system -- tells us that the problem is larger than that.

- [Capturing Relationships](tinats/2.md)

  [Encapsulating Complexity](tinats/3.md)

  [Querying The Data Base](tinats/4.md)

  [Solving The Problem](tinats/5.md)
