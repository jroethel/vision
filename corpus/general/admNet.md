---
provenance: "docs/original/admNet.htm#overview"
unit_type: "general"
title: "The Vision Network"
ingested: "2026-09-22"
---

## Overview

Most database management systems only store the raw data associated with manual inputs and various data feeds. Your Vision database network includes this raw data as well as all the structures, rules, and applications that integrate and utilize this data. The various components are managed as a single network of information, so that the integration and management issues are hidden from most users.

Your *Vision Network* contains all the objects, data, and navigation rules needed to integrate, access, manipulate, and update shared and private information. The network consists of a set of interconnected *Object Spaces* that correspond to directories for storing the data, structures, and protocol associated with a particular database or user. Each object space consists of a set of *Segments* that correspond to the actual files that contain information. The object spaces and segments are all related and managed through a single network controller file known as the *NDF (Network Directory File)*.

The default NDF is the file */localvision/network/NDF*. The object spaces associated with the default network are stored under the directory */localvision/network/*. Object spaces are directories numbered consecutively from 1. Each of these directories consists of a set of files that represent the segments in the object space. The *Vision Network* directory and file structure is illustrated below:

- ![Vision Network Directory and File Structure Image](admNet1.gif)

The segments for a particular object space can be physically distributed across multiple disks. In workstation versions of the software, the Vision network can physically be distributed across multiple workstation nodes as well. Symbolic links are placed in the Vision network directory to point to the actual location of specific object spaces.

Although object spaces and segments correspond to directories and files, most users should never need to know about this organization. The Database Administrator should understand this organization, but will always interact with the Vision network using the update and maintenance tools described later in this manual.

The Database Administrator can modify and create information in any of the object spaces. Private users can modify and create information only in their own object space. The update process is described in detail in the section [Updating the Vision Network](admUpdat.md). The network update procedures are designed to work incrementally; the existing network is left intact and additional segments are created that contain the structures that have been changed or added. Each time the network is updated, new segments are added to the network and the NDF is updated to reflect the new information that has been stored. Since the database is never changed in place, aborted transactions do not effect the actual database.

Although segments and the structures they contain are never directly changed, updates to the network may produce changes that have the effect of making some old structures obsolete. For example, when a large external database is updated, a set of new segments is added to the network. The segments that contain the previous version of the database are left unchanged. As a result, some redundant data may exist in the network. Two network maintenance procedures, [*compaction*](admTools/8.md) and [*rollback*](admTools/18.md), are available for eliminating extraneous segments and for reverting back to earlier versions of the network if necessary. These and other tools are described in detail in the section [*Network Administration Tools*](admTools.md).

To protect against possible disk problems or accidental deletion of a file, you should periodically back up the network to some form of archival storage (e.g., another disk, magnetic tape). The frequency of backup depends on the frequency of changes happening in the network. Overnight backup should be appropriate and adequate for most situations. Since changes to the network can be identified by the time stamps of specific files, it is not necessary to back up the entire network (which could be several gigabytes) each night. A typical strategy is to run a "full" backup once a week and daily incremental backup during the week.

------------------------------------------------------------------------
