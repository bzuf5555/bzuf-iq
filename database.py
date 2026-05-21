import logging
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, DB_NAME, USERS_COLLECTION, RESULTS_COLLECTION

logger = logging.getLogger(__name__)

_client: AsyncIOMotorClient | None = None


async def init_db() -> None:
    global _client
    _client = AsyncIOMotorClient(MONGO_URI)
    db = _client[DB_NAME]
    await db[USERS_COLLECTION].create_index("user_id", unique=True)
    await db[RESULTS_COLLECTION].create_index("user_id")
    logger.info("MongoDB connected successfully")


def get_db():
    return _client[DB_NAME]


async def get_user(user_id: int) -> dict | None:
    db = get_db()
    return await db[USERS_COLLECTION].find_one({"user_id": user_id})


async def upsert_user(user_id: int, data: dict) -> None:
    db = get_db()
    await db[USERS_COLLECTION].update_one(
        {"user_id": user_id},
        {"$set": data, "$setOnInsert": {"created_at": datetime.utcnow()}},
        upsert=True,
    )


async def save_contact(user_id: int, phone: str, first_name: str, last_name: str, username: str) -> None:
    await upsert_user(user_id, {
        "user_id": user_id,
        "phone_number": phone,
        "first_name": first_name,
        "last_name": last_name or "",
        "username": username or "",
        "contact_shared": True,
        "updated_at": datetime.utcnow(),
    })


async def save_result(user_id: int, iq_score: int, iq_label: str, correct: int,
                      total: int, time_seconds: int, answers: list) -> None:
    db = get_db()
    await db[RESULTS_COLLECTION].insert_one({
        "user_id": user_id,
        "iq_score": iq_score,
        "iq_label": iq_label,
        "correct_answers": correct,
        "total_questions": total,
        "time_seconds": time_seconds,
        "answers": answers,
        "created_at": datetime.utcnow(),
    })
    await upsert_user(user_id, {
        "last_iq": iq_score,
        "last_test_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    })


async def get_global_stats() -> dict:
    db = get_db()
    pipeline = [
        {"$group": {"_id": None, "avg_iq": {"$avg": "$iq_score"}, "count": {"$sum": 1}}}
    ]
    result = await db[RESULTS_COLLECTION].aggregate(pipeline).to_list(1)
    if result:
        return {"avg_iq": round(result[0]["avg_iq"], 1), "count": result[0]["count"]}
    return {"avg_iq": 100, "count": 0}
