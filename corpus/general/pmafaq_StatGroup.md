---
provenance: "docs/original/pmafaq_StatGroup.htm"
unit_type: "general"
title: "Vision Portfolio Management FAQ: Customizing the Account Characteristic Application"
ingested: "2026-09-22"
---

#### Goal

- To change the statistics displayed in the Account Characteristics report.

#### Description:

- A feed has been defined which allows you to name data items and indicate the types of summary statistics associated with each item. For example, you may want to define a data item named "mcap" which accesses the information following the navigation "funDataM marketCap" from Company. For any data item, you can indicate whether you want total, average, weighted average, and median to be displayed. Once you have defined your data items, you can use the [UniverseMaster](../feeds/pma_UniverseMaster.md) and [UniverseMembers](../feeds/pma_UniverseMembers.md) feeds to define subsets of these items to display as a unit.

  A number of data items have been pre-defined and are displayed on the characteristic report by default:

  - DataItem     BaseClass     AccessPath
        mcapUS       Security      marketCapUS 
        pe           Security      pe
        pb           Security      priceToBook

  The *DataItem* column identifies the statistic. The *BaseClass* column indicates the entity class from which the navigation to the data begins. The *AccessPath* column contains the message or navigation expression needed to actually access the data relative to the base class.

#### DataFeed Assumptions:

DataFeed

Fields

[McapGroups](../feeds/pma_McapGroups.md)

*startValue, endValue, label*

DataItemFeed

*id, shortName, baseClass, accessPath, isStat, showTot, showAvg, showWtAvg, showMed*

[UniverseMaster](../feeds/pma_UniverseMaster.md)

*id, name, memberType*

[UniverseMembers](../feeds/pma_UniverseMembers.md)

*groupId, memberId*

#### Topic 1: Defining Statistics

1.  Use the **DataItemFeed** to create new items and update display options.
    1.  Set up the spreadsheet to look like the following. Note that the feed name *DataItemFeed* is in the top left of the range.
        - DataItemFeed

              id     shortName  baseClass  accessPath     isStat  showTot showAvg showWtAvg showMed

              sales  Sales      Company    funDataA sales   T     T       T       F         F
              qsales Qtr Sales  Company    funDataQ sales   T     T       F       F         F

    2.  Select the entire range.

    3.  Select *Upload Data* from the *VUpload* menu.

    4.  Select the *Range* button.

        The *shortName* field is used as the label for the statistic in the characteristic report. The *isStat* field should be set to **True (T)** to include the item as a statistic in the report. The last columns can be set to **True (or T or Yes or Y)** or **False (or F or No or N)** to indicate whether the total, average, weighted average, and/or median should be computed for the item. If weighted average is selected, the statistic is weighted by each holding's percent of portfolio.

        This feed can also include the *sortCode* field which can be used to control the order in which the statistics appear in the report. The *defaultDecimals* field can be used to control the number of decimal points displayed for a statistic.
2.  Check the results.
    1.  

    2.  Open the Vision Reporter in your web browser.

    3.  Select *Account Reports*.

    4.  Select *AccountCharacteristics*.

    5.  Enter an account and run the report.

        The values for *Qtr Sales-Total*, *Sales-Total*, and *Sales-Avg* should now appear as part of report.

------------------------------------------------------------------------

#### Topic 2: Creating Sets of Characteristics

1.  Define the **Stat Group**, **SalesChars** by using the [*UniverseMaster*](../feeds/pma_UniverseMaster.md) feed.
    1.  Set up the spreadsheet to look like the following. Note that the feed name *UniverseMaster* is in the top left of the range.
        - UniverseMaster
              id          name                     memberType
              SalesChars  Sales Characteristics    DataItem

    2.  Select the entire range.

    3.  Select *Upload Data* from the *VUpload* menu.

    4.  Select the *Range* button.

        *SalesChars* has been created.
2.  Define the members of the **SalesChars** group by using the [*UniverseMembers*](../feeds/pma_UniverseMembers.md) feed:
    1.  Set up the spreadsheet to look like the following. Note that the feed name *UniverseMembers* is in the top left of the range.
        - UniverseMembers

              groupId            memberId
              SalesChars         sales
              SalesChars         qsales

    2.  Select the entire range.

    3.  Select *Upload Data* from the *VUpload* menu.

    4.  Select the *Range* button.

        The *SalesChars* members have been defined.
3.  Check the results.
    1.  

    2.  Open the Vision Reporter in your web browser.

    3.  Select *Account Reports*.

    4.  Select *AccountCharacteristics*.

    5.  Enter an account and run the report.

        *SalesChars* should now appear in the *Stat Group* menu at the bottom of report. If you choose this one, the report should only include these two statistics.

{% include doc-footer.htm copydates="1999" %}
