# docker_seminar

This project includes two Django REST API apps:

- 📚 `library_app`: Manages books
- ✅ `tasks_app`: Manages tasks
- 🐘 PostgreSQL as the database (shared across apps)
- 🐳 Dockerized for easy development and deployment

---

## 🧾 Project Structure

.
├── docker-compose.yml
├── .env
├── library_app/
│ ├── ...
│ └── manage.py
├── tasks_app/
│ ├── ...
│ └── manage.py

---

## ⚙️ Environment Variables (`.env`)

Create a `.env` file in the project root:

```env
POSTGRES_DB=projectdb
POSTGRES_USER=projectuser
POSTGRES_PASSWORD=projectpass

SUPERUSER_ADMIN=admin
SUPERUSER_EMAIL=admin@example.com
SUPERUSER_PASSWORD=adminpass

🚀 Run the Project
Step 1: Build and Start Services
docker compose up --build

This will:
Build both apps and the database
Run migrations
Create a superuser (via custom createsuperuser command)

Start both servers:
library_app at http://localhost:8001
tasks_app at http://localhost:8002

🔑 Admin Panel
Visit:

http://localhost:8001/admin/ — for library_app

http://localhost:8002/admin/ — for tasks_app

Login using the credentials in your .env file.

📡 API Endpoints
App	Base URL	Example Endpoint
Library	/api/books/	http://localhost:8001/api/books/
TaskManager	/api/tasks/	http://localhost:8002/api/tasks/

Test using tools like Postman or curl.

🔧 Common Docker Commands
# Rebuild all services
docker compose up --build

# Stop all containers
docker compose down

# Access a running container
docker exec -it task_app bash
🐞 Troubleshooting
❌ Can't log in to admin?

Check .env values.

Ensure createsuperuser.py exists in yourapp/management/commands/.

Make sure you're calling python manage.py createsuperuser (not create_superuser) in docker-compose.yml.

❌ Database not connecting?

Confirm HOST = 'db' in settings.py.

Ensure .env values match those used in docker-compose.yml.

🧼 Cleanup
# Stop containers and remove volumes
docker compose down -v

📜 License
MIT — free to use and modify.

