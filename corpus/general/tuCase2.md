---
provenance: "docs/original/tuCase2.htm"
unit_type: "general"
title: "Case Study 2: Basic Tabular Reporting"
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
> Any other files referenced can be read from the */localvision/samples/general/* directory.
>
> **Note:** The *sample.load* file runs by default on a *Unix* environment. If you are using a *Windows NT* platform, this location may be prefixed by a drive and optional path (e.g. *d:/visiondb/localvision/samples/general/sample.load*). Check with your Vision Administrator for further details.
>
> ------------------------------------------------------------------------

It is often useful to display many data items for a list of entities. Read the file *example2.a* you should see:

     !testList <- Company masterList 
        rankDown: [ sales ] . 
        select: [ rank <= 20 ] ; 

Execute this program. This variable *testList* will now contain the list of top 20 companies by sales.

------------------------------------------------------------------------

The file *example2.b* displays sample data for each company in this list:

-  "***  Multiple Company Data Sheet  ***" centerNL: 70 . print; 
       newLine print ; 

       "Ticker" print: 10 ; 
       "Name" print: 30 ; 
       "Industry" print: 10 ; 
       "Sales" print: -10 ; 
       "P-E" print: -8 ; 
       newLine print ; 
       "-" fill: 70 . printNL ; 

       testList 
       do: [ 
           ticker print: 10 ; 
           name print: 30 ; 
           industry code print: 10 ; 
           sales print: 10 ; 
           price / earningsPerShare print: 8 ; 
           newLine print ; 
           ] ; 

Execute this program. You should see:

-              ***  Multiple Company Data Sheet  ***

      Ticker  Name                    Industry   Sales      P-E

      AET     Aetna Life & Cas        INSUR      22114.11    5.46
      T       American Tel & Tel      TEL        51209.02   23.20
      AN      Amoco Corp              OIL        20174.00   19.91
      ARC     Atlantic Richfield      OIL        16282.00   18.15
      CI      CIGNA Corp              INSUR      16909.30    6.90
      ...

The first line of the program centers a title over the report. The next lines display column headings. Notice that the print format uses negative values for columns that contain numbers so that the heading is right-justified in these columns. Five data items including the computed price-earnings ratio are then displayed for each company.

------------------------------------------------------------------------

The file *example2.c* groups the companies into industries and displays the industry code and name followed by the companies in the industry for each industry present in the list:

-  "***  Multiple Company Data Sheet  ***" centerNL: 70 . print; 
       newLine print ; 
       "Ticker" print: 10 ; 
       "Name" print: 30 ; 
       "Industry" print: 10 ; 
       "Sales" print: -10 ; 
       "P-E" print: -8 ; 
       newLine print ; 
       "-" fill: 70 . printNL ; 

       testList groupedBy: [ industry ] .  #-- group into industry 
       do: [ code print: 10 ;              #-- industry code 
             name print: 30 ;              #-- industry name 
             newLine print ; 
             groupList                     #-- company list 
                  do: [ ticker print: 10 ; 
                        name print: 30 ; 
                        industry code print: 10 ; 
                        sales print: 10 ; 
                        price / earningsPerShare print: 8 ; 
                        newLine print ; 
                 ] ; 
             newLine print ;                #-- skip line between industries 
            ] ; 

Execute this program. You should see:

-                ***  Multiple Company Data Sheet  ***

      Ticker  Name                      Industry     Sales     P-E

      FBT     Food, Beverage, Tobacco
      MO      Philip Morris Cos         FBT       22279.00   43.69

      HH      Household Products
      PG      Procter & Gamble Co       HH        17000.00  105.05

      AUTO    Automotive
      C       Chrysler Corp             AUTO      26276.51    3.92
      F       Ford Motor Company        AUTO      71643.38    4.36
      GM      General Motors Corp       AUTO      10178.00    6.39

      RETAIL  Retail Store
      KM      K Mart Corp               RETAIL    24046.00   17.96
      S       Sears Roebuck & Co        RETAIL    48439.61   10.29
      ...

This report displays the code and name for each industry followed by a carriage return. The *groupList* message returns the list of companies in the original list that are in the current industry. The *ticker*, *name*, *industry code*, *sales*, and *price-earnings ratio* for each company in the industry are then displayed. Notice that the industry code is the same for all companies in a given industry group. An extra line is skipped between industries.

------------------------------------------------------------------------

The next variation of this report includes summary information for each industry. The total industry sales is defined as the sum of the sales for each company in the industry. The industry price-earnings ratio is defined as the average ratio for the companies in the industry. The file *example2.d* includes the summary information:

-  "***  Multiple Company Data Sheet  ***" centerNL: 70 . print; 
       newLine print ; 
       "Ticker" print: 10 ; 
       "Name" print: 30 ; 
       "Industry" print: 10 ; 
       "Sales" print: -10 ; 
       "P-E" print: -8 ; 
       newLine print ; 
       "-" fill: 70 . printNL ; 

       testList groupedBy: [ industry ] . 
       do: [ code print: 10 ; 
             name print: 30 ; 
             " " print: 10 ; 
             groupList total: [ sales ] . print: 10 ;    #-- total sales 
             groupList                                   #-- average pe 
                 average: [ price / earningsPerShare ] . print: 8 ; 
             newLine print ; 
             groupList 
             do: [ ticker print: 10 ; 
                   name print: 30 ; 
                   industry code print: 10 ; 
                   sales print: 10 ; 
                   price / earningsPerShare print: 8 ; 
                   newLine print ; 
                 ] ; 
             newLine print ; 
           ] ; 

Execute this program. You should see:

                   ***  Multiple Company Data Sheet  ***

    Ticker  Name                 Industry   Sales          P-E

    FBT     Food, Beverage, Tobacco         22279.00       43.69
    MO      Philip Morris Cos       FBT     22279.00       43.69

    HH      Household Products              17000.00      105.05
    PG      Procter & Gamble Co     HH      17000.00      105.05

    AUTO    Automotive                     221376.67        4.89
