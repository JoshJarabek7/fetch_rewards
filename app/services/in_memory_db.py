from uuid import uuid4, UUID
from app.schemas.receipt import Receipt

class InMemoryDB:
    def __init__(self):
        self._data: dict[UUID, Receipt] = {}
    
    def add_receipt(self, receipt: Receipt) -> UUID:
        receipt_id = uuid4()
        self._data[receipt_id] = receipt
        return receipt_id
    
    def get_receipt(self, receipt_id: UUID) -> Receipt:
        return self._data.get(receipt_id)
    
    def get_all_receipts(self) -> dict[UUID, Receipt]:
        return self._data
    
db_instance = InMemoryDB()