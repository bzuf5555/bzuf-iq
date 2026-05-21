import logging
import time
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from data.questions import QUESTIONS
from utils.keyboards import answer_keyboard, remove_keyboard
from utils.iq_calculator import progress_bar

logger = logging.getLogger(__name__)
router = Router()


class TestStates(StatesGroup):
    waiting_contact = State()
    answering = State()


async def send_question(target: Message | CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    idx: int = data.get("q_index", 0)

    if idx >= len(QUESTIONS):
        # Barcha savollar tugadi — natijalar chiqariladi
        from handlers.results import show_results
        msg = target if isinstance(target, Message) else target.message
        await show_results(msg, state)
        return

    q = QUESTIONS[idx]
    total = len(QUESTIONS)
    bar = progress_bar(idx, total)

    text = (
        f"{bar} *{idx + 1}/{total}*\n\n"
        f"{q['text']}\n\n"
        f"_Javobni tanlang:_"
    )

    msg = target if isinstance(target, Message) else target.message
    await msg.answer(
        text,
        parse_mode="Markdown",
        reply_markup=answer_keyboard(q["options"]),
    )
    await state.set_state(TestStates.answering)


@router.callback_query(F.data == "start_test")
async def cb_start_test(cb: CallbackQuery, state: FSMContext) -> None:
    await cb.message.edit_reply_markup(reply_markup=None)
    await state.update_data(
        q_index=0,
        score=0,
        correct_count=0,
        answers=[],
        start_time=int(time.time()),
    )
    await cb.answer()
    await send_question(cb, state)


@router.callback_query(F.data == "restart_test")
async def cb_restart_test(cb: CallbackQuery, state: FSMContext) -> None:
    await cb.message.edit_reply_markup(reply_markup=None)
    await state.clear()
    await state.update_data(
        q_index=0,
        score=0,
        correct_count=0,
        answers=[],
        start_time=int(time.time()),
    )
    await cb.answer("🔄 Test qayta boshlanmoqda...")
    await send_question(cb, state)


@router.callback_query(TestStates.answering, F.data.in_({"A", "B", "C", "D"}))
async def cb_answer(cb: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    idx: int = data.get("q_index", 0)
    score: int = data.get("score", 0)
    correct_count: int = data.get("correct_count", 0)
    answers: list = data.get("answers", [])

    if idx >= len(QUESTIONS):
        await cb.answer()
        return

    q = QUESTIONS[idx]
    chosen = cb.data
    is_correct = chosen == q["correct"]

    if is_correct:
        score += q["points"]
        correct_count += 1
        feedback = f"✅ To'g'ri! _{q['explanation']}_"
    else:
        correct_opt = next(o for o in q["options"] if o.startswith(q["correct"]))
        feedback = f"❌ Noto'g'ri. To'g'ri javob: *{correct_opt}*\n_{q['explanation']}_"

    answers.append({"q_id": q["id"], "chosen": chosen, "correct": is_correct})

    await state.update_data(
        q_index=idx + 1,
        score=score,
        correct_count=correct_count,
        answers=answers,
    )

    await cb.message.edit_reply_markup(reply_markup=None)
    await cb.answer(feedback[:200], show_alert=False)

    # Keyingi savolga o'tish
    await send_question(cb, state)
