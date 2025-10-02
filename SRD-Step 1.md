# Step 1 — requirements-document.md

# Software Requirements Document (SRD)

## 1. Project Identification

**Project Name:** ABC Complaint Management System (CMS)  
**Document Version:** 0.1 (draft)  
**Date:** 2025-09-30  
**Author(s):** Individual student submission

## 2. Document Purpose

This document describes functional and non-functional requirements, business rules, and constraints for a multi-tenant CMS for banking/telecom organizations, guiding architecture, design, and PoC scope.

## 3. System Overview

**System Description:** Multi-channel complaint lifecycle: log, triage, assign, resolve, confirm/close; channels include web, mobile, and phone; extensible to chatbot and other regions.  
**System Objectives:** Streamline complaint handling, improve SLA compliance and CSAT, provide dashboards and auditability, and ensure tenant isolation for enterprise customers.  
**Target Audience/End Users:** Consumers, Help Desk Agents, Support Engineers, Managers, and System Administrators per tenant.  
**General Functional Scope:** Complaint creation and tracking, assignment and updates, resolution and closure, analytics dashboards, onboarding, RBAC, notifications, audit, attachments, search/filter.

## 4. Functional Requirements

| Code | Name | Description | Acceptance Criteria | Priority |
|------|------|-------------|---------------------|----------|
| RF01 | Submit Complaint | Consumers submit complaints via web/mobile with attachments. | Validated fields; unique ticket ID; confirmation; status Open; create ≤10s. | High |
| RF02 | Phone Logging | Agents log complaints from calls with verified consumer. | Channel=phone; same validation; confirmation to caller. | High |
| RF03 | Track Status | Consumers view complaint status and timeline. | Secure to owner; updates within 10s; notifications on changes. | High |
| RF04 | Assign Support | Agents assign support with priority/SLA. | Assignment recorded; support notified. | High |
| RF05 | Update Resolution | Support updates notes and status transitions. | Only assigned support; valid transitions; timestamped notes. | High |
| RF06 | Confirm & Close | Consumers confirm resolution and provide CSAT. | Allowed only if Resolved; closure timestamp; CSAT captured. | Medium |
| RF07 | Dashboards | Managers view SLA performance, TTR, workload, CSAT. | Filters by time and user/team; key KPIs visible. | Medium |
| RF08 | Tenant Onboarding | Admins create tenant, branding, hours, channels. | Roles seeded; users invited; isolation smoke test passes. | High |
| RF09 | RBAC | Role-based permissions by tenant. | Least privilege; role assignment audited. | High |
| RF10 | Notifications | Email/SMS notifications for major status changes. | Retries and preferences supported. | Medium |
| RF11 | Audit Trail | Log create/update/delete with actor and tenant. | Timestamped; before/after where feasible. | High |
| RF12 | Attachments | Upload evidence to complaints. | File checks; stored references linked to ticket. | Medium |
| RF13 | Search/Filter | Find and filter complaints. | Filter by status, priority, assignee, date. | Medium |

## 5. Non-Functional Requirements

| Code | Type | Description | Priority |
|------|------|-------------|----------|
| RNF01 | Availability | Online channels available 24/7; phone per tenant hours. | High |
| RNF02 | Accessibility | Key flows conform to WCAG 2 basics (contrast, keyboard, labels, focus). | High |
| RNF03 | Security | Tenant isolation, RBAC, secure auth, audit logs, compliance readiness. | High |
| RNF04 | Performance | Create/view actions respond within target times under expected load. | Medium |
| RNF05 | Scalability | Support growth to large enterprise volumes; plan for regional expansion. | Medium |
| RNF06 | Extensibility | Future chatbot channel and regionalization supported. | Medium |

## 6. Business Rules

| Code | Description |
|------|-------------|
| RN01 | Only assigned support or agents can change complaint statuses per workflow. |
| RN02 | Consumers can close complaints only from Resolved state and must provide CSAT. |
| RN03 | All actions are logged with tenant context and actor identity. |
| RN04 | Cross-tenant data access is prohibited and blocked at UI, API, and data layers. |

## 7. Integration Requirements

- Email/SMS provider for notifications.
- Optional SSO/identity provider; future chatbot/IVR integrations.

## 8. Technical Restrictions

- Use architectural standards suitable for C4 modelling and ADR documentation; ensure RBAC and multi-tenancy enforcement in chosen stack.
- Follow inclusivity/accessibility guidance from the assessment brief.

## 9. General Acceptance Criteria

- Creating a complaint issues a unique ID, sends confirmation, and shows status within 10s under normal load.
- Tenant isolation holds across UI/API/data; cross-tenant attempts are denied and audited.
- Accessibility checks pass on complaint creation and status flows.

## 10. Annexes/References

Assessment Case Study and Assessment Brief; future links to diagrams and ADRs.
