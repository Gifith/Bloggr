# Bloggr

Application back-end avec le micro framework Flask
crée dans le cadre de notre cursus informatique à l'IMIE/Caen

## Utiliser le dépot

Ces instructions vous permettront d'obtenir une copie du projet à faire fonctionner sur votre machine pour des fins de développement et de test

### Prérequis

Python 2.7 :
 * [Python](https://www.python.org)
 
Pip :
* [Pip](https://pypi.org/project/pip/)


### Installation

1. Installer les dépendances

```
Récupérer toutes les dépendance du projet dans le fichier requirements.txt
```


2. Accéder à l'application

```
Avec un terminal de commande, déplacez vous dans le dossier du projet puis executer server.py avec Python 2.7
```

### Session API

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


### Auteurs

* **Clément T**
* **Martin M**
* **Quentin T**


