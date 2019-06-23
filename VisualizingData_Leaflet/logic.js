// Store our API endpoint inside queryUrl
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Marker size
function markerSize(mag) {
  return mag * 40000;
}

// Marker Color
function markerColor(mag) {
      if (mag <= 3) {
          return "Green";
      } else if (mag <= 4) {
          return "Yellow";
      } else if (mag <= 5) {
          return "Red";
      } else {
          return "Red";
      };
    }

// Perform a GET request to the query URL
d3.json(link, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {

  var earthquakes = L.geoJSON(earthquakeData, {
  // Define a function we want to run once for each feature in the features array
  // Give each feature a popup describing the place and time of the earthquake
 onEachFeature : function (feature, layer) {

    layer.bindPopup("<h3>" + feature.properties.place +
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>" + "<p> Magnitude: " +  feature.properties.mag + "</p>")
    },     pointToLayer: function (feature, latlng) {
      return new L.circle(latlng,
        {radius: markerSize(feature.properties.mag),
        fillColor: markerColor(feature.properties.mag),
        fillOpacity: 0.5,
        stroke: false
    })
  }
  });
    
  // Sending our earthquakes layer to the createMap function
  createMap(earthquakes);
}

function createMap(earthquakes) {

  // Define lightmap layer
  var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  });


  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Light Map": lightmap,
  };

  // Create our map, giving it the lightmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [31.57853542647338,-99.580078125],
    zoom: 3,
    layers: [lightmap, earthquakes]
  });

}