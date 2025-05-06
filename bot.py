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
    (re.compile(r'\bислам\b', re.IGNORECASE), 'Ислам — не тормоз, а газ в пол! 🏎️'),
    (re.compile(r'\bасылжан\b', re.IGNORECASE), 'Асылжан — не просто план, это ураган! 🌪️'),
    (re.compile(r'\bарслан\b', re.IGNORECASE), 'Арслан — разносит, как танк по каштанам! 💥'),
    (re.compile(r'\bжандос\b', re.IGNORECASE), 'Жандос — босс, как в Лос-Сантос! 🎮'),
    (re.compile(r'\bдимаш\b', re.IGNORECASE), 'Димаш — и голос, и стиль, и кураж! 🎤'),
    (re.compile(r'\bдаир\b', re.IGNORECASE), 'Даир — всегда в эфир, без фальшивых гирь! 📡'),
    (re.compile(r'\bарлан\b', re.IGNORECASE), 'Арлан — не человек, а целый клан! 🛡️'),
    (re.compile(r'\bберекет\b', re.IGNORECASE), 'Берекет — угощает всех без бед! 🍉'),
    (re.compile(r'\bдота\b', re.IGNORECASE), 'Дота — для геев. 🕹️ Шучу... может.'),
    (re.compile(r'\bстая\b', re.IGNORECASE), 'СТРОЙСЯЯЯ!!! 🐺'),
    (re.compile(r'\bрегресс\b', re.IGNORECASE), 'Регресс — никогда не закончится. 🔁'),
    (re.compile(r'\bрелиз\b', re.IGNORECASE), 'зима не будет, релиз не будет'),
    (re.compile(r'\bфлаттер\b', re.IGNORECASE), 'кто-то сказал гачи?'),
    (re.compile(r'\bflutter\b', re.IGNORECASE), 'кто-то сказал гачи?'),
]

async def handle_message(message: Message):
    text = message.text.strip()
    for pattern, response in TRIGGERS:
        if pattern.search(text):
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
