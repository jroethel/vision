---
provenance: "docs/original/admProduction.htm#overview"
unit_type: "general"
title: "Vision Administration: Production Processing"
ingested: "2026-09-22"
---

## Overview

Many Vision installations expect to receive various data feeds on a regular basis. Once the data is saved in the Vision database, other updates that rely on this data can be performed. In addition, standard production reports can be generated based on the completion of one or more updates.

It is useful to automate the production cycle so that standard updates and report generations can be scheduled to run each night. There are a number of ways that you can automate your daily production cycle. A comprehensive set of scripts has been provided for Unix environments as a template for this automation. These tools enable you to:

- Define any number of update and report jobs that can be scheduled to run on a daily or as needed basis.
- Assign dependencies to jobs so that specific tasks will not begin until other tasks have completed.
- Get a quick snapshot of the status of the current production cycle.

These scripts can be used directly or can serve as a basis for designing your own production processing. With the exception of the last section, the remainder of this document refers to the production management tools included with Unix installations. [The last section](#custom) describes the building blocks you will need if you design your own production processing.

------------------------------------------------------------------------
