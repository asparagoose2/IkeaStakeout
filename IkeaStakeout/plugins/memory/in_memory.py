from .base import AbstractMemoryPlugin


class InMemoryPlugin(AbstractMemoryPlugin):
    def __init__(self):
        self._data: dict[str, dict[str,set]] = dict()
        self._store_names: dict[str, str] = dict()

    async def get_store_name(self, store_id: str) -> str:
        return self._store_names.get(store_id, None)

    async def set_store_name(self, store_id: str, store_name: str) -> None:
        self._store_names[store_id] = store_name

    async def get_all_products(self) -> list:
        return self._data.copy()

    async def product_has_no_subscribers(self, product_id: str) -> bool:
        for key in self._data[product_id]:
            if not self._data[product_id][key] == set():
                return False
        return True

    async def get_chat_ids_for_product(self, product_id: str, store_id: str) -> list:
        return self._data.get(product_id, dict()).get(store_id, list()).copy()

    async def get_store_ids_for_product(self, product_id: str) -> list:
        return list(self._data.get(product_id, dict()).keys())

    async def subscribe(self, product_id: str, store_id: str, chat_id: int) -> None:
        self._data.setdefault(product_id, dict()).setdefault(store_id,set()).add(chat_id)

    async def unsubscribe(self, product_id: str, store_id: str, chat_id: int) -> None:
        self._data[product_id][store_id].discard(chat_id)
        if product_id in self._data and await self.product_has_no_subscribers(product_id):
            self._data.pop(product_id)
