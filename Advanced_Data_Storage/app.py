import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# Path to sqlite
database_path = "Resources/hawaii.sqlite"

# Create an engine that can talk to the database
engine = create_engine(f"sqlite:///{database_path}")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcomr to my Climate App!<br>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():

    """
    - Convert the query results to a Dictionary using date as the key and prcp as the value.
    - Return the JSON representation of your dictionary.
    """
    
    # Query all dates in Measurement table
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    # Create a dictionary from the row data and append to a list of precipitate
    precipitate = []
    for date, prcp in results:
        precipitate_dict = {}
        precipitate_dict[date] = prcp
        precipitate.append(precipitate_dict)

    return jsonify(precipitate)


@app.route("/api/v1.0/stations")
def stations():

    """
    - Return a JSON list of stations from the dataset
    """
    
    # Query all station from Sation table
    results = session.query(Station.station).all()
    session.close()

    # Create a list of stations
    station = []
    for station_ in results:
        station.append(station_)

    return jsonify(station)



@app.route("/api/v1.0/<start>/<end>")
@app.route("/api/v1.0/<start>/", defaults={"end": None})

def temp(start, end=None):

  """
  - Return a JSON list of the minimum temperature, the average temperature, 
    and the max temperature for a given start or start-end range.
  - When given the start and the end date, calculate the TMIN, TAVG, and TMAX
    for dates between the start and end date inclusive.
  """

  if(end):
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), \
          func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    
    return jsonify(results)
    

  else:
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), \
          func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    return jsonify(results)
 


if __name__ == '__main__':
    app.run(debug=True)
