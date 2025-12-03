# Data Design

The data design for the Complaint Management System (CMS) defines the core entities, attributes, and relationships required to support the complaint lifecycle and multi-tenant architecture. The schema reflects the real Django models implemented in the proof-of-concept (PoC) system and supports tenant isolation, role-based access, and complaint status auditing.

---

## Company (Tenant)

Represents an organisation using the CMS.  
This entity enables multi-tenant isolation.

### Attributes
- `id` — Primary key  
- `name` — Organisation name  
- `industry` — e.g., Banking, Telecom, Airline  

*Note: Additional attributes such as operational hours or metadata can be added later but are not required for the PoC.*

---

## User + UserProfile (Authentication + Domain Roles)

The CMS uses Django’s built-in `User` model for authentication and a related `UserProfile` model for tenant and role information.

### Django `User` (built-in)
- `id` — Primary key  
- `username`  
- `password` (hashed)  
- `email` (optional)  
- Standard Django flags (`is_staff`, `is_superuser`, etc.)

### `UserProfile` (domain model)
- `id` — Primary key  
- `user` — One-to-one FK to `User`  
- `company` — FK to `Company`  
- `role` — `CONSUMER`, `AGENT`, `SUPPORT`, `MANAGER`, `ADMIN`

The combination of **User + UserProfile** replaces the conceptual “User” table in the high-level design.

---

## Complaint

Represents a customer complaint submitted by a consumer.  
Staff roles (Agent, Support, Manager, Admin) can view and update complaints.

### Attributes
- `id` — Primary key  
- `company` — FK to `Company`  
- `created_by` — FK to `User` (must be a Consumer)  
- `title`  
- `description`  
- `category`  
- `priority` — Low / Medium / High  
- `status` — Open / In Progress / Pending / Resolved / Closed  
- `channel` — Web (PoC)  
- `created_at`  
- `updated_at`

Only the core subset is implemented in the PoC, consistent with the MVP requirement.

---

## ComplaintStatusHistory

Tracks every status change applied to a complaint.  
This provides the required audit trail within the PoC.

### Attributes
- `id` — Primary key  
- `complaint` — FK to `Complaint`  
- `changed_by` — FK to `User`  
- `old_status`  
- `new_status`  
- `changed_at`  
- `note` — Optional text explaining the update

---

# Entity Relationships

| Relationship | Type |
|-------------|------|
| Company → UserProfile | 1 to Many |
| User → UserProfile | 1 to 1 |
| Company → Complaints | 1 to Many |
| User (Consumer) → Complaints (created_by) | 1 to Many |
| Complaint → ComplaintStatusHistory | 1 to Many |
| User → ComplaintStatusHistory (changed_by) | 1 to Many |
| Complaint → Attachments (future) | 1 to Many |
| Company → AuditLog (future) | 1 to Many |

These relationships support:

- Multi-tenant isolation  
- Complaint lifecycle management  
- Staff vs consumer role-based workflows  
- Auditable state transitions  

---

# Multi-Tenant Data Strategy

The CMS uses a **shared-database, row-level multi-tenant architecture**.

- Each **UserProfile** points to one **Company**  
- Each **Complaint** points to one **Company**  
- Each **StatusHistory** record inherits its tenant via `complaint.company`  

The application layer consistently filters by:

