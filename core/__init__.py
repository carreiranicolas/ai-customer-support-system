import pymysql

pymysql.install_as_MySQLdb() # Fazemos isso porque o django usa por padrão a lib mysqlclient,
# mas ela travou