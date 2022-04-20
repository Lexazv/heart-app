# import pytest
# from fastapi.testclient import TestClient

# from main import app
# from database import get_db
# from tests.data.users import (
#     VALID_USER_DATA, INVALID_ERROR_RESPONSE, USER_PROFILE
# )
# from conftest import (
#     manage_test_db, get_test_db, create_test_user, get_access_token
# )


# app.dependency_overrides[get_db] = get_test_db

# client = TestClient(app)


# def test_welcome():
#     response = client.get('/users/hello')

#     assert response.status_code == 200
#     assert response.json() == {
#         'message': 'Hello! This is a service for heart disease prediction!'
#     }


# def test_create_user(manage_test_db):
#     response = client.post('/users/register', json=VALID_USER_DATA)

#     assert response.status_code == 201
#     assert response.json() == {
#         'login': 'testlogin',
#         'created_on': response.json().get('created_on')
#     }


# def test_create_existing_user(manage_test_db):
#     create_test_user(db=get_test_db())
#     response = client.post('/users/register', json=VALID_USER_DATA)

#     assert response.status_code == 400
#     assert response.json() == {
#         'detail': 'user with entered email already exists'
#     }


# @pytest.mark.parametrize(
#     'test_invalid_data, msg',
#     [
#         ({'login': '123'}, 'invalid login'),
#         ({'login': 'abc'}, 'invalid login'),
#         ({'email': 'testemail'}, 'invalid email'),
#         ({'email': 'testemail@'}, 'invalid email'),
#         ({'password': 'testpsw'}, 'insecure password'),
#         (
#             {'password': 'psw2', 'confirmed_password': 'psw1'},
#             'insecure password'
#         )
#     ]
# )
# def test_create_user_exception(manage_test_db, test_invalid_data, msg):
#     request_template = VALID_USER_DATA.copy()

#     for field in test_invalid_data:
#         request_template[field] = test_invalid_data[field]

#     response = client.post('/users/register', json=request_template)

#     assert response.status_code == 422
#     assert msg == INVALID_ERROR_RESPONSE['detail'][0]['msg']


# def test_login_user(manage_test_db):
#     create_test_user(db=get_test_db())
#     response = client.post(
#         '/users/login',
#         json={
#             'login': VALID_USER_DATA.get('login'),
#             'password': VALID_USER_DATA.get('password')
#         }
#     )
#     token = response.json().get('token')

#     assert response.status_code == 200
#     assert response.json() == {'token': token}


# def test_login_non_existing_user(manage_test_db):
#     create_test_user(db=get_test_db())
#     response = client.post(
#         '/users/login', json={'login': 'abc', 'password': '123'}
#     )

#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Not Found'}


# def test_get_user_profile(manage_test_db):
#     test_user = create_test_user(db=get_test_db())

#     token = get_access_token(client=client)
#     response = client.get(f'/users/{test_user.id}', headers={'token': token})

#     assert response.status_code == 200
#     assert response.json() == USER_PROFILE


# def test_get_non_existing_user_profile(manage_test_db):
#     create_test_user(db=get_test_db())

#     token = get_access_token(client=client)
#     response = client.get(f'/users/19999', headers={'token': token})

#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Not Found'}


# def test_unauth_get_user_profile(manage_test_db):
#     response = client.get(f'/users/19999')

#     assert response.status_code == 401
#     assert response.json() == {'detail': 'Unauthorized'}
