---
provenance: "docs/original/invAccount.htm#Overview"
unit_type: "general"
title: "The Account Classes"
ingested: "2026-09-22"
---

## Overview

The class **Account** is a super class of the classes **Portfolio**, **AggAccount**, and **IndexAccount**. A Portfolio is defined as an account whose holdings are created via a feed from an internal accounting system. The actual portfolio instances may represent *real* or *test* portfolios. An AggAccount is defined as an account whose holdings are created by combining the holdings for a list of component portfolios. This portfolio list may be explicit or derived. An IndexAccount is defined as an account whose holdings are created starting with a list of securities and one or more rules to derive a *shares owned* value.

Messages that apply to all Account subclasses are defined at Account. Messages that address the unique requirements of Portfolio, AggAccount, and IndexAccount instances are defined at the appropriate subclass. Your installation may define additional subclasses.

Instances of the Account classes are named at the lowest level class. For example, portfolio XYZ would be accessed using:

      Named Portfolio XYZ

An extra naming dictionary is defined at the Account class to allow interchangeable access among the classes. For example, the expression:

      Named Account XYZ

also returns portfolio XYZ. If the same id is used to identify a portfolio and another account instance, the expression will return the portfolio instance. The property *uniqueId* is used to create a unique identifier for each instance. The expressions:

      Named Account P_XYZ = Named Portfolio XYZ

      Named Account A_XYZ = Named AggAccount XYZ

and

      Named Account I_XYZ = Named IndexAccount XYZ

all return the value TRUE. The message *locateId:* has been redefined at the Account class to use the following search rule:

- Named Account
- Named Portfolio
- Named AggAccount
- Named IndexAccount

For example, the expression:

      Account locateId: "XYZ"

returns *Named Account XYZ* if it is defined, otherwise it returns *Named Portfolio XYZ*, otherwise *Named AggAccount XYZ*, otherwise *Named IndexAccount XYZ*, otherwise NA.

------------------------------------------------------------------------
