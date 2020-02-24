from repository.my_sql_datasource import mysqlDataSource
from string import Template

class PeopleRepository:

    def listPeople(self, offset, limit):
        totalQuery = ("SELECT count(*) FROM people.people")
        pagQuery = ("SELECT name, surname, email FROM people.people LIMIT %s,%s")

        cursor = mysqlDataSource.getCursor()

        cursor.execute(totalQuery)
        result = {
            'total': cursor.fetchone()[0]
        }

        cursor.execute(pagQuery, (offset, limit))
        result['data'] = cursor.fetchall()

        mysqlDataSource.closeConnection()

        return result

    def createPerson(self, name, surname, email):
        insertQuery = Template("""
        INSERT INTO people.people (name, surname, email)
        VALUES ("$name", "$surname", "$email")
        """).safe_substitute({
            'name': name,
            'surname': surname,
            'email': email
        })

        connection = mysqlDataSource.getConnection()
        cursor = mysqlDataSource.getCursor()

        cursor.execute(insertQuery)
        connection.commit()

        mysqlDataSource.closeConnection()


peopleRepository = PeopleRepository()