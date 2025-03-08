# Bank Loans Project

This project is a **bank loan management system** that allows loan providers to contribute funds, loan customers to apply for loans, and bank personnel to manage loan products and requests. The system is built using **Django** for the backend and **React** for the frontend.

---

## Features

### **User Roles**
1. **Loan Providers**:
   - Contribute funds to the bank.
   - View their contributed funds.

2. **Loan Customers**:
   - Apply for loans.
   - View loan details and amortization schedules.

3. **Bank Personnel**:
   - Define loan products (min/max amount, interest rate, duration).
   - Approve or reject loan requests.
   - Disable/enable user accounts.

---

## Technologies Used

### **Backend**
- **Django**: Python web framework for building the backend API.
- **Django REST Framework (DRF)**: For building RESTful APIs.
- **PostgresSQL**: Default database for development.

### **Frontend**
- **React**: JavaScript library for building the user interface.
- **React Router**: For routing and navigation.
- **Axios**: For making API requests.
- **Bootstrap**: For styling the UI.

### **Containerization**
- **Docker**: For containerizing the application.
- **Docker Compose**: For managing multi-container Docker applications.

---

## Project Structure

### **Backend**
backend/
├── users/                  # User management app
│   ├── models.py           # User model
│   ├── serializers.py      # Serializers for user data
│   ├── views.py            # API views for users
│   ├── urls.py             # URL routing for users
│   └── permissions.py      # Custom permissions
├── loans/                  # Loan management app
│   ├── models.py           # Loan and LoanFund models
│   ├── serializers.py      # Serializers for loans
│   ├── views.py            # API views for loans
│   └── urls.py             # URL routing for loans
├── manage.py               # Django management script
└── settings.py             # Django project settings

### **Frontend**
frontend/
├── public/                 # Static assets
├── src/
│   ├── components/         # Reusable components
│   ├── pages/              # Page components
│   ├── services/           # API services
│   ├── App.js              # Main app component
│   ├── index.js            # Entry point
│   ├── index.css           # Global styles
│   └── setupProxy.js       # Proxy setup for API calls
├── Dockerfile              # Dockerfile for the frontend
└── package.json            # Frontend dependencies

---

## Setup Instructions

### **Prerequisites**
- Docker and Docker Compose installed on your machine.
- Node.js and npm installed for local frontend development (optional).
- Django and requirements.txt are installed (optional).

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/bank-loans-project.git
cd Bank-Loans
```
### **2. Run the project**
```bash
docker-compose up --watch
```

### **2. Access the application**
Frontend: Open http://localhost:3000 in your browser.

Backend swagger: Open http://localhost:8000/swagger in your browser.

Database: Open http://localhost:5050 in your browser (credentials are provided in the docker-compose in the pgadmin service).