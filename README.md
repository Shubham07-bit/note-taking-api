
# Note Taking API

This is a RESTful API for a simple note-taking application built using Django and Django Rest Framework (DRF). The API provides endpoints to create, fetch, query, and update notes. Swagger UI has been integrated to allow for easy testing of the API, along with endpoint documentation.

## Features

- Create, retrieve, update, and delete notes.
- Query notes based on the title.
- Swagger and Redoc integration for API documentation.

## Models

- **Note**: Contains fields for title, content, created_at, and updated_at.

## Endpoints

- `GET /notes/`: List all notes.
- `POST /notes/`: Create a new note.
- `GET /notes/{id}/`: Retrieve a note by ID.
- `PUT /notes/{id}/`: Update a note by ID.
- `DELETE /notes/{id}/`: Delete a note by ID.
- `GET /notes/query/?title={title}`: Search notes by title.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- PostgreSQL (for database setup)
- Virtualenv (recommended)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Shubham07-bit/note-taking-api.git
   cd note-taking-api
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   env\Scripts\activate   # On Linux use `source env/bin/activate`
   ```

3. **Install the required dependencies**:
   ```bash
   cd mysite
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**(or you can just comment out these lines in settings.py file):

   Ensure PostgreSQL is installed and running. Create a database named `notes` and configure the user and password in the `DATABASES` section of the `settings.py` file:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'notes',
           'USER': 'postgres',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
       }
   }
   ```

5. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Swagger UI**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/swagger/
   ```

8. **Access the API**:
   The base URL for the API is:
   ```
   http://127.0.0.1:8000/notes/
   ```

## Contact

For any inquiries, please contact [shubhamjolapara256@gmail.com](mailto:shubhamjolapara256@gmail.com).
