from fastapi import FastAPI
from app.routers import especie, audio, espectrograma, segmentacion, resultado_identificacion, historial_espectrograma
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # para pruebas locales
    "https://ecoacustica-website-ziUK5fgyIEW.vercel.app",  # dominio en Vercel
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(especie.router)
app.include_router(audio.router)
app.include_router(espectrograma.router)
app.include_router(segmentacion.router)
app.include_router(resultado_identificacion.router)
app.include_router(historial_espectrograma.router)
from app.database.session import get_db 

@app.get("/")
def read_root():
    return {"message": "API ecoacústica iniciada correctamente"}
