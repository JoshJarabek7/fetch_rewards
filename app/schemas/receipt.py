"""
This module defines the Pydantic models for receipts and related entities.
"""

from pydantic import BaseModel, UUID4, Field, field_validator
from decimal import Decimal
from datetime import date, time


class Item(BaseModel):
    """
    Represents an item on a receipt.
    """

    shortDescription: str
    price: Decimal = Field(gt=0, decimal_places=2)

    @field_validator("shortDescription")
    def strip_short_description(cls, value: str) -> str:
        """
        Strips whitespace from the short description.

        Parameters
        ----------
        value : str
            The short description of the item.

        Returns
        -------
        str
            The trimmed short description.
        """
        return value.strip()


class Receipt(BaseModel):
    """
    Represents a receipt with details about the purchase.
    """

    retailer: str
    purchaseDate: date
    purchaseTime: time
    items: list[Item]
    total: Decimal = Field(gt=0, decimal_places=2)

    @field_validator("retailer")
    def strip_retailer(cls, value: str) -> str:
        """
        Strips whitespace from the retailer name.

        Parameters
        ----------
        value : str
            The name of the retailer.

        Returns
        -------
        str
            The trimmed retailer name.
        """
        return value.strip()


class ReceiptIDResponse(BaseModel):
    """
    Represents the response containing a receipt ID.
    """

    id: UUID4


class PointsResponse(BaseModel):
    """
    Represents the response containing the points awarded for a receipt.
    """

    points: int
