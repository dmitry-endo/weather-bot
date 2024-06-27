import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    bot = Bot(config.bot_token.get_secret_value())

    dp = Dispatcher()
    # dp.include_router(event_monitoring.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
