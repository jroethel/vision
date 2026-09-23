---
provenance: "docs/original/pmaTutor2.htm"
unit_type: "general"
title: "PMA Tutorial 2: Account and Holding Access"
ingested: "2026-09-22"
---

> 
>
> ------------------------------------------------------------------------
>
> **Reminder!**
>
> To run these examples, you should first start a new session then load the sample database using:
>
>         "/localvision/samples/pma/sample.load" asFileContents evaluate ; 
>
> Any other files referenced can be read from the */localvision/samples/pma* directory.
>
> **Note:** The *sample.load* file runs by default on a *Unix* environment. If you are using a *Windows NT* platform, this location may be prefixed by a drive and optional path (e.g. *d:/visiondb/localvision/samples/pma/sample.load*). Check with your Vision Administrator for further details.
>
> ------------------------------------------------------------------------

------------------------------------------------------------------------

The following example displays the basic holdings data for an Account. Read the file *example2.a.* You should see:

- Named Account \102 holdings
      do:
         [
          security code print:10 ;
          security name print:30 ;
          shares print:10 ;
          totalMarketValue printWithCommas:15 ;
          percentOfPort printNL ;
         ];

Execute this program. You should see:

-        
      02364J10  AMERICA ONLINE INC DEL COM       8200.00     695,975.00    14.95
      37044210  GENERAL MTRS CORP COM            7800.00     497,741.40    10.69
      00949T10  AIRTOUCH COMMUNICATNS COM       15200.00     589,000.00    12.65
      ...

The message *holdings* is a list that contains the individual securities held within the specific account. The message *shares*, *totalMarketValue*, and *percentOfPort* directly access data for each individual holding. The message *security* navigates to specific security level messages like *name* and *code*.

------------------------------------------------------------------------

The next example displays holdings data with headings, sorted by percentage of portfolio. Read the file *example2.b.* You should see:

- # Add headers 
      "Code" print:10 ;
      "Name" print:35 ;
      "Shares" print:12 ;
      "Total Mkt Val" print:15 ;
      "% of Port" printNL ;
      newLine print ;

      Named Account \102 holdings
      sortDown:[percentOfPort] .  # sorted in descending order 
      do:
         [
          security code print:10 ;
          security name print:35 ;
          shares print:10 ;
          totalMarketValue printWithCommas:15 ;
          percentOfPort printNL ;
         ];

Execute this program. You should see:

- Code      Name                               Shares      Total Mkt Val  % of Port

      24702510  DELL COMPUTER CORP COM                8600.00     717,566.80    15.41
      02364J10  AMERICA ONLINE INC DEL COM            8200.00     695,975.00    14.95
      00949T10  AIRTOUCH COMMUNICATNS COM            15200.00     589,000.00    12.65
      ...

This example expands on the previous example by adding column headings and sorting the holdings. The message *sortDown* displays the holdings in descending order. The data can also be displayed in ascending order by using the message *sortUp*.

------------------------------------------------------------------------

The next example displays holdings data with headings, sorted by percentage of portfolio from a different date. Read the file *example2.c.* You should see:

- "Code" print:10 ;
      "Name" print:37 ;
      "Shares" print:12 ;
      "Total Mkt Val" print:15 ;
      "% of Port" printNL ;
      newLine print ;

      971105 evaluate:  # access the data as of this date
      [
      Named Account \102 holdings
      sortDown:[percentOfPort] .
      do:
         [
          security code print:10 ;
          security name print:35 ;
          shares printWithCommas:10 ;
          totalMarketValue printWithCommas:15 ;
          percentOfPort printNL ;
         ];
      ];

Execute this program. You should see:

- Code      Name                                 Shares      Total Mkt Val  % of Port

      40410010  HBO & CO COM                        19,600.00     852,600.00     9.61
      37935240  GLOBAL MARINE INC COM               25,400.00     790,575.00     8.91
      24702510  DELL COMPUTER CORP COM               8,600.00     689,075.00     7.77
      ...

By surrounding the request with a changed date, you are able to display the same report but with different data. The *evaluate:* message will access the data as of the date supplied. This date becomes the default date used for all operations inside the brackets.

------------------------------------------------------------------------

This example displays sectors for each holding. Read the file *example2.d*. You should see:

- "Code" print:10 ;
      "Name" print:37 ;
      "Shares" print:12 ;
      "Total Mkt Val" print:15 ;
      "% of Port" print:10 ;
      "Sector" printNL:-10 ;

      newLine print;

      Named Account \102 holdings
      sortDown:[percentOfPort] .
      do:
         [
          security code print:10 ;
          security name print:35 ;
          shares printWithCommas:10 ;
          totalMarketValue printWithCommas:15 ;
          percentOfPort print:10 ;
          security company industry sector name printNL:-35 ;  #Navigate to sector
         ];

Execute this program. You should see:

- Code      Name                                 Shares      Total Mkt Val  % of Port     Sector

      24702510  DELL COMPUTER CORP COM               8,600.00     717,566.80     15.41                         Technology
      02364J10  AMERICA ONLINE INC DEL COM           8,200.00     695,975.00     14.95                  Consumer services
      00949T10  AIRTOUCH COMMUNICATNS COM           15,200.00     589,000.00     12.65     Commercial/industrial services
      ...

One aspect of navigational flow in Vision is that messages are defined to return objects from other classes. The example *security company industry sector name*, is a continuation of the navigational theme. The message *company* at the class **Security**, returns an instance of the **Company** class. The message *industry* at the class **Company**, returns an instance of the **Industry** class. The message *sector* at the class Industry returns an instance of the **Sector** class. The full expression *security company industry sector name* navigates from the specific holding to its sector and accesses the sector's name.

------------------------------------------------------------------------

This example displays holdings grouped into sectors. Read the file *example2.e.* You should see:

    Named Account \102 holdings
    groupedBy:[security company industry sector] .  # group into sectors
    sortUp:[name] . # sort by sector name
    do:
       [
        code print:10 ;      # sector code
        name printNL:35 ;    # sector name
        groupList           # for each holding in sector
        do:
           [
            security code print:10 ;
            security name print:30 ;
            shares print:10 ;
