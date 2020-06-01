from flaskinstance import app
from flaskext.mysql import MySQL

mysql = MySQL()

# mysql podaci za logiranje kako bi se mogli povući podaci za REST API
app.config["MYSQL_DATABASE_USER"] = "dinko"
app.config["MYSQL_DATABASE_PASSWORD"] = "Dinko_Pass_1"
app.config["MYSQL_DATABASE_DB"] = "Netscanner"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)