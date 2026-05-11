# Individual Plan

## Author
Angelo

## Date
2026-05-11

## Origin Prompt
@ChatGPT create an individual structural and backend improvement plan for the inventory app. Focus on services, architecture, and maintainability.

---

## Focus
This plan focuses on backend structure and improving maintainability.

---

## Proposed Improvements

1. Separate Business Logic into Services
- Move logic from app.py into:
  - auth_service.py
  - inventory_service.py

2. Improve Data Handling
- Use DataManager consistently for all JSON operations

3. Use Models Properly
- Ensure all data is handled through:
  - User class
  - InventoryItem class
  - Sale class

4. Improve Code Organization
- Reduce size of app.py
- Keep UI separate from logic

5. Prepare for AI Integration
- Create ai_assistant.py
- Keep AI logic separate from UI

---

## Reasoning
These changes make the app easier to maintain and align with the instructor’s examples. It also prepares the project for future features like AI integration.

---

## Layer Impact
- Service layer
- Data layer
- Model layer