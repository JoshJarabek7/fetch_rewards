"""
This module defines the API endpoints for processing receipts and retrieving points.
"""

from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from app.schemas.receipt import Receipt, ReceiptIDResponse, PointsResponse
from app.services.in_memory_db import db_instance
from app.services.receipt_service import calculate_points

router = APIRouter(prefix="/receipts")


@router.post("/process", response_model=ReceiptIDResponse)
async def process_receipt(receipt: Receipt):
    """
    Processes a receipt and stores it in the in-memory database.

    Parameters
    ----------
    receipt : Receipt
        The receipt to be processed.

    Returns
    -------
    ReceiptIDResponse
        The response containing the unique identifier of the processed receipt.
    """
    receipt_id = db_instance.add_receipt(receipt)
    return ReceiptIDResponse(id=receipt_id)


@router.get("/{id}/points", response_model=PointsResponse)
async def get_receipt_points(id: UUID):
    """
    Retrieves the points awarded for a given receipt.

    Parameters
    ----------
    id : UUID
        The unique identifier of the receipt.

    Returns
    -------
    PointsResponse
        The response containing the points awarded for the receipt.

    Raises
    ------
    HTTPException
        If the receipt is not found, raises a 404 error.
    """
    receipt = db_instance.get_receipt(id)
    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Receipt not found"
        )

    points = calculate_points(receipt)

    return PointsResponse(points=points)
