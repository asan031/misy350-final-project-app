# Feature Analysis

## Authors
- Sean
- Angelo

## Origin Prompt
@ChatGPT analyze the current app features. Identify current features, missing features, incomplete workflows, usability issues, and areas for improvement.

## Current Features
The app currently includes:
- User registration
- User login/logout
- Role-based access (admin vs employee)
- Inventory management (admin can add/edit/delete items)
- Employee can view inventory
- Sales recording system
- JSON-based data persistence

## Missing Features
- No AI assistant (required for Phase 2)
- No advanced dashboard (basic UI only)
- No filtering/search for inventory
- No analytics or summaries (e.g., total sales)
- No error handling improvements

## Incomplete Workflows
- Sales workflow does not provide strong feedback or validation
- Inventory updates may not reflect instantly in all views
- No confirmation messages for important actions

## Usability Issues
- UI is mostly one long page (not modular)
- Limited use of Streamlit layout tools (columns, tabs, sidebar)
- Navigation is not very clear between actions

## Areas for Improvement
- Add sidebar navigation
- Use tabs/columns for dashboards
- Improve feedback messages (success, error, warning)
- Add summary metrics (total inventory, total sales)
- Improve form structure using st.form()
- Add AI assistant for inventory insights