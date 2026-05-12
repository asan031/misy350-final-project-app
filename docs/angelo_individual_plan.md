# Angelo Individual Plan

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
