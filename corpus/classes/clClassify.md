---
provenance: "docs/original/clClassify.htm"
unit_type: "class"
title: "Vision Class: Classification"
ingested: "2026-09-22"
---

## Classification Overview

The **Classification** class is an abstract class used to organize a number of subclasses that define instances used for grouping and summarization purposes. Instances of Classification subclasses are normally referenced by other Entity instances. For example, the property *country* could be define for the class *Company* to return an instance of the *Country* class representing the country in which the company is based and the property *industry* could be defined to return an instance of the class *Industry* representing the company's major industry.

The Classification class is a direct subclass of Entity:

      Object
         |
      Entity
         |
         Classification
            |
            |-- RangeClassification

The class Classification is used to unify all the protocol that is common to classifications. Your installation may define any number of subclasses of Classification. To determine which subclasses have been defined, use the expression:

      Classification showInheritance

------------------------------------------------------------------------

## Basic Usage

The standard messages are used to create new [subclasses](clEntity/5.md), [instances](clEntity/6.md), and [messages](../general/Messages.md) for the Classification subclasses. For example, to define a new subclass and some instances representing countries and a property that links specific currencies to specific countries, use the following:

      #--  Define the new class and some instances
      Classification createSubclass: "Country" ;
      Country createInstance: "US" . 
         setNameTo: "Unites States" ;
      Country createInstance: "CA" .
         setNameTo: "Canada" ;

      #--  Define a message at Currency that returns country
      Currency defineFixedProperty: 'country' ;
      Named Currency USD :country <- Named Country US ;
      Named Currency CAD :country <- Named Country CA ;

Instances of many classification subclasses are often managed as a hierarchy. For example, *Industry 123* may refer to "Book Publishing", *Industry 120* may refer to "General Publishing", and *Industry 100* may refer to "General Media". It is often useful to be able to link these instances. The property *parent* is defined at Classification and is used to store a reference to another instance of the class that represents the *parent* instance. The message *setParentTo:* allows you to set up these relationships. For example:

      #--  Create Industry subclass
      Classification createSubclass: "Industry" ;

      #--  Create Industry instances and link to parent industry
      Industry createInstance: "100" . 
          setNameTo: "General Media" ;
      Industry createInstance: "120" . 
          setNameTo: "General Publishing" .
          setParentTo: Named Industry \100 ;
      Industry createInstance: "123" . 
          setNameTo: "Book Publishing" .
          setParentTo: Named Industry \120 ;

The expression:

      Named Industry \123 parent name

accesses the name of industry 123's parent, "General Publishing". The message *displayHierarchy* displays the industry hierarchy:

      Named Industry \123 displayHierarchy

produces:

       123       Book Publishing
          120       General Publishing
             100       General Media

When new instances are created, the *parent* property is initialized to return the new instance. The *isParent* message returns *TRUE* if the recipient is its own parent instance.

------------------------------------------------------------------------

## The RangeClassification Class

The class **RangeClassification** has been created to manage classes whose instances are used to assign values falling into a particular numeric range. Instances are not directly created for this class; instead, you would create subclasses of RangeClassification for each distinct range being tracked. Instances of subclasses of RangeClassification define the properties *lowerBound* and *upperBound*. The message *getClassificationFor: inputValue* is used to access the instance whose range contains the supplied value. The message *rangeName* returns a string formatted as:

      (lowerBound, upperBound)

For example, you can create a class to track market capitalization ranges using:

      RangeClassification createSubclass: "MCapGroup"

New instances are created by supplying the lower and upper boundary values to the *createInstance:* message. NA values are used to indicate that a lower or upper bound is undefined: For example, you can create the instances for MCapGroup using:

      MCapGroup
        createInstance: NA, 400 .
        setNameTo: "less than $400M" ;
      MCapGroup
        createInstance: 400, 1000 .
        setNameTo: "$400M - $1,000M" ;
      MCapGroup
        createInstance: 1000, 2000 .
        setNameTo: "$1,000M - $2,000M" ;
      MCapGroup
        createInstance: 2000, 5000 .
        setNameTo: "$2,000M - $5,000M" ;
      MCapGroup
        createInstance: 5000, NA .
        setNameTo: "greater than $5,000M" ;

The expression:

      MCapGroup getClassificationFor: 2300

returns the instance represented by the range 2000,5000 . Selection is done using:

      inputValue >= lowerBound && inputValue < upperBound

Assume that the property *marketCap* is defined for the class *Security* to return a numeric value. For reporting purposes you may want to group your securities into their market capitalization range and display summary data for each group. For example:

      Security masterList
      extendBy: 
        [ !mcapGroup <- 
             ^global MCapGroup getClassificationFor: marketCap ;
        ] .
      groupedBy: [ mcapGroup ] .
      do: [ name print: 30 ; 
            groupList count print ;
            groupList min: [ marketCap ] . print ; 
            groupList max: [ marketCap ] . printNL ;
          ] ;

{% include doc-footer.htm copydates="1997" %}
