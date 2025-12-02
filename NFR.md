# Non-Functional Requirements

| ID | Theme | Description | Priority (MoSCoW) |
|----|--------|-------------|-------------------|
| **NFR01** | **Availability** | The CMS online services must be available 24/7 with a minimum uptime of **99.9%** per month. Scheduled maintenance must be limited to **no more than 2 hours per month**, with tenants notified at least 48 hours in advance. | **Must** |
| **NFR02** | **Accessibility** | All key user flows (logging a complaint, viewing status, updating a case) must conform to **WCAG 2.1 Level AA** standards, including correct semantic labels, keyboard navigability, appropriate contrast ratios, and assistive technology compatibility. | **Must** |
| **NFR03** | **Security** | The CMS must enforce **tenant-level data isolation**, ensuring that no cross-organisation data exposure occurs at the UI, API, or database layers. Strict RBAC must be implemented so users can only access features permitted by their role. | **Must** |
| **NFR04** | **Security** | All sensitive operations must be protected using Django’s built-in security mechanisms, including **CSRF protection**, **input validation**, **password hashing**, and **session management**. Audit logs must track all create/update/delete operations with timestamp, actor, and tenant ID. | **Must** |
| **NFR05** | **Performance** | The system must allow consumers to create a complaint in **≤ 10 seconds** under normal load, including validation and database write operations. Viewing complaint status must retrieve results in **≤ 5 seconds**. | **Should** |
| **NFR06** | **Scalability** | The system must support enterprise-level tenants with **20 million+ potential users**, with capacity to handle **10% annual growth** in traffic and data volume without requiring major architectural redesign. | **Should** |
| **NFR07** | **Extensibility** | The CMS architecture must permit future integration of AI-powered chatbots, SMS gateways, and regional deployments without requiring core redesign of business logic or data structures. | **Could** |
| **NFR08** | **Reliability** | All complaint-related operations must complete atomically. Failed workflows (e.g., partial updates) must be rolled back automatically to maintain data consistency. | **Must** |
| **NFR09** | **Usability** | Staff users (agents, support engineers, managers) must be able to navigate core workflows with **no more than 3 clicks** from the dashboard. Consumer flows must remain simple and low-cognitive-load, especially on mobile. | **Should** |
| **NFR10** | **Maintainability** | The system must use a layered, modular architecture so that components (UI, business logic, data access) can be changed or extended independently. Common maintenance tasks must be executable within **< 30 minutes** by system administrators. | **Could** |


# Functional Requirements (FR)

| Code | Name | Description | Acceptance Criteria | Priority |
|------|------|-------------|---------------------|----------|
| **RF01** | **Submit Complaint** | Consumers submit complaints via web/mobile with attachments. | Validated fields; unique ticket ID; confirmation; status Open; create ≤10s. | High |
| **RF02** | **Phone Logging** | Agents log complaints from calls with verified consumer. | Channel=phone; same validation; confirmation to caller. | High |
| **RF03** | **Track Status** | Consumers view complaint status and timeline. | Secure to owner; updates within 10s; notifications on changes. | High |
| **RF04** | **Assign Support** | Agents assign support with priority/SLA. | Assignment recorded; support notified. | High |
| **RF05** | **Update Resolution** | Support updates notes and status transitions. | Only assigned support; valid transitions; timestamped notes. | High |
| **RF06** | **Confirm & Close** | Consumers confirm resolution and provide CSAT. | Allowed only if Resolved; closure timestamp; CSAT captured. | Medium |
| **RF07** | **Dashboards** | Managers view SLA performance, TTR, workload, CSAT. | Filters by time and user/team; key KPIs visible. | Medium |
| **RF08** | **Tenant Onboarding** | Admins create tenant, branding, hours, channels. | Roles seeded; users invited; isolation smoke test passes. | High |
| **RF09** | **RBAC** | Role-based permissions by tenant. | Least privilege; role assignment audited. | High |
| **RF10** | **Notifications** | Email/SMS notifications for major status changes. | Retries and preferences supported. | Medium |
| **RF11** | **Audit Trail** | Log create/update/delete with actor and tenant. | Timestamped; before/after where feasible. | High |
| **RF12** | **Attachments** | Upload evidence to complaints. | File checks; stored references linked to ticket. | Medium |
| **RF13** | **Search/Filter** | Find and filter complaints. | Filter by status, priority, assignee, date. | Medium |
