from fastapi import FastAPI, HTTPException
from config import get_database
from analytics import SurveyAnalytics
import py_eureka_client.eureka_client as eureka_client


EUREKA_SERVER = "http://ec2-13-216-183-248.compute-1.amazonaws.com:8761/eureka/"
SERVICE_NAME = "survey-analytics-service"
SERVICE_PORT = 8000

eureka_client.init(
    eureka_server=EUREKA_SERVER,
    app_name=SERVICE_NAME,
    instance_port=SERVICE_PORT,
    instance_host="ec2-13-216-183-248.compute-1.amazonaws.com"
)

app = FastAPI(title="Survey Analytics API")

try:
    db = get_database()
    analytics = SurveyAnalytics(db)
except Exception as e:
    print(f"Error iniciando la aplicación: {e}")
    raise e

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

@app.get("/analytics/trend/{days}")
async def get_trend_analytics(days: int = 30):
    try:
        return analytics.get_trend_analysis(days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=SERVICE_PORT, reload=True)
