from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    name: str
    email: str
    password: str

#to do list:
    #1. get one user by email
    #2. update one user in the list

    #3. patch one property from one user
    #4. delete one user from the list

class UpdateBody(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None



@app.post('/user/')
async def create_user(user: User):
    users.append(user)
    return user


@app.get('/user/{email}')
async def get_user(email):
    for user in users:
       if user.email == email:
           return user 
       

@app.get('/users/') 
async def get_users():
    return users


@app.delete('/user/{email}')
async def delete_user(email):
    for CurrentUser in users:
        if CurrentUser.email == email:
            users.remove(CurrentUser)
            return CurrentUser


@app.put('/user/')
async def update_user(name: str, email: str, password: str):
    for currentUser in users:
        if currentUser.email == email:
            currentUser.name = name
            currentUser.password = password
            currentUser.email = email
            return currentUser

@app.patch('/user/{email}')
async def patch_user(email: str, body: UpdateBody):
    for currentUser in users:
        if currentUser.email == email:
            currentUser.name = body.name
            return currentUser
        f