# 🏎️ F1 Wiki

F1 Wiki is a web application built with **Django** where users can add, edit, and delete Formula 1 drivers.  
Each user can create drivers with name, team, age, description, and photo. Drivers are displayed as modern cards, and each has a dedicated detail page.  
The app also includes pages for all drivers created by a specific user.

---

## 🚀 Features
- User authentication (login/logout)
- Create drivers with:
  - name, age, team, description
  - image upload
- Edit and delete drivers (only by the creator)
- Delete confirmation page
- Dedicated detail pages for each driver
- List of drivers filtered by user
- Automated tests with **pytest** + **pytest-django**

---

## 🛠️ Technologies Used
- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [SQLite3](https://www.sqlite.org/index.html) (default)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Pytest](https://docs.pytest.org/) for testing

---

## ⚙️ Installation

### 1. Clone the repository:
```
git clone https://github.com/user/f1_wiki.git
cd f1_wiki
```

### 2. Create a venv (if it's needed):
```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies:
```
pip install -r requirements.txt
```

### 4. Apply database migrations:
```
python manage.py migrate
```

### 5. Create a superuser for the admin panel:
```
python manage.py createsuperuser
```

### 6. Run the server:
```
python manage.py runserver
```

### 7. Access the app in your browser:
```
http://127.0.0.1:8000/
```

💻 Running in PyCharm

1. Open the project in PyCharm.
2. Go to File → Settings → Project → Python Interpreter and select .venv.
3. Run:
   - manage.py runserver to start the application
   

4. You can also configure quick runs:
   - Run → Edit Configurations
   - Add a new Django Server for manage.py runserver.


### 8. Project Structure
```
F1_Wiki/
│── f1/                  
│   ├── templates/        
│   │   ├── home.html
│   │   ├── drivers.html
│   │   ├── driver_detail.html
│   │   ├── driver_confirmation_delete.html
│   │   └── driver_error_delete.html
│   ├── static/           
│   ├── views.py          
│   ├── models.py         
│   └── tests.py          
│
├── manage.py             
├── requirements.txt      
└── README.md             
```