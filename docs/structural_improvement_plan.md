# Structural Improvement Plan

## Authors
- Sean
- Partner

## Origin Prompt
@ChatGPT create a structural improvement plan for Phase 2. Focus on organization, layering, maintainability, and separation of concerns.

## Goal
Refactor the app so app.py focuses mostly on Streamlit UI, while data handling, authentication, inventory logic, and models are separated into utils files.

## Planned Structural Changes
1. Keep app.py as the UI layer.
2. Use utils/data_manager.py for JSON loading and saving.
3. Use utils/models.py for User, InventoryItem, and Sale classes.
4. Create utils/auth_service.py for login, registration, logout, and role checks.
5. Create utils/inventory_service.py for inventory CRUD and sales logic.
6. Create utils/ai_assistant.py later for OpenAI assistant logic.

## Protected Functionality
Do not break:
- login
- registration
- logout
- admin dashboard
- employee dashboard
- inventory CRUD
- sales recording
- JSON persistence

## Implementation Order
1. Finish DataManager
2. Add models
3. Move auth logic into AuthService
4. Move inventory and sales logic into InventoryService
5. Test app after each refactor
6. Commit each working step separately