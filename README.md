 `README.md`

```md
# HackOverflow-
for hackMit25

# AI-Powered Smart Inventory Restocking System

## Project Description
This project is an AI-powered system that automates inventory restocking using machine learning algorithms. It predicts demand and optimizes stock levels to reduce wastage and improve efficiency. 

We are actively refining our **AI-powered demand prediction** to ensure the most accurate results. The system is fully functional, and we are debugging the prediction pipeline to enhance performance.

## Installation Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/DevyaniSisodia/HackOverflow-.git
   ```

2. Navigate to the project directory:
   ```sh
   cd HackOverflow-
   ```

3. Set up the virtual environment (if not already activated):
   ```sh
   python -m venv venv
   ```

4. Activate the virtual environment:
   - **Windows (PowerShell)**:
     ```sh
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```sh
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

6. Run the backend server:
   ```sh
   cd backend
   python -m uvicorn main:app --reload
   ```

7. Run the frontend:
   ```sh
   cd frontend
   npm install
   npm start
   ```

## Features and Functionality

- 📊 **Machine Learning-Based Demand Prediction** *(Currently being optimized for better accuracy)*
- 🛒 **Automated Inventory Restocking**
- 📈 **Data Analytics Dashboard**
- 🖥 **FastAPI Backend**
- 🔍 **Real-time Monitoring and Alerts**

## Team Members and Contributions

- **[Devyani Sisodia]** – Backend Development & API Integration
- **[Varun Pingale]** – Frontend Development
- **[Hritika Khattar]** – Machine Learning & Data Analytics
- **[Sayali Datar]** – Documentation & Testing
- **[Mandar Gade & Saurav Kumar]** – SQL Database

## Dependencies & APIs Used

- **Python 3.10+**
- **FastAPI** for backend
- **Uvicorn** for ASGI server
- **pandas** for data processing
- **joblib** for model loading
- **MySQL** for database management
- **scikit-learn** for ML algorithms
- **React** for frontend

---

### **Status:**
✅ **Frontend & Backend connected successfully**  
✅ **Database integration working**  
⚙️ **Demand prediction currently being optimized**  

We are close to achieving a **fully functional AI-powered inventory system! 🚀**  

