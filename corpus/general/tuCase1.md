---
provenance: "docs/original/tuCase1.htm"
unit_type: "general"
title: "Case Study 1: Single Company Reporting"
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

It is often useful to display many data items over time for a single company. Read the file *example1.a* You should see the following:

- Named Company GM 
      do: [ 
           !dr <- 90 to: 88 by: 1 yearEnds ;          #--create date range 
           " " print: 15 ;                            #--indent
           dr evaluate: [ ^date year print: 10 ; ] ;  #--display years 
           newLine print ; 

           "Sales" print: 15 ; 
           dr evaluate: [ sales print: 10 ] ; 
           newLine print ; 

           "EPS" print: 15 ; 
           dr evaluate: [ earningsPerShare print: 10 ]; 
           newLine print ; 

           "Price" print: 15 ; 
           dr evaluate: [ price print: 10 ] ; 
           newLine print ; 
          ] ;

Execute this program. You should see:

-                  1990         1989           1988
      Sales       101781.00    102813.00       96371.63
      EPS              5.03         4.11           6.14
      Price           32.12        32.12          32.12 

This program displays some basic financial data about GM for the years 1990, 1989, and 1988. Each line is introduced with a 15 character label. The specific data item is then printed for each year, one year per column.

------------------------------------------------------------------------

Suppose you want to enhance this report by adding a title and underlining the years. Read the file *example1.b*. You should see:

- Named Company GM 
      do: [ 
           !dr <- 90 to: 88 by: 1 yearEnds ;
           name centerNL: 45 . print;                  #-- center the name 
           "Financial Summary" centerNL: 45 . print;   #-- center report title 
           newLine print ; 

           " " print: 15 ; 
           dr evaluate: [ ^date year print: 10 ; ] ; 
           newLine print ; 
           " " print: 15 ; 
           dr evaluate: [ " " print ; "-" fill: 9 . print ] ; #-- underline 
           newLine print ; 

           "Sales" print: 15 ; 
           dr evaluate: [ sales print: 10 ] ; 
           newLine print ; 

           "EPS" print: 15 ; 
           dr evaluate: [ earningsPerShare print: 10 ] ; 
           newLine print ; 

           "Price" print: 15 ; 
           dr evaluate: [ price print: 10 ] ; 
           newLine print ; 
         ] ; 

Execute this program. You should see:

-          General Motors Corp 
                Financial Summary 

                 1990       1989       1988
             --------  ---------   -------- 
      Sales 101781.00  102813.00   96371.63 
      EPS        5.03       4.11       6.14 
      Price     32.12      32.12      32.12 

The report now contains a two-line title. The first line is the company name centered over 45 characters. The second line contains the title *Financial Summary*. The *fill: 9* message is used to create a string containing the "-" character 9 times. This is used to underline each year.

------------------------------------------------------------------------

Notice that the value for the price is the same in all years. Since the message *price* is defined as a fixed property in the sample database, its value is the same independent of the evaluation date. The value of price can therefore be made part of the report header. The next variation of this report makes this change and adds the preparation date to the header as well. The *price* data row is replaced by a row that computes the ratio of price to earnings. Read the file *example1.c.* You should see:

- Named Company GM 
      do: [ 
           !dr <- 90 to: 88 by: 1 yearEnds ; 
           name centerNL: 45 . print; 
           "Financial Summary" centerNL: 45 . print; 
           "Prepared:  " print ; 
           ^today formatUsingShortName print ;  #-- format today's date 
           " Latest Price: " print ;            #-- display string 
           price printNL ;                      #-- display price 
           newLine print ; 

           " " print: 15 ; 
           dr evaluate: [ ^date year print: 10 ; ] ; 
           newLine print ; 
           " " print: 15 ; 
           dr evaluate: [ " " print ;  "-" fill: 9 . print ] ; 
           newLine print ; 

           "Sales" print: 15 ; 
           dr evaluate: [ sales print: 10 ] ; 
           newLine print ; 

           "EPS" print: 15 ; 
           dr evaluate: [ earningsPerShare print: 10 ] ; 
           newLine print ; 

           "PE" print: 15 ; #-- PE is a calculation 
           dr evaluate: [ price / earningsPerShare print: 10 ] ; 
           newLine print ; 
         ] ; 

Execute this program. You should see:

-        General Motors Corp 
                      Financial Summary 
      Prepared: 12-Jan 1993 Latest Price: 32.12 

                    1990      1989      1988
               --------- --------- --------- 
      Sales    101781.00 102813.00  96371.63 
      EPS           5.03      4.11      6.14 
      PE            6.39      7.82      5.23 

The preparation date and the latest price now appear in the header. The third data line contains the price-earnings ratio. Notice that you were able to compute the price-earnings ratio in the *dr evaluate:* block. Blocks can contain any Vision program including single messages and complex multi-statement calculations.

------------------------------------------------------------------------

The next variation of this report converts this program to a *Company* method. This basically requires changing the *[do:](../messages/mList/do.md)* message to a *defineMethod:* message and naming the method. The contents of the program itself need not change. Read the file *example1.d*. You should see:

    Company defineMethod:      #-- this line is new 
    [ | financialAnalysis |    #-- name the method 
