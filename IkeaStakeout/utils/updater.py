import asyncio
import logging

from aiogram import Bot
from aiogram.utils.exceptions import TelegramAPIError

from IkeaStakeout.consts import UPDATE_INTERVAL_IN_SECONDS, PRODUCT_IN_STOCK_MSG
from IkeaStakeout.plugins import AbstractMemoryPlugin
from IkeaStakeout.utils.ikea import get_list_of_stores_with_stock


async def update_subscriber(bot: Bot, chat_id: int, memory_plugin: AbstractMemoryPlugin, store_name: str, product_id: str, store_id: str):
    """
    Update subscriber and unsubscribe him for the specific restaurant
    """
    try:
        await bot.send_message(chat_id=chat_id, text=PRODUCT_IN_STOCK_MSG.format(product_id=product_id, store_name=store_name))
    except TelegramAPIError:
        logging.exception(f'Unable to update chat {chat_id}')
    finally:
        await memory_plugin.unsubscribe(product_id, store_id, chat_id)


async def update_forever(bot: Bot, memory_plugin: AbstractMemoryPlugin):
    """
    Clients updater
    """
    while True:
        for product_id in await memory_plugin.get_all_products():
            logging.info(f'Checking if {product_id} is now in stock!')
            logging.info(await get_list_of_stores_with_stock(product_id))
            for store_id in await get_list_of_stores_with_stock(product_id):
                store_name = await memory_plugin.get_store_name(store_id)
                logging.info(f'{product_id} is now in stock in {store_name}! updating subscribers')
                for chat_id in await memory_plugin.get_chat_ids_for_product(product_id,store_id):
                    await update_subscriber(bot, chat_id, memory_plugin, store_name, product_id, store_id)
        await asyncio.sleep(UPDATE_INTERVAL_IN_SECONDS)
