# Data Design

The data design for the Complaint Management System (CMS) defines the core entities, their attributes, and the relationships required to support the complaint lifecycle and multi-tenant functionality. The model ensures tenant isolation, auditability, and compatibility with the layered architecture and proof-of-concept (PoC) scope.

---

## Core Entities

### **Company (Tenant)**
Represents each organisation using the CMS.

- `company_id` – primary key  
- `name` – organisation name  
- `industry` – banking, telecom, etc.  
- `hours_of_operation`  
- `created_at`

---

### **User**
Represents consumers, agents, support engineers, managers, and administrators.

- `user_id` – primary key  
- `company_id` – foreign key to Company  
- `name`  
- `email`  
- `role` – Consumer / Agent / Support / Manager / Admin  
- `password_hash`  
- `created_at`

---

### **Complaint**
Primary record representing a complaint ticket.

- `complaint_id` – primary key  
- `company_id` – foreign key to Company  
- `user_id` – foreign key to User (creator)  
- `assigned_to` – optional foreign key to User (handler)  
- `category`  
- `title`  
- `description`  
- `priority`  
- `status` – Open / In Progress / Pending / Resolved / Closed  
- `channel` – Web / Mobile / Phone  
- `created_at`  
- `updated_at`

The PoC uses a simplified subset of these attributes (title, description, status, timestamps).

---

### **StatusHistory**
Tracks each transition in a complaint’s lifecycle.

- `history_id` – primary key  
- `complaint_id` – foreign key to Complaint  
- `changed_by` – foreign key to User  
- `from_status`  
- `to_status`  
- `changed_at`

---

### **AuditLog**
Captures actions performed across the system for traceability.

- `audit_id` – primary key  
- `company_id` – foreign key to Company  
- `actor_id` – foreign key to User  
- `entity_type` – e.g., Complaint, User  
- `entity_id` – ID of affected record  
- `action` – Create / Update / Delete  
- `timestamp`

---

## Entity Relationships

- **Company → Users:** 1 to Many  
- **Company → Complaints:** 1 to Many  
- **User → Complaints:** 1 to Many  
- **Complaint → StatusHistory:** 1 to Many  
- **Complaint → Attachments:** 1 to Many  
- **User → StatusHistory:** 1 to Many  
- **Company → AuditLog:** 1 to Many  

These relationships support complaint lifecycle tracking, auditing, and data isolation.

---

## Multi-Tenant Data Strategy

The CMS uses a shared database with **row-level tenant isolation**.  
Each tenant-owned table (User, Complaint, StatusHistory, Attachment, AuditLog) includes a `company_id` attribute.

Django ORM queries filter by `company_id`, ensuring:

- Users only access data from their own organisation  
- Cross-tenant access is impossible  
- Security and compliance requirements are met  
- Consistent behaviour across UI, service, and data layers  


