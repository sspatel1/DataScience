# The VBA of Wall Street

## Background

Use VBA scripting to analyze real stock market data.

### Files

* [Test Data](Resources/alphabtical_testing.xlsx) - Use this Test Data to test the scripts.

* [Stock Data](Resources/Multiple_year_stock_data.xlsx) - Run your scripts on this data to generate the final report.

### Stock market analyst

![stock Market](Images/stockmarket.jpg)

### Part 1

* Create a script that will loop through one year of stock data for each run and return the total volume each stock had over that year.

* Display the ticker symbol to coincide with the total stock volume.

* Result should look as follows (note: all solution images are for 2015 data).

![easy_solution](Images/easy_solution.png)

### Part 2

* Create a script that will loop through all the stocks for one year for each run and take the following information.

  * The ticker symbol.

  * Yearly change from opening price at the beginning of a given year to the closing price at the end of that year.

  * The percent change from opening price at the beginning of a given year to the closing price at the end of that year.

  * The total stock volume of the stock.

* Also use conditional formatting that will highlight positive change in green and negative change in red.

* The result should look as follows.

![moderate_solution](Images/moderate_solution.png)

### Part 3

* Solution will be able to return the stock with the "Greatest % increase", "Greatest % Decrease" and "Greatest total volume".

* Solution will look as follows.

![hard_solution](Images/hard_solution.png)

### Part 4

* Make the appropriate adjustments to the script that will allow it to run on every worksheet, i.e., every year, just by running it once.

### Other Considerations

* Use the sheet `alphabetical_testing.xlsx` while developing the code. This data set is smaller and will test faster. Code should run on this file in less than 3-5 minutes.

* Make sure that the script acts the same on each sheet. The joy of VBA is to take the tediousness out of repetitive task and run over and over again with a click of the button.

- - -

### Copyright

Coding Boot Camp © 2019. All Rights Reserved.