# Individual Final Report

### Student Name:
Sean

### Team Members:
Angelo

### Project Name:
Small Business Inventory Manager

---

## My Role in the Team

I was responsible for backend development, service layer refactoring, and integrating the AI assistant. I focused on organizing the code, handling data logic, and connecting the application to the OpenAI API.

---

## Phase 1 Contribution Summary

In Phase 1, I worked on:

- Inventory management (add, update, delete items)
- Recording sales
- User authentication (login/register)
- Connecting the UI to JSON data storage

The app worked, but most of the logic was inside `app.py`, which made it harder to manage.

---

## Phase 1 Issues

- Logic mixed with UI in one file
- No clear separation of layers
- Code was harder to maintain
- No AI assistant
- Limited error handling

---

## Phase 2 Changes

I refactored the app by moving logic into service files:

- `inventory_service.py`
- `auth_service.py`

This separated the UI from the business logic.

I also added an AI assistant using OpenAI:

- Created `ai_assistant.py`
- Connected it to inventory and sales data
- Added an AI Assistant page in the app

I added error handling so the app does not crash if the API fails.

---

## Results

- Cleaner code structure (UI, service, data layers)
- More organized and reusable functions
- Working AI assistant integrated into the app
- Improved stability with error handling

---

## What I Learned

- How to separate UI and backend logic
- How to refactor code into services
- How to integrate an external API (OpenAI)
- How to improve application structure

---

## Conclusion

This project helped me understand how to build a more organized and scalable application. The addition of the AI assistant and improved structure made the app more complete and professional.