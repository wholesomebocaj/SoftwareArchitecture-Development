# Step 3 — requirements-use-cases.md

# Use Cases

Interactions between users and the system in structured narratives.

## UC001 — Submit Complaint

**Identifier:** UC001  
**Name:** Submit Complaint  
**Main Actor:** Consumer  
**Description:** Consumer submits a complaint with details and optional attachments via web/mobile.  
**Main Flow:** 
1. Open form
2. Enter details
3. Attach files
4. Submit
5. System validates
6. System creates ticket and sends confirmation
7. Status page shown

**Alternative Flows / Exceptions:**
- A) Validation errors
- B) Attachment too large
- C) Unauthenticated—email verification path

## UC002 — Log Complaint via Phone

**Identifier:** UC002  
**Name:** Log Complaint via Phone  
**Main Actor:** Help Desk Agent  
**Description:** Agent records a caller's complaint and creates a ticket flagged as phone channel.  
**Main Flow:**
1. Verify/create consumer
2. Capture details
3. Submit
4. Ticket created with channel=phone
5. Provide confirmation

**Alternative Flows / Exceptions:**
- A) Consumer not found—create provisional profile
- B) Immediate solution accepted—close ticket

## UC003 — Assign Support

**Identifier:** UC003  
**Name:** Assign Support  
**Main Actor:** Help Desk Agent  
**Description:** Agent assigns the ticket to a support engineer and sets priority/SLA.  
**Main Flow:**
1. Open ticket
2. Choose support user
3. Set priority and SLA
4. Save assignment
5. Notify support

**Alternative Flows / Exceptions:**
- A) No support available queue with escalation rule

## UC004 — Update Resolution

**Identifier:** UC004  
**Name:** Update Resolution  
**Main Actor:** Support Engineer  
**Description:** Assigned support updates notes and transitions status with notifications.  
**Main Flow:**
1. Open ticket
2. Add notes/attachments
3. Change status
4. Save
5. Notify consumer

**Alternative Flows / Exceptions:**
- A) Request more info—status Pending Customer
- B) Invalid transition blocked

## UC005 — Confirm Resolution

**Identifier:** UC005  
**Name:** Confirm Resolution  
**Main Actor:** Consumer  
**Description:** Consumer reviews resolution, confirms, and provides CSAT, closing the ticket.  
**Main Flow:**
1. Open resolved ticket
2. Review resolution
3. Confirm resolution
4. Provide CSAT
5. Ticket Closed

**Alternative Flows / Exceptions:**
- A) Reject resolution—ticket Reopened

## UC006 — Tenant Onboarding

**Identifier:** UC006  
**Name:** Tenant Onboarding  
**Main Actor:** System Administrator  
**Description:** Admin creates a tenant, configures branding/hours/channels, seeds roles, and invites users.  
**Main Flow:**
1. Create tenant
2. Configure settings
3. Seed roles
4. Invite users
5. Verify isolation

**Alternative Flows / Exceptions:**
- A) Domain conflict
- B) License limits

## UC007 — View SLA Dashboard

**Identifier:** UC007  
**Name:** View SLA Dashboard  
**Main Actor:** Manager  
**Description:** Manager reviews operational metrics, SLA performance, and workload to identify bottlenecks.  
**Main Flow:**
1. Open dashboard
2. Select time range
3. Apply filters (team/user, priority, status)
4. Review KPIs (TTR, SLA breaches, backlog)
5. Drill down to ticket lists

**Alternative Flows / Exceptions:**
- A) No data for period—show empty state
- B) Export report triggered—download generated

## UC008 — Manage Users and Roles

**Identifier:** UC008  
**Name:** Manage Users and Roles  
**Main Actor:** System Administrator  
**Description:** Admin creates, updates, deactivates users and assigns roles within a tenant.  
**Main Flow:**
1. Open User Management
2. Create or edit user
3. Assign RBAC role(s)
4. Save and send invitation/update
5. Changes captured in audit

**Alternative Flows / Exceptions:**
- A) Duplicate email—block with error
- B) Attempt to assign disallowed role—deny and log

## UC009 — Configure Notifications

**Identifier:** UC009  
**Name:** Configure Notifications  
**Main Actor:** Consumer or Staff User  
**Description:** User selects preferred channels and events for complaint notifications.  
**Main Flow:**
1. Open notification settings
2. Choose channels (email/SMS)
3. Toggle event types (status changes, assignments)
4. Save preferences
5. Confirmation shown

**Alternative Flows / Exceptions:**
- A) Invalid phone/email—validation error
- B) Channel temporarily unavailable—show warning and retry later

## UC010 — Search and Filter Complaints

**Identifier:** UC010  
**Name:** Search and Filter Complaints  
**Main Actor:** Agent or Manager  
**Description:** Staff search and filter complaints to locate cases and manage workloads.  
**Main Flow:**
1. Open complaints list
2. Enter keywords or apply filters (status, priority, assignee, date)
3. View paginated results
4. Open selected complaint

**Alternative Flows / Exceptions:**
- A) No results—show suggestions
- B) Unauthorized item in results—system excludes based on tenant/role

## UC011 — Upload Attachment

**Identifier:** UC011  
**Name:** Upload Attachment  
**Main Actor:** Consumer or Support Engineer  
**Description:** Attach evidence or supporting files to a complaint.  
**Main Flow:**
1. Open complaint
2. Click add attachment
3. Select file
4. System validates size/type
5. Upload and link to complaint
6. Show success

**Alternative Flows / Exceptions:**
- A) File too large/type blocked—error
- B) Virus scan placeholder flags file—reject and notify

## UC012 — Export Reports

**Identifier:** UC012  
**Name:** Export Reports  
**Main Actor:** Manager  
**Description:** Manager exports performance and backlog data for offline review or sharing.  
**Main Flow:**
1. Open dashboard
2. Select export type (CSV/PDF)
3. Choose date range and filters
4. Request export
5. Download file

**Alternative Flows / Exceptions:**
- A) Large dataset—queued and notified when ready
- B) Permission denied—block and log
