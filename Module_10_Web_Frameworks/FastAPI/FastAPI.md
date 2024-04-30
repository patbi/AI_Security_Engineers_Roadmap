- FastAPI ( What we will Learn )

```bash

A super fast Python Web Framework

```

- Automatic docs

```bash

- Swagger UI

- ReDoc

```
- Just Modern Python

```bash

Python 3.6 with type using Pydantic

from typing import List, Dict
from datetime import date

from pydantic import BaseModel

# Declare a variable as a str
# and get editor support inside the function

def main(user_id str):
	return user_id


# A Pydantic model

class User(BaseModel):
	id: int
	name: str
	joined: date

```

- Based on open standards

```bash

- JSON Schema

- Open API

```

- Editors

```bash

- Vscode Editor support

- PyCharm Editor support 

```

- Security and authentication

```bash

- HTTP Basic

- OAuth2 (also with JWT tokens)

- API keys in

	- Headers
	- Query parameters
	- Cookies, etc

```

- Dependency 
- Injection Unlimited "plug-ins" 
- Tested


```bash

- Starlette Features:

	- WebSocked support
	- GraphQL support
	- In-process background tasks
	- Startup and shutdown events
	- Test client built on requests
	- CORS, GZip, Static Files, Streaming responses
	- Session and Cookie support
```


- Other Supports

```bash
- SQL databases

- NoSQL databases

- GraphQL
```


- Getting Started

```bash

- Install And Setup

- Break it down, how it structured
```


- Basics Concepts

```bash

- Path Parameters

- API Docs - swagger/redocs

- Query parameters

- Request body

```


- Intermediate Concepts


```bash

- Debugging FastAPI

- Pydantic Schemas

- SqlAlchemy database connection

- Models and table

```


- Database Tasks


```bash

- Store blog to database

- Get blogs from database

- Delete

- Update

```



- Responses

```bash

- Handling Exceptions

- Return response

- Define response model

```


- User and Password

```bash

- Create user

- Hash user password

- Show single user

- Define docs tags

```


- Relationship

```bash

- Define User to Blog relationship

- Define blog to user relationship

```


- Refactor for bigger Application

```bash

- API Router

- API Router with parameters

```


- Authentication using JWT

```bash

- Create Login route

- Login and verify password

- Return JWT access token

- Routes behind authentication

```


- Deploy FastAPI ( Website )