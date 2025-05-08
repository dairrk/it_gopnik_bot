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
    (re.compile(r'\bислам\b', re.IGNORECASE), 'Қашан үйленесің зæбал?'),
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
    (re.compile(r'\bНартай\b', re.IGNORECASE), 'Нартай, ну не скатай!'),
    (re.compile(r'\bАлиомар\b', re.IGNORECASE), 'Алиомар, за баги держи удар!'),
    (re.compile(r'\bАман\b', re.IGNORECASE), 'Аман, не забудь про спринт-план!'),
    (re.compile(r'\bАсхат\b', re.IGNORECASE), 'Асхат, ты сегодня — батчат!'),
    (re.compile(r'\bМиржалал\b', re.IGNORECASE), 'Миржалал, код ревью провал!'),
    (re.compile(r'\bМеиржан\b', re.IGNORECASE), 'Меиржан, зальёшь баг — держи бан!'),

    # Айти, скрам, дота, кс, такси
    (re.compile(r'\bрегресс\b', re.IGNORECASE), 'Регресс — никогда не закончится'),
    (re.compile(r'\bрелиз\b', re.IGNORECASE), 'Зима не будет, релиз не будет'),
    (re.compile(r'\bсимпл\b', re.IGNORECASE), 'Симпл снова клатч потащил'),
    (re.compile(r'\bклатч\b', re.IGNORECASE), 'Клатч один на пять — и ты в халявный рай'),
    (re.compile(r'\bинт\b', re.IGNORECASE), 'Инт заинтил, теперь в бэкенде дебаг'),
    (re.compile(r'\bзаказ\b', re.IGNORECASE), 'Новый заказ — снова в Тулпар'),
        # IT / QA / DevOps / Scrum
    (re.compile(r'\bбаг(и)?\b', re.IGNORECASE), 'Баг багом погоняет, а тест-кейс всё страдает'),
    (re.compile(r'\bфикс(ы)?\b', re.IGNORECASE), 'Были фиксы, стали фичи'),
    (re.compile(r'\bрелиз(ы)?\b', re.IGNORECASE), 'Зима не будет, релиз не будет'),
    (re.compile(r'\bспринт\b', re.IGNORECASE), 'Спринт не спринт, если нет дедлайна'),
    (re.compile(r'\bбэклог\b', re.IGNORECASE), 'Бэклог растёт, а разработка идёт'),
    (re.compile(r'\bстендап\b', re.IGNORECASE), 'На стендапе ты стоишь, а таски — нет'),
    (re.compile(r'\bревью\b', re.IGNORECASE), 'Код ревью — как мини-интервью'),
    (re.compile(r'\bфича\b', re.IGNORECASE), 'Это не баг, это фича!'),
    (re.compile(r'\bмерж\b', re.IGNORECASE), 'Смержил не туда — винду переустанови тогда'),
    (re.compile(r'\bдеплой\b', re.IGNORECASE), 'Деплой прошёл, но всё упало'),

    # Dota
    (re.compile(r'\bроша(н)?\b', re.IGNORECASE), 'Рошан пал — пиши пропал'),
    (re.compile(r'\bмид(ер)?\b', re.IGNORECASE), 'Мидер фидит — репорт за обид'),
    (re.compile(r'\bгг(вп)?\b', re.IGNORECASE), 'ГГ ВП — и в следующую без меня'),
    (re.compile(r'\bпудж\b', re.IGNORECASE), 'Пудж без хука — как клава без пробела'),
    (re.compile(r'\bинт\b', re.IGNORECASE), 'Инт заинтил — плачь на стене'),

    # CS
    (re.compile(r'\bсимпл\b', re.IGNORECASE), 'Симпл снова один в пять'),
    (re.compile(r'\bклатч\b', re.IGNORECASE), 'Клатч зашел — и всем хорошо'),
    (re.compile(r'\bдиффуз\b', re.IGNORECASE), 'Без диффуза ты как без шансов'),
    (re.compile(r'\bбомба\b', re.IGNORECASE), 'Бомба тикала, а ты тикток смотрел'),
    (re.compile(r'\bэйс\b', re.IGNORECASE), 'Эйс сделал? Теперь отдыхай'),

    # Такси / логистика
    (re.compile(r'\bзаказ\b', re.IGNORECASE), 'Новый заказ — снова в Тулпар'),
    (re.compile(r'\bдоставка\b', re.IGNORECASE), 'Доставка без водителя — это просто ожидание'),
    (re.compile(r'\bводитель\b', re.IGNORECASE), 'Водитель ждал, пока ты спал'),
    (re.compile(r'\bпростой\b', re.IGNORECASE), 'Простой — это когда заказов нет, но ты на линии'),
    (re.compile(r'\bподача\b', re.IGNORECASE), 'Подача 5 минут? На деле все 15'),

    # Общие термины
    (re.compile(r'\bрелизный поезд\b', re.IGNORECASE), 'Релизный поезд не ждет опоздавших'),
    (re.compile(r'\bгорячая фикса\b', re.IGNORECASE), 'Горячая фикса — завтра в проде будет жара'),
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
