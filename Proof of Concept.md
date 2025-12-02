# Proof of Concept (PoC) Plan

The Proof of Concept (PoC) will demonstrate a working slice of the Complaint Management System (CMS) that validates two functional requirements and one usability requirement, as required by the assessment. The PoC will be implemented using Django, PostgreSQL, and HTML templates, consistent with the layered architecture defined in the Solution Architecture.

---

## PoC Objective

To build a minimal but functional version of the CMS that allows a consumer to:

1. Log into the system  
2. Create/submit a complaint  
3. View a list of their submitted complaints  
4. (Optional) View and update complaint details  

This validates core workflow behaviour and demonstrates how the system meets key architectural, security, and usability requirements.

---

## Functional Requirements Covered

### **RF01 – Submit Complaint**
- User fills out a simple complaint form (title, description, category).  
- Django validates the input.  
- Complaint is saved to PostgreSQL with user_id + company_id.  
- User receives confirmation that the complaint was created.  

### **RF03 – Track Status**
- Logged-in users can view a list of their complaints.  
- Each complaint displays its status (Open, In Progress, Resolved, etc.).  
- Users can click into the detail page (if implemented).  
- Ensures users only see **their own** complaint data.  

### **RF05 – Update Resolution**
- A simple dropdown on the complaint detail page allows updating a complaint’s status.  
- Used only for demonstration (e.g., marking as "In Progress" or "Resolved").  

---

## Usability Requirement Covered (NFR09)

The PoC validates the usability requirement through:

- A clean UI with clear navigation  
- Complaint creation in 2–3 clicks  
- WCAG-friendly structure (labels, headings, semantic HTML)  
- Simple, low-cognitive-load layout  
- Form error messages for validation feedback  

This directly satisfies **NFR09 – Usability**.

---

## Additional NFRs Automatically Demonstrated

### **Security (NFR03 & NFR04)**
- Django Authentication  
- Session-based login  
- CSRF protection on forms  
- Users can only access their own complaints (basic tenant isolation behaviour)  

### **Performance (NFR05)**
- All actions (create, view list) execute in well under 10 seconds  
- Django ORM performs efficiently for PoC-scale data  

### **Maintainability (NFR10)**
- Layered Django architecture  
- Clean separation: Views → Services → Models → Templates  

---

## Architecture Components Used in PoC

- **Presentation Layer:** HTML templates (complaint list, create form, navigation bar)  
- **Application Layer:** Django views + form validation  
- **Business Logic Layer:** Complaint service functions  
- **Data Layer:** PostgreSQL via Django ORM  

This directly aligns with the C4 Container and Component Diagrams.


