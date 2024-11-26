"""
This module contains tests for the receipt processing API endpoints.
"""

import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
from app.main import app


@pytest.mark.asyncio
async def test_process_receipt():
    """
    Tests the receipt processing endpoint to ensure it returns a valid receipt ID.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-02",
            "purchaseTime": "13:13",
            "total": "1.25",
            "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
        }

        response = await ac.post("/receipts/process", json=receipt_data)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "id" in data


@pytest.mark.asyncio
async def test_get_receipt_points():
    """
    Tests the endpoint for retrieving points to ensure it returns the correct points for a receipt.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-02",
            "purchaseTime": "13:13",
            "total": "1.25",
            "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
        }
        process_response = await ac.post("/receipts/process", json=receipt_data)
        receipt_id = process_response.json()["id"]

        points_response = await ac.get(f"/receipts/{receipt_id}/points")
        assert points_response.status_code == status.HTTP_200_OK
        points_data = points_response.json()
        assert "points" in points_data
        assert isinstance(points_data["points"], int)


@pytest.mark.asyncio
async def test_example_receipt_1():
    """
    Tests the receipt processing and points calculation for the first example receipt.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
                {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
                {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
                {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
                {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
            ],
            "total": "35.35"
        }
        process_response = await ac.post("/receipts/process", json=receipt_data)
        receipt_id = process_response.json()["id"]

        points_response = await ac.get(f"/receipts/{receipt_id}/points")
        assert points_response.status_code == status.HTTP_200_OK
        points_data = points_response.json()
        assert points_data["points"] == 28


@pytest.mark.asyncio
async def test_example_receipt_2():
    """
    Tests the receipt processing and points calculation for the second example receipt.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        receipt_data = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
            ],
            "total": "9.00"
        }
        process_response = await ac.post("/receipts/process", json=receipt_data)
        receipt_id = process_response.json()["id"]

        points_response = await ac.get(f"/receipts/{receipt_id}/points")
        assert points_response.status_code == status.HTTP_200_OK
        points_data = points_response.json()
        assert points_data["points"] == 109