# C4 Level 3: Flask API Component Diagram

<img width="676" height="955" alt="image" src="https://github.com/user-attachments/assets/dbc47783-54fd-40c0-822d-df5a6c4f18a3" />
<img width="463" height="1125" alt="c4 level 3 python django" src="https://github.com/user-attachments/assets/528ca6ff-76e2-467e-8742-eb18faca1944" />

*Component diagram showing the internal structure of the Flask API using layered architecture*

## Architecture Description

This component diagram shows how the Django API container is structured internally. It illustrates the layered architecture that handles the CMS's core business logic. The API is organised into three distinct layers that ensure proper separation of concerns and maintainable code structure.

## Component Layers

### Views Layer (Presentation)
**Responsibility**: Handle incoming HTTP requests and responses

| Component | Technology | Purpose |
|-----------|------------|---------|
| Complaint Views | Django Views | Receives and validates all complaint-related web requests |
| User Views | Django Views | Manages user authentication, registration, and account management |

### Services Layer (Business Logic)
**Responsibility**: Implement business rules and workflow orchestration

| Component | Technology | Purpose |
|-----------|------------|---------|
| Complaint Service | Python Class | Oversees the complete complaint process and business rules |
| User Service | Python Class | Handles user management, authentication, and role-based permissions |

### Data Layer (Persistence)
**Responsibility**: Handle data storage and retrieval operations

| Component | Technology | Purpose |
|-----------|------------|---------|
| Django ORM | Django ORM | Provides database operations with automatic multi-tenant filtering |

## External Dependencies

| System | Role | Interaction |
|--------|------|-------------|
| Web Application | User Interface | Sends HTTP requests for all user interactions |
| PostgreSQL Database | Data Storage | Persistent storage for users, complaints, and company data |

## Data Flow

### Complaint Creation Workflow:
1. **Web Application** → Sends request → **Complaint Views**
2. **Complaint Views** → Processes request → **Complaint Service**
3. **Complaint Service** → Checks permissions → **User Service**
4. **Complaint Service** → Saves data → **Django ORM**
5. **Django ORM** → Reads/writes → **PostgreSQL Database**

### User Authentication Workflow:
1. **Web Application** → Sends request → **User Views**
2. **User Views** → Processes request → **User Service**
3. **User Service** → Saves/loads data → **Django ORM**
4. **Django ORM** → Reads/writes → **PostgreSQL Database**

## Key Architectural Features

### Design Patterns
- **Layered Architecture**: Clear separation between presentation, business logic, and data access
- **Single Responsibility**: Each component has a focused, specific purpose
- **Dependency Injection**: Services are independent and testable

### Multi-tenancy Implementation
- Automatic `company_id` filtering at the Django ORM level
- Data isolation enforced throughout the data access layer
- Role-based permissions managed by User Service

### Security Features
- Centralised authentication via User Service
- Role-based access control
- Input validation at views level
- Django's built-in security middleware

## Technology Implementation

| Layer | Components | Technologies |
|-------|------------|--------------|
| Presentation | Views | Django Views, HTTP handling |
| Business Logic | Services | Python classes, business rules |
| Data Access | Django ORM | Object-relational mapping, multi-tenant filtering |

## Component Responsibilities

### Complaint Views
- Validate incoming complaint data
- Route requests to appropriate services
- Return HTTP responses to web application

### User Views  
- Handle login/logout requests
- Manage user registration
- Process profile updates

### Complaint Service
- Orchestrate complaint workflow
- Enforce business rules
- Manage status transitions
- Handle multi-tenant data routing

### User Service
- Authenticate user credentials
- Manage role-based permissions
- Handle company onboarding
- Enforce security policies

### Django ORM
- Execute database operations
- Apply company_id filtering
- Manage database connections
- Handle data persistence through models

This layered component architecture ensures that the Django API can handle the complex requirements of multi-tenant complaint management while remaining scalable, maintainable, and testable. The use of Django's built-in ORM and view system provides a robust foundation for enterprise-grade application development.

---
