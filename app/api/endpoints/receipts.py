from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from app.schemas.receipt import Receipt, ReceiptIDResponse, PointsResponse
from app.services.in_memory_db import db_instance
from app.services.receipt_service import calculate_points

router = APIRouter(prefix="/receipts")

@router.post("/process", response_model=ReceiptIDResponse)
async def receipts_process_route(receipt: Receipt):
    receipt_id = db_instance.add_receipt(receipt)
    return ReceiptIDResponse(id=receipt_id)

@router.get("/{id}/points", response_model=PointsResponse)
async def get_receipt_points(id: UUID):
    receipt = db_instance.get_receipt(id)
    if not receipt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receipt not found")
    
    points = calculate_points(receipt)
    
    return PointsResponse(points=points)