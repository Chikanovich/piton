import pymysql
from flaskinstance import app
from dbcfg import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import security

#pozivanje lokalne stranice na http://127.0.0.1:5000/stats
@app.route("/stats") #određuje path
def user():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM stats;")
        #dohvaćanje svih podataka iz databaze, pretvaranje u .json format i odgovor "200"
        #ukoliko je komunikacija između korisnika i servera uspješno izvršena
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

#ukoliko se dogodi greška (nemoguće pristupiti podacima i sl.)
@app.errorhandler(404)
def not_found(error = None):
    message = {
        "status": 404,
        "message": "Not found: " + request.url,
        }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
