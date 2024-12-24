from aiogram import Bot, Dispatcher, F
import logging
import sys
import yaml
from handlers import handler_start_command

with open('configs/secrets.yml', 'r') as file:
    CONSTANTS = yaml.safe_load(file)

API_TOKEN = CONSTANTS['API_TOKEN']

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, stream=sys.stdout)
    bot: Bot = Bot(token=API_TOKEN)
    dp: Dispatcher = Dispatcher()
    dp.include_router(handler_start_command.router)

    print("----- Start -----")
    dp.run_polling(bot)
