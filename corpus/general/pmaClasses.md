---
provenance: "docs/original/pmaClasses.htm#overview"
unit_type: "general"
title: "Vision Portfolio Management Application Classes"
ingested: "2026-09-22"
---

## Overview

The core Vision system comes with a set of classes already defined. These classes include an initial set of methods which can be modified and extended by the user. Vision's built-in class hierarchy is discussed in detail in the [general Vision documentation](../classes/clXRef.md). The **Portfolio Management Application Layer** defines classes, protocol, and starter applications that address the needs of the portfolio management function. This layer is entirely implemented using the Vision language. You can therefore modify, extend, and reorganize the structures to meet the specific needs of your organization.

The **Portfolio Management Application Layer** includes the following classes:

      Object
         |
         DataRecord
         |  |
         |  |-- DivRecord
         |  |
         |  |-- PriceRecord
         |
         Entity
         |  |
         |  |-- Account
         |  |      |
         |  |      |-- AggAccount
         |  |      |
         |  |      |-- CompositeAccount
         |  |      |
         |  |      |-- IndexAccount
         |  |      |
         |  |      |-- Portfolio
         |  |
         |  |-- Classification
         |  |      |
         |  |      |-- AssetCategory
         |  |      |
         |  |      |-- Country
         |  |      |
         |  |      |-- Industry
         |  |      |
         |  |      |-- Sector
         |  |      |
         |  |      |-- SecurityType
         |  |
         |  |-- Company
         |  |
         |  |-- Currency
         |  |
         |  |-- Security
         |  |
         |  |-- Universe
         |
         LinkRecord
            |
            |-- CompositeAccount Component
            |
            |-- Holding
