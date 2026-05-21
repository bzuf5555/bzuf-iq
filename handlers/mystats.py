from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from motor.motor_asyncio import AsyncIOMotorCollection

from database import get_db
from config import RESULTS_COLLECTION
from utils.iq_calculator import IQ_LABELS

router = Router()


async def _get_user_results(user_id: int) -> list[dict]:
    db = get_db()
    col: AsyncIOMotorCollection = db[RESULTS_COLLECTION]
    cursor = col.find({"user_id": user_id}).sort("created_at", -1).limit(5)
    return await cursor.to_list(5)


def _label_for(iq: int) -> str:
    for threshold, label, _ in IQ_LABELS:
        if iq >= threshold:
            return label
    return "📋 Chegaraviy"


@router.message(Command("mystats"))
async def cmd_mystats(message: Message) -> None:
    results = await _get_user_results(message.from_user.id)

    if not results:
        await message.answer(
            "📊 Siz hali test topshirmagansiz.\n\n/test — Testni boshlash",
            parse_mode="Markdown",
        )
        return

    best = max(results, key=lambda r: r["iq_score"])
    last = results[0]

    lines = [
        "📊 *Mening natijalarim*\n",
        f"🏅 *Eng yuqori IQ:* `{best['iq_score']}` — {_label_for(best['iq_score'])}",
        f"🕐 *So'nggi natija:* `{last['iq_score']}` — {_label_for(last['iq_score'])}\n",
        f"🔁 Jami test: *{len(results)}* ta (oxirgi 5 ko'rsatildi)\n",
        "*So'nggi 5 natija:*",
    ]

    for i, r in enumerate(results, 1):
        dt = r["created_at"].strftime("%d.%m %H:%M") if r.get("created_at") else "—"
        lines.append(
            f"{i}. `{r['iq_score']}` IQ — {r['correct_answers']}/{r['total_questions']} to'g'ri — {dt}"
        )

    await message.answer("\n".join(lines), parse_mode="Markdown")
