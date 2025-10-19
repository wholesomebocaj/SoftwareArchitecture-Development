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
