---
provenance: "docs/original/pma_PeGroups.htm"
unit_type: "feed"
title: "Vision Upload Format: PeGroups"
ingested: "2026-09-22"
entity: "PeGroup"
fields: [{"name": "startValue", "property": "lowerBound", "type": "Number", "desc": "minimum value in range"}, {"name": "endValue", "property": "upperBound", "type": "Number", "desc": "maximum value in range"}, {"name": "label", "property": "name", "type": "-", "desc": "label that describes range"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](../general/pmaFeeds.md) \|

------------------------------------------------------------------------

**Data Feed:** *PeGroups*

**Category:** *RangeGroupFeed*

## Summary:

- The *PeGroups* feed is used to define and update **PEGroup** ranges and to classify **Security** instances into ranges based on a security's current *priceToEarnings* value using the *peCurr* method defined at **Security**. The security property *peGroup* stores the current range value. The **RangeClassification** class is described in more detail in the [*Portfolio Management Application Classes*](pmaSupp.htm#RangeClass) document.

## Available Fields:

|          Field          | PeGroup Property |  Type  |        Description         |
|:-----------------------:|:----------------:|:------:|:--------------------------:|
| --- Required Fields --- |                  |        |                            |
|       startValue        |    lowerBound    | Number |   minimum value in range   |
|        endValue         |    upperBound    | Number |   maximum value in range   |
|          label          |       name       |   \-   | label that describes range |

## Special Processing Rules:

- This feed replaces all existing instances of the **PEGroup** classes with the instances defined by this feed.
- Using the ranges defined by this feed, the **Security** property *peCurr* is used to determine an **PEGroup** classification which is used to update the *peGroup* property at the security.
- Use the value *NA* to indicate a range is unbounded for its start or end point. Ranges are assumed to be contiguous.

<span id="related"></span>

## Related Feeds:

- [*FundamentalM*](pma-FundamentalM.md): updates monthly earnings
- [*PriceFeed*](pma-PriceFeed.md): updates prices

## Sample Upload:

The following tab-delimited feed could be used to define and update price-to-earnings groups. The fields must be supplied in this order. The header line should be included, but the header values are ignored:

         Interface ExternalFeedManager upload: "PeGroups" using:
           "startValue     endValue   label
            NA             1          less than 1
            1              5          1 to 5
            5             10          5 to 10
            10            20          10 to 20
            20            NA          more than 20
          " ;

{% include doc-footer.htm copydates="1998" %}
