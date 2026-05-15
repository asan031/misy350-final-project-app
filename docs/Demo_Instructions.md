# Application Instructions

## How to Run the Application

1. Install dependencies:

pip install -r requirements.txt

2. Run the app:

streamlit run app.py

---

## Demo Accounts

Use the following accounts to test the application:

Admin:
- Username: owner1
- Password: 1234

Employee:
- Username: worker1
- Password: 1234

---

## Features to Test

1. Login System
- Log in as admin and employee
- Verify role-based access

2. Admin Features
- Add, update, delete inventory
- View dashboard metrics
- Check low stock alerts

3. Employee Features
- View inventory dashboard
- View low stock alerts

4. Record Sales
- Record a sale
- Confirm stock decreases

5. AI Assistant
- Ask:
  - What items are low stock?
  - What should I restock?
- If API limit is hit, a fallback message will appear

---

## Project Structure

- app.py → UI layer
- utils/data_manager.py → data handling
- utils/inventory_service.py → inventory logic
- utils/auth_service.py → authentication
- utils/ai_assistant.py → AI assistant

---

## Notes

- Uses JSON for storage
- API key stored in .env
- AI assistant is integrated but may be limited by quota