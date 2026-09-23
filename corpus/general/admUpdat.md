---
provenance: "docs/original/admUpdat.htm#overview"
unit_type: "general"
title: "Updating the Vision Network"
ingested: "2026-09-22"
---

## Overview

There are two basic types of update that can be performed: *Global Updates* which can create and change any object or message and *Private User Updates* which can only create and change objects in a particular object space. The *dbadmin* user code usually performs global updates. Other users can perform private user updates within their object space. A utility is available that allows non-*dbadmin* users to submit changes for global update.

Within any Vision session, any user can create new classes or instances, define or modify methods, and create or update property values. During your session, you can safely modify classes and instances that you do not control (i.e., shared *object space 3* objects), since these changes will only impact your session. Any definitions or modifications made during your session will apply throughout your session and will disappear when you exit the session without saving your changes.

An update is really just a Vision session whose actions are committed to the permanent database. Although any user can change shared objects during a session, only the *dbadmin* can save the changes as a permanent part of the database. Global (i.e., *dbadmin*) updates can affect objects in one or more object spaces. Private users can permanently save changes made to objects that they own. Private user updates commit changes to a single object space.

When Vision saves changes to the network, new segments are created. Private saves will create segments in the top level object space only. Global updates may create segments in several object spaces.

If you choose to commit a Vision session to the permanent database, Vision will attempt to do a global update if the following conditions are met:

- The user code appears in the file */localvision/network/NDF.GURL*.
- The session has the VisionAdm environment variable set.

If both of these conditions are not met, Vision will perform a private user update.

The *NDF.GURL* file contains a list of user codes that have permission to perform global updates. By default, this file contains only the *dbadmin* user code. You can edit this file to contain any number of users, one per line: however, it is usually preferable to limit the number of users with global update rights.

All updates to the Vision network are recorded in the *NDF.JOURNAL* file located in */localvision/network*. Minimally, this Ascii file lists the segments created with each update. When you use the [*dbSubmit*](#The%20dbSubmit%20Utility) utility and the database [network maintenance tools](admTools.md), additional annotations will be placed in this file for each update. The [*NDF.JOURNAL*](admTools.htm#NDF.JOURNAL%20File) and related tools are described further in the section, [Network Administration Tools](admTools.md)

------------------------------------------------------------------------
