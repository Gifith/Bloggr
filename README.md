# Bloggr

A back-end API using Flask framework
built at IMIE/Caen

## How to use

What follows will help you to build this API on your own computer

### Prerequites

Python 2.7 :
 * [Python](https://www.python.org)
 
Pip :
* [Pip](https://pypi.org/project/pip/)


### Installation

1. Build dependancies

```
All pip's dependances are located in requirements.txt
```


2. Acessing our app

```
Using a console, move to the project folder then execute server.py with Python 2 >= 2.7
```

##### Sessions

### Init session
* **URL:** /tokens
* **Description:** Request a session token to uses other api endpoints.
* **Method:** POST
* **headers:** Content-type: application/json
* **Returns:** 
200 (OK) with token as payload
401(UNAUTHORIZED)

### Kill session
* **URL:** /tokens
* **Description:** Destroys a session identified by a session token.
* **Method:** DELETE
* **headers:** 
Content-type: application/json \n
Authorization : given valid webtoken
* **Returns:** 
204 (no content) 
410 (Gone)

##### Posts

### List posts
* **URL:** /posts/list
* **Description:** Return the list of existing posts.
* **Method:** GET
* **headers:** 
Content-type: application/json \n
Authorization : given valid webtoken
* **Returns:** 
200 (ok)
payload: TODO

### Get a post
* **URL:** /posts/:id
* **Description:** Return the post datas identified by the given id 
* **Method:** GET
* **headers:** 
Content-type: application/json \n
Authorization : given valid webtoken
* **Returns:** 
200 (ok) 
payload: TODO

### Create a post
* **URL:** /posts/
* **Description:** Create a post with the datas sent as payload
* **Method:** POST
* **headers:** 
Content-type: application/json \n
Authorization : given valid webtoken
* **body** *:
title = string
corpus = string
imagelink = string
tags = string : tags separated with commas
isActive = boolean
* **Returns:** 
200 (ok) 
payload: TODO

### Delete a post
* **URL:** /posts/:id
* **Description:** Delete the post identified by the given id
* **Method:** DELETE
* **headers:** 
Content-type: application/json \n
Authorization : given valid webtoken
* **Returns:** 
204 (no content)
410 (gone)
payload: TODO


#### GET /users/login

Login user to our API

#### Request:

#### Body:

```
{
    "username" : " Username",
    "password" : " Your password "
}
```
#### Response: 
200 (OK) | 302 (FOUND)

#### Body:

200 (OK)
```
{
    "token": " JWT Token"
}
```

#### GET /users/register

Add a user to our API

#### Request:

#### Body:
```
{
    "username": " Username",
    "email" : " Mail",
    "password" : " Your password "
}
```

#### POST /users/saving

Add a given user to the database

#### Request:

#### GET /users/list

Return a list of all users

#### Request:

#### Body:
```
{
    User
    {
        email: " mail of a given user",
        username: "username of a given user"
    },
    ...
}
```

#### GET /users/reset

Send an email to a given username/email combo

#### Request:

#### Body:
```
{
    "username" : " Username",
    "email" : " Email"
}

```

#### POST /users/reset

reset password of a given user

#### Request:

#### Body:
```
{
    "pass": "new password"
    "confirm": "new password again"
}
```


### Authors

* **Clément T**
* **Martin M**
* **Quentin T**


