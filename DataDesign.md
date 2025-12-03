# Data Design – Complaint Management System (CMS)

This data design describes the **exact** database schema implemented in the CMS Proof-of-Concept. It is fully aligned with the actual PostgreSQL ERD generated from the Django project, containing **only the tables that exist** and reflecting the true multi-tenant, RBAC-based structure.

---
<img width="5376" height="4096" alt="diagram" src="https://github.com/user-attachments/assets/e19e12d7-cc64-49be-a80c-ecc64497150f" />
---

# 1. Tenant & User Domain

## 1.1 `accounts_company`
Stores organisations (tenants) using the CMS.

| Field | Type | Description |
|-------|-------|-------------|
| id | PK | Unique identifier |
| name | varchar | Company name |
| industry | varchar | Company sector (banking, telecom, etc.) |

---

## 1.2 `accounts_userprofile`
Extends the built-in Django user with role and tenant information.

| Field | Type | Description |
|-------|-------|-------------|
| id | PK | Unique identifier |
| user_id | FK → auth_user.id | Associated Django user |
| company_id | FK → accounts_company.id | Tenant the user belongs to |
| role | varchar | Role: consumer/agent/support/manager/admin |

---

## 1.3 Django Authentication & RBAC Tables

These tables are automatically created by Django and provide user accounts, permissions, and role/group assignment:

- `auth_user`
- `auth_group`
- `auth_permission`
- `auth_group_permissions`
- `auth_user_groups`
- `auth_user_user_permissions`

**Purpose:** Implements Django’s built-in authentication and role-based access control (RBAC).

---

# 2. Complaint Domain

## 2.1 `complaints_complaint`
The core complaint record.

| Field | Type | Description |
|-------|-------|-------------|
| id | PK | Unique complaint ID |
| title | varchar | Complaint title |
| description | varchar | Detailed complaint content |
| category | varchar | Complaint category |
| priority | varchar | Priority value |
| status | varchar | Current complaint status |
| channel | varchar | Submission channel (web/phone) |
| created_at | timestamp | When the complaint was created |
| updated_at | timestamp | Last time it was modified |
| company_id | FK → accounts_company.id | Tenant the complaint belongs to |
| created_by_id | FK → auth_user.id | User who created the complaint |
| assigned_to_id | FK → auth_user.id (nullable) | User assigned to resolve the complaint |

---

## 2.2 `complaints_complainthistory`
Tracks changes to complaint status over time.

| Field | Type | Description |
|-------|-------|-------------|
| id | PK | Unique history entry |
| old_status | varchar | Status before change |
| new_status | varchar | Status after change |
| note | varchar | Optional note about the change |
| changed_at | timestamp | When the change occurred |
| changed_by_id | FK → auth_user.id | User who performed the action |
| complaint_id | FK → complaints_complaint.id | Related complaint |

**Purpose:** Provides auditability and supports managerial reporting.

---

# 3. Django System Tables

These tables support Django’s internal framework functionality and appear in the live database:

## 3.1 `django_admin_log`
Tracks administrative actions (add/update/delete) performed in Django Admin.

## 3.2 `django_migrations`
Tracks applied migrations to manage schema version control.

## 3.3 `django_session`
Stores authenticated session data for logged-in users.

## 3.4 `django_content_type`
Metadata table mapping Django models to permissions and admin functionality.

---

# 4. Relationships Summary

- **Company → Users**  
  One company has many users (`accounts_company` → `accounts_userprofile`)

- **Company → Complaints**  
  One company owns many complaints (`accounts_company` → `complaints_complaint`)

- **User → Created Complaints**  
  `auth_user` links to `complaints_complaint.created_by_id`

- **User → Assigned Complaints**  
  `auth_user` links to `complaints_complaint.assigned_to_id`

- **Complaint → Complaint History Entries**  
  One complaint has many history entries (`complaints_complaint` → `complaints_complainthistory`)

- **User → Complaint History Actions**  
  `auth_user` links to `complaints_complainthistory.changed_by_id`

---

# 5. Scope Notes

This data model intentionally represents **only the implemented PoC**.  
The following are **not included** because they were not implemented in the live database:

- Attachment storage  
- Notification preferences  
- SLA/priority lookup tables  
- Tenant settings/config  
- Chatbot integrations  

These may be part of future iterations but are outside the current Proof-of-Concept.

---

# ✔ Final Statement

This data design matches the ERD and the Django project **exactly**, ensuring complete consistency across:

- C4 architecture diagrams  
- The layered architecture  
- The actual PostgreSQL database  
- The implemented Django models  

This file is ready for submission and inclusion in your GitHub project.


