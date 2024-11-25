"""
This module provides functions for processing receipts.
"""

from app.schemas.receipt import Receipt
from math import ceil


def calculate_points(receipt: Receipt) -> int:
    """
    Calculate the points for a given receipt based on predefined rules.

    Parameters
    ----------
    receipt : Receipt
        A Pydantic model representing the receipt details.

    Returns
    -------
    int
        The total points calculated for the receipt.
    """
    points = 0

    # One point for every alphanumeric character in the retailer name.
    points += sum(c.isalnum() for c in receipt.retailer)

    # 50 points if the total is a round dollar amount with no cents.
    total = float(receipt.total)
    if total.is_integer():
        points += 50

    # 25 points if the total is a multiple of 0.25.
    if total % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt.
    points += (len(receipt.items) // 2) * 5

    # Points based on item description length.
    for item in receipt.items:
        description_length = len(item.shortDescription.strip())
        if description_length % 3 == 0:
            item_price = float(item.price)
            points += ceil(item_price * 0.2)

    # 6 points if the day in the purchase date is odd.
    day = receipt.purchaseDate.day
    if day % 2 != 0:
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    hour = receipt.purchaseTime.hour
    if 14 <= hour < 16:
        points += 10

    return points
