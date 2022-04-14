# import os

# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
# from fastapi.testclient import TestClient


# from database import Base
# from app.models import User
# from Users.auth import get_password_hash
# from tests.tests_data import VALID_USER_DATA
# # from config import TEST_DATABASE_URL


# engine = create_engine(
#     TEST_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def get_test_db():
#     return SessionLocal()


# @pytest.fixture
# def manage_test_db():
#     Base.metadata.create_all(bind=engine)
#     yield
#     os.unlink('test_db.db')


# def create_test_user(db: Session) -> User:
#     user_data = VALID_USER_DATA.copy()

#     user_data['password'] = get_password_hash(user_data['password'])
#     user_data.pop('confirmed_password')

#     new_user = User(**user_data)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# def get_access_token(client: TestClient) -> dict:
#     response = client.post(
#         '/users/login',
#         json={
#             'login': VALID_USER_DATA.get('login'),
#             'password': VALID_USER_DATA.get('password')
#         }
#     )
#     return response.json().get('token')
