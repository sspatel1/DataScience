
// Get a reference to the table body
var tbody = d3.select("tbody");


/******************************************************
 *                                                    *
 *              Normal Function Method                *
 *              =======================               *
 * Using UFO Dataset, append a table to the web page. *
 * Add new rows of data for each UFO sighting.        *
 *                                                    *
 * ****************************************************/
/*
 // Use d3 to update each cell's text with UFO values
 data.forEach(function(ufoReport) {
   
   var row = tbody.append("tr");
   Object.entries(ufoReport).forEach(function([key, value]) {
     //console.log(key, value);
     
     // Append a cell to the row for each value
     // in the weather report object
     var cell = row.append("td");
     cell.text(value);
   });
 });
*/



/******************************************************
 *                                                    *
 *              Arrow Function Method                 *
 *              =====================                 *
 * Using UFO Dataset, append a table to the web page. *
 * Add new rows of data for each UFO sighting.        *
 *                                                    *
 * ****************************************************/
// Use d3 to update each cell's text with UFO values
 data.forEach((ufoReport) => {
  var row = tbody.append("tr");
  Object.entries(ufoReport).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});



/****************************************************
 *                                                  *
 *                  OPTIONIONAL                     *
 *                  ===========                     *
 * Uisng multiple input tags, set multiple filters  *
 * and seach for UFO sighting using the following   *
 * criteria based on the table columns:             *
 *                                                  *
 * 1. date/time                                     *
 * 2. city                                          *
 * 3. state                                         *
 * 4. country                                       *
 * 5. shape                                         *
 *                                                  *
 ****************************************************/

// Select the submit button
var submit1 = d3.select("#filter-btn1");
var submit2 = d3.select("#filter-btn2");
var submit3 = d3.select("#filter-btn3");
var submit4 = d3.select("#filter-btn4");
var submit5 = d3.select("#filter-btn5");

// Event trigger from click on date button
submit1.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    var inputId = "#datetime";
    var cell = 0;
    filterRows(inputId, cell);

});

// Event trigger from click on city button
submit2.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    var inputId = "#city";
    var cell = 1;
    filterRows(inputId, cell);

});

// Event trigger from click on state button
submit3.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    var inputId = "#state";
    var cell = 2;
    filterRows(inputId, cell);

});

// Event trigger from click on country button
submit4.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    var inputId = "#country";
    var cell = 3;
    filterRows(inputId, cell);

});

// Event trigger from click on shape button
submit5.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    var inputId = "#shape";
    var cell = 4;
    filterRows(inputId, cell);

});


// Function to filter matching rows based on search criteria
// Keep the matching rows and delete the non-matching rows
function filterRows(inputId, cell) {

    // Select the input element and get the raw HTML node
    var inputElement = d3.select(inputId);
    
    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    console.log(inputValue);
    console.log(inputId);
  
    // Get a reference to table with (id = ufo-table)
    var table = document.getElementById("ufo-table");
    
    
    // Loop through all the rows in the table
    // For the row with matching data don't do any thing. Go to next row
    // For the row with non-matching data, delete the row
    length = table.rows.length;
    j = 1;
    for (var i = 1 ; i < length; i++) {

        // Read the data from row j
        result = table.rows[j].cells[cell].innerHTML;

        if(inputValue === result) {
            j = j + 1;
        } else {
            table.deleteRow(j);
        }
    }

}

