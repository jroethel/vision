---
provenance: "docs/original/invHolding.htm#Overview"
unit_type: "general"
title: "The Holding Class"
ingested: "2026-09-22"
---

## Overview

The class **Holding** is used to represent a specific holding by an account in a security as of a specific point in time. Holdings are rarely (if ever) referenced directly. Instead they are accessed via a particular security or account. In general, holdings are created as part of the process that updates the accounts each day. Key data items such as *totalMarketValue* and *percentOfPort* for each Holding and Account summary information such as *totalMarketValue* and *totalCost* are also computed at this time.

The Holding data structure is illustrated below:

**Data Structure Diagram: Class Holding**

      _____________
      |  Holding  |--|
      |___________|  |                     ______________
                     |---- security   ---> |  Security  |
                     |                     |____________|          ___________
                     |                        |                    |   ...   |
                     |                        |---- holdings  ---> | Holding |
                     |                        |                    | Holding |
                     |                        |                    |   ...   |
                     |                        |                    |_________|
                     |                        |                    ___________
                     |                        |---- taxlots   ---> |   ...   |
                     |                        |                    | taxlot  |
                     |                        |---- cusip          | taxlot  |
                     |                        |---- name           |   ...   |
                     |                        |---- price          |_________|
                     |                        |---- company --->
                     |                     __________________
                     |---- account    ---> |  Account       |
                     |                     |________________|      ___________
                     |                        |                    |   ...   |
                     |                        |---- holdings  ---> | Holding |
                     |                        |                    | Holding |
                     |                        |                    |   ...   |
                     |                        |                    |_________|
                     |                        |
                     |---- date               |                    ___________
                     |---- baseCurrency       |---- taxlots   ---> |   ...   |
                     |---- percentOfPort      |---- code           | taxlot  |
                     |---- shares             |---- name           | taxlot  |
                     |---- totalCost          |---- totalMarketVal |   ...   |
                     |---- totalMarketValue   |---- inceptionDate  |_________|
                     |                        |---- portfolioManager -->

------------------------------------------------------------------------
