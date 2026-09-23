---
provenance: "docs/original/pmaIssues.htm#overview"
unit_type: "general"
title: "Vision Portfolio Management Application Issues"
ingested: "2026-09-22"
---

## Overview

Special structures have been designed to manage dividend, price, and adjustment data in the Vision database. These structures have been created to correctly handle split and currency adjustments automatically. In addition, these structures have been designed to facilitate future reorganizations as the database grows, so that applications that use this data are sheltered from structural changes.

Many items defined for a security are affected by stock splits including price, shares outstanding, and dividends per share. By default, data is returned split adjusted relative to the current date. In general, message names that begin with the character '\_' indicate the "raw", unadjusted data value in its initial units. For example, the property *\_sharesOut* defined at **Security** refers to the actual shares outstanding value as of a specific date. The message *sharesOut* returns this value adjusted for any splits that have occurred since that date.

------------------------------------------------------------------------
