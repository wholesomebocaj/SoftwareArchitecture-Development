# System Context Diagram (C4 Level 1)

## Diagram
<img width="841" height="591" alt="C4 Level 1" src="https://github.com/user-attachments/assets/bbb7d6ce-86a5-461c-9ed4-8a78ee445a08" />

## Description
This System Context diagram provides a high-level overview of the Complaint Management System (CMS), showing the system boundaries and its relationships with external users and systems.

## Key Components

### Core System
- **Complaint Management System (CMS)** - The main system managing complaint lifecycle

### User Roles
- **System Administrator** - Manages system configuration and tenants
- **Help Desk Manager** - Oversees support operations and performance
- **Support Person** - Handles complaint resolution and updates
- **Consumer** - Submits and tracks complaints
- **Help Desk Agent** - Logs and assigns complaints

### External Systems & Data Stores
- **Company Web Application** - Web interface for all users
- **Company Mobile Applications** - Mobile access for consumers and staff
- **Telephone Service** - Phone-based complaint logging
- **Company Databases** - Primary data storage for complaints, users, and configurations
- **Email / SMS Notification Service** - Handles user notifications
- **Potential Future Chatbot** - Planned AI/chat interface for complaint handling

## Relationships & Interactions

### User Interactions
- Consumers interact via Web/Mobile apps and Telephone
- Internal staff (Agents, Support, Managers) use Web Application
- System Administrators manage system configuration

### System Dependencies
- CMS relies on Company Databases for data persistence
- Notification Service for user communications
- Future extensibility with Chatbot integration

## System Boundaries
**Internal Systems:** CMS, Company Databases  
**External Interfaces:** Web App, Mobile Apps, Telephone Service, Notification Service  
**Future Components:** Chatbot integration

---
