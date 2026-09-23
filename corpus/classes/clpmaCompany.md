---
provenance: "docs/original/clpmaCompany.htm#overview"
unit_type: "class"
title: "Vision Application Classes: Company and Security"
ingested: "2026-09-22"
---

## Overview

The instances of the class **Company** represent the individual corporate entities for which you track information. Information maintained for a company typically includes country, industry, sales, and earnings. The instances of the class **Security** represent the individual securities issued by a company or equivalent entity such as the government. A variety of security types exist including cash, common and preferred stocks, convertible and non-convertible bonds, and put and call options. Data maintained for a security typically includes price, dividend and shares/amount outstanding information. Portfolios hold specific amounts of one or more securities.

The following subset of the class hierarchy displays the classes directly related to **Company** and **Security**:

      Object
         |
         Entity
         |  |
         |  |-- Company
         |  |
         |  |-- Security
         |  |
         |  |-- Classification
         |         |
         |         |-- Country
         |         |
         |         |-- Industry
         |         |
         |         |-- Sector
         |         |
         |         |-- SecurityType
         |         |
         |         |-- AssetCategory
         |    
         DataRecord
            |
            |-- DivRecord
            |
            |-- PriceRecord

------------------------------------------------------------------------
