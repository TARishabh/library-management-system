# Library Management System

This project provides a comprehensive system for managing a library's collection and user interactions. It's built with Python's Django web framework, making it efficient and scalable.

## Features

### Manage Users:
- Create, view, update, and delete user accounts.
- Assign librarian roles for managing the system (optional, based on your needs).

### Manage Books:
- Add new books to the library, including titles, authors, ISBNs, genres, publication dates, quantities, and descriptions.
- View details of existing books.
- Update book information as needed.
- Keep track of the number of copies available for each book.

### Issue Books:
- Lend books to registered users.
- Specify due dates for borrowed books.
- (Optional) Implement functionalities for tracking returned books, renewals, and overdue notices.

### Explore Additional Features:
- You can extend this system to include functionalities like searching for books, managing user accounts and borrowing history, adding categories, and generating reports.

## Getting Started

### Prerequisites:
- Python (version 3.x recommended)
- pip (Python package manager)
- A code editor or IDE (e.g., Visual Studio Code, PyCharm)

### Installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/TARishabh/library-management-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd library-management-system
    ```

3. Create a virtual environment (recommended for isolating project dependencies):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate.bat
    ```

4. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration:

1. Create a local copy of `settings.py.example` and name it `settings.py`.
2. Update the database settings in `settings.py` with your database credentials (e.g., username, password, host, etc.).

### Database Migrations:

Apply database migrations to create the tables needed for the system:
```bash
python manage.py makemigrations
python manage.py migrate

```

Run the Development Server:
Start the Django development server:
```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your web browser to access the API endpoints.


views.py file flow:
Assume you have called the api http://127.0.0.1:8000/ with get request (list action), now the flow is:
Request Handling:

When a GET request for listing users (/api/users/) is received, Django REST framework maps this to the list() method of ListModelMixin.

Django REST Framework Flow:

The request enters the list() method of ListModelMixin, which then delegates to the appropriate method based on the HTTP method.
In a GET request for listing (list() action), it will call get_queryset() to retrieve the queryset of User objects.
get_queryset() Method:

The get_queryset() method of UserViewSet is called. It executes super().get_queryset(), which returns the queryset defined at the class level (User.objects.all()). Example:

def get_queryset(self):
    queryset = super().get_queryset()  # Returns User.objects.all()
    return queryset

Serializer and Pagination:

After retrieving the queryset, Django REST framework prepares to serialize the queryset using UserSerializer.
Pagination is applied if configured (TaskPagination).
Custom Renderer Context:

Before rendering the response, Django REST framework calls get_renderer_context() of UserViewSet.
In get_renderer_context(), it updates the renderer context with message and status_code based on the response_data dictionary for list action.
CustomRenderer Class:

Finally, the response data is passed to CustomRenderer.render() method.
Inside CustomRenderer.render(), it retrieves the message and status_code from renderer_context.
Constructs a response dictionary including message, status, code, data, and optionally page_info if present in the response data.
If the status code does not start with '2' (indicating success), it adjusts the response to mark it as an error.
Response:

The constructed response dictionary is rendered into JSON format by CustomRenderer, ensuring consistent formatting and including custom messages and status codes.
