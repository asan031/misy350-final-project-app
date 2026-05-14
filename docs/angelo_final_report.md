# Individual Final Report

### Student Name:
Angelo

### Team Members:
Sean

### Project Name:
Small Business Inventory Manager

---

## My Role in the Team

I was primarily responsible for the user interface (UI) design and improvements. This included building and refining the dashboards, improving layout and usability, and ensuring a clean and organized user experience across all pages. I also worked on updating the Record Sales page and improving the overall design consistency of the application.

---

## 1. Phase 1 Contribution Summary

In Phase 1, I helped build the front-end interface of the application. I contributed to:

- Creating the admin and employee dashboards  
- Designing the layout of pages using Streamlit components  
- Displaying inventory and sales data to users  
- Helping implement navigation between pages  
- Assisting with basic CRUD interface elements  

One issue in Phase 1 was that many pages looked like long vertical lists of widgets and lacked structure. The UI was functional but not visually organized or user-friendly.

---

## 2. Phase 1 Issues Identified

- The UI layout was basic and lacked structure  
- Pages were long and cluttered with widgets  
- The Record Sales page was not well organized  
- Feedback messages were inconsistent  
- Some sections lacked clear separation and readability  
- Overall design did not feel polished  

---

## 3. Phase 2 Refactoring Report (UI Layer)

### Original Code Issue

The original Record Sales page used individual widgets without structure:

```python
selected_label = st.selectbox(...)
quantity = st.number_input(...)

if st.button("Record Sale"):
    ...

Refactored Code:
with st.form("record_sale_form"):
    selected_label = st.selectbox(...)
    quantity = st.number_input(...)
    submitted = st.form_submit_button("Record Sale")