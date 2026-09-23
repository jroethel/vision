---
provenance: "docs/original/rel612Unix.htm"
unit_type: "general"
title: "Release 6.1.2 Upgrade for Unix"
ingested: "2026-09-22"
---

## Download Contents:

ReadMe.txt

Installation instructions (this document).

visionUpgrade_1.5_to_1.6.unix

A C-Shell Unix script that will install the updated database support files and create a new Object Space to your network.

CHcore.6.1.2

Incorporates new primitives. This file is read by the *visionUpgrade_1.5_to_1.6.unix* script.

CHdbs.6.1.2

Miscellaneous changes to the bulk database driver. This file is read by the *visionUpgrade_1.5_to_1.6.unix* script.

rollbackNetwork.cmd

A C-Shell Unix script that has been updated to work with the PMA 1.6 release. This file is read by the *visionUpgrade_1.5_to_1.6.unix* script.

## Installation Procedures:

These installation procedures have been automated for PMA installations. Non-PMA installations can review the release contents for applicability to their environment.

1.  Backup the current */vision* and */localvision* contents by following the appropriate backup procedures for your installation.

2.  Close any sessions to the Vision database prior to starting this process.

3.  Make sure you are logged into the system as the Vision Administrator.

4.  Extract the contents of the [VisionUpgrade.tar](download/VisionUpgrade.tar) archive to a temporary directory of your choice.
    1.  Go to the directory that has the *VisionUpgrade.tar* file.

    2.  Extract the files from:

                           tar xpf VisionUpgrade.tar

5.  Install the new vision executables over the old version or create a new link.
    1.  Go to the directory that will hold the vision files and subdirectories.

    2.  Copy the appropriate [vision.sol.tar.Z](download/vision.sol.tar.Z), [vision.hpux.tar.Z](download/vision.hpux.tar.Z), or [vision.aix.tar.Z](download/vision.aix.tar.Z) file to this directory.

    3.  Decompress the tar file using the appropriate options to preserve permissions:

                           uncompress vision.*.tar.Z

    4.  Extract the files and subdirectories from:

                           tar xpf vision.*.tar

    5.  Re-link if necesary.

6.  Run the *visionUpgrade_1.5_to_1.6.unix* script to run the protocol and Object Space creation steps as well as copy the updated *rollbackNetwork.cmd* script into place.
    1.  Execute the script from the directory that has the *VisionUpgrade.tar* file.

                           visionUpgrade_1.5_to_1.6.unix

7.  Review the upgrade output in the generated log:

                            /localvision/logs/visionUpgrade_1.5_to_1.6.log

{% include doc-footer.htm copydates="1999" %}
