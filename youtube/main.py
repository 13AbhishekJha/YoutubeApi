import os
import json
from flask import Flask, request
from rake_nltk import Rake
import mysql.connector

app = Flask(__name__)

# Establishing connection to the MySQL server
db = mysql.connector.connect(host="mysql", user="root", passwd="my_secret_pw", database="yt_api")
mycursor = db.cursor()

# Rake is used to optimize the search result by extracting keywords using NLTK
r = Rake()

# API routes
@app.route("/get", methods=["POST"])
def paginated():
    payload = request.json
    cursor_lead = (payload["page_number"] * 10) - 10
    mycursor.execute('SELECT * FROM Football LIMIT %s, %s', (cursor_lead, 10))
    data = list(mycursor.fetchall())
    return json.dumps(data, indent=4)

@app.route("/search", methods=["POST"])
def search():
    payload = request.json
    keywords = r.extract_keywords_from_text(payload["query"])
    ranked = r.get_ranked_phrases()

    result = []

    for i in ranked:
        search_term = f"%{i}%"
        mycursor.execute("SELECT * FROM Football WHERE title LIKE %s OR description LIKE %s", (search_term, search_term))
        partial_response = mycursor.fetchall()
        if partial_response:
            result.extend(partial_response)

    return json.dumps(result, indent=4)

# For local development. Not required if running Flask using a WSGI server like Gunicorn.
if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
