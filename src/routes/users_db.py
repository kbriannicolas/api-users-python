from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schemas, users_schemas
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix='/users', tags=['Users'], responses={
                   status.HTTP_404_NOT_FOUND: {'message': 'not found'}})


@router.get('/')
async def users():
    return users_schemas(db_client.users.find())


@router.get('/{id}')
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def newuser(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="the user already exists")

    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schemas(db_client.users.find_one({'_id': id}))
    return User(**new_user)


@router.put("/", response_model=User)
async def userupdate(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    try:
       db_client.users.find_one_and_replace({'_id':ObjectId(user.id)},user_dict)
    except:
        return {"error": "The user could not update"}

    return search_user('_id',ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def userdelete(id: str):
    found = db_client.users.find_one_and_delete({'_id': ObjectId(id)})
    if not found:
        return {"error": "The user could not delete"}


def search_user(field: str, key):

    try:
        user = user_schemas(db_client.users.find_one({field: key}))
        return User(**user)
    except:
        return {"error": "user undefined"}