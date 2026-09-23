---
provenance: "docs/original/pmaSupp.htm"
unit_type: "general"
title: "Vision Portfolio Management Application Supplemental Classes"
ingested: "2026-09-22"
---

## Overview

A number of optional classes are provided as part of the **Portfolio Management Application Layer**. These classes can be installed as is or modified as needed, depending on your requirements. Many of the [*Headstart Applications*](pmaApps.md) use data defined for these classes. Supplemental classes include:

              Object
                 |
                 DataRecord
                 |  |
                 |  |-- AnalystEstimate
                 |  |
                 |  |-- EconomicData
                 |  |
                 |  |-- FundamentalData
                 |         |
                 |         |-- FundamentalDataA
                 |         |
                 |         |-- FundamentalDataM
                 |         |
                 |         |-- FundamentalDataQ
                 |
                 Entity
                    |
                    |-- Analyst
                    |
                    |-- Classification
                           |
                           |-- RangeClassification
                                  |
                                  |--  MCapGroup
                                  |
                                  |--  PBGroup
                                  |
                                  |--  PEGroup
           

{% include doc-footer.htm copydates="1998" %}
