from objects import *

if __name__ == "__main__":
    DATABASE.connect()
    DATABASE.create_tables([Product, OrderStatus, Address, UserRole, User, PhoneNumber, Order, CommodityItem])

    # Добавляем роли пользователей
    admin_role = UserRole.get_or_none(name='admin')
    client_role = UserRole.get_or_none(name='client')