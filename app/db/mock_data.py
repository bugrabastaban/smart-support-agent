# app/db/mock_data.py

mock_orders = {
    "TR1001": {
        "customer_email": "ahmet@gmail.com",
        "status": "Kargoda",
        "expected_delivery": "2026-04-14",
        "items": ["Kablosuz Kulaklık", "Telefon Kılıfı"],
        "total_price": 650.00,
        "is_delayed": False
    },
    "TR1002": {
        "customer_email": "ayse@gmail.com",
        "status": "Teslim Edildi",
        "expected_delivery": "2026-04-10",
        "items": ["Spor Ayakkabı"],
        "total_price": 1250.00,
        "is_delayed": False
    },
    "TR1003": {
        "customer_email": "mehmet@gmail.com",
        "status": "Hazırlanıyor",
        "expected_delivery": "2026-04-09",
        "items": ["Mekanik Klavye"],
        "total_price": 2400.00,
        "is_delayed": True
    }
}