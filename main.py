from fastapi import FastAPI
from firebase_auth_implementation import router as firebase_auth_router
app = FastAPI()
app.include_router(firebase_auth_router)


