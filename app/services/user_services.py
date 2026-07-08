
from fastapi import HTTPException
from app.models.user_model import User
from app.utils.auth import pass_hash, create_access_token, verify_password

# create user
def create_user(db, user):
    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Create new user
    new_user = User(
        name=user.name,
        email=user.email,
        password=pass_hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# user login 
def login_user(db, user):
    # Find user by email
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Generate JWT token
    token = create_access_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# delete users
def delete_user(db, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }

