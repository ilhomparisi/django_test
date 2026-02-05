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

### Docker Deployment

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

2. The application will be available at `http://localhost:8000`

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
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## Docker Commands

### Build and Run
```bash
docker-compose up --build
```

### Run in Background
```bash
docker-compose up -d
```

### View Logs
```bash
docker-compose logs -f
```

### Stop Services
```bash
docker-compose down
```

### Clean Up
```bash
docker-compose down --volumes --remove-orphans
```

## Environment Variables

When using Docker, you can customize the following environment variables:

- `DEBUG=0` - Disable debug mode in production
- `SECRET_KEY` - Django secret key
- `DATABASE_URL` - Database connection string

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support and questions, please contact the development team.