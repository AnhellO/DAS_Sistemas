from peewee import PostgresqlDatabase
from settings import *

db = PostgresqlDatabase(
    DATABASE['NAME'],
    user=DATABASE['USER'],
    password=DATABASE['PASSWORD'],
    host=DATABASE['HOST'],
    port=DATABASE['PORT']
)