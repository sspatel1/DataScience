Attribute VB_Name = "Module1"
' Steps:
' ----------------------------------------------------------------------------

' Part Moderate:

' 1.  Loop through all the stocks and take the following info.
' 1a. Yearly change from what the stock opened the year at to what the closing price was.
' 1b. The percent change from the what it opened the year at to what it closed.
' 1c. The total Volume of the stock
' 1d. Ticker symbol

' 2. Use conditional formatting that will highlight positive change in green and negative change in red.



' Part Hard:

' 1. Locate the stock with the "Greatest % increase", "Greatest % Decrease", and "Greatest total volume"



Sub WallStreet()

Dim Ticker As String
Dim TotalStockVolume As Double
Dim TickerRow As Integer
Dim Flag As String
Dim CurrentTickerOpeningPrice As Double
Dim CurrentTickerClosingPrice As Double
Dim NextTickerOpeningPrice As Double
Dim YearlyChange As Double
Dim PercentChange As Double

Dim GreatestPercentIncreaseTicker As String
Dim GreatestPercentDecreaseTicker As String
Dim GreatestTotalVolumeTicker As String
Dim GreatestPercentIncreaseValue As Double
Dim GreatestPercentDecreaseValue As Double
Dim GreatestTotalVolumeValue As Double



    ' --------------------------------------------
    ' LOOP THROUGH ALL SHEETS
    ' --------------------------------------------
    For Each ws In Worksheets
   
        
        ' Determine the Last Row
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

        ' Add the word Ticker to Column 9 Header
        ws.Cells(1, 9).Value = "Ticker"
        
        ' Add the word Yearly Change to Column 10 Header
        ws.Cells(1, 10).Value = "Yearly Change"
        
        ' Add the word Percent Change to Column 11 Header
        ws.Cells(1, 11).Value = "Percent Change"
               
        ' Add the word Total Stock Volume to Column 12 Header
        ws.Cells(1, 12).Value = "Total Stock Volume"

        ' Add the word Ticker to Column 16 Header
        ws.Cells(1, 16).Value = "Ticker"
        
        ' Add the word Value to Column 17 Header
        ws.Cells(1, 17).Value = "Value"
        
        ' Add the word Greatest % Increase in Row 2, Column 15
        ws.Cells(2, 15).Value = "Greatest % Increase"
        
        ' Add the word Greatest % Decrease in Row 3, Column 15
        ws.Cells(3, 15).Value = "Greatest % Decrease"
        
        ' Add the word Greatest Total Volume in Row 4, Column 15
        ws.Cells(4, 15).Value = "Greatest Total Volume"
        
        
        ' Keep track of the location of row for each Ticker starting with Row 2
        TickerRow = 2
            
        ' Initialize Total Stock Volume
        TotalStockVolume = 0

        ' Before entering the loop store the Opening Price of first Ticker
        NextTickerOpeningPrice = ws.Cells(2, 3).Value
            
        ' Initialize values
        GreatestPercentIncreaseValue = 0
        GreatestPercentDecreaseValue = 0
        GreatestTotalVolumeValue = 0
        
        
        For i = 2 To LastRow

            ' Check if we are still within the same ticker, if it is not...
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
             
                ' Set the Ticker name
                Ticker = ws.Cells(i, 1).Value
                              
                ' Print the Ticker in column 9
                ws.Cells(TickerRow, 9).Value = Ticker
                
                ' Find out Yearly Change in stock price using Opening and Closing Stock Price.
                CurrentTickerOpeningPrice = NextTickerOpeningPrice
                CurrentTickerClosingPrice = ws.Cells(i, 6).Value
                YearlyChange = CurrentTickerClosingPrice - CurrentTickerOpeningPrice
            
                ' Print Yearly Change for a Ticker in Column 10
                ws.Cells(TickerRow, 10).Value = YearlyChange
                
                ' Conditionally highlight Percent Change cells with color
                ' +ve change as Green and -ve change as Red
                If YearlyChange >= 0 Then
                
                    ws.Cells(TickerRow, 10).Interior.ColorIndex = 4 ' Green color
                
                Else
                    
                    ws.Cells(TickerRow, 10).Interior.ColorIndex = 3 ' Red color
                
                End If
                
                
                ' Print Percent Change in Column 11.
                ' Use format cell method to dispaly percentage
                ' If Opening price is zero then don't calculate the percent change. mark it as NA
                If CurrentTickerOpeningPrice = 0 Then
                
                    ws.Cells(TickerRow, 11).Value = "NA"
                
                Else
                    PercentChange = YearlyChange / CurrentTickerOpeningPrice
                    ws.Cells(TickerRow, 11).Value = Format(PercentChange, "0.00%")
                                        
                End If
                        
                                   
                ' Add to the Total Stock Volume
                TotalStockVolume = TotalStockVolume + ws.Cells(i, 7).Value

                ' Print the total Stock Volume in column 12
                ws.Cells(TickerRow, 12).Value = TotalStockVolume
      
      
                ' --------------------------------------------
                ' HARD          HARD                HARD
                ' --------------------------------------------
                If PercentChange > GreatestPercentIncreaseValue Then
                
                    GreatestPercentIncreaseValue = PercentChange
                    GreatestPercentIncreaseTicker = ws.Cells(TickerRow, 9).Value
                    
                End If
                
              
                If PercentChange < GreatestPercentDecreaseValue Then
                
                   GreatestPercentDecreaseValue = PercentChange
                   GreatestPercentDecreaseTicker = ws.Cells(TickerRow, 9).Value
                
                End If
                
                
                If ws.Cells(TickerRow, 12).Value > GreatestTotalVolumeValue Then
                
                    GreatestTotalVolumeValue = ws.Cells(TickerRow, 12).Value
                    GreatestTotalVolumeTicker = ws.Cells(TickerRow, 9).Value
                
                End If
                               
            
                ' Initialize Total Stock Volume
                TotalStockVolume = 0
                
                ' Increment Row to print next Ticker
                TickerRow = TickerRow + 1
                
                ' Before continuing with next Ticker, read and store next Ticker opening price from row i+1
                NextTickerOpeningPrice = ws.Cells(i + 1, 3).Value
                
            Else
                
                ' Add to the Total Stock Volume
                TotalStockVolume = TotalStockVolume + ws.Cells(i, 7).Value
                             
                                        
            End If

        Next i ' FOR loop from start to end row in a given worksheet
   
                
        ' Print the Ticker and value of greatest Percent Increase, Greatest Percent Decrease and Greatest Total Volume
        ws.Cells(2, 16).Value = GreatestPercentIncreaseTicker
        ws.Cells(3, 16).Value = GreatestPercentDecreaseTicker
        ws.Cells(4, 16).Value = GreatestTotalVolumeTicker
        
        ws.Cells(2, 17).Value = Format(GreatestPercentIncreaseValue, "0.00%")
        ws.Cells(3, 17).Value = Format(GreatestPercentDecreaseValue, "0.00%")
        ws.Cells(4, 17).Value = GreatestTotalVolumeValue
        
             
        ' Make the width of columns to fit the contents
        ws.Columns("A:Q").AutoFit
        
    
    Next ws ' FOR loop for worksheets

    
MsgBox ("Complete")


End Sub

