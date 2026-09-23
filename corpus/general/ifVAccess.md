---
provenance: "docs/original/ifVAccess.htm#Introduction"
unit_type: "general"
title: "Using VAccess and COM to Access Vision"
ingested: "2026-09-22"
---

## Introduction

VAccess provides a COM compatible interface to Vision.  Using VAccess, you can execute Vision code and retrieve structured results using any programming language capable of functioning as a COM client.  Among the many examples of such environments are Microsoft Visual Basic, VBScript, and MatLab.

The classes, properties, and operations implemented by VAccess are based on the C++ classes documented in [Sample C++ Access to Vision](ifCAccess.md), modified and updated to make them COM aware.  The structured query operations implemented in VAccess by *[ExtractWS](#class%20ExtractWS)* objects are built using the Vision **[Interface ExtractWS](tkInterface/6.md)** tool kit.

VAccess is supplied in both executable and source code form.  This document describes the capabilities available in the standard executable version.  If you have the need and the skills to do so, you are free to modify and recompile the source code to add custom capabilities; however, that is beyond the scope of this description.
