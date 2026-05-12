# Angelo Individual Plan w/ Entries

## Author
Angelo

## Date
2026-05-12

## Origin Prompt
@ChatGPT explain what Angelo should do for his individual Phase 2 UI/usability work and create a plan based on that.

## Focus
My focus is improving the user interface and usability of the Streamlit inventory application.


## Planned Improvements

1. Add Sidebar Navigation
- Use Streamlit sidebar to organize pages (Dashboard, Inventory, Sales)

2. Improve Layout with Tabs and Columns
- Use tabs to separate sections
- Use columns to organize content

3. Add Dashboard Metrics
- Show total inventory items
- Show total sales
- Show low stock alerts

4. Improve Forms
- Use st.form() for cleaner input handling

5. Add Feedback Messages
- Show success, error, and warning messages for user actions


## Reasoning
These changes improve usability, make the app easier to navigate, and create a cleaner interface for both admin and employee users. This also aligns with Streamlit best practices.

## Layers Affected
- UI layer (app.py)
- Minor interaction with service layer if needed for displaying metrics



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