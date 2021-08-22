import flask
import json
from flask import request, jsonify
from database import get_db_conn


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
def api_all():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM profiles''')
    row_headers=[x[0] for x in cur.description]
    data = cur.fetchall()

    cur.close()
    conn.close()
    json_data=[]
    for result in data:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all_books():
    return api_all()

app.run(port='3000')
