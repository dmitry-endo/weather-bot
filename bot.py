import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()
    # dp.include_router(event_monitoring.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
