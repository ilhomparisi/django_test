# Django Single Page CRUD Application

A single-page CRUD (Create, Read, Update, Delete) application built with Django and vanilla JavaScript.

## Features

- **Single Page Application**: No page refreshes required for CRUD operations
- **Modern UI**: Clean, responsive design with Bootstrap-like styling
- **Real-time Updates**: Instant feedback for all operations
- **Uzbek Interface**: Complete Uzbek language support
- **Docker Support**: Containerized deployment ready

## Container Name

**Ilhom aka veb sayti. AIFU 2-semestr dasturiy injiniring**

## Technologies Used

- **Backend**: Django 4.2+
- **Frontend**: HTML, CSS, JavaScript (ES6+)
- **Database**: SQLite (default), PostgreSQL (Docker)
- **Server**: Gunicorn
- **Containerization**: Docker, Docker Compose

## Installation

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd crud_project
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://localhost:8000`

### Docker Deployment with Dokploy

1. Build and run with Docker:
```bash
docker build -t django-crud-app .
docker run -p 8000:8000 django-crud-app
```

2. For Dokploy deployment:
   - Use the provided Dockerfile
   - Set environment variables in Dokploy dashboard
   - Application will be available at your configured domain

3. The application will be available at your configured domain

## Usage

The application provides a simple interface to manage items with the following operations:

- **Create**: Add new items with name and description
- **Read**: View all items in a table format
- **Update**: Edit existing items
- **Delete**: Remove items with confirmation

## API Endpoints

- `GET /api/items/` - Get all items
- `POST /api/items/create/` - Create new item
- `PUT /api/items/{id}/update/` - Update item
- `DELETE /api/items/{id}/delete/` - Delete item

## Project Structure

```
crud_project/
├── items/
│   ├── models.py          # Django models
│   ├── views.py           # API views
│   ├── urls.py            # URL patterns
│   └── templates/
│       └── items/
│           └── index.html # Single page application
├── crud_project/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI application
├── Dockerfile             # Docker configuration optimized for Dokploy
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## Docker Commands for Dokploy

### Build and Run
```bash
docker build -t django-crud-app .
```

### Run locally for testing
```bash
docker run -p 8000:8000 django-crud-app
```

### View Logs
```bash
docker logs <container-id>
```

### Stop Container
```bash
docker stop <container-id>
```

## Environment Variables for Dokploy

When deploying with Dokploy, configure these environment variables:

- `DEBUG=0` - Disable debug mode in production (set in Dockerfile)
- `SECRET_KEY` - Django secret key (set in Dokploy environment variables)
- `DATABASE_URL` - Database connection string (if using external database)
- `ALLOWED_HOSTS` - Your domain name (set in Dokploy environment variables)

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support and questions, please contact the development team.