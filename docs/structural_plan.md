# Structural Improvement Plan

## Authors
- Sean
- Angelo

## Date
2026-05-11

## Origin Prompt
@ChatGPT create a structural improvement plan for the current app. Focus on improving organization, layering, maintainability, and separation of concerns. Include the original prompt for recordkeeping.

---

## Goal
Refactor the application so that responsibilities are clearly separated into layers:
- UI layer (Streamlit)
- Service layer (business logic)
- Data layer (JSON handling)
- Model layer (classes)

---

## Current Issues
- app.py contains UI, data handling, and business logic all together
- JSON file handling is mixed with UI code
- Hard to maintain and extend
- Does not fully match instructor’s structured examples

---

## Proposed Structure

### UI Layer
File:
- app.py  
Responsibility:
- handle Streamlit UI
- user input/output
- display data

---

### Data Layer
File:
- utils/data_manager.py  
Responsibility:
- load JSON files
- save JSON files

---

### Model Layer
File:
- utils/models.py  
Responsibility:
- define:
  - User
  - InventoryItem
  - Sale

---

### Service Layer

Files:
- utils/auth_service.py
- utils/inventory_service.py

Responsibilities:

auth_service.py:
- login
- registration
- session logic

inventory_service.py:
- add/edit/delete inventory
- process sales
- enforce business rules

---

## Implementation Plan

1. Finalize DataManager (JSON handling)
2. Add models (User, InventoryItem, Sale)
3. Create auth_service.py and move login/register logic
4. Create inventory_service.py and move CRUD + sales logic
5. Reduce app.py to UI only
6. Test after each step

---

## Protected Features (DO NOT BREAK)

- login system
- registration system
- logout
- role-based routing
- inventory CRUD
- sales recording
- JSON data integrity

---

## Expected Outcome

- cleaner, modular code
- easier debugging
- matches instructor examples
- meets Phase 2 structure requirements