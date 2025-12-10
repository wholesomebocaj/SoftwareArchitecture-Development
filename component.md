C4 Component Diagram (level 3)

Component diagram showing the internal structure of the Django API using layered architecture.

In software architecture literature, layered architectures are commonly represented as either three-tier (Presentation, Application/Business, Data) or four-tier structures where Application and Business Logic are separated. For this CMS, the architecture adopts the standard three-layer structure (Presentation, Application & Business, Data), while still recognising that Django allows business rules to be refined into service components within the middle layer as the system evolves.

Architecture Description  
This component diagram shows how the Django-based Complaint Management System (CMS) is structured internally. It follows a three-layer architecture:

1. Presentation / UI Layer  
2. Application & Business Layer  
3. Data Layer  

The Presentation layer runs in the web front end, while the Application & Business and Data layers are hosted inside the Django backend container. This structure provides clear separation of concerns while remaining compatible with Django’s idiomatic patterns and the Proof of Concept implementation.

Component Layers  

1. Presentation / UI Layer (Web Frontend)  
Responsibility: Render user interfaces and capture user input.

This layer is primarily shown in the Context and Container diagrams, but is included here for completeness:

Component      | Technology              | Purpose
-------------- | ----------------------- | -----------------------------------------------
Web Pages      | Django Templates (HTML) | Render complaint forms, dashboards, and status views.
Static Assets  | CSS, basic JavaScript   | Provide layout, styling, and accessibility (WCAG 2.1).

This layer does not contain business rules; it only displays data and sends user input to the backend via HTTP requests.

2. Application & Business Layer (Views, Forms, Services)  
Responsibility: Handle HTTP requests, coordinate use cases, enforce rules, and apply complaint workflow logic.

Component                | Technology                 | Purpose
------------------------ | -------------------------- | -----------------------------------------------
Complaint Views & Forms  | Django Views + ModelForms  | Receive and validate complaint requests, enforce role- and tenant-based access, coordinate create/update flows, and redirect to appropriate screens.
User Views & Forms       | Django Views + Forms       | Handle login/logout, registration, and account management, enforcing RBAC and tenant mapping.
(Planned) Service Classes| Python Classes             | Extract more complex business rules and workflow logic into dedicated, testable components as the system evolves.

In Django terms these are “views” and “forms”, but in this architecture they collectively make up the Application & Business layer: they orchestrate use cases and apply business rules, independent of how data is physically stored.

3. Data Layer (Persistence)  
Responsibility: Store and retrieve tenant-isolated data reliably and securely.

Component          | Technology               | Purpose
------------------ | ------------------------ | -----------------------------------------------
ORM Models & Repos | Django ORM + PostgreSQL  | Define domain entities (companies, users, complaints, history), execute queries with `company_id`-based tenant isolation, and ensure relational integrity and ACID-compliant persistence.

External Dependencies  

System          | Role           | Interaction
--------------- | -------------- | -----------------------------------------------
Web Application | User Interface | Sends HTTP requests and renders HTML/CSS responses from the backend.
PostgreSQL DB   | Data Storage   | Persists users, companies, complaints, and history records via Django ORM.

This three-layer component architecture aligns with the overall layered design defined in the C4 Container model and ADR, while remaining compatible with Django’s recommended patterns and the Proof of Concept implementation.

Implementation Alignment with Layered Architecture  
Django does not physically enforce a split between application flow and business rules. In the current Proof of Concept (PoC), the responsibilities of the Application & Business layer are implemented together within Django views and forms, which:

- handle request flow and validation  
- enforce role-based access control and tenant checks  
- apply complaint workflow logic (e.g. status changes, history updates)  
- map data into ORM models

The Presentation / UI layer is implemented using Django templates and CSS, and all persistence is handled by Django ORM models backed by PostgreSQL, with `company_id` used to enforce multi-tenant isolation.

This approach remains fully aligned with the three-layer architecture defined in the C4 models. As the system evolves, more complex business rules can be refactored into dedicated service classes inside the Application & Business layer, without changing the overall architecture.
