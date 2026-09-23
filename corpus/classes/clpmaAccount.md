---
provenance: "docs/original/clpmaAccount.htm#overview"
unit_type: "class"
title: "Vision Application Classes: The Account Classes "
ingested: "2026-09-22"
---

## Overview

The class **Account** is a super class of the classes **Portfolio**, **AggAccount**, **IndexAccount**, and **CompositeAccount**. A **Portfolio** is defined as an **Account** whose holdings are created via a feed from an internal accounting system. An **AggAccount** is defined as an **Account** whose holdings are created by combining the holdings for the list of **Portfolios** instances defined for the aggregate. An **IndexAccount** is defined as an **account** whose holdings are created starting with a list of **Securities** and a rule to derive a *shares owned* value. A **CompositeAccount** is defined as an **Account** whose holdings are created as a weighted combination of the holdings in a set of portfolio, aggregate, index and/or other composite accounts defined for the composite.

Messages that apply to all **Account** subclasses are defined at **Account**. Messages that address the unique requirements of **Portfolio**, **AggAccount**, **IndexAccount** and **CompositeAccount** instances are defined at the appropriate subclass. Your installation may define additional subclasses.

You do not directly create instances of the class **Account**. Instances are created for the different subclasses. In addition to the messages defined directly by the subclass, all instances respond to the messages defined for the class **Account**.

The following subset of the class hierarchy displays the classes directly related to **Account**:

      Object
         |
         Entity
         |  |
         |  |-- Account
         |        |
         |        |-- AggAccount
         |        |
         |        |-- CompositeAccount
         |        |
         |        |-- IndexAccount
         |        |
         |        |-- Portfolio
         |
         LinkRecord
            |
            |-- CompositeAccount Component
            |
            |-- Holding

------------------------------------------------------------------------
