---
provenance: "docs/original/pmaTutor3.htm"
unit_type: "general"
title: "PMA Tutorial 3: Basic Report Methods"
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

In order to best understand basic report methods, it is important to take a look at an example from PMA Tutorial 2, which is below as *example3.a*. There you defined an example that displays holdings data with headings, sorted by percentage of portfolio. If you read *example3.a* you should see:

- "Code" print:10 ;
      "Name" print:37 ;
      "Shares" print:12 ;
      "Total Mkt Val" print:15 ;
      "% of Port" printNL ;
      newLine print ;

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

Since you have seen this example before you do not need to execute it.

------------------------------------------------------------------------

A Method provides a way to define a program that can be run without recalling the entire original code each time. *Example3.b* defines a method that will produce the same results as *example3.a*. In this example the method is named *firstReport*. Read the file *example3.b*. You should see:

- Account defineMethod: 
          [ | firstReport | 
      "Code" print:10 ;
      "Name" print:35 ;
      "Shares" print:12 ;
      "Total Mkt Val" print:15 ;
      "% of Port" printNL ;
      newLine print ;

      holdings
      sortDown:[percentOfPort] .  # sort largest to smallest
      do:
         [
          security code print:10 ;
          security name print:35 ;
          shares print:10 ;
          totalMarketValue printWithCommas:15 ;
          percentOfPort printNL ;
         ];
      ];

Methods are defined for a specific class. In this case, the method is defined for the class Account. This means that the method can be run for any instance of an Account subclass. Vertical bars (\|\|) are needed in order to define the method name.

When you execute this program the output buffer should be blank because the code is defining, not running, the method.

------------------------------------------------------------------------

The next example runs the method *firstReport* for the *Account 102*. Read the file *example3.c.* You should see:

- Named Account \102 firstReport

Execute this program. You should see:

- Code      Name                               Shares      Total Mkt Val  % of Port

      24702510  DELL COMPUTER CORP COM                8600.00     717,566.80    15.41
      02364J10  AMERICA ONLINE INC DEL COM            8200.00     695,975.00    14.95
      00949T10  AIRTOUCH COMMUNICATNS COM            15200.00     589,000.00    12.65
      ...

The expression *Named Account \102* *firstReport* runs the method for the *Account 102*. This example shows that using a method produces the same output as using original code.

------------------------------------------------------------------------

The next example runs the method *firstReport* for a different Account. Read the file *example3.d.* You should see:

- Named Account \232 firstReport

Execute this program. You should see:

- Code      Name                               Shares      Total Mkt Val  % of Port

      40410010  HBO & CO COM                         12000.00     519,756.00     7.15
      24702510  DELL COMPUTER CORP COM                5900.00     492,284.20     6.77
      40169810  GUIDANT CORP COM                      8000.00     480,000.00     6.60
      ...

Although the values are different, the basic report is the same because you are using the same method.

------------------------------------------------------------------------

The next example alters the method *firstReport*, by centering the account identifier at the top of the report. This will make it easier to distinguish which account was used. Read the file *example3.e.* You should see:

- Account defineMethod: 
          [ | firstReport | 

      "Account: " concat: code . center:80 . printNL;  # center account 
      newLine print ;

      "Code" print:10 ;
      "Name" print:35 ;
      "Shares" print:12 ;
      "Total Mkt Val" print:15 ;
      "% of Port" printNL ;
      newLine print ;

      holdings
      sortDown:[percentOfPort] .  # sorted in descending order
      do:
         [
          security code print:10 ;
          security name print:35 ;
          shares print:10 ;
          totalMarketValue printWithCommas:15 ;
          percentOfPort printNL ;
         ];
      ];

The *concat:* statement appends the value of the message *code* for the current Account to the string *"Account: "*. The message *center:* centers the string and the *printNL* displays the result.

Execute this program. You should see a blank output buffer.

------------------------------------------------------------------------

The next example runs the new version of the method *firstReport* for the *Account 102*, this time with the Account identifier centered at the top of the report. Read the file *example3.f.* You should see:

- Named Account \102 firstReport

Execute the program. You should see:

-                                   Account: 102                                  

      Code      Name                               Shares      Total Mkt Val  % of Port

      24702510  DELL COMPUTER CORP COM                8600.00     717,566.80    15.41
      02364J10  AMERICA ONLINE INC DEL COM            8200.00     695,975.00    14.95
      00949T10  AIRTOUCH COMMUNICATNS COM            15200.00     589,000.00    12.65
      ...

------------------------------------------------------------------------

The next example runs the method *firstReport* for the *Account 232*. Read the file *example3.g*. You should see:

- Named Account \232 firstReport

Execute the program. You should see:

                                      Account: 232                                  

    Code      Name                               Shares      Total Mkt Val  % of Port

    40410010  HBO & CO COM                         12000.00     519,756.00     7.15
    24702510  DELL COMPUTER CORP COM                5900.00     492,284.20     6.77
    40169810  GUIDANT CORP COM                      8000.00     480,000.00     6.60
    ...
