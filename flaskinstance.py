from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#@app.route("/home/dinko/Desktop/nmap/piton/vizualizacija/index.html")
@app.route("/home/dinko/Desktop/projekt/index.html")
def helloWorld():
  return "Hello, cross-origin-world!"

#potrebno ubaciti kako bi se moglo pristupiti lokalnim fileovima (databaza iz koje se povlače podaci za vizualizaciju)