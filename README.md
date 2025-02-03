# test_suite

A practice repo for UI (Selenium + Pytest), API Testing (Pytest + Requests) and Healenium Integration

Mock API used: https://dummyjson.com



```
get all users
GET https://dummyjson.com/users?limit=4

get user token for user1
POST https://dummyjson.com/auth/login
{
  "username": "emilys",
  "password": "emilyspass"
}

response:
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3Mzg2MDIyOTYsImV4cCI6MTczODYwNTg5Nn0.6_2WxpBNEc_nzZSAkqxmbyonVz7iZaIPKPc_itibbuA",
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3Mzg2MDIyOTYsImV4cCI6MTc0MTE5NDI5Nn0.LkYlTIytD8ZWq0Hr09pVVeA3TxF4nI2bcsWSS3ctkiw",
  "id": 1,
  "username": "emilys",
  "email": "emily.johnson@x.dummyjson.com",
  "firstName": "Emily",
  "lastName": "Johnson",
  "gender": "female",
  "image": "https://dummyjson.com/icon/emilys/128"
}


get current user

get single user

search users

filter users

create user
fetch('https://dummyjson.com/users/add', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    firstName: 'Muhammad',
    lastName: 'Ovi',
    age: 250,
    /* other user data */
  })
})
.then(res => res.json())
.then(console.log);

Update user
/* updating lastName of user with id 2 */
fetch('https://dummyjson.com/users/2', {
  method: 'PUT', /* or PATCH */
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    lastName: 'Owais'
  })
})
.then(res => res.json())
.then(console.log);


Delete user
fetch('https://dummyjson.com/users/1', {
  method: 'DELETE',
})
.then(res => res.json())
.then(console.log);
```