from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardRemove,
)


def contact_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Telefon raqamimni ulashish", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def remove_keyboard() -> ReplyKeyboardRemove:
    return ReplyKeyboardRemove()


def answer_keyboard(options: list[str]) -> InlineKeyboardMarkup:
    buttons = [[InlineKeyboardButton(text=opt, callback_data=opt[0])] for opt in options]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def start_test_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🚀 Testni boshlash", callback_data="start_test")
    ]])


def result_keyboard(iq_score: int, bot_username: str) -> InlineKeyboardMarkup:
    share_text = (
        f"Men BZUF-IQ testini yechdim va IQ ballim {iq_score} ga teng chiqdi! "
        f"Sen ham sinab ko'r 👉 https://t.me/{bot_username}"
    )
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📤 Natijani do'stlarga ulashish",
            url=f"https://t.me/share/url?url={share_text}"
        )],
        [InlineKeyboardButton(text="🔄 Qayta test topshirish", callback_data="restart_test")],
    ])
