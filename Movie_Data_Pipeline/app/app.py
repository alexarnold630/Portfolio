import datetime as dt
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, redirect
import json
from sqlHelper import SQLHelper



#######################################################

app = Flask(__name__)

sqlHelper = SQLHelper()

#Set Flask Routes

@app.route("/")
def home():
    """List all routes that are available."""

    return (
        "<h1>Movies</h1>"
        f"Available Routes:<br/>"
        f"/api/v1.0/top_10_movies<br/>"
        f"/api/v1.0/avg_rating_genre<br/>"
        f"/api/v1.0/director_rating<br/>"
        f"/api/v1.0/actor_count<br/>"
        f"/api/v1.0/titles_by_country"
    )

@app.route("/api/v1.0/top_10_movies")
def get_top_10_movies():
    data = sqlHelper.get_top_10_movies()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/avg_rating_genre")
def get_avg_rating_by_genre():
    data = sqlHelper.get_avg_rating_by_genre()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/director_rating")
def get_director_rating():
    data = sqlHelper.get_director_count()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/actor_count")
def get_actor_count():
    data = sqlHelper.get_actor_count()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/titles_by_country")
def get_titles_by_country(self):
    data = sqlHelper.get_titles_by_country()
    return jsonify(json.loads(data.to_json(orient="records")))

if __name__ == "__main__":
    app.run(debug=True)
