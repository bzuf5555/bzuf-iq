"""
BZUF-IQ Telegram Bot — Entry Point
Dual-mode: webhook (production/Render) | polling (local dev)
"""
import asyncio
import logging
import sys
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from config import BOT_TOKEN, MONGO_URI, WEBHOOK_URL, WEBHOOK_PATH, HEALTH_PATH, PORT, DEBUG
from database import init_db
from handlers import start, test, results

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def build_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(test.router)
    dp.include_router(results.router)
    return dp


# ── Health endpoint (UptimeRobot pings this) ─────────────────────────
async def health_handler(request: web.Request) -> web.Response:
    return web.Response(text="OK", status=200)


# ── Webhook mode (production) ─────────────────────────────────────────
async def on_startup(bot: Bot) -> None:
    await init_db()
    webhook_url = f"{WEBHOOK_URL}{WEBHOOK_PATH}"
    await bot.set_webhook(webhook_url, drop_pending_updates=True)
    logger.info("Webhook set: %s", webhook_url)


async def on_shutdown(bot: Bot) -> None:
    await bot.delete_webhook()
    logger.info("Webhook deleted")


def run_webhook() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    dp = build_dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()
    app.router.add_get(HEALTH_PATH, health_handler)

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)

    logger.info("Starting webhook server on port %d", PORT)
    web.run_app(app, host="0.0.0.0", port=PORT)


# ── Polling mode (local development) ─────────────────────────────────
async def run_polling() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    dp = build_dispatcher()

    await init_db()
    logger.info("Starting polling mode (local dev)")
    await dp.start_polling(bot, drop_pending_updates=True)


if __name__ == "__main__":
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not set — check your .env file")
        sys.exit(1)
    if not MONGO_URI:
        logger.error("MONGO_URI not set — check your .env file")
        sys.exit(1)

    if WEBHOOK_URL:
        run_webhook()
    else:
        asyncio.run(run_polling())
