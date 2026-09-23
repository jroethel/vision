---
provenance: "docs/original/clEntity.htm#overview"
unit_type: "class"
title: "Vision Class: Entity "
ingested: "2026-09-22"
---

## Entity Overview

The **Entity** class is an abstract class that is used to organize the classes in the hierarchy whose instances represent real-world entities such as companies, products, and industries. Each instance of these classes corresponds to a particular entity. For example, the instances of the class *Company* could represent individual corporate entities such as *GM*. Instances of the class *Industry* represent specific industries such as *Autos*.

The Entity class is a direct subclass of Object:

      Object
         |
         Entity
            |
            |-- Classification
            |
            |-- Currency
            |
            |-- Universe

------------------------------------------------------------------------
