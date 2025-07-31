from peewee import SqliteDatabase
import yaml

def get_db():
    with open('configs/secrets.yml', 'r') as file:
        config = yaml.safe_load(file)
    return SqliteDatabase(config['DB_NAME'])
