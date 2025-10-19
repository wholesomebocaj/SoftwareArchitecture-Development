# Architectural Style Selection for CMS

## Context and Problem Statement

The Complaint Management System (CMS) needs an architecture that supports multiple tenants from banking and telecom sectors, providing scalable, maintainable, and secure complaint management across web, mobile, and phone channels. Which architectural style balances ease of implementation for learners and robustness for production use?

## Considered Options

- Layered (N-Tier) Architecture  
- Three-Tier Architecture  
- Client-Server Architecture  

## Decision Outcome

Chosen option: "Layered (N-Tier) Architecture", because it provides clear separation of concerns into presentation, business logic, and persistence layers, enabling modular development and maintainability. It also aligns well with extensibility requirements and the C4 modeling approach used in the module.

## Consequences

Good, because this style supports modularity, testability, and clear division of responsibilities, making it easier to develop and maintain the CMS progressively. It also facilitates compliance with accessibility and security requirements.

Bad, because it may introduce some inter-layer communication overhead and can lead to increased complexity if layers are over-engineered or poorly managed.

# Technology Stack Implementation

## Selected Technologies

**Presentation Layer:** HTML, CSS, JavaScript  
**Application Layer:** Node.js, Express.js, JWT and bcrypt authentication  
**Data Layer:** SQLite with multi-tenant design (company_id isolation)

## Rationale for Technology Choices

### Why HTML/CSS/JavaScript
- Low learning curve for proof-of-concept development
- Direct support for WCAG accessibility requirements
- No complex build tools or frameworks needed for initial implementation
- Suitable for demonstrating core functionality without overhead

### Why Node.js + Express.js
- Single language (JavaScript) across frontend and backend reduces complexity
- Express.js provides minimal, flexible framework for overall product development
- Extensive ecosystem for rapid prototyping
- Aligns with learning objectives for web application development

### Why SQLite
- Supports relational data modeling needed for complaint management
- Enables multi-tenancy through simple company_id field approach
- Reduces deployment complexity during development phase

### Why JWT 
- JWT provides stateless authentication suitable for overall product development
- lightweight and focused on core requirements

## Consequences

### Positive Outcomes
- Simple, well-known technologies reduce development risk
- Single language stack (JavaScript) improves maintainability
- Lightweight stack enables rapid proof-of-concept development
- Clear separation of concerns supports incremental implementation
- Technologies align with module learning objectives

### Negative Outcomes
- SQLite has scalability limitations for production deployment
- Simplified stack may lack enterprise features needed for large-scale deployment
- Limited framework support may require more custom implementation
- May need technology upgrades for production readiness
