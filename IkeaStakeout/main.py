import asyncio
import logging
import os

import click
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from IkeaStakeout.consts import IKEASTAKEOUT_API_TOKEN_KEY
from IkeaStakeout.plugins import InMemoryPlugin
from IkeaStakeout.utils import setup_handlers
from IkeaStakeout.utils import update_forever

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option('--api-token', default=os.environ.get(IKEASTAKEOUT_API_TOKEN_KEY), help='The bot API token', required=True)
def main(api_token: str):
    loop = asyncio.get_event_loop()
    memory_plugin = InMemoryPlugin()
    bot = Bot(token=api_token)
    dp = Dispatcher(bot)
    loop.create_task(update_forever(bot, memory_plugin))
    setup_handlers(dp, memory_plugin, bot)
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
