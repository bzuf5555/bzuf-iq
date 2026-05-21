from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from utils.keyboards import start_test_keyboard

router = Router()

HELP_TEXT = (
    "🧠 *BZUF-IQ Bot — Yordam*\n\n"
    "*Komandalar:*\n"
    "▸ /start — Botni ishga tushirish\n"
    "▸ /test — Yangi test boshlash\n"
    "▸ /mystats — Mening natijalarim\n"
    "▸ /help — Ushbu yordam xabari\n\n"
    "*Test haqida:*\n"
    "• 54 ta savoldan 20 tasi random tanlanadi\n"
    "• Har gal javob variantlari aralashadi\n"
    "• Natijada IQ ball + batafsil tahlil\n"
    "• Natijani do'stlaringga ulashish mumkin\n\n"
    "*IQ darajalari:*\n"
    "🏆 145+ — Daho\n"
    "🥇 130–144 — Juda yuqori\n"
    "🥈 120–129 — Yuqori\n"
    "🥉 110–119 — O'rtachadan yuqori\n"
    "✅ 90–109 — O'rtacha\n"
    "📊 80–89 — O'rtachadan past\n"
    "📉 65–79 — Past\n\n"
    "_Omad! 🚀_"
)


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(HELP_TEXT, parse_mode="Markdown", reply_markup=start_test_keyboard())


@router.message(Command("test"))
async def cmd_test(message: Message) -> None:
    await message.answer(
        "🎯 *Yangi test boshlashga tayyormisiz?*\n20 ta random savol — IQ ballingizni bilib oling!",
        parse_mode="Markdown",
        reply_markup=start_test_keyboard(),
    )
