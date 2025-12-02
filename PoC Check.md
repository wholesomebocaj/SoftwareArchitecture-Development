# Layered Architecture in the Proof of Concept

This proof-of-concept follows a **layered architectural style**, consistent with the system design from Task 1.  
Although Django does not enforce strict separation between “application” and “business” layers, the PoC aligns with the conceptual architecture by implementing clear **Presentation**, **Application/Business**, and **Data** layers.

---

## 1. Presentation Layer (UI Layer)

The presentation layer handles all interaction with the end user through HTML and CSS.  
It contains **no business logic** and is only responsible for displaying data and collecting input.

### Components in this layer:
- Templates:
  - `base.html`
  - `complaint_list.html`
  - `complaint_detail.html`
  - `complaint_create.html`
  - `login.html`
- Static styling:
  - CSS files in `static/css/`

This layer renders the interface and posts user input back to the application/business layer through forms.

---

## 2. Application / Business Logic Layer

In traditional layered architecture, the “application layer” and “business logic layer” may be separate components.  
**In Django, these two layers naturally merge**, because Django views and forms together handle:

- use-case coordination  
- role and permission rules  
- validation  
- business decisions  
- request flow  
- mapping input into domain models  

For this PoC, the **Application/Business layer** is implemented via:

- `complaints/views.py`
- `complaints/forms.py`

### Responsibilities performed here:
- Enforcing role-based access (“only consumers can create complaints”)
- Mapping complaints to the correct tenant (`request.user.profile.company`)
- Assigning the creator (`created_by`)
- Managing complaint creation workflow
- Filtering complaints so users only see their own data
- Validating form input using Django ModelForms
- Redirecting between screens based on user actions

Although the C4 diagrams include the option for separate service classes (e.g., `ComplaintService`), the PoC intentionally keeps logic inside views and forms — which is normal and appropriate for a Django implementation.  
The responsibilities remain cleanly separated from UI and data concerns, preserving the layered structure.

---

## 3. Data Layer (Persistence Layer)

The data layer defines the structure of the system, its entities, and how they are stored.  
Django’s ORM abstracts database operations and ensures data consistency.

### Components in this layer:
- Models:
  - `Complaint`
  - `ComplaintStatusHistory`
  - `Company`
  - `UserProfile`

### Responsibilities:
- Database schema definition
- Relationships (e.g., complaint belongs to a company)
- Encapsulation of domain data
- Querying via Django ORM
- Maintaining tenant isolation at the data level (company-based filtering)

The application/business layer interacts with the database exclusively through these model classes.

---

## Summary

The PoC implements a **Django-style layered architecture** aligned with the design in Task 1:

- **Presentation Layer**  
  HTML templates + CSS for rendering the UI.

- **Application & Business Layer**  
  Views and forms that implement business rules, validation, RBAC, complaint workflow, and tenant filtering.

- **Data Layer**  
  ORM models representing tenant-aware domain entities stored in PostgreSQL.

While the full design allows for separate service or domain layers, the PoC adopts Django’s idiomatic structure where business logic lives within views and forms.  
This still maintains a clear separation of concerns consistent with the layered architectural style.

