---
provenance: "docs/original/invSecurity.htm#Overview"
unit_type: "general"
title: "The Company And Security Classes"
ingested: "2026-09-22"
---

## Overview

The instances of the class Company represent the individual corporate entities for which you track information. Information maintained for a company typically includes sales, earnings estimates, and ratings. A large amount of raw data about companies is available in external databases. In Vision, the data provided by each external company database is viewed as a property of the company. In other words, the company *Nestles* is a Vision object whose properties could include *IbesData* and *WorldScopeData* in addition to *name*, *industry*, and *earnings*.

The instances of the class Security represent the individual securities issued by a corporation, government, or some other entity. A variety of security types exist including common and preferred stocks, convertible and non-convertible bonds, cash, and put and call options. Data maintained for a security typically includes price, dividend and shares outstanding information. Portfolios hold specific amounts of one or more individual securities. Some external databases provide information about specific securities. The security *Nestles Common Stock* is a Vision object whose properties could include *MSCIData* in addition to *name*, *price*, and *sharesOut*.

The security *Nestles Common Stock* is a Vision object whose properties include pricing, dividend, and split information. This object is distinct from the company *Nestles* whose properties include sales, earnings, and industry information. Although Company and Security are distinct classes in the Vision hierarchy, there is obviously a close relationship between related instances of the two classes since each security is issued by a unique company (or other issuer).

When you refer to the price earnings ratio for a security, you are really asking for the current price of the security divided by the earnings per share for the corporate entity that issued the security. The property *company* is defined at Security to return the value of the company associated with the security. The actual object representing the company is returned. For example, the Vision expression:

        Named Security GM company

returns the object representing the company GM and the expression:

        Named Security GM company = Named Company GM 

yields the result TRUE. Note that several securities may have the same value for company since more than one security can be issued by a single Company entity. By default, the value of *company* for a security is the default company instance. Automated and manual rules can be used to link a security to its "real" company instance.

When you refer to the price earnings ratio for a company, you are really asking for the current price of the company's primary security divided by the earnings per share for the company. The property *primarySecurity* is defined at Company to return the value of the security defined as the primary security for the company. The actual object representing the security is returned. For example, the Vision expression:

        Named Company GM primarySecurity 

returns the object representing GM's common stock security and the expression:

        Named Company GM primarySecurity = Named Security GM

yields the result TRUE. Note that only one security can be assigned as the *primarySecurity* for a Company. By default, the value of *primarySecurity* for a company is the default security instance. Automated and manual rules can be used to link a company to its *real* primary security instance.

------------------------------------------------------------------------
