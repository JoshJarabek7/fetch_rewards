from app.schemas.receipt import Receipt
from math import ceil

def calculate_points(receipt: Receipt) -> int:
    points = 0
    
    points += sum(c.isalnum() for c in receipt.retailer)

    total = float(receipt.total)
    if total.is_integer():
        points += 50

    if total % 0.25 == 0:
        points += 25
    
    points += (len(receipt.items) // 2) * 5

    for item in receipt.items:
        description_length = len(item.shortDescription.strip())
        if description_length % 3 == 0:
            item_price = float(item.price)
            points += ceil(item_price * 0.2)
    
    day = receipt.purchaseDate.day
    if day % 2 != 0:
        points += 6
    
    hour = receipt.purchaseTime.hour
    if 14 <= hour < 16:
        points += 10
    
    return points