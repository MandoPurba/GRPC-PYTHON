import psycopg2
from typing import Union, List, Tuple


class Database:
    def __init__(self, dbname, host, user, password, port):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to database")
        except psycopg2.Error as e:
            print("Error connecting to database")

    def exec(self, query: str, fetch_result: bool = False) -> Union[List[Tuple], Exception]:
        """
        Execute a database query.
        Args:
            query (str): The SQL query to execute.
            fetch_result (bool): Whether to fetch and return query result.
        Returns:
            Union[List[Tuple], Exception]:  If fetch_result is True, returns the query result as a list of tuples.
                                            If an error occurs during execution, returns an Exception object.
        """
        try:
            self.cursor.execute(query)
            self.connection.commit()
            if fetch_result:
                result = self.cursor.fetchall()
                return result
        except psycopg2.Error as e:
            return e

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print('Disconnect from database')
