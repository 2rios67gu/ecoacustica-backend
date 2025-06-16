# 🌿 Ecoacústica Backend

Este es el backend de la plataforma Ecoacústica, diseñado para procesar audios y espectrogramas utilizando modelos de inteligencia artificial para la segmentación del paisaje acústico y la identificación de especies.

---

## 🚀 Despliegue

Backend desplegado en Render:  
🔗 [`https://ecoacustica-backend.onrender.com/docs`](https://ecoacustica-backend.onrender.com/docs) (Documentación Swagger)

Frontend desplegado en Vercel:  
🔗 [`https://v0.dev/chat/ecoacustica-website-ziUK5fgyIEW`](https://v0.dev/chat/ecoacustica-website-ziUK5fgyIEW)

---

## 🧱 Estructura del proyecto

```bash
ecoacustica-backend/
├── app/
│   ├── core/          # Configuración global y variables de entorno
│   ├── crud/          # Operaciones de base de datos
│   ├── database/      # Conexión a MySQL (Railway)
│   ├── models/        # Modelos SQLAlchemy
│   ├── routers/       # Rutas FastAPI (por módulo)
│   ├── schemas/       # Esquemas Pydantic
│   └── utils/         # Funciones auxiliares
├── main.py            # Punto de entrada FastAPI
├── requirements.txt   # Dependencias
└── README.md          # Documentación del backend
