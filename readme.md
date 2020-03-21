# Course Info REST API Project

A simple REST API for getting the lists of books information, creating, updating and deleting one using 
+ Python 3
+ Django 3
+ Django REST framework

### Endpoints
```/courses``` GET: get all books

```/courses``` POST: create new book

```/courses/id``` PUT/PATCH: update the book (/courses/1)

```/courses/id``` DELETE: delete the book (/courses/1)

#### Sample JSON
```javascript
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "url": "http://localhost:8000/courses/1/",
        "name": "Python Programming for everyone",
        "langauge": "Python",
        "price": "$49"
    },
    {
        "id": 2,
        "url": "http://localhost:8000/courses/2/",
        "name": "Ruby for everyone",
        "langauge": "Ruby",
        "price": "$30"
    },
    {
        "id": 3,
        "url": "http://localhost:8000/courses/3/",
        "name": "Javascript for beginner",
        "langauge": "Javascript",
        "price": "$49"
    },
    {
        "id": 4,
        "url": "http://localhost:8000/courses/4/",
        "name": "React for newbie",
        "langauge": "react",
        "price": "10"
    }
]
```