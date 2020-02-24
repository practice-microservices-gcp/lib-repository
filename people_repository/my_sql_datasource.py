from os import environ
from mysql import connector


class MysqlDataSource:

    def __init__(self):
        self.config = {
            'user': environ['MYSQL_USER'],
            'password': environ['MYSQL_PASSWORD'],
            'database': environ['MYSQL_DATABASE'],
            'raise_on_warnings': (environ['MYSQL_RAISE_ON_WARNINGS'] == 'True')
        }

        if 'MYSQL_HOST' in environ:
            self.config['host'] = environ['MYSQL_HOST']
        else:
            self.config['unix_socket'] = environ['MYSQL_SOCKET_PATH']
            
        self._connection = None
        self._cursor = None

    def getConnection(self):
        self._connection = connector.connect(**self.config)
        return self._connection

    def getCursor(self):
        if(not self._connection):
            self.getConnection()
        
        self._cursor = self._connection.cursor()
        return self._cursor

    def closeConnection(self):
        if (self._cursor):
            self._cursor.close()
            self._cursor = None

        if (self._connection):
            self._connection.close()
            self._connection = None


mysqlDataSource = MysqlDataSource()
