
**To run**
          uvicorn main:app --reload

*Structure of project look like this*

``` txt
.
├── README.md
├── alembic
├── core
│   ├── models
│   │   └── database.py
│   ├── schemas
│   │   └── schema.py
│   ├── settings.py
│   └── views
│       └── v1_views.py
├── dependencies.py
├── main.py
├── templates
│   └── index_v1.html
├── tests
│   ├── v2
│   └── vi
│       └── test_vi.py
└── v1
    ├── api.py
    └── endpoints
        └── endpoints.py
```

Let's the folders into parts:

-   **Core**
    -   **models**
        -   **database.py**
    -   **schemas**
        -   **users.py**
        -   **something.py**
    -   **settings.py**
    -   **views**  _(Add this if you are going to render templates)_
        -   **v1_views.py**
        -   **v2_views.py**
-   **tests**
-   **v1**
-   **v2**

### Models

It is for your database models, by doing this you can import the same database session or object from v1 and v2.

### Schemas

Schemas are your Pydantic models, we call it schemas because it is actually used for creating OpenAPI schemas since FastAPI is based on OpenAPI specification we use schemas everywhere, from Swagger generation to endpoint's expected request body.

### settings.py

It is for  [Pydantic's Settings Management](https://pydantic-docs.helpmanual.io/usage/settings/)  which is extremely useful, you can use the same variables without redeclaring it, to see how it could be useful for you check out our documentation for  [Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)

### Views

This is optional if you are going to render your frontend with Jinja, you can have something close to MVC pattern

-   **Core**
    -   **views**
        -   **v1_views.py**
        -   **v2_views.py**

It would look something like this if you want to add views.

### Tests

It is good to have your tests inside your backend folder.

### APIs

Create them independently by APIRouter, instead of gathering all your APIs inside one file.

### Notes

You can use absolute import for all your importing since we are using  `__init__`  everywhere, see  [Python's packaging](https://docs.python.org/3/tutorial/modules.html#packages)  docs.

So assume you are trying to import  **v1's endpoint.py**  from  **v2**, you can simply do

```python
from my_project.v1.endpoints.endpoint import something
```