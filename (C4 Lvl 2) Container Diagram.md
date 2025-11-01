# Container Diagram (C4 Level 2)

## System Overview

<img width="1860" height="1600" alt="image" src="https://github.com/user-attachments/assets/e9bef470-088b-4939-b322-b4824d10cca3" />

*Figure 1: Container diagram showing the internal structure of the Complaint Management System using a layered N-tier architecture*

## Architecture Description

This container diagram uses a layered (N-tier) architecture to show the Complaint Management System's (CMS) internal organisation. The system supports multi-tenant architecture and is divided into discrete layers, each with unique responsibilities and technologies.

## Architectural Layers

### Presentation Layer
**Responsibility**: User interface and client-side interactions

| Component | Technology | Purpose |
|-----------|------------|---------|
| Web Application | HTML, CSS, JavaScript | Responsive web interface serving all user roles with WCAG-compliant accessibility |

### Business Layer
**Responsibility**: Business logic and application services

| Component | Technology | Purpose |
|-----------|------------|---------|
| Flask API | Python, Flask | Core backend service handling complaint processes and multi-tenant routing |
| Auth Module | JWT, bcrypt | User authentication and token-based security |
| Notification Module | Python | Centralised email notification delivery |

### Data Layer
**Responsibility**: Data persistence and storage

| Component | Technology | Purpose |
|-----------|------------|---------|
| SQLite Database | SQLite | Primary data store with multi-tenant architecture using company_id field isolation |

## External Integrations

### Current Integrations
- SMTP Server: Email delivery for complaint notifications and status updates

### Future Integrations
- SMS Gateway: SMS alert capabilities for real-time notifications
- Payment System: Refund processing functionality for financial transactions
- Chatbot Service: Automated problem resolution using AI/NLP
- Mobile Application: Native mobile access for consumers

## Key Architectural Features

### Structural Patterns
- **Layered Architecture**: Clear separation of concerns between presentation, business, and data layers
- **Multi-tenancy**: Data isolation between different client companies using company_id field
- **API-First Design**: Standardised communication between frontend and backend components

### Quality Attributes
- **Centralized Notifications**: Email notification services handled by dedicated Notification Module
- **Accessibility Compliance**: WCAG standards implemented throughout the presentation layer
- **Security**: JWT-based authentication with bcrypt password hashing
- **Scalability**: Designed to handle a large scale of users

## Technology Stack Summary

| Layer | Technologies |
|-------|-------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Database | SQLite |
| Authentication | JWT, bcrypt |
| Notifications | Python, SMTP |

## System Capabilities

The architecture supports the core complaint management workflow while maintaining:
- **Scalability** via multi-tenant architecture and modular design
- **Security** via proper separation of concerns and token-based authentication
- **Maintainability** with clear layer boundaries and Python/Flask simplicity
- **Extensibility** for future integrations (SMS, payments, chatbot, mobile)

In addition to supporting the complex needs of multi-tenant complaint management across numerous industries, this layered approach guarantees that each component has clearly defined responsibilities, making the system simpler to develop, test, and maintain.

---
