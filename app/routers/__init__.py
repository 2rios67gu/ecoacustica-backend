from . import audio, especie, espectrograma, segmentacion, resultado_identificacion, historial_espectrograma

routers = [
    audio.router,
    especie.router,
    espectrograma.router,
    segmentacion.router,
    resultado_identificacion.router,
    historial_espectrograma.router,
]
