from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserResponse, UserCreate, UserLogin
from app.core.dbsession import get_db
from app.services.user_services import create_user, login_user, delete_user
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post('/', response_model=UserResponse)
def add_user(
    user : UserCreate,
    db:Session=Depends(get_db)
): 
    return create_user(db, user)

@router.post('/login')
def login(
    user: UserLogin,
    db:Session=Depends(get_db)
):
    return login_user(db, user)


@router.delete("/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)