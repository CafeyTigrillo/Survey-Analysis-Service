from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from typing import Dict, List, Any

class SurveyAnalytics:
    def __init__(self, db):
        self.db = db
        self.collection = db.surveys

    def get_basic_stats(self) -> Dict[str, Any]:

        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "promedio": {"$avg": "$satisfaction"},
                    "total_encuestas": {"$sum": 1},
                    "valores": {"$push": "$satisfaction"},
                    "min": {"$min": "$satisfaction"},
                    "max": {"$max": "$satisfaction"}
                }
            }
        ]
        
        result = list(self.collection.aggregate(pipeline))
        if not result:
            return {
                "error": "No se encontraron datos de encuestas"
            }
            
        result = result[0]
        valores = result["valores"]
        
        return {
            "promedio": round(result["promedio"], 2),
            "total_encuestas": result["total_encuestas"],
            "moda": int(pd.Series(valores).mode()[0]),
            "min": result["min"],
            "max": result["max"],
            "desviacion_estandar": round(np.std(valores), 2)
        }
        
        distribution = list(self.collection.aggregate(pipeline))
        if not distribution:
            return {"error": "No se encontraron datos"}
            
        total = sum(item["count"] for item in distribution)
        
        result = {}
        for i in range(1, 6):
            found = next((item for item in distribution if item["_id"] == i), None)
            count = found["count"] if found else 0
            result[str(i)] = {
                "count": count,
                "percentage": round((count / total) * 100, 2) if total > 0 else 0
            }
            
        return result

    def get_trend_analysis(self, days: int = 30) -> List[Dict[str, Any]]:

        date_limit = datetime.now() - timedelta(days=days)
        
        pipeline = [
            {
                "$match": {
                    "timestamp": {"$gte": date_limit}
                }
            },
            {
                "$group": {
                    "_id": {
                        "año": {"$year": "$timestamp"},
                        "mes": {"$month": "$timestamp"},
                        "dia": {"$dayOfMonth": "$timestamp"}
                    },
                    "promedio_diario": {"$avg": "$satisfaction"},
                    "total_encuestas": {"$sum": 1},
                    "min_satisfaction": {"$min": "$satisfaction"},
                    "max_satisfaction": {"$max": "$satisfaction"}
                }
            },
            {"$sort": {"_id.año": 1, "_id.mes": 1, "_id.dia": 1}}
        ]
        
        results = list(self.collection.aggregate(pipeline))
        
        formatted_results = []
        for result in results:
            formatted_results.append({
                "fecha": f"{result['_id']['año']}-{result['_id']['mes']}-{result['_id']['dia']}",
                "promedio": round(result["promedio_diario"], 2),
                "total_encuestas": result["total_encuestas"],
                "min": result["min_satisfaction"],
                "max": result["max_satisfaction"]
            })
            
        return formatted_results
