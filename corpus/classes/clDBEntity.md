---
provenance: "docs/original/clDBEntity.htm#Overview"
unit_type: "class"
title: "External Database Access and Investment Databases"
ingested: "2026-09-22"
---

## Overview

The Vision database provides access to a variety of database sources that are updated by an external vendor on a regular basis. These databases are linked to specific entities such as the IBM security object or the Nestles company object during an update process known as reconciliation. The reconciliation process addresses any adjustments that are local to the specific external database so that access to multiple databases can appear as homogeneous as possible. Cusip changes, split adjustments, and fiscal year management are all addressed in a uniform manner so that arbitrary decisions defined by the individual database vendors become irrelevant.

Each external database source supplies one or more tables of information usually related to a specific entity type such as Company or Security. Each table of information can contain multiple records for a specific entity, representing data as of different points in time. Access to this data is provided via a set of messages defined to link a specific entity instance with its corresponding data in the external source.

A specific data source may send incremental updates for each new period of time or may resend many periods of data with each update. The former approach is referred to as an *Incremental* or *Append* type of update; the latter is known as a *Full Refresh* or *Replacement* type of update. The individual records in one of these tables are often referred to as *snapshots* since they represent a set of data values for a specific entity as of a specific point in time.

------------------------------------------------------------------------
