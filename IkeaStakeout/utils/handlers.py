import logging

from aiogram import types, Dispatcher, Bot



from IkeaStakeout.consts import  WILL_UPDATE_MSG, WELCOME_MSG, CHOOSE_STORE_MSG,PRODUCT_NOT_FOUND_MSG
from IkeaStakeout.plugins import AbstractMemoryPlugin
from IkeaStakeout.utils.ikea import get_list_of_stores_with_id, search_product_by_product_number


def keyboard_maker(stores: list, product_id: str):
    kb = types.InlineKeyboardMarkup()
    for store in stores:
        kb.add(types.InlineKeyboardButton(text=store["store_name"], callback_data=str(product_id)+'/'+str(store["store_id"])))
    return kb

async def update_stores_dict(stores: list, memory_plugin: AbstractMemoryPlugin):
    for store in stores:
        await memory_plugin.set_store_name(store["store_id"], store["store_name"])

async def reply_welcome(message: types.message):
    await message.reply(WELCOME_MSG)

async def check_status(message: types.Message, memory_plugin: AbstractMemoryPlugin):
    """
    Gets message and dislpay list of stores
    """
    logging.info(f'Trying to get venue status for {message.text}')

    stores = None
    try:
        product_id = await search_product_by_product_number(message.text)
        logging.info(f'Product id is {product_id}')
        stores = await get_list_of_stores_with_id(product_id)
        kb = keyboard_maker(stores, product_id)
        await message.answer(CHOOSE_STORE_MSG, reply_markup=kb)
    except Exception as e:
        logging.error(f'Error while getting venue status for {message.text}')
        logging.error(e)
        await message.answer(PRODUCT_NOT_FOUND_MSG)

async def inline_kb_answer_callback_handler(query: types.CallbackQuery, memory_plugin: AbstractMemoryPlugin, bot: Bot):
    await query.answer()
    product = query.data.split('/')[0]
    store = query.data.split('/')[1]
    
    if not await memory_plugin.get_store_name(store):
        await update_stores_dict(await get_list_of_stores_with_id(product), memory_plugin)

    await bot.send_message(query.from_user.id, WILL_UPDATE_MSG.format(store_name=await memory_plugin.get_store_name(store), product_id=product))
    await memory_plugin.subscribe(product, store, query.from_user.id)

def setup_handlers(dispatcher: Dispatcher, memory_plugin: AbstractMemoryPlugin, bot: Bot):
    dispatcher.register_message_handler(reply_welcome, commands=['start', 'help'])
    dispatcher.register_message_handler(lambda message: check_status(message, memory_plugin))
    dispatcher.register_callback_query_handler(lambda message: inline_kb_answer_callback_handler(message, memory_plugin, bot))
