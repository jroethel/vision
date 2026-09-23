---
provenance: "docs/original/admBatch.htm#overview"
unit_type: "general"
title: "Vision Administration: Batch Processing"
ingested: "2026-09-22"
---

## Overview

The [Vision Administrator Module](pmaDBA.md) performs various Database Administration functions in an interactive Windows environment. You may find it useful to use scripts to perform these same functions in a batch environment. Such sample scripts are described in this document and can serve as a basis for designing your own. These scripts work outside the VAdmin module and allow you to perform multiple functions and/or load multiple files simultaneously, as well as allow you to keep an 'audit trail' of your scripting iterations.

The examples as provided assume certain environment variables have been set to the standards established in PMA Release 1.7. If you are on a prior release, you will need to modify these variables before running your scripts as described in this document:

On Unix:

Modify the general defaults for Vision Database Administrator processing in */localvision/include/DBAVision.env*:

- Add *setenv VisionAdm 1*  
  Add *setenv UserOSI 3*  
  Change the *VisionMaxSegSize* from *50000000* to *33554432*

On NT:

Modify the System Variables:

- Add *%VisionRoot%bin* to the values listed for the Path variable  
  Add the new variable *NDFPathName* with a value of *%LocalVisionRoot%network\NDF*

Modify the User Variables for the Vision Administrator:

- Add the new variable *UserOSI* with a value of *3*  
  Add the new variable *VisionAdm* with a value of *1*  
  Add the new variable *VisionMaxSegSize* with a value of *33554432*

If you need additional help setting up these variables, please contact your Insyte consultant.

------------------------------------------------------------------------
