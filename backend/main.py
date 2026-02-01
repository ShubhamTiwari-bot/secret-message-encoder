from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.encoder_routes import router

app = FastAPI(title="Secret Message Encoder API")

# Enable CORS for integration with frontend/mobile/apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Secret Message Encoder API is running"}
