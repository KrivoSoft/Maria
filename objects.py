from __future__ import annotations
from typing import Optional
from peewee import *
import yaml
from datetime import date

db = "db_name"


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


class User(BaseModel):
    name = CharField()
    role = ForeignKeyField(UserRole, backref="role")

    class Meta:
        table_name = 'Users'


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
