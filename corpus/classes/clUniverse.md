---
provenance: "docs/original/clUniverse.htm"
unit_type: "class"
title: "Vision Class: Universe "
ingested: "2026-09-22"
---

## Universe Overview

The **Universe** class is a subclass of **Entity** used to name and track lists of related entities over time. For example, a **Universe** instance named *SP500* could be defined to track the list of **Security** instances comprising the *Standard & Poors 500* each month.

The Universe class is a direct subclass of Entity:

      Object
         |
      Entity
         |
         Universe

------------------------------------------------------------------------

## Basic Usage

**Universe** instances are created to name and track related entities over time. A universe can be restricted to a certain type of entity by setting its *entityType* property using the *setEntityTypeTo:* message. For example, to create the *Dow Jones 30* universe of securities:

      Universe createInstance: "DJ30" .
          setEntityTypeTo: Security ;

The time series property *list* is defined at the class **Universe** to store lists of entities over time. This property can be updated using the *setListTo:* message which creates a new **IndexedList**, adds the entities supplied in the parameter, and stores the list in the *list* property as of the current evaluation date. If an *entityType* has been specified, the elements in the supplied list are only added if they represent instances of that class. List elements can be supplied as explicit objects or as string. Strings will be converted to instances of the *entityType's* class using the *locateId:* message for that class. For example:

      95 evaluate:
        [ Named Universe DJ30 
             setListTo: Named Security IBM, "XON", "GM" ;
        ] ;

stores a list of three securities in the *list* property for the *DJ30* universe as of year-end 1995. The strings *XON* and *GM* are converted into security instances. The *addMember:* and *deleteMember:* messages can be use used to modify an existing list. Instances are added or deleted from the list stored as of the evaluation date.

To view the universe members as of a specific date use:

      #-- latest
      Named Universe DJ30 list do: [ displayInfo ] ;

      #-- as of last month
      ^today - 1 monthEnds evaluate:
        [ Named Universe DJ30 list do: [ displayInfo ] ;
        ] ;

      #-- alternative
      Named Universe DJ30 :list lag: 1 monthEnds . do: [ displayInfo ] ;

      #-- all periods
      Named Universe DJ30 :list
      do: [ ^date print ; count print ; " members" printNL ; 
            ^self do: [ displayInfo ] ;
          ] ;

The *displayMemberHistory* report shows changes in the universe membership over time. For example:

      96 evaluate:
        [ Named Universe DJ30 
             setListTo: "IBM", "XON", "GIS", "DD" ;
        ] ;

      Named Universe DJ30 displayMemberHistory ;

displays:

                          ---  Membership History Report  ---                     
                              for Universe DJ30 DJ30                           

      01/01/1                0 current         0 prior
      12/31/1995             3 current         0 prior
          added ... 30229010     XON          EXXON CORP COM
          added ... 37044210     GM           GENERAL MTRS CORP COM
          added ... 45920010     IBM          INTERNATIONAL BUSINESS MACH COM
      12/31/1996             4 current         3 prior
          added ... 26353410     DD           DU PONT E I DE NEMOURS & CO COM
          added ... 37033410     GIS          GENERAL MLS INC COM
        dropped ... 37044210     GM           GENERAL MTRS CORP COM

The message *universe* has been defined for the class **Entity** and returns the list of **Universe** instances that contain the recipient object. For example:

      Named Security IBM universes
      do: [ displayInfo ] 

will display the *DJ30* and any other universe in which the security *IBM* is a member.

------------------------------------------------------------------------

## Using the ExternalFeedManager

The earlier sections in this document describe ways to directly create and update **Universe** instances. The **Interface** class [**ExternalFeedManager**](clDataFeed.md) has been created to provide a uniform way to create and update any entity-related information. A separate **DataFeed** subclass is defined to translate one or more rows of information into the appropriate structures in your Vision database. Data can be supplied from a file, a spreadsheet, a relational database, or any other table-based source. You can also supply data directly as a string, using the tab character to delimit columns and the carriage return to delimit rows.

Several **DataFeed** classes have been defined to work with **Universe** data:

DataFeed

Description

[UniverseMaster](../feeds/pma_UniverseMaster.md)

creates **Universe** instances and refreshes basic properties

[UniverseMembers](../feeds/pma_UniverseMembers.md)

updates memberships for universes over time

For example, the following tab-delimited string could be used to create and refresh **Universe** instances:

      Interface ExternalFeedManager upload: "UniverseMaster" using:
      "Id   Name                      MemberType    
       SP500     Standard & Poors 500     Security  
       DJ30      Dow Jones 30 Industrials  Security
       DJT       Dow Jones Transportation  Security
      " ;

The following tab-delimited string could be used to define **Universe/ **memberships over time:****

      Interface ExternalFeedManager upload: "UniverseMembers" using:
      "groupId     date       memberId
       SP500       19971031   45920010  
       SP500       19971031   37044210  
       SP500       19971031   88553510  
       #---  ...
       SP500       19971130   45920010  
       SP500       19971130   37044210  
       SP500       19971130   88553510  
       #---  ...
       DJT         Default    01165910
       DJT         Default    00176510
       DJT         Default    00202M10
       #---  ...
      " ;

{% include doc-footer.htm copydates="1998" %}
