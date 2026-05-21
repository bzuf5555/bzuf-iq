import logging
import time
from typing import Any, Awaitable, Callable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery

logger = logging.getLogger(__name__)

# Throttle: user_id → oxirgi bosish vaqti
_last_action: dict[int, float] = {}
THROTTLE_SECONDS = 1.0


class ThrottleMiddleware(BaseMiddleware):
    """Foydalanuvchi 1 soniyada bir martadan ko'p bosolmaydi."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        user_id = None
        if isinstance(event, (Message, CallbackQuery)):
            user_id = event.from_user.id if event.from_user else None

        if user_id:
            now = time.monotonic()
            last = _last_action.get(user_id, 0.0)
            if now - last < THROTTLE_SECONDS:
                if isinstance(event, CallbackQuery):
                    await event.answer("⏳ Biroz kuting...", show_alert=False)
                return
            _last_action[user_id] = now

        return await handler(event, data)


class ErrorMiddleware(BaseMiddleware):
    """Barcha kutilmagan xatolarni ushlab logga yozadi, botni to'xtatmaydi."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception as exc:
            user_id = None
            if isinstance(event, (Message, CallbackQuery)):
                user_id = event.from_user.id if event.from_user else None
            logger.error("Unhandled error [user=%s]: %s", user_id, exc, exc_info=True)

            try:
                if isinstance(event, Message):
                    await event.answer("⚠️ Xatolik yuz berdi. Iltimos /start bilan qayta boshlang.")
                elif isinstance(event, CallbackQuery):
                    await event.answer("⚠️ Xatolik. /start bilan qayta boshlang.", show_alert=True)
            except Exception:
                pass
