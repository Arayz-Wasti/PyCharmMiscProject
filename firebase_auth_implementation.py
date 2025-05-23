import pyrebase
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/api",
    tags=["firebase_auth"]
)
firebase_auth_config = {
    "apiKey": "AIzaSyC45JXA5uq-wmqtdFDoRTxy3eViHpZGvJg",
    "authDomain": "authimplementation-7f86d.firebaseapp.com",
    "databaseURL": "https://authimplementation-7f86d-default-rtdb.firebaseio.com",  # ✅ Add this line!
    "projectId": "authimplementation-7f86d",
    "storageBucket": "authimplementation-7f86d.appspot.com",
    "messagingSenderId": "1076080351662",
    "appId": "1:1076080351662:web:5d813b986598875d5f903f",
    "measurementId": "G-V2JCKKFXGZ"
}

firebase = pyrebase.initialize_app(firebase_auth_config)
auth = firebase.auth()

class SignUpRequest(BaseModel):
    email: str
    password: str

@router.post("/signup")
async def signup(request: SignUpRequest):
    print("Sign Up...")
    try:
        user = auth.create_user_with_email_and_password(request.email, request.password)
        return {"message": "SUCCESS","user": user}
    except Exception as e:
        return {"message": str(e)}

@router.post("/login")
async def login(request: SignUpRequest):
    print("Log In...")
    try:
        user_login = auth.sign_in_with_email_and_password(request.email, request.password)
        return {"message": "SUCCESS","user": user_login}
    except Exception as e:
        return {"message": str(e)}



