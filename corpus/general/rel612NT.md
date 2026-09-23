---
provenance: "docs/original/rel612NT.htm"
unit_type: "general"
title: "Release 6.1.2 Upgrade for NT"
ingested: "2026-09-22"
---

Click here to download the [Release 6.1.2 Upgrade for NT](download/VisionUpgrade.exe).

## Download Contents:

ReadMe.txt

Installation instructions (this document).

NT.6.1.2.exe

A self-extracting zip file that will upgrade the vision executables. This will prompt you to enter the root location of your existing *vision* directory. The default provided is "C:\\.

visionUpgrade_1.5_to_1.6.cmd

A Windows NT command script that will install the updated database support files and create a new Object Space to your network.

CHcore.6.1.2

Incorporates new primitives. This file is read by the *visionUpgrade_1.5_to_1.6.cmd* script.

CHdbs.6.1.2

Miscellaneous changes to the bulk database driver. This file is read by the *visionUpgrade_1.5_to_1.6.cmd* script.

rollbackNetwork.cmd

A Windows NT command script that has been updated to work with the PMA 1.6 release. This file is read by the *visionUpgrade_1.5_to_1.6.cmd* script.

## Installation Procedures:

These installation procedures have been automated for PMA installations. Non-PMA installations can review the release contents for applicability to their environment.

1.  Backup the current */vision* and */localvision* contents by following the appropriate backup procedures for your installation.

2.  Close any sessions to the Vision database prior to starting this process.

3.  Make sure you are logged into the system as the Vision Administrator.

4.  Double-click on the *VisionUpgrade* self-extracting file and extract the contents to a temporary directory of your choice.

5.  Double-click on the *NT.6.1.2* self-extracting file and install the new vision executables over the old version. (default to C:\\.

6.  Double-click on the *visionUpgrade_1.5_to_1.6.cmd* NT command script to run the protocol and Object Space creation steps as well as copy the updated *rollbackNetwork.cmd* script into place.

7.  Review the upgrade output in the generated log:

                %LocalVisionRoot%logs/visionUpgrade_1.5_to_1.6.log.

{% include doc-footer.htm copydates="1999" %}
