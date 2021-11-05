import logging
import aiohttp

from IkeaStakeout.consts import IKEA_STOCK_API, IKEA_PRODUCT_IN_STOCK_STATUS, IKEA_SYNONYM_API_URL
from IkeaStakeout.exceptions import ProductWasNotFoundException

# product_id : ikea's internal product id
# product_number : published ikea product/part number

async def get_product_stock(product_id: str) -> dict:
    """
    Get the product stock data dict from IKEA API
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(IKEA_STOCK_API.format(product_id=product_id)) as response:
            response_json = await response.json()
            if response_json['data'] == []:
                raise ProductWasNotFoundException()
            return response_json['data']


async def is_product_in_stock(product_id: str, store_id: str) -> bool:
    """
    The function returns whether the product is in stock in a store
    """
    data = await get_product_stock(product_id)
    for store in data:
        if store['store_id'] == store_id:
            if store['store_id']['status'] == IKEA_PRODUCT_IN_STOCK_STATUS:
                return True
            else:
                return False
        return False

async def get_list_of_stores_with_stock(product_id: str) -> list:
    """
    Get list of stores with stock
    """
    data = await get_product_stock(product_id)
    stores = []
    for store in data:
        if store['status'] == IKEA_PRODUCT_IN_STOCK_STATUS:
            stores.append(store['store_id'])
    return stores

async def get_list_of_stores_with_id(product_id: str) -> list:
    """
    Get list of stores with product if
    """
    logging.info(f'Getting list of stores with id {product_id}')
    data = await get_product_stock(product_id)
    stores = []
    for store in data:
        stores.append({"store_name" : store['store_name'], "store_id" : store['store_id']})
    return stores

async def get_list_of_stores_with_number(product_number: str) -> list:
    """
    Get list of stores with product number
    """
    logging.info(f'Getting list of stores with number {product_number}')
    product_id = await get_product_id_by_product_number(product_number)
    return await get_list_of_stores_with_id(product_id)


async def get_product_id_by_product_number(product_number: str) -> str:
    """
    Search product by product_number and returns the product_id
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(IKEA_SYNONYM_API_URL.format(product_number=product_number)) as response:
            result = await response.json()
            if result['grouped']['FamilyName_s']['ngroups'] < 1:
                return None
            return result['grouped']['FamilyName_s']['groups'][0]['doclist']['docs'][0]['product_id_i']

