"""
This module provides an in-memory database for storing and retrieving receipts.
"""

from uuid import uuid4, UUID
from app.schemas.receipt import Receipt


class InMemoryDB:
    """
    A simple in-memory database to store receipts using UUIDs as keys.
    """

    def __init__(self):
        """
        Initializes the in-memory database with an empty dictionary.
        """
        self._data: dict[UUID, Receipt] = {}

    def add_receipt(self, receipt: Receipt) -> UUID:
        """
        Adds a receipt to the database and returns its unique identifier.

        Parameters
        ----------
        receipt : Receipt
            The receipt to be added to the database.

        Returns
        -------
        UUID
            The unique identifier assigned to the receipt.
        """
        receipt_id = uuid4()
        self._data[receipt_id] = receipt
        return receipt_id

    def get_receipt(self, receipt_id: UUID) -> Receipt:
        """
        Retrieves a receipt from the database by its unique identifier.

        Parameters
        ----------
        receipt_id : UUID
            The unique identifier of the receipt to retrieve.

        Returns
        -------
        Receipt
            The receipt associated with the given identifier, or None if not found.
        """
        return self._data.get(receipt_id)

    def get_all_receipts(self) -> dict[UUID, Receipt]:
        """
        Returns all receipts stored in the database.

        Returns
        -------
        dict[UUID, Receipt]
            A dictionary of all receipts with their unique identifiers.
        """
        return self._data


db_instance = InMemoryDB()
