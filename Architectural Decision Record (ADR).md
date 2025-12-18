Architecture Decision Records 

Architectural Style Selection for CMS 

Context and Problem Statement 

The Complaint Management System (CMS) must support multiple tenants from banking and telecom sectors, providing scalable, maintainable, and secure complaint management across web, mobile, and phone channels. The architecture should balance ease of implementation (suitable for learners) and robustness for production deployment. 

Considered Options: 

*   Layered (N-Tier) Architecture 
    

*   Three-Tier Architecture 
    

*   Client-Server Architecture 
    

Decision Outcome 

Chosen option: Layered (N-Tier) Architecture, because it supports clear separation into presentation, business logic, and persistence layers, facilitating modular development, maintainability, and extensibility. This style aligns well with the C4 modelling approach and accessibility/security compliance. 

Consequences 

Good: 

*   Modular design ensures separation of concerns, improving testability and maintainability. 
    

*   Facilitates progressive development and scaling in multi-tenant environments. 
    

*   Supports accessibility and security requirements effectively. 
    

Bad: 

*   May introduce inter-layer communication overhead. 
    

*   There is a risk of increased complexity if the layers are over-engineered or not managed properly. 
    

Technology Stack Implementation 

Considered Options: 

Application Layer: I wanted to code in Python, which led me to decide on either Django or Flask for my backend of the CMS. 

Data Layer: PostgreSQL, SQLite, SQLAlchemy 

Consequences of Flask: 

Advantages: 

*   Lightweight and minimal framework. 
    

*   High flexibility in structuring the application. 
    

*   Suitable for small applications and simple Proofs-of-Concept. 
    

Disadvantages: 

*   No built\-in authentication. 
    

*   Security features must be implemented manually or via third-party libraries. 
    

*   No built-in admin interface for managing data. 
    

*   Increased development effort to enforce layered architecture and role-based access control. 
    

*   Higher risk of inconsistency between architectural design and implementation. 
    

Consequences of SQLite: 

Advantages: 

*   Doesn’t require a separate database server. 
    

*   Very easy to configure and use for small-scale applications. 
    

*   Suitable for rapid prototyping and development environments. 
    

Disadvantages: 

*   Not suitable for enterprise-scale or high\-traffic systems. 
    

*   Lacks advanced security and access control features. 
    

*   Poor fit for multi-tenant architectures with large data volumes. 
    

*   File-based databases in a big application with lots of users can cause many problems, for example, data redundancy and inconsistency, limited scalability or lack of data integrity. 
    

Consequences of SQLAlchemy: 

Advantages: 

*   A powerful and flexible ORM library 
    

*   Allows switching between database backends making it extremely flexible  
    

*   Widely used and well-documented within the Python ecosystem 
    

Disadvantages: 

*   Requires additional configuration compared to Django ORM 
    

*   No built-in integration with authentication or authorised systems 
    

*   Multi-tenant data isolation must be manually enforced 
    

*   Increased overall development complexity  
    

Selected Technologies 

Presentation Layer: HTML, CSS, JavaScript 

Application Layer: Python, Django, Django's built-in authentication 

Data Layer: PostgreSQL with a multi-tenant design approach 

Rationale for Technology Choices 

Why HTML/CSS/JavaScript 

*   Low learning curve for frontend prototyping. 
    

*   Native support for WCAG accessibility standards. 
    

*   Enables demonstration of core functionalities with minimal overhead. 
    

Why Python and Django 

*   Robust and Scalable: Django's comprehensive features suit enterprise-grade applications for banking and telecom clients. 
    

*   Built-in Authentication: Provides secure, feature-rich authentication and authorisation out-of-the-box, including role-based access control. 
    

*   Modular and Maintainable: Aligns with layered architecture principles and supports clear separation of concerns. 
    

*   Multi-tenancy Support: Can implement tenancy isolation effectively, supported by rich middleware and ORM capabilities. 
    

*   Testing and Security: Extensive tooling and community support for quality assurance and security best practices. 
    

Why PostgreSQL 

*   Production-Ready: Highly scalable and reliable for expected CMS workloads. 
    

*   Advanced Features: Supports robust multi-tenancy, complex queries, indexing, and full-text search, which is beneficial for complaint management. 
    

*   Security: Provides advanced database security features aligning with compliance needs. 
    

*   Django Integration: Highly compatible with Django ORM for a seamless development experience. 
    

Consequences 

Advantages 

*   Improved scalability and reliability for production deployment. 
    

*   The integration of advanced security and authentication features has been seamless. 
    

*   The system exhibits strong alignment with the goals of maintainability, modularity, and extensibility. 
    

*   Django's admin interface enhances the admin capabilities for system management. 
    

Disadvantages 

*   A steeper learning curve compared to Flask, which may initially slow development. 
    

*   Increased complexity in setting up and managing multi-tenant architecture. 
    

*   Requires PostgreSQL deployment and management infrastructure.
