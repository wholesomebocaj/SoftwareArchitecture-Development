# C4 Level 2: Container Diagram

## System Overview

![C4 Level 2 Container Diagram](https://github.com/user-attachments/assets/63308f39-6370-4039-9243-3911993b1486)

*Figure 1: Container diagram showing the internal structure of the Complaint Management System using a layered N-tier architecture*

## Architecture Description

This container diagram illustrates the internal structure of the Complaint Management System (CMS) using a **layered (N-tier) architecture**. The system is organized into three distinct layers, each with specific responsibilities and technologies.

## Architectural Layers

### Presentation Layer
**Responsibility**: User interface and client-side interactions

| Component | Technology | Purpose |
|-----------|------------|---------|
| Web Application | HTML, CSS, JavaScript | Responsive web interface serving all user roles with WCAG-compliant accessibility |

### Application Layer
**Responsibility**: Business logic and application services

| Component | Technology | Purpose |
|-----------|------------|---------|
| Express.js API | Node.js, Express.js | Core backend service, handles all the complaint processes and talks to both the website and the database |
| Auth Module | JWT, bcrypt | User authentication and token-based security |
| Notification Module |   | Centralized email and SMS notification delivery |

### Data Layer
**Responsibility**: Data persistence and storage

| Component | Technology | Purpose |
|-----------|------------|---------|
| SQLite Database | SQLite | Primary data store with multi-tenant architecture using company_id field isolation |

## External Integrations

### Current Integrations

### Future Integrations
- SMS Gateway: SMS alert capabilities for real-time notifications
- Payment System: Refund processing functionality for financial transactions
- SMTP Server: Email delivery for complaint notifications and status updates


## Key Architectural Features

### Structural Patterns
- Layered Architecture: Clear separation of concerns between presentation, application, and data layers
- Multi-tenancy: Data isolation between different client companies using company_id field
- RESTful APIs: Standardized communication between frontend and backend components

### Quality Attributes
- Centralized Notifications: All notification services (email and SMS) handled by dedicated Notification Module
- Accessibility Compliance: WCAG standards implemented throughout the presentation layer
- Security: JWT-based authentication with bcrypt password hashing

## Technology Stack Summary

| Layer | Technologies |
|-------|-------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Node.js, Express.js |
| Database | SQLite |
| Authentication | JWT, bcrypt |
| Notifications | SMTP |

## System Capabilities

The architecture supports the core complaint management workflow while maintaining:
- Scalability through modular design
- Security via proper separation of concerns
- Maintainability with clear layer boundaries
- Extensibility for future integrations

This layered approach ensures that each component has well-defined responsibilities, making the system easier to develop, test, and maintain while supporting the complex requirements of multi-tenant complaint management.
