from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
import scraper
# import pymongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
# mongo = PyMongo(app)

# conn="mongodb://localhost:27017"
# client=pymongo.MongoClient(conn)
# db=client.craigslist_app

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

@app.route("/")
def index():
	# listings = mongo.db.listings.find_one()
    # listings = db.listings.find_one()
    return render_template("index.html", table_in_html=scraper.scrape_to_html())


# @app.route("/scrape")
# def scraper():
#     # listings = mongo.db.listings
#     listings = db.listings
#     listings_data = scrape_craigslist.scrape()
#     listings.update({}, listings_data, upsert=True)
#     return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)