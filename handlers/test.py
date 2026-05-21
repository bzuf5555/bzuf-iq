import logging
import random
import time
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.questions import QUESTIONS, TEST_SIZE
from utils.iq_calculator import progress_bar

logger = logging.getLogger(__name__)
router = Router()

LETTERS = ["A", "B", "C", "D"]


class TestStates(StatesGroup):
    waiting_contact = State()
    answering = State()


def _build_answer_keyboard(shuffled_opts: list[str]) -> InlineKeyboardMarkup:
    """Aralashtirilgan variantlar uchun inline klaviatura."""
    buttons = [
        [InlineKeyboardButton(
            text=f"{LETTERS[i]}) {opt}",
            callback_data=LETTERS[i]
        )]
        for i, opt in enumerate(shuffled_opts)
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def _shuffle_question(q: dict) -> tuple[list[str], str]:
    """
    Savol variantlarini aralashtiradi.
    Qaytaradi: (aralashtirilgan_variantlar, to'g'ri_harf)
    """
    opts = q["options"].copy()
    random.shuffle(opts)
    correct_letter = LETTERS[opts.index(q["correct"])]
    return opts, correct_letter


async def send_question(target: Message | CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    idx: int = data.get("q_index", 0)
    selected: list = data.get("selected_questions", [])

    if idx >= len(selected):
        from handlers.results import show_results
        msg = target if isinstance(target, Message) else target.message
        await show_results(msg, state)
        return

    q = selected[idx]
    total = len(selected)
    bar = progress_bar(idx, total)

    # Har savolda variantlarni qayta aralashtir
    shuffled_opts, correct_letter = _shuffle_question(q)

    # To'g'ri harfni state ga saqlash
    await state.update_data(current_correct=correct_letter)

    text = (
        f"{bar} *{idx + 1}/{total}*\n\n"
        f"{q['text']}\n\n"
        f"_Javobni tanlang:_"
    )

    msg = target if isinstance(target, Message) else target.message
    await msg.answer(
        text,
        parse_mode="Markdown",
        reply_markup=_build_answer_keyboard(shuffled_opts),
    )
    await state.set_state(TestStates.answering)


@router.callback_query(F.data == "start_test")
async def cb_start_test(cb: CallbackQuery, state: FSMContext) -> None:
    await cb.message.edit_reply_markup(reply_markup=None)

    # 20 ta random savol tanlash va aralashtirish
    selected = random.sample(QUESTIONS, TEST_SIZE)
    max_pts = sum(q["points"] for q in selected)

    await state.update_data(
        q_index=0,
        score=0,
        correct_count=0,
        answers=[],
        selected_questions=selected,
        max_points=max_pts,
        start_time=int(time.time()),
    )
    await cb.answer()
    await send_question(cb, state)


@router.callback_query(F.data == "restart_test")
async def cb_restart_test(cb: CallbackQuery, state: FSMContext) -> None:
    await cb.message.edit_reply_markup(reply_markup=None)
    await state.clear()

    selected = random.sample(QUESTIONS, TEST_SIZE)
    max_pts = sum(q["points"] for q in selected)

    await state.update_data(
        q_index=0,
        score=0,
        correct_count=0,
        answers=[],
        selected_questions=selected,
        max_points=max_pts,
        start_time=int(time.time()),
    )
    await cb.answer("🔄 Yangi savollar bilan test boshlanmoqda...")
    await send_question(cb, state)


@router.callback_query(TestStates.answering, F.data.in_({"A", "B", "C", "D"}))
async def cb_answer(cb: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    idx: int = data.get("q_index", 0)
    score: int = data.get("score", 0)
    correct_count: int = data.get("correct_count", 0)
    answers: list = data.get("answers", [])
    selected: list = data.get("selected_questions", [])
    current_correct: str = data.get("current_correct", "")

    if idx >= len(selected):
        await cb.answer()
        return

    q = selected[idx]
    chosen = cb.data
    is_correct = chosen == current_correct

    if is_correct:
        score += q["points"]
        correct_count += 1
        feedback = f"✅ To'g'ri! _{q['explanation']}_"
    else:
        feedback = f"❌ Noto'g'ri. _{q['explanation']}_"

    answers.append({"q_id": q["id"], "chosen": chosen, "correct": is_correct})

    await state.update_data(
        q_index=idx + 1,
        score=score,
        correct_count=correct_count,
        answers=answers,
    )

    await cb.message.edit_reply_markup(reply_markup=None)
    await cb.answer(feedback[:200], show_alert=False)
    await send_question(cb, state)
