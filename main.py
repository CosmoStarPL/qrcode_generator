from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

import utility.qr_code_generator as qcg

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello. Write the message or link and bot will send you qr-code of your message or link")


@dp.message_handler()
async def answer(message: types.Message):
    qcg.qr_code_generator(message.text)
    with open("qrcode.png", "rb") as photo:
        await bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
