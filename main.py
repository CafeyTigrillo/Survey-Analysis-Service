from fastapi import FastAPI, HTTPException
import os
import sys
from typing import Optional

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from config import get_database
from analytics import SurveyAnalytics

app = FastAPI(title="Survey Analytics API")
db = get_database()
analytics = SurveyAnalytics(db)

@app.get("/")
async def root():
    return {"message": "Survey Analytics API is running"}

@app.get("/analytics/basic")
async def get_basic_analytics():
    try:
        result = analytics.get_basic_stats()
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analytics/summary")
async def get_summary():
    try:
        return analytics.get_summary_report()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)