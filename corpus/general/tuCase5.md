---
provenance: "docs/original/tuCase5.htm"
unit_type: "general"
title: "Case Study 5: Advanced Classification Techniques"
ingested: "2026-09-22"
---

> 
>
> ------------------------------------------------------------------------
>
> **Reminder!**
>
> To run these examples, you should first start a new session and then load the sample database using:
>
>       "/localvision/samples/general/sample.load" asFileContents evaluate ;
>
> and load *testList* using:
>
> - !testList <- Company masterList 
>           rankDown: [ sales ] . 
>           select: [ rank <= 20 ] ;
>
> Any other files referenced can be read from the */localvision/samples/general/* directory.
>
> **Note:** The *sample.load* file runs by default on a *Unix* environment. If you are using a *Windows NT* platform, this location may be prefixed by a drive and optional path (e.g. *d:/visiondb/localvision/samples/general/sample.load*). Check with your Vision Administrator for further details.
>
> ------------------------------------------------------------------------

------------------------------------------------------------------------
