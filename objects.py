from __future__ import annotations
from typing import Optional
from peewee import *
import yaml
from datetime import date


with open('configs/secrets.yml', 'r') as file:
    CONSTANTS = yaml.safe_load(file)
db_name = CONSTANTS['DB_NAME']
db = SqliteDatabase(db_name)


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = CharField()
    article_number = CharField()
    relevant = BooleanField()

    class Meta:
        table_name = 'Products'

    def __repr__(self):
        return self.name

    def get_name(self):
        return self.name


class OrderStatus(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'OrderStatuses'


class Address(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'Addresses'


class UserRole(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'UserRoles'

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.save()


class User(BaseModel):
    name = CharField()
    telegram_id = CharField()
    role = ForeignKeyField(UserRole, backref="role")

    class Meta:
        table_name = 'Users'

    def __init__(self, name: str, telegram_id: str, role: UserRole, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.telegram_id = telegram_id
        self.role = role
        self.save()


class PhoneNumber(BaseModel):
    number = CharField()
    user_id = ForeignKeyField(User, backref="user_id")

    class Meta:
        table_name = 'PhoneNumbers'


class Order(BaseModel):
    creation_date = DateTimeField()
    issue_date = DateTimeField()
    creator_id = ForeignKeyField(User, backref="creator_id")
    status_id = ForeignKeyField(OrderStatus, backref="status_id")
    address_id = ForeignKeyField(Address, backref="address_id")
    price = IntegerField()

    class Meta:
        table_name = 'Orders'


class CommodityItem(BaseModel):
    price = IntegerField()
    quantity = IntegerField()
    product_id = ForeignKeyField(Product, backref="product_id")
    order_id = ForeignKeyField(Order, backref="order_id")
