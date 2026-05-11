# Structural Analysis

## Authors
- Sean
- Angelo

## Origin Prompt
@ChatGPT follow these Phase 2 instructions and analyze the current app structure. Identify the UI layer, service layer, data/database layer, models/classes, important dependencies, and what should be protected before making changes.

## Current Project Structure
The app is currently a Streamlit inventory management app with JSON storage.

## UI Layer
The UI is mainly handled in app.py using Streamlit components such as forms, buttons, inputs, and dashboards.

## Service Layer
The service layer is currently limited/incomplete. Some business logic is still mixed directly into app.py.

## Data Layer
The data layer uses JSON files stored in the data folder:
- users.json
- inventory.json
- sales.json

A DataManager class has started being added in utils/data_manager.py.

## Models / Classes
The project is beginning to add model classes in utils/models.py, including:
- User
- InventoryItem
- Sale

## Important Dependencies
- streamlit
- json
- pathlib

## What Should Be Protected Before Changes
Before refactoring, we should protect:
- working login and registration
- user roles
- existing JSON data
- inventory CRUD
- sales recording
- branch history
- main branch stability

## Structural Issues Found
- app.py currently handles too much responsibility
- UI logic, data logic, and business rules need clearer separation
- services should be moved into utils files
- future AI assistant code should be isolated from app.py