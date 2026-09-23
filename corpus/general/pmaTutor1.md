---
provenance: "docs/original/pmaTutor1.htm"
unit_type: "general"
title: "PMA Tutorial 1: Basic Security and Account Access"
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

The first example displays a basic data item for a single Security. Read the file *example1.a*. You should see the following:

- Named Security IBM ticker print ;

Execute this program. You should see:

- IBM

The message *ticker* is a property of Security.

------------------------------------------------------------------------

This example displays two basic data items for a single Security. Read the file *example1.b*. You should see the following:

- Named Security IBM ticker print ;
      Named Security IBM price print ;

Execute this program. You should see:

- IBM   102.00

------------------------------------------------------------------------

The next example displays multiple data items in one statement for a single security. Read the file *example1.c* You should see the following:

- Named Security IBM
      do: [ 
            ticker print: 5 ; 
            name print: 30 ; 
            price print:10 ;
           ] ;

Execute this program. You should see:

- IBM  INTERNATIONAL BUSINESS MACH CO    102.00

The *do:* statement is used to streamline repetitive code. In this example, the *do:* statement is used to write three separate messages *name*, *ticker*, and *price* into one statement.

------------------------------------------------------------------------

In the previous examples the current date was used because one had not been supplied. However, it is possible to access data from any date. The following example displays the same data as the previous example but as of 12/10/97. Read the file *example1.d*. You should see:

- 971210 evaluate: 
        [
         Named Security IBM 
         do: [ 
              ticker print: 5 ; 
              name print: 30 ; 
              price print:10 ;
             ] ;
         ];

Execute this program. You should see:

- IBM  INTERNATIONAL BUSINESS MACH CO    106.50

The *evaluate:* message will access all data as of the date supplied. This date becomes the default date used for all operations contained inside the brackets.

------------------------------------------------------------------------

This example displays some additional data about IBM. Read the file *example1.e*. You should see:

-  Named Security IBM 
         do: [ 
              ticker print: 5 ; 
              company fiscalYearEnd print:-5 ;
          company industry sector print: 8 ; 
              price print:10 ;
             ] ;

Execute this program. You should see:

- IBM  12   TECH        102.00

One aspect of navigational flow in Vision is that messages are defined to return objects from other classes. An example of this is in the message *company fiscalYearEnd*, which displays the month in which a company has its fiscal year end. The message *company* at the class **Security** returns an instance of the **Company** class, which enables you to access the message *fiscalYearEnd* or any other message defined at the **Company** class, such as *industry* or *country*.

The example *company industry sector*, is a continuation of the navigational theme. The message *industry*, which is defined at **Company**, allows you to find the *sector* for the security IBM.

------------------------------------------------------------------------

This next program displays the same data, but for a list of Securities. Read the file *example1.f.* You should see:

- Security masterList
         first: 100 . 
         do: [ 
              ticker print: 10 ; 
              name print: 30 ; 
              price printNL:10;
             ] ;

Execute this program. You should see:

-        
      CashUS    CashUS                               NA 
      AOL       AMERICA ONLINE INC DEL COM         83.94
      GM        GENERAL MTRS CORP COM              64.38
      IBM       INTERNATIONAL BUSINESS MACH CO    102.00
      ...

The expression *Security masterList* is a list of all securities in the database. The message *first:100* limits the output to the first 100 in the database.

------------------------------------------------------------------------

This next example displays the same data for multiple Securities as of a different date. Read the file *example1.g.* You should see:

- 971210 evaluate:
      [
       Security masterList
         do: [ 
              ticker print: 5 ; 
              name print: 30 ; 
              price printNL:10;
             ] ;
      ];

Execute this program. You should see:

-        
      CashUCashUS                               NA 
      AOL  AMERICA ONLINE INC DEL COM         85.00
      GM   GENERAL MTRS CORP COM              64.38
      IBM  INTERNATIONAL BUSINESS MACH CO    106.50
      ...

------------------------------------------------------------------------

The next example displays securities with a price over \$50. Read the file *example1.h.* You should see:

- Security masterList 
      select:[ price > 50 ] .
      sortUp: [ name ] .
      do: [ 
            code print:15 ; 
            name print:30 ;
            price printNL:10 ;
          ];

Execute this program. You should see:

- 02364J10       AMERICA ONLINE INC DEL COM         83.94
      37044210       GENERAL MTRS CORP COM              64.38
      45920010       INTERNATIONAL BUSINESS MACH CO    102.00
      275438         ROYAL BK CDA MONTREAL QUE COM      53.50

The *select:* message eliminates all data that does not meet the criteria inside its brackets. The *sortUp:* message sorts the information in ascending order by a chosen message. In this case, it is sorted by the name.

------------------------------------------------------------------------

The next example displays securities with a price over \$50 as of a different date. Read the file *example1.i.* You should see:

- 971210 evaluate:
      [
      Security masterList 
      select:[ price > 50 ] .
      sortUp: [ name ] .
      do: [ 
            code print:15; 
            name print:30;
            price printNL:10;
          ];
      ];

Execute this program. You should see:

    02364J10       AMERICA ONLINE INC DEL COM         85.00
    37044210       GENERAL MTRS CORP COM              64.38
