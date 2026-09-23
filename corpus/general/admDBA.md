---
provenance: "docs/original/admDBA.htm#DeletingUnneededReferences"
unit_type: "general"
title: "Database Administration"
ingested: "2026-09-22"
---

## Deleting Unneeded References

The [*garbage collection*](admTools.htm#Garbage%20Collection) and [*compaction*](admTools/8.md) tools can be used to eliminate structures from your Vision database network that are no longer active. There are some structures associated with property values and methods that are not automatically purged by these tools. Several messages have been defined that allow you to flag additional information for the garbage collector to free.

Vision properties and collections manage internal structures for each type (i.e., class) of value stored for any of its instances. Vision properties and lists retain references to types even after none of the instances they represent refer to values of the type. To support the selective deletion of unneeded references, two primitives are available: the *cleanStore* message operates on the instances of a class and the *cleanDictionary* message operates on the message dictionary of a class. Both messages are defined at the class *Object* and return a *Boolean* value indicating whether the recipient object was "cleaned". The cover methods *rcleanStore* and *rcleanDictionary* can be used to recursively clean the stores or dictionaries of the recipient object. The messages *cleanStoreAndDictionary* and *rcleanStoreAndDictionary* can be used to perform both types of clean up for the recipient object.

The *cleanStore* message can be sent to a class to eliminate any unneeded references for its properties. For properties that reference instances of other user-defined classes, an alignment operation is also performed if necessary. The alignment operation replaces a chain of pointers with a single pointer in cases where the referenced class has had additions or deletions since the last time the property was updated, thereby speeding up access. The *cleanStore* message should also be explicitly sent to any properties that reference collections to align these structures as well. For example, if Security defines a fixed property *heldList* that contains a list of *Holding* instances, you would use:

      mySecurity heldList cleanStore

to align the list as well as to purge old, non-referenced structures. If values of *heldList* are clustered for all securities, you only need to run *cleanStore* for one element. If the values of *heldList* are not clustered, you could use:

      Security instanceList do: [ heldList cleanStore ] ;

The message *cleanDictionary* is the class level analog of *cleanStore*. It aligns the class dictionary and purges unneeded *define:toBe:* and *defineMethod:* definitions.

It is useful to periodically clean the stores and dictionaries for each class in your database. For most classes, this simply involves executing the *cleanStoreAndDictionary* message. Classes that contain property values which reference lists of elements need to also execute the *cleanStore* message on any of these properties as well. Also, any class that manages multiple clusters (i.e., parallel stores created using the *newPrototype* message) must explicitly send the cleanStore message to each of these clusters.

The message *cleanupClassStructures* has been defined at the class *Object* to perform the basic *cleanStoreAndDictionary* operation on the recipient and display a confirmation if the recipient required cleaning. This message can be redefined for any class that requires additional steps. For example, to redefine this message to also clean the *heldList* property at *Security*, use:

      Security
      defineMethod:
      [ | cleanupClassStructures |
        ^super cleanupClassStructures ;      #-- runs the general version
        heldList cleanStore
            ifTrue: [ "-- cleaned Security heldList" printNL ] ;
        ^self
      ] ;

------------------------------------------------------------------------
