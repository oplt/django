import psycopg2
from psycopg2 import sql

dataBase = psycopg2.connect(
                            dbname="django_crm",
                            user="django_crm",
                            password="123456",
                            host="localhost",
                            port="5432"
                        )

cursor = dataBase.cursor()
