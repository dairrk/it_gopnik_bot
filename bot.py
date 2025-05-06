import asyncio
import re
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

TRIGGERS = [
    (re.compile(r'\bк[оа]роч[ье]?\b', re.IGNORECASE), 'У кого короче, тот дома сидит!'),
    (re.compile(r'\bнет\b', re.IGNORECASE), 'пидора ответ'),
    (re.compile(r'\bда\b', re.IGNORECASE), 'пизда'),
    (re.compile(r'\bхо(чу|тим|тят|тел|тела)\b', re.IGNORECASE), 'Хотеть невредно!'),
    (re.compile(r'\bкс\b', re.IGNORECASE), 'Работа! Какой КС??? 🧢'),
    (re.compile(r'\bтез\b', re.IGNORECASE), 'Тез? Это вы про лучшее приложение в мире! 🚖'),
]

async def handle_message(message: Message):
    text = message.text.strip()
    for pattern, response in TRIGGERS:
        if pattern.match(text):
            await message.reply(response)
            break

async def main():
    bot = Bot(
        token=API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    dp.message.register(handle_message)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
