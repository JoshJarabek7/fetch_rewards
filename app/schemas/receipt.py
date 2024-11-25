from pydantic import BaseModel, UUID4, Field, field_validator
from decimal import Decimal
from datetime import date, time

class Item(BaseModel):
    shortDescription: str
    price: Decimal = Field(gt=0, decimal_places=2)

    @field_validator('shortDescription')
    def strip_short_description(cls, value: str) -> str:
        return value.strip()
    
class Receipt(BaseModel):
    retailer: str
    purchaseDate: date
    purchaseTime: time
    items: list[Item]
    total: Decimal = Field(gt=0, decimal_places=2)

    @field_validator('retailer')
    def strip_retailer(cls, value: str) -> str:
        return value.strip()


class ReceiptIDResponse(BaseModel):
    id: UUID4

class PointsResponse(BaseModel):
    points: int