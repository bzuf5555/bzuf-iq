import logging
import time
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database import save_result, get_global_stats
from utils.iq_calculator import calculate_iq, iq_percentile
from utils.keyboards import result_keyboard

logger = logging.getLogger(__name__)
router = Router()


async def show_results(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    score: int = data.get("score", 0)
    correct_count: int = data.get("correct_count", 0)
    answers: list = data.get("answers", [])
    start_time: int = data.get("start_time", int(time.time()))

    elapsed = int(time.time()) - start_time
    total_questions = 20

    iq_score, iq_label, iq_desc = calculate_iq(score, elapsed)
    percentile = iq_percentile(iq_score)

    await save_result(
        user_id=message.from_user.id,
        iq_score=iq_score,
        iq_label=iq_label,
        correct=correct_count,
        total=total_questions,
        time_seconds=elapsed,
        answers=answers,
    )

    stats = await get_global_stats()
    mins, secs = divmod(elapsed, 60)
    time_str = f"{mins}:{secs:02d}"

    # Foizli taqqoslash
    vs_avg = iq_score - stats["avg_iq"]
    vs_text = f"+{vs_avg:.0f}" if vs_avg >= 0 else f"{vs_avg:.0f}"

    result_text = (
        f"🏁 *Test yakunlandi!*\n\n"
        f"━━━━━━━━━━━━━━━━━\n"
        f"🧠 *IQ Ballingiz:*  `{iq_score}`\n"
        f"{iq_label}\n"
        f"━━━━━━━━━━━━━━━━━\n\n"
        f"📊 *Batafsil natija:*\n"
        f"• To'g'ri javoblar: *{correct_count}/{total_questions}*\n"
        f"• Vaqt: *{time_str}*\n"
        f"• Foizlik: *{percentile}%* (siz {100 - percentile}% dan ustunroqsiz)\n"
        f"• O'rtachadan: *{vs_text}* ball\n\n"
        f"💬 *Tahlil:*\n_{iq_desc}_\n\n"
        f"👥 Ishtirokchilar o'rtachasi: `{stats['avg_iq']}` (jami {stats['count']} kishi)"
    )

    try:
        bot = message.bot
        bot_me = await bot.get_me()
        bot_username = bot_me.username
    except Exception:
        bot_username = "bzuf_iq_bot"

    await state.clear()
    await message.answer(
        result_text,
        parse_mode="Markdown",
        reply_markup=result_keyboard(iq_score, bot_username),
    )
