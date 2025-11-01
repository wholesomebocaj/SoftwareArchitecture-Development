# C4 Level 3: Flask API Component Diagram

<img width="676" height="955" alt="image" src="https://github.com/user-attachments/assets/dbc47783-54fd-40c0-822d-df5a6c4f18a3" />

*Component diagram showing the internal structure of the Flask API using layered architecture*

## Architecture Description

This component diagram shows how the Flask API container is put together on the inside. It shows the layered architecture that handles the CMS's main business logic. The API is split into three separate layers that make sure that different issues are handled properly and that the code structure is easy to maintain.

## Component Layers

### Controllers Layer (Presentation)
**Responsibility**: Handle incoming HTTP requests and responses

| Component | Technology | Purpose |
|-----------|------------|---------|
| Complaint Controller | Flask Routes | Receives and validates all complaint-related web requests |
| User Controller | Flask Routes | Manages user authentication, registration, and account management |

### Services Layer (Business Logic)
**Responsibility**: Implement business rules and workflow orchestration

| Component | Technology | Purpose |
|-----------|------------|---------|
| Complaint Service | Python Class | Oversees the whole process of complaints and business rules |
| User Service | Python Class | Handles user management, authentication, and role-based permissions |

### Data Layer (Persistence)
**Responsibility**: Handle data storage and retrieval operations

| Component | Technology | Purpose |
|-----------|------------|---------|
| Data Manager | Python Class | Provides database operations with automatic multi-tenant filtering |

## External Dependencies

| System | Role | Interaction |
|--------|------|-------------|
| Web Application | User Interface | Sends HTTP requests for all user interactions |
| SQLite Database | Data Storage | Persistent storage for users, complaints, and company data |

## Data Flow

### Complaint Creation Workflow:
1. **Web Application** → Sends request → **Complaint Controller**
2. **Complaint Controller** → Processes request → **Complaint Service**
3. **Complaint Service** → Checks permissions → **User Service**
4. **Complaint Service** → Saves data → **Data Manager**
5. **Data Manager** → Reads/writes → **SQLite Database**

### User Authentication Workflow:
1. **Web Application** → Sends request → **User Controller**
2. **User Controller** → Processes request → **User Service**
3. **User Service** → Saves/loads data → **Data Manager**
4. **Data Manager** → Reads/writes → **SQLite Database**

## Key Architectural Features

### Design Patterns
- **Layered Architecture**: Clear separation between presentation, business logic, and data access
- **Single Responsibility**: Each component has a focused, specific purpose
- **Dependency Injection**: Services are independent and testable

### Multi-tenancy Implementation
- Automatic `company_id` filtering at the Data Manager level
- Data isolation enforced throughout the data access layer
- Role-based permissions managed by User Service

### Security Features
- Centralised authentication via User Service
- Role-based access control
- Input validation at controller level

## Technology Implementation

| Layer | Components | Technologies |
|-------|------------|--------------|
| Presentation | Controllers | Flask Routes, HTTP handling |
| Business Logic | Services | Python classes, business rules |
| Data Access | Data Manager | SQL queries, multi-tenant filtering |

## Component Responsibilities

### Complaint Controller
- Validate incoming complaint data
- Route requests to appropriate services
- Return HTTP responses to web application

### User Controller  
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

### Data Manager
- Execute database operations
- Apply company_id filtering
- Manage database connections
- Handle data persistence

This layered component architecture makes sure that the Flask API can handle the complex needs of managing complaints from multiple tenants while still being scalable, maintainable, and testable.

---
