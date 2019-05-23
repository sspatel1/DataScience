# What's the Weather Like?

## Summary

Using Python requests, APIs, and JSON traversals, determine what is the weather like as we approach the equator"


![Equator](Images/equatorsign.png)

## WeatherPy

Use Python script to visualize the weather of 500+ cities across the world of varying distance from the equator, utilizing a [Python library](https://pypi.python.org/pypi/citipy), the [OpenWeatherMap API](https://openweathermap.org/api). Create a representative model of weather across world cities.

Python requests, APIs, and JSON traversals to answer a fundamental question: "What's the weather like as we approach the equator?"

Build a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude

Final notebook will incldue:

* Randomly select **at least** 500 unique (non-repeat) cities based on latitude and longitude.
* Perform a weather check on each of the cities using a series of successive API calls.
* Include a print log of each city as it's being processed with the city number and city name.
* Save both a CSV of all data retrieved and png images for each scatter plot.

As final considerations:

* Complete analysis using a Jupyter notebook.
* Matplotlib or Pandas for plotting libraries.
* Labeling of plots like: Plot Titles (with date of analysis) and Axes Labels..

## Hints and Considerations

* The city data to be generated based on random coordinates.

* Next, study the OpenWeatherMap API to answer basic questions about the API: Where to request the API key? Which Weather API in particular is needed? What URL endpoints does it expect? What JSON structure does it respond with? Aim to have a crystal clear understanding of the intended outcome.

* Learn how Citipy works: [citipy Python library](https://pypi.python.org/pypi/citipy). Create a simple test cases outside the main script to confirm that the library is used correctly.

* This is a challenging activity. Push yourself! If you complete this task, then you can safely say that you've gained a strong mastery of the core foundations of data analytics and it will only go better from here. Good luck!

## Copyright

Data Boot Camp © 2018. All Rights Reserved.