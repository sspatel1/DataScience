function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`
    var selector = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    selector.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    d3.json(`/metadata/${sample}`).then((sample) => {
         
      Object.entries(sample).forEach(([key, value]) => {
        // console.log(`${key}: ${value}`);
        selector
          .append("h5")
          .text(`${key}: ${value}`);
      });

    });


    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  // sampleData = d3.json(`/samples/${sample}`);
  d3.json(`/samples/${sample}`).then((sample) => {
        
    // Create Array of all the three key values 
    var otu_ids = sample.otu_ids;
    var sample_values = sample.sample_values;
    var otu_labels = sample.otu_labels;
        
    // Create array of Objects (one Object for each sample) 
    var sampleArray = [];
    for (var i=0; i < otu_ids.length; i++) {
      dictTemp = {};

      dictTemp["otu_ids"] = otu_ids[i];
      dictTemp["sample_values"] = sample_values[i];
      dictTemp["otu_labels"] = otu_labels[i];

      sampleArray[i] = dictTemp;

    };  
    
    // Sorts descending
    sampleArray.sort(function compareFunction(firstNum, secondNum) {
      return secondNum.sample_values - firstNum.sample_values;
    });


    // Slice top 10 by sample_value to be used for Pie Chart
    sampleArrayTen = sampleArray.slice(0, 10);
    

    
    /********************************************************
     *                                                      *
     *                  PIE CHART                           *
     *                                                      *
     ********************************************************/
    var trace1 = {
      values: sampleArrayTen.map(row => row.sample_values),
      labels: sampleArrayTen.map(row => row.otu_ids),
      type: "pie"
    };
    
    // data
    var data = [trace1];
    
    var layout = {
      margin: {
        l: 0,
        r: 0,
        t: 0,
        b: 0
      }
    };
    
    Plotly.newPlot("pie", data, layout);




    /********************************************************
     *                                                      *
     *                  BUBBLE CHART                        *
     *                                                      *
     ********************************************************/
    var trace1 = {
      x: sampleArray.map(row => row.otu_ids),
      y: sampleArray.map(row => row.sample_values),
      text: sampleArray.map(row => row.otu_labels),
      marker: { 
        size: sampleArray.map(row => row.sample_values),
        color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)', 'rgb(255, 65, 54)', 'rgb(255, 65, 54)', 'rgb(255, 65, 54)', 'rgb(255, 65, 54)', 'rgb(255, 65, 54)', 'rgb(255, 65, 54)'],
      },
      mode: "markers"
    };
    
    // data
    var data = [trace1];
    
    var layout = {
      margin: {
        l: 0,
        r: 0,
        t: 0,
        b: 0
      }
    };
    
    Plotly.newPlot("bubble", data, layout);
  
  });

}



function init() {
  // console.log("I was here")

  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
