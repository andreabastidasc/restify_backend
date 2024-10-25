
# 🌙 Restify 🌙

Restify is an application designed to help users optimize their sleep schedules by automatically setting alarms based on sleep patterns detected through various methods such as smartwatch data, phone inactivity, sound detection, and more. 🛏️⏰

## ✨ Features

- 🕒 User-configurable sleep duration
- 💤 Sleep monitoring via smartwatch, phone sensors, or sound detection
- 🔔 Automatic alarm configuration based on detected sleep onset
- 👤 User preferences management

## 🗂️ Project Structure

```
restify_backend/
│
├── restify_backend/   # Main project folder containing Django settings
│
├── sleep_management/  # Application for managing sleep data and user preferences
│   ├── migrations/    # Database migrations for the sleep_management app
│   ├── models.py      # Data models for the app
│   ├── views.py       # Views for the REST API
│   ├── serializers.py # API serializers
│   ├── ...
│
├── manage.py          # Django management script
│
├── .gitignore         # Git ignore file
│
└── README.md          # Project README
```

## 🚀 Getting Started

### Prerequisites

- 🐍 Python 3.x installed
- 🐳 Docker installed (recommended for containerized development)
- 🌐 Django and Django Rest Framework dependencies

### ⚙️ Setup

1. **Clone the repository:** 📂
   ```bash
   git clone https://github.com/your-username/restify.git
   cd restify_backend
   ```

2. **Environment Configuration:** 🔐  
   Create a `.env` file in the root of the project with the following contents:
   ```plaintext
   POSTGRES_DB=your_database
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=db
   ```

3. **Running with Docker:** 🐋  
   Start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. **Running Locally (Optional):** 🖥️  
   To run locally without Docker, make sure to install dependencies and migrate:
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the Application:** 🌐  
   Open your browser and navigate to `http://localhost:8000/`

## 🧪 Testing

Run tests using the following command:
```bash
docker-compose exec web python manage.py test
```

## 🔮 Future Enhancements

- 🤖 Add machine learning capabilities for more accurate sleep detection
- 📱 Expand integration with other wearable devices
- 🔐 Implement user authentication with JWT

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue. 📝

## ©️ Copyright

© 2024 Andrea Bastidas. All rights reserved. ✨
