---
provenance: "docs/original/pmaLoad.htm#overview"
unit_type: "general"
title: "PMA Tutorial : Loading Sample Data "
ingested: "2026-09-22"
---

## Overview

All sample [PMA Tutorials](pmaTutor.md) are based on the data described in this section. Several sample data files have been supplied in addition to sample Vision code which can be executed to read these files and create the database.

By default, all files referenced are in the directory */localvision/samples/pma/*. Check with your Vision Administrator if you do not see the following files in the directory:

**File Name**

**Function**

**Reference**

*Currency.pma*

Tab-delimited file containing currency identifiers and names.

[CurrencyMaster](../feeds/pma_CurrencyMaster.md)

*Country.pma*

Tab-delimited file containing country identifiers and names and a currency identifier.

[CountryMaster](../feeds/pma_CountryMaster.md)

*Sector.pma*

Tab-delimited file containing sector identifiers and names.

[SectorMaster](../feeds/pma_SectorMaster.md)

*Industry.pma*

Tab-delimited file containing industry identifiers and names and a sector identifier.

[IndustryMaster](../feeds/pma_IndustryMaster.md)

*Company.pma*

Tab-delimited file containing basic company information: id, name, country, industry id, and fiscalYearEnd.

[CountryMaster](../feeds/pma_CountryMaster.md)

*SecType.pma*

Tab-delimited file containing basic SecurityType information: id, name, unitcalc, assetcategory

[SecurityTypeMaster](../feeds/pma_SecurityTypeMaster.md)

*Security.pma*

Tab-delimited file containing security information: id, name, currency, cusip, ticker, companyId, security type, and latestMarketCapUS.

[SecurityMaster](../feeds/pma_SecurityMaster.md)

*Portfolio.pma*

Tab-delimited file containing additional portfolio information: id, name

[SecurityMaster](../feeds/pma_PortfolioMaster.md)

*Price.pma*

Tab-delimited file containing price information for different time points.

[PriceFeed](../feeds/pma_PriceFeed.md)

*Holdings.pma*

Tab-delimited file containing holdings information for portfolios over time.

[HoldingsFeed](../feeds/pma_HoldingsFeed.md)

*sample.pma*

File containing Vision code that loads the *.pma* files.

You can read the *sample.load* file into your favorite [Vision Editor](Editor.md) or you can execute the code in this file using the [asFileContents evaluate](Input/3.md) expression:

      "/localvision/samples/pma/sample.load" asFileContents evaluate ;

**Note:** The *sample.load* file runs by default on a *Unix* environment. If you are using a *Windows NT* platform, this location may be prefixed by a drive and optional path (e.g., *d:/visiondb/localvision/samples/pma/sample.load*). In additition, the *sample.load* file must be edited by your Vision Administrator to reflect the correct locations.

------------------------------------------------------------------------
