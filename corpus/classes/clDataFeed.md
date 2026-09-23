---
provenance: "docs/original/clDataFeed.htm#overview"
unit_type: "class"
title: "Vision Class: DataFeed"
ingested: "2026-09-22"
---

## DataFeed Overview

The **DataFeed** class is an abstract class that is used to organize the classes that translate data from sources external to Vision into Vision objects. An external feed corresponds to a flat, tabular structure. It may be loaded into Vision from a file, a spreadsheet, a relational database, or any other source capable of presenting records of information.

Several subclasses of **DataFeed** have been defined to encapsulate different ways to map data from external formats into Vision objects. These include:

--- DataFeed Subclasses ---

**MasterFeed**

used to create new instances in an **Entity** subclass and refresh key properties for instances of that class.

**EntityExtenderFeed**

used to update properties and **DataRecord** instances associated with a specific **Entity** or **Bridge**, potentially over time.

**TransactionFeed**

used to create and cross reference instances of a **LinkRecord** subclass, classes that associate two or more entities.

**AliasFeed**

used to establish multiple aliases for existing **Entity** instances.

**XRefFeed**

used to load alternative identifiers for existing **Entity** instances.

**MembershipFeed**

used to update and cross reference one-to-many relationships between two **Entity** instances over time.

**RangeGroupFeed**

used to define and update numeric ranges and categorize **Entity** instances into the appropriate range group.

**SchemaFeeds**

used to define new core classes, properties, and data feed classes.

The initial **DataFeed** class hierarchy is illustrated below:

               Object
                 |
                 IncorporatorPrototype
                    |
                    DataFeed
                       |
                       |-- MasterFeed
                       |   |-- CurrencyMaster
                       |   |-- UniverseMaster
                       |
                       |-- EntityExtenderFeed
                       |   |-- ExchangeRateFeed
                       |   |-- EstimateRecordFeed
                       |
                       |-- TransactionFeed
                       |
                       |-- AliasFeed
                       |-- XRefFeed
                       |
                       |-- MembershipFeed
                       |   |-- UniverseMembers
                       |
                       |-- RangeGroupFeed
                       |
                       |-- SchemaFeeds
                       |   |-- ClassSetup
                       |   |-- PropertySetup
                       |   |-- MessageSetup
                       |   |-- DataFeedSetup
                       |
                       |-- GlobalsFeed

A separate subclass is defined for each format of external data you wish to load into your Vision database. For example, subclasses of the **MasterFeed** class are defined to create and update instances of a specific **Entity**, such as **Currency** or **Security**. Subclasses of the **EntityExtenderFeed** class are defined to update a specific relationship between an **Entity** subclass and associated data, such as pricing data for a security.

------------------------------------------------------------------------
