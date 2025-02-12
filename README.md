# SurveyAnalytics 📊

**SurveyAnalytics** es una clase en Python diseñada para analizar encuestas de satisfacción de clientes almacenadas en una base de datos MongoDB. Proporciona estadísticas clave, distribuciones de respuestas y análisis de tendencias para mejorar la toma de decisiones basada en datos.

## 🚀 Características

🔹 **Estadísticas básicas**: Obtiene promedio, moda, mínimo, máximo y desviación estándar de las respuestas.

🔹 **Distribución de respuestas**: Calcula el porcentaje de encuestas que corresponden a cada nivel de satisfacción (1-5).

🔹 **Análisis de tendencias**: Evalúa cómo han evolucionado las respuestas en los últimos días, permitiendo detectar cambios en la percepción de los clientes.

## 🛠️ Uso

### 1️⃣ Inicialización
Para comenzar a usar la clase, debes instanciar `SurveyAnalytics` pasando una conexión válida a la base de datos MongoDB:
```python
from pymongo import MongoClient

db = MongoClient()["nombre_de_tu_base_de_datos"]
analytics = SurveyAnalytics(db)
```

### 2️⃣ Obtener estadísticas básicas
```python
stats = analytics.get_basic_stats()
print(stats)
```
📌 **Ejemplo de salida:**
```json
{
  "promedio": 4.2,
  "total_encuestas": 150,
  "moda": 5,
  "min": 2,
  "max": 5,
  "desviacion_estandar": 0.8
}
```

### 3️⃣ Obtener distribución de respuestas
```python
distribution = analytics.get_distribution()
print(distribution)
```
📌 **Ejemplo de salida:**
```json
{
  "1": {"count": 5, "percentage": 3.33},
  "2": {"count": 10, "percentage": 6.67},
  "3": {"count": 20, "percentage": 13.33},
  "4": {"count": 40, "percentage": 26.67},
  "5": {"count": 75, "percentage": 50.00}
}
```

### 4️⃣ Obtener análisis de tendencias
```python
trend = analytics.get_trend_analysis(30)
print(trend)
```
📌 **Ejemplo de salida:**
```json
[
  {"fecha": "2025-02-01", "promedio": 4.3, "total_encuestas": 10, "min": 3, "max": 5},
  {"fecha": "2025-02-02", "promedio": 4.1, "total_encuestas": 12, "min": 2, "max": 5}
]
```

---

📈 **SurveyAnalytics te permite comprender mejor la experiencia del cliente y tomar decisiones informadas basadas en datos reales. ¡Optimiza tu negocio con datos confiables!** 🚀

