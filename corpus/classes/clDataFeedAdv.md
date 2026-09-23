---
provenance: "docs/original/clDataFeedAdv.htm#overview"
unit_type: "class"
title: "Vision Class: DataFeed"
ingested: "2026-09-22"
---

## DataFeed Review

The **DataFeed** class is an abstract class that is used to organize the classes that translate data from sources external to Vision into Vision objects. An external feed corresponds to a flat, tabular structure. Several subclasses of **DataFeed** have been defined to encapsulate different ways to map data from external formats into Vision objects. You can get a full list of the feeds defined in your environment using:

         DataFeed showInheritance ;

A separate subclass is defined for each format of external data you wish to load into your Vision database. For example, subclasses of the **MasterFeed** class are defined to create and update instances of a specific **Entity**, such as **Currency** or **Security**. Subclasses of the **EntityExtenderFeed** class are defined to update a specific relationship between an **Entity** subclass and associated data, such as pricing data for a security.

At its simplest, a feed is a tab or vertical bar delimited string containing one or more columns of information for one or more rows. For example, to create and update **Currency** instances, you could use:

         CurrencyMaster updateFromString: 
         "entityId | name                 | shortName
          USD      | United States Dollar | US Dollar
          CAD      | Canadian Dollar      | CA Dollar
          GBP      | Great British Pound  | GB Pound
         " ;

This example loads data using the **CurrencyMaster** feed. This feed will create **Currency** instances for any *entityId* not already defined and will update the *name* and *shortName* properties for the three instances included.

The message *updateFromString:* can be sent to any **DataFeed** subclass to update data from the string supplied as a parameter. Alternatively, the message *loadFromFile:* can be sent to any **DataFeed** subclass to read the data from the file name supplied as a parameter.

The document [*Vision Class: DataFeed*](clDataFeed.md) provides a detailed description of the **DataFeed class**. A number of specialized interfaces have been defined that package feeds for [batch processing](../general/admBatch/3.md). This document provides additional advanced techniques for working with the feeds through the use of examples. If you need additional assistance implementing some of these techniques in your environment, contact your Insyte consultant.

------------------------------------------------------------------------
