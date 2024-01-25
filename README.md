uvicorn main:app --reload

Let's the folders into parts:

Core
models
database.py
schemas
users.py
something.py
settings.py
views (Add this if you are going to render templates)
v1_views.py
v2_views.py
tests
v1
v2
Models
It is for your database models, by doing this you can import the same database session or object from v1 and v2.

Schemas
Schemas are your Pydantic models, we call it schemas because it is actually used for creating OpenAPI schemas since FastAPI is based on OpenAPI specification we use schemas everywhere, from Swagger generation to endpoint's expected request body.

settings.py
It is for Pydantic's Settings Management which is extremely useful, you can use the same variables without redeclaring it, to see how it could be useful for you check out our documentation for Settings and Environment Variables

Views
This is optional if you are going to render your frontend with Jinja, you can have something close to MVC pattern

Core
views
v1_views.py
v2_views.py
It would look something like this if you want to add views.

Tests
It is good to have your tests inside your backend folder.

APIs
Create them independently by APIRouter, instead of gathering all your APIs inside one file.

Notes
You can use absolute import for all your importing since we are using __init__ everywhere, see Python's packaging docs.

So assume you are trying to import v1's endpoint.py from v2, you can simply do

from my_project.v1.endpoints.endpoint import something