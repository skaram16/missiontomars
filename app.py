{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d461d86",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import tools\n",
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update_one({}, {\"$set\":mars_data}, upsert=True)\n",
    "   return redirect('/', code=302)\n",
    "\n",
    ".update_one(query_parameter, {\"$set\": data}, options)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "   app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29f6ea4e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
