from .base import AbstractMemoryPlugin


class InMemoryPlugin(AbstractMemoryPlugin):
    def __init__(self):
        self._data: dict[str, set] = dict()

    async def get_all_products(self) -> list:
        return list(self._data.keys()).copy()

    async def get_chat_ids_for_products(self, product_id: str) -> set:
        return self._data.get(product_id, set()).copy()

    async def subscribe(self, product_id: str, chat_id: int) -> None:
        self._data.setdefault(product_id, set()).add(chat_id)

    async def unsubscribe(self, product_id: str, chat_id: int) -> None:
        self._data[product_id].discard(chat_id)
        if product_id in self._data and not self._data[product_id]:
            self._data.pop(product_id)
