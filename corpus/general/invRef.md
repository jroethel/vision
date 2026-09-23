---
provenance: "docs/original/invRef.htm"
unit_type: "general"
title: "Vision Investment Management Application Layer"
ingested: "2026-09-22"
---

## Overview

The core Vision system comes with a set of classes already defined. These classes include an initial set of methods which can be modified and extended by the user. Vision's built-in class hierarchy is discussed in detail in the general Vision reference manuals. Insyte offers an Application Layer that presents a set of useful classes and protocol designed to support investment management applications. The Investment Management classes and messages were entirely implemented using the Vision language. You can therefore modify, extend, and reorganize the structures to meet the specific needs of your organization.

Note that the instances created for the core investment classes will be dependent on your installation's requirements. Many of the named instances used in the examples in these document are included for illustration purposes only and may not exist in your environment. You can create them using the techniques provided or substitute instance identifiers that are defined for you organization.

------------------------------------------------------------------------

## The Company Class

The instances of the class **Company** represent the individual corporate entities for which you track information. Information maintained for a company typically includes sales, earnings estimates, and ratings. A large amount of raw data about companies is provided by external data vendors. In Vision, this data is viewed as a property of the company.

The document, [*The Company and Security Classes*](invSecurity.md), describes this class in more details.

------------------------------------------------------------------------

## The Security Class

The instances of the class **Security** represent the individual securities issues by a corporation, government, or other entity. A variety of security types exist including common and preferred stock, convertible and non-convertible bonds, and options. Data maintained for a security typically includes price, dividend, and shares outstanding information. Portfolios hold specific amounts of one or more individual securities. Raw data about securities is often provided by external data vendors. In Vision, this data is viewed as a property of the security.

The document, [*The Company and Security Classes*](invSecurity.md), describes this class in more details.

------------------------------------------------------------------------

## The Account Class

The class **Account** is a super class of the classes **Portfolio**, **AggAccount**, and **IndexAccount**. A Portfolio is defined as an account whose holdings are created via a feed from an internal portfolio accounting system. An AggAccount is defined as an account whose holdings are created by combining the holdings for a list of component portfolios. An IndexAccount is defined as an account whose holdings are created starting with a universe of securities.

The document, [*The Account Class*](invAccount.md), describes this class in more details.

------------------------------------------------------------------------

## The Holding Class

The class **Holding** is used to represent a specific holding by an account in a specific security as of a specific point in time. Holdings are rarely referenced directly. Instead they are accessed via a particular security or account. Data maintained for a holding typically includes shares held and total market value.

The document, [*The Holding Class*](invHolding.md), describes this class in more details.

------------------------------------------------------------------------

## Special Issues

Special structures have been designed to manage dividend, price, and adjustment data in the Vision database. These structures have been created to correctly handle split and currency adjustments automatically. In addition, these structures have been designed to facilitate future reorganizations as the database grows, so that applications that use this data are sheltered from structural changes.

The document, [*Special Issues*](invIssues.md) describes these issues in more detail.

------------------------------------------------------------------------

## External Data Sets

The Investment Management Application Layer provides access to a variety of data sources that are updated by an external vendor on a regular basis. These data sets are linked to specific companies, securities, or other instances as part of an update process known as reconciliation. The reconcile addresses any adjustments that are local to a specific vendor so that access to multiple data sources can appear as homogeneous as possible. Cusip changes, splits adjustments, and fiscal year management are all addressed in a uniform manner.

The document, [*External Data Sets*](invExtDB.md) describes this process in more detail. {% include doc-footer.htm copydates="1997" %}
