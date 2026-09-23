---
provenance: "docs/original/tuCase3.htm"
unit_type: "general"
title: "Case Study 3: Cross Tabular Reporting"
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

It is often useful to look at data at an aggregate level instead of looking at each specific record. Example 3 develops a cross-tabular report that aggregates a list using different criteria and displays summary information by aggregate.

------------------------------------------------------------------------

Read the file *example3.a*. You should see:

-  #---  Build a List that is extended by 2 quintile values 
       !quintileList <- testList 
          quintileUp: [ netIncome ] . 
          extendBy: [ !quintile1 <- quintile ] . 
          quintileUp: [ earningsPerShare ] . 
          extendBy: [ !quintile2 <- quintile ] ; 
       #---  Display Basic Report for this List 
       quintileList 
       do: [ ticker print: 10 ; 
             netIncome print: 10 ; 
             quintile1 print: 3 ; 
             earningsPerShare print: 10 ; 
             quintile2 print: 3 ; 
             sales print: 10 ; 
             newLine print ; 
           ] ; 

Execute this program. You should see:

- AET 920.60  2   7.48    5   22114.11
      T      2044.00  4   1.88    1   51209.02
      AN     1360.00  3   2.65    2   20174.00
      ARC    1224.00  2   6.68    4   16282.00
      CI  728.30  1   7.25    5   16909.30
      ...

The first step creates a list named *quintileList* which is extended by two variables: *quintile1* is the quintile (1-5) of the *netIncome* value and *quintile2* is the quintile (1-5) of the *earningsPerShare* value. A simple report showing actual data and these quintile values is then displayed for each company in the list.

------------------------------------------------------------------------

The next version of this report eliminates the company detail and just displays summary information. For each of the *netIncome* quintiles, the report displays the distribution of *earningsPerShare* quintiles. Read in the file *example3.b:*

-  #---  group by netIncome quintiles (quintile1) 
       quintileList groupedBy: [ quintile1 ] . 
          sortUp: [ ^self ] . 
       do: [            #--  for each net income quintile 
           "netIncome Quintile " print ; 
            ^self print: 3 ;                          #-- print the quintile1 number 
            newLine print ; 
            #---  group the current quintile1 companies by quintile2 
            groupList groupedBy: [ quintile2 ] . 
              sortUp: [ ^self ] . 
            do: [ "   earningsPerShare Quintile " print ; 
                  ^self print: 3 ;         #-- print quintile2 number 
                  " Includes: " print ; 
                  groupList count print: 5 ;   #-- print quintile2 count 
                  " Elements" printNL ; 
                ] ; 
            newLine print ; 
          ] ; 

Execute this program. You should see:

- netIncome Quintile   1
        earningsPerShare Quintile 1 Includes: 2 Elements
        earningsPerShare Quintile 3 Includes: 1 Elements
        earningsPerShare Quintile 5 Includes: 1 Elements
       
      netIncome Quintile   2
        earningsPerShare Quintile 2 Includes: 1 Elements
        earningsPerShare Quintile 3 Includes: 1 Elements
        earningsPerShare Quintile 4 Includes: 1 Elements
        earningsPerShare Quintile 5 Includes: 1 Elements

      netIncome Quintile   3
        earningsPerShare Quintile 2 Includes: 1 Elements
        earningsPerShare Quintile 3 Includes: 1 Elements
        earningsPerShare Quintile 4 Includes: 2 Elements

      netIncome Quintile   4
        earningsPerShare Quintile 1 Includes: 2 Elements
        earningsPerShare Quintile 2 Includes: 2 Elements

      netIncome Quintile   5
        earningsPerShare Quintile 3 Includes: 1 Elements
        earningsPerShare Quintile 4 Includes: 1 Elements
        earningsPerShare Quintile 5 Includes: 2 Elements

This report groups the original list by *quintile1*. In other words, 5 distinct groups are formed corresponding to the integers 1 through 5. The *groupList* message for each of these groups returns the list of companies in the current quintile group. For each of these *quintile1* groups, a label is displayed identifying the *netIncome* quintile number. The *groupList* is then grouped by *quintile2*. A summary line is then printed for each *earningsPerShare* quintile present in the current group.

This report displays the count for the different combination of quintile pairs that exist. For example, you can see that 2 companies have a *netIncome* quintile of 4 and an *earningsPerShare* quintile of 1. Only the combinations that exist are displayed in this report. For example, there is no summary line for *netIncome* quintile 1 and *earningsPerShare* quintile 2, implying that there are no companies with these characteristics.

The program in *example3.c* displays an entry for every combination:

-  quintileList groupedBy: [ quintile1 ] . 
          sortUp: [ ^self ] . 
       do: [ "netIncome Quintile " print ; 
             ^self print: 3 ; 
             newLine print ; 

             5 sequence    #---  For each number from 1 to 5 
             do: [ !q <- ^self ; 
                   "   earningsPerShare Quintile " print ; 
                   q print: 3 ; 
                   " Includes: " print ; 
                   ^my groupList  #-- select companies in this quintile 
                      select: [ quintile2 = ^my q ] . count print: 5 ; 
                   " Elements" printNL ; 
                 ] ; 
             newLine print ; 
           ] ; 

Execute this program. You should see:

    netIncome Quintile   1
       earningsPerShare Quintile    1 Includes: 2 Elements
       earningsPerShare Quintile    2 Includes: 0 Elements
       earningsPerShare Quintile    3 Includes: 1 Elements
       earningsPerShare Quintile    4 Includes: 0 Elements
       earningsPerShare Quintile    5 Includes: 1 Elements

    netIncome Quintile   2
       earningsPerShare Quintile    1 Includes: 0 Elements
       earningsPerShare Quintile    2 Includes: 1 Elements
       earningsPerShare Quintile    3 Includes: 1 Elements
