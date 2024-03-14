from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

import utility.qr_code_generator as qcg
import utility.qr_code_read as qcr

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello. Write the message or link and bot will send you qr-code of your message or link or "
                        "just send qr-code and bot will send qr-code decodet message")


@dp.message_handler()
async def answer(message: types.Message):
    qcg.qr_code_generator(message.text)
    with open("qrcode.png", "rb") as photo:
        await bot.send_photo(message.chat.id, photo)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def qr_code_reader(message: types.Message):
    photo_info = message.photo[-1]
    photo_file = await photo_info.download()
    await message.reply(qcr.qr_code_read(photo_file.name)[0])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
