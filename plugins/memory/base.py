
class AbstractMemoryPlugin:
    """
    An abstract class which keeps the memory of current subscribers
    """
    async def get_all_products(self) -> list:
        """
        Returns list of all subscribed products
        """
        raise NotImplementedError

    async def get_chat_ids_for_products(self, product_id: str) -> set:
        """
        Get all subscribed chat ids for specific product and store
        """
        raise NotImplementedError

    async def subscribe(self, product_id: str, chat_id: int) -> None:
        """
        Subscribe chat id to specific product and store
        """
        raise NotImplementedError

    async def unsubscribe(self, product_id: str, chat_id: int) -> None:
        """
        Unsubscribe chat id for specific product and store
        """
        raise NotImplementedError
