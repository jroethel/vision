---
provenance: "docs/original/pma_McapGroups.htm"
unit_type: "feed"
title: "Vision Upload Format: McapGroups"
ingested: "2026-09-22"
entity: "MCapGroup"
fields: [{"name": "startValue", "property": "lowerBound", "type": "Number", "desc": "minimum value in range"}, {"name": "endValue", "property": "upperBound", "type": "Number", "desc": "maximum value in range"}, {"name": "label", "property": "name", "type": "-", "desc": "label that describes range"}]
---

## Vision Portfolio Management Application Layer: Data Feeds

\| [Application Feeds](pmaFeeds.htm) \|

------------------------------------------------------------------------

**Data Feed:** *McapGroups*

**Category:** *RangeGroupFeed*

## Summary:

- The *McapGroups* feed is used to define and update **MCapGroup** ranges and to classify **Security** instances into ranges based on a security's *latestMarketCapUS* value. The security property *marketCapGroup* stores the current range value. The **RangeClassification** class is described in more detail in the [*Portfolio Management Application Classes*](pmaSupp.htm#RangeClass) document.

## Available Fields:

| Field | MCapGroup Property | Type | Description |
|:--:|:--:|:--:|:--:|
| --- Required Fields --- |  |  |  |
| startValue | lowerBound | Number | minimum value in range |
| endValue | upperBound | Number | maximum value in range |
| label | name | \- | label that describes range |

## Special Processing Rules:

- This feed replaces all existing instances of the **MCapGroup** classes with the instances defined by this feed.
- Using the ranges defined by this feed, the **Security** property *latestMarketCapUS* is used to determine an **MCapGroup** classification which is used to update the *marketCapGroup* property at the security.
- Use the value *NA* to indicate a range is unbounded for its start or end point. Ranges are assumed to be contiguous.

<span id="related"></span>

## Related Feeds:

- [*SecurityMaster*](pma_SecurityMaster.md): defines Security instances and updates *latestMarketCapUS* property

## Sample Upload:

The following tab-delimited feed could be used to define and update market capitalization groups. The fields must be supplied in this order. The header line should be included, but the header values are ignored:

         Interface ExternalFeedManager upload: "McapGroups" using:
           "startValue     endValue     label
            NA             250          less than $250M
            250            500          $250M - $500
            500            1000         $500M - $1B
            1000           2500         $1B - $2.5B
            2500           5000         $2.5B - $5B
            5000           10000        $5B - $10B
            10000          NA           greater than $10B
          " ;

{% include doc-footer.htm copydates="1998" %}
