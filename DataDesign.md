# Data Design – Complaint Management System (CMS)

This data design describes the **exact** database schema implemented in the CMS Proof-of-Concept. It is fully aligned with the actual PostgreSQL ERD generated from the Django project, containing **only the tables that exist** and reflecting the true multi-tenant, RBAC-based structure.

---
<img width="5376" height="4096" alt="diagram" src="https://github.com/user-attachments/assets/e19e12d7-cc64-49be-a80c-ecc64497150f" />
---

1\. Tenant & User Domain 

1.1 accounts\_company 

Stores organisations (tenants) using the CMS. 

| Field | Type | Description |
| --- | --- | --- |
| id | PK | Unique identifier |
| name | varchar | Company name |
| industry | varchar | Company sector (banking, telecom, etc.) |

1.2 accounts\_userprofile 

Extends the built-in Django user with role and tenant information. 

| Field | Type | Description |
| --- | --- | --- |
| id | PK | Unique identifier |
| user_id | FK → auth_user.id | Associated Django user |
| company_id | FK → accounts_company.id | Tenant the user belongs to |
| role | varchar | Role: consumer/agent/support/manager/admin |

1.3 Django Authentication & RBAC Tables 

These tables are automatically created by Django and provide user accounts, permissions, and role/group assignments: 

*   auth\_user 
    

*   auth\_group 
    

*   auth\_permission 
    

*   auth\_group\_permissions 
    

*   auth\_user\_groups 
    

*   auth\_user\_user\_permissions 
    

Purpose: Implements Django’s built-in authentication and role-based access control. 

2\. Complaint Domain 

2.1 complaints\_complaint 

The core complaint record. 

| Field | Type | Description |
| --- | --- | --- |
| id | PK | Unique complaint ID |
| title | varchar | Complaint title |
| description | varchar | Detailed complaint content |
| category | varchar | Complaint category |
| priority | varchar | Priority value |
| status | varchar | Current complaint status |
| channel | varchar | Submission channel (web/phone) |
| created_at | timestamp | When the complaint was created |
| updated_at | timestamp | Last time it was modified |
| company_id | FK → accounts_company.id | The tenant the complaint belongs to |
| created_by_id | FK → auth_user.id | User who created the complaint |
| assigned_to_id | FK → auth_user.id (nullable) | A user was assigned to resolve the complaint. |

2.2 complaints\_complainthistory 

Tracks changes to complaint status over time. 

| Field | Type | Description |
| --- | --- | --- |
| id | PK | Unique history entry |
| old_status | varchar | Status before change |
| new_status | varchar | Status after change |
| note | varchar | Optional note about the change |
| changed_at | timestamp | When the change occurred |
| changed_by_id | FK → auth_user.id | User who performed the action |
| complaint_id | FK → complaints_complaint.id | Related complaint |

Purpose: Provides auditability and supports managerial reporting. 

3\. Django System Tables 

These tables support Django’s internal framework functionality and appear in the live database: 

3.1 django\_admin\_log 

Tracks administrative actions (add/update/delete) performed in Django Admin. 

3.2 django\_migrations 

Tracks applied migrations to manage schema version control. 

3.3 django\_session 

Stores authenticated session data for logged-in users. 

3.4 django\_content\_type 

Metadata table mapping Django models to permissions and admin functionality. 

4\. Relationships Summary 

Company \-> Users One company has many users (accounts\_company → accounts\_userprofile) 

Company \-> Complaints One company owns many complaints (accounts\_company → complaints\_complaint) 

User \-> Created Complaints auth\_user links to complaints\_complaint.created\_by\_id 

User \-> Assigned Complaints auth\_user links to complaints\_complaint.assigned\_to\_id 

Complaint \-> Complaint History Entries One complaint has many history entries (complaints\_complaint → complaints\_complainthistory) 

User \-> Complaint History Actions auth\_user links to complaints\_complainthistory.changed\_by\_id 

Security Considerations 

Security is a fundamental requirement for the CMS given the sensitivity of consumer data and the multi-tenant operating model. The security design supports NFR03 (Security), NFR04 (Security) and NFR08 (Reliability) and is implemented across all layers of the architecture. 

Authentication 

Django’s authentication framework is used for secure login and session management: 

*   Passwords are stored as salted, hashed values. 
    

*   Server-side session handling with HTTP-only cookies. 
    

*   Consistent login/logout flows through Django Auth. 
    

Authorisation & Role-Based Access 

Access is controlled by both role and tenant: 

*   UserProfile enforces one role per user. 
    

*   Views and forms limit what each role can access and perform. 
    

*   Administrative features are available only to platform admins. 
    

This ensures users only interact with data and functionality assigned to their role. 

Tenant-Level Data Isolation 

Multi-tenant isolation is enforced through the data model: 

*   Every complaint and user record links to a company via company\_id. 
    

*   All queries use tenant filtering to prevent cross-organisation visibility. 
    

Defence-in-depth roadmap: PostgreSQL row-level security (RLS) for database\-level enforcement. 

Protection from Common Web Threats 

Django provides built-in protections aligned with OWASP principles: 

*   CSRF tokens on all state-changing requests. 
    

*   Template auto-escaping reduces XSS risk. 
    

*   The ORM prevents SQL injections through parameterised queries. 
    

*   Security middleware. 
    

Deployment assumes HTTPS to encrypt communication between client and server. 

Auditability & Data Integrity 

To support accountability and reliable operations: 

*   The complaint history table records status changes (who/what/when). 
    

*   ACID-compliant PostgreSQL transactions prevent partial updates. 
    

*   The migration system ensures consistent schema management.
