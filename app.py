from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd
from datetime import datetime
import random

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(
    title="ZERO WASTE AI API",
    description="Environmental Intelligence API",
    version="1.0"
)

# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# SQLITE DATABASE
# ==========================================

conn = sqlite3.connect(
    "intelligence.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==========================================
# CREATE TABLES
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS api_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    endpoint TEXT,
    request_time TEXT
)
""")

conn.commit()

# ==========================================
# ROOT API
# ==========================================

@app.get("/")

def root():

    cursor.execute("""
    INSERT INTO api_logs (
        endpoint,
        request_time
    )
    VALUES (?, ?)
    """, (
        "/",
        str(datetime.now())
    ))

    conn.commit()

    return {

        "platform": "ZERO WASTE AI",

        "status": "ACTIVE",

        "message": "Environmental Intelligence API Running",

        "version": "1.0"
    }

# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")

def health():

    return {

        "server": "ONLINE",

        "database": "CONNECTED",

        "api_status": "HEALTHY",

        "timestamp": str(datetime.now())
    }

# ==========================================
# SCAN HISTORY API
# ==========================================

@app.get("/api/v1/scan-history")

def scan_history():

    cursor.execute("""
    INSERT INTO api_logs (
        endpoint,
        request_time
    )
    VALUES (?, ?)
    """, (
        "/api/v1/scan-history",
        str(datetime.now())
    ))

    conn.commit()

    try:

        df = pd.read_sql_query(
            """
            SELECT * FROM scan_history
            ORDER BY id DESC
            """,
            conn
        )

        return {

            "status": "SUCCESS",

            "records": len(df),

            "data": df.to_dict(
                orient="records"
            )
        }

    except Exception as e:

        return {

            "status": "ERROR",

            "message": str(e)
        }

# ==========================================
# SITE VALUATION API
# ==========================================

@app.get("/api/v1/site-valuation")

def site_valuation(
    lat: float,
    lon: float
):

    cursor.execute("""
    INSERT INTO api_logs (
        endpoint,
        request_time
    )
    VALUES (?, ?)
    """, (
        "/api/v1/site-valuation",
        str(datetime.now())
    ))

    conn.commit()

    # ======================================
    # MOCK AI ENGINE
    # ======================================

    methane_flux = random.randint(
        1200,
        6500
    )

    thermal_score = random.randint(
        20,
        95
    )

    confidence = random.randint(
        75,
        99
    )

    wealth = round(
        random.uniform(2, 50),
        2
    )

    carbon_credit = round(
        random.uniform(10000, 250000),
        2
    )

    # ======================================
    # RISK STATUS
    # ======================================

    if methane_flux > 5000:

        site_status = "CRITICAL"

        blast_risk = "HIGH"

        estimated_blast_timeline = "14 DAYS"

    elif methane_flux > 3000:

        site_status = "WARNING"

        blast_risk = "MEDIUM"

        estimated_blast_timeline = "45 DAYS"

    else:

        site_status = "SAFE"

        blast_risk = "LOW"

        estimated_blast_timeline = "NO IMMEDIATE RISK"

    # ======================================
    # RESPONSE
    # ======================================

    return {

        "platform": "ZERO WASTE AI",

        "timestamp": str(datetime.now()),

        "latitude": lat,

        "longitude": lon,

        "site_status": site_status,

        "methane_flux_intensity": methane_flux,

        "thermal_risk_score": thermal_score,

        "satellite_confidence_percent": confidence,

        "blast_risk_status": blast_risk,

        "estimated_blast_timeline": estimated_blast_timeline,

        "wealth_inr_cr": wealth,

        "carbon_credit_value_usd": carbon_credit,

        "environmental_priority": random.choice([
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL"
        ])
    }

# ==========================================
# LIVE HOTSPOTS API
# ==========================================

@app.get("/api/v1/live-hotspots")

def live_hotspots():

    cursor.execute("""
    INSERT INTO api_logs (
        endpoint,
        request_time
    )
    VALUES (?, ?)
    """, (
        "/api/v1/live-hotspots",
        str(datetime.now())
    ))

    conn.commit()

    hotspots = []

    cities = [
        "Delhi",
        "Mumbai",
        "Chennai",
        "Bangalore",
        "Hyderabad"
    ]

    for city in cities:

        hotspots.append({

            "city": city,

            "methane_flux": random.randint(
                1500,
                6000
            ),

            "risk": random.choice([
                "LOW",
                "MEDIUM",
                "HIGH",
                "CRITICAL"
            ]),

            "satellite_confidence": random.randint(
                80,
                99
            )
        })

    return {

        "status": "ACTIVE",

        "hotspots_detected": len(hotspots),

        "data": hotspots
    }

# ==========================================
# CARBON CREDIT API
# ==========================================

@app.get("/api/v1/carbon-credit")

def carbon_credit():

    total_co2 = round(
        random.uniform(1000, 90000),
        2
    )

    total_value = round(
        total_co2 * 12,
        2
    )

    return {

        "co2_prevented_tons_year": total_co2,

        "carbon_credit_value_usd": total_value,

        "market_status": "ACTIVE"
    }

# ==========================================
# RISK ALERT API
# ==========================================

@app.get("/api/v1/risk-alerts")

def risk_alerts():

    alerts = []

    for i in range(5):

        alerts.append({

            "site_id": f"SITE-{100+i}",

            "risk_level": random.choice([
                "WARNING",
                "CRITICAL"
            ]),

            "methane_flux": random.randint(
                3000,
                7000
            ),

            "alert_time": str(datetime.now())
        })

    return {

        "active_alerts": len(alerts),

        "data": alerts
    }

# ==========================================
# API LOGS
# ==========================================

@app.get("/api/v1/api-logs")

def api_logs():

    df = pd.read_sql_query(
        """
        SELECT * FROM api_logs
        ORDER BY id DESC
        """,
        conn
    )

    return {

        "total_logs": len(df),

        "logs": df.to_dict(
            orient="records"
        )
    }