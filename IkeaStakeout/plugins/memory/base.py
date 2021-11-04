
class AbstractMemoryPlugin:
    """
    An abstract class which keeps the memory of current subscribers
    """

    async def get_store_name(self, store_id: str) -> str:
        """
        Get store name for specific store id
        """
        raise NotImplementedError

    async def set_store_name(self, store_id: str, store_name: str) -> None:
        """
        Set store name for specific store id
        """
        raise NotImplementedError

    async def get_all_products(self) -> list:
        """
        Returns list of all subscribed products
        """
        raise NotImplementedError

    async def get_chat_ids_for_product(self, product_id: str, store_id: str) -> list:
        """
        Get all subscribed chat ids for specific product and store
        """
        raise NotImplementedError

    async def get_store_ids_for_product(self, product_id: str) -> list:
        """
        Get all subscribed store ids for specific product
        """
        raise NotImplementedError

    async def product_has_no_subscribers(self, product_id: str) -> bool:
        """
        Returns True if product has no subscribers
        """
        raise NotImplementedError

    async def subscribe(self, product_id: str, store_id: str, chat_id: int) -> None:
        """
        Subscribe chat id to specific product and store
        """
        raise NotImplementedError

    async def unsubscribe(self, product_id: str, store_id: str, chat_id: int) -> None:
        """
        Unsubscribe chat id for specific product and store
        """
        raise NotImplementedError
