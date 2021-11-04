from aiogram.utils.emoji import emojize

WELCOME_MSG = emojize("Hi!\n"
                      "Please enter product's code from ikea, and i'll let you know when the venue is open :smile: \n")
PRODUCT_NOT_FOUND_MSG = emojize('Product was not found! :cry:')
WILL_UPDATE_MSG = "I'll let you know when {product_id} is back in stock in {store_name}!\n(Product number might be different than the one entred. It is normal)"
PRODUCT_IN_STOCK_MSG = "Product number {product_id} is back in stock in {store_name}\n"
CHOOSE_STORE_MSG = emojize("Please choose store from the list below:\nYou can select more than one :wink:")

UPDATE_INTERVAL_IN_SECONDS = 1800

IKEA_SYNONYM_API_URL = 'https://www.ikea.co.il/api/solr?defType=synonym_edismax&facet=true&facet.field%5B%5D=%7B!ex%3DColor_ss%7DColor_ss&facet.field%5B%5D=%7B!ex%3Dshort_color_ss%7Dshort_color_ss&facet.field%5B%5D=%7B!ex%3Dspecial_filter_ss%7Dspecial_filter_ss&facet.limit=500&facet.mincount=2&facet.missing=false&facet.sort=count&fq%5B%5D=lang_code_s:(%22he%22)&fq%5B%5D=group_id_is:(%221%22)&fq%5B%5D=-Hide_by_Force_s:4&group=true&group.field=FamilyName_s&group.limit=16&group.ngroups=true&group.sort=popularity_f+desc&q={product_number}&q.op=AND&rows=50&sort=popularity_f+desc&start=0&stats=true&stats.field=%7B!ex%3Dlist_price_f%7Dlist_price_f&synonyms=true'
IKEA_STOCK_API = 'https://www.ikea.co.il/api/public/productStockStatus/{product_id}.json'
IKEA_PRODUCT_IN_STOCK_STATUS = "0"

IKEASTAKEOUT_API_TOKEN_KEY = "IKEASTAKEOUT TOKEN"
