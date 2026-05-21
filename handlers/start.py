import logging
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, Contact
from aiogram.fsm.context import FSMContext

from database import get_user, save_contact
from utils.keyboards import contact_keyboard, remove_keyboard, start_test_keyboard
from handlers.test import TestStates

logger = logging.getLogger(__name__)
router = Router()

WELCOME_NEW = (
    "👋 Salom, *{name}*!\n\n"
    "🧠 *BZUF-IQ* — Aql-idrok testi botiga xush kelibsiz!\n\n"
    "📋 *Test haqida:*\n"
    "• 20 ta savol\n"
    "• Turli kognitiv sohalar\n"
    "• Oxirida IQ ball va tahlil\n\n"
    "📱 Davom etish uchun telefon raqamingizni ulashing:"
)

WELCOME_BACK = (
    "👋 Qaytib keldingiz, *{name}*!\n\n"
    "🧠 *BZUF-IQ* testini boshlashga tayyormisiz?\n"
    "20 ta savol — natijangiz tayyor bo'lganda IQ ballingizni bilib olasiz."
)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    user = await get_user(message.from_user.id)
    name = message.from_user.first_name or "Do'stim"

    if user and user.get("contact_shared"):
        await message.answer(
            WELCOME_BACK.format(name=name),
            parse_mode="Markdown",
            reply_markup=start_test_keyboard(),
        )
    else:
        await message.answer(
            WELCOME_NEW.format(name=name),
            parse_mode="Markdown",
            reply_markup=contact_keyboard(),
        )
        await state.set_state(TestStates.waiting_contact)


@router.message(TestStates.waiting_contact, F.contact)
async def handle_contact(message: Message, state: FSMContext) -> None:
    contact: Contact = message.contact

    # Faqat o'z raqamini ulashishga ruxsat
    if contact.user_id != message.from_user.id:
        await message.answer(
            "❌ Iltimos, *o'z* telefon raqamingizni ulashing.",
            parse_mode="Markdown",
            reply_markup=contact_keyboard(),
        )
        return

    await save_contact(
        user_id=message.from_user.id,
        phone=contact.phone_number,
        first_name=message.from_user.first_name or "",
        last_name=message.from_user.last_name or "",
        username=message.from_user.username or "",
    )

    await message.answer(
        "✅ *Telefon raqamingiz saqlandi!*\n\nEndi testni boshlashingiz mumkin 🚀",
        parse_mode="Markdown",
        reply_markup=remove_keyboard(),
    )
    await message.answer(
        "🎯 *BZUF-IQ Testi*\n\n20 ta savol — IQ ballingizni aniqlaylik!",
        parse_mode="Markdown",
        reply_markup=start_test_keyboard(),
    )
    await state.clear()


@router.message(TestStates.waiting_contact)
async def contact_required(message: Message) -> None:
    await message.answer(
        "📱 Davom etish uchun *telefon raqamingizni ulashing* (pastdagi tugmani bosing).",
        parse_mode="Markdown",
        reply_markup=contact_keyboard(),
    )
