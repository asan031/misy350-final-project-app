## Entry 2 - 2026-05-12

### Author
Angelo

### What Changed
- Improved Admin Dashboard UI.
- Added metrics using st.metric.
- Added tabs for inventory summary and low stock alerts.

### Why It Changed
To make the admin dashboard easier to read and better for the final demo.

### Layers Affected
- UI layer (app.py)



## Entry 3 - 2026-05-12

### Author
Angelo

### What Changed
- Improved Admin Dashboard with metrics and tabs.
- Improved Employee Dashboard with metrics and tabs.
- Updated Employee Dashboard permissions so admins can view it too.

### Why It Changed
Admins should be able to view employee-facing dashboard information while employees remain restricted from admin-only pages.

### Layers Affected
- UI layer
- Role access logic





## Entry 4 - 2026-05-12

### Author
Angelo

### Origin Prompt
@ChatGPT what items should I test and is handling duplicate inventory items within scope?

### What Changed
- Tested Manage Inventory functionality (Add, Update, Delete).
- Verified tab-based layout works correctly.
- Identified an issue where adding duplicate items creates separate entries instead of updating stock.

### Why It Changed
To ensure the UI improvements function correctly and to validate core inventory workflows as part of Phase 2 testing.

### Layers Affected
- UI layer (testing and validation)
- Inventory logic (issue identified for backend improvement)

### Notes
- Duplicate item handling will be addressed by Sean as part of backend/service logic improvements.






## Entry 5 - 2026-05-13

### Author
Sean

### Origin Prompt
@ChatGPT how do I check to make sure the duplicate item fix is working properly?

### What Changed
- Fixed duplicate inventory item handling.
- Adding an item with the same name now increases the existing stock instead of creating a duplicate listing.

### Why It Changed
To improve inventory accuracy and fix an issue found during UI testing.

### Layers Affected
- Inventory logic
- Data layer


## Entry 6 - 2026-05-14

### Author
Sean

### Origin Prompt
@ChatGPT next

### What Changed
- Created utils/inventory_service.py.
- Moved inventory and sales logic out of app.py.
- app.py now imports inventory functions from the service layer.

### Why It Changed
To improve separation of concerns and match the required Phase 2 structure.

### Layers Affected
- Service layer
- UI layer
- Data layer



## Entry 7 - 2026-05-14

### Author
Sean

### Origin Prompt
@ChatGPT what next

### What Changed
- Created utils/auth_service.py.
- Moved authentication helper functions out of app.py.
- app.py now imports authentication logic from the service layer.

### Why It Changed
To improve separation of concerns and reduce business logic inside the UI layer.

### Layers Affected
- Service layer
- UI layer
- Data layer



## Entry 8 - 2026-05-14

### Author
Sean

### Origin Prompt
@ChatGPT help me add an AI assistant to the inventory app

### What Changed
- Added an AI assistant connected to the OpenAI API.
- Created `utils/ai_assistant.py` with an `InventoryAIAssistant` class.
- Added an AI Assistant page in `app.py`.
- Added sidebar navigation for the AI Assistant.
- Connected the assistant to inventory and sales data.
- Added error handling so the app does not crash if API quota/key issues occur.

### Why It Changed
To meet the Phase 2 requirement for an AI assistant that provides useful inventory-related support inside the app.

### Files Changed
- app.py
- utils/ai_assistant.py
- requirements.txt
- .env
- .gitignore
- docs/implementation_log.md

### Layers Affected
- UI layer
- Service layer
- AI assistant layer

### Result
- Users can ask inventory-related questions.
- The assistant uses current inventory and sales data to generate responses.
- The app handles API issues without crashing.



## Entry 9 - 2026-05-14

### Author
Angelo

### Origin Prompt
@ChatGPT lets get to the next part

### What Changed
- Refactored Record Sales page using st.form().
- Improved layout and user interaction.
- Added consistent feedback messages.

### Why It Changed
To improve usability and match the design quality of other UI components.

### Files Changed
- app.py

### Layers Affected
- UI layer