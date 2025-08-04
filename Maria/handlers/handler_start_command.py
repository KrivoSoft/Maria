from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Инициализируем роутер уровня модуля
router = Router()


@router.message(Command(commands=["start"]))
async def handler_start_command(message: Message):
    """ Этот хэндлер обрабатывает команду "/start" """
    await message.answer("OK")
