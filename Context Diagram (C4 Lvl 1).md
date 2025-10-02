# System Context Diagram (C4 Level 1)

## Diagram
<img width="899" height="746" alt="image" src="https://github.com/user-attachments/assets/b5de0d23-09ca-4737-b802-182608ea6742" />

At the system context level, CMS is the central system in scope, surrounded by the different **users (people)** and **external systems** it interacts with.

## People (Actors)
- **Consumers** – They use the system to log complaints, check complaint status, and confirm when an issue is resolved.  
- **Help Desk Agents** – They receive consumer calls, log complaints on behalf of consumers, update statuses, resolve simple issues, and close complaints once consumers confirm satisfaction.  
- **Support Persons** – Specialists who work on assigned complaints, provide technical resolutions, and update resolution notes in CMS.  
- **Help Desk Managers** – Supervisors who monitor complaint resolution times, track performance of support staff and agents, and generate reports to improve efficiency.  
- **System Administrators** – ABC Limited’s internal administrators who onboard new organisations, configure roles and permissions, and maintain the system.  

## External Systems
- **Company Web/Mobile Application** – Provides the user interface for consumers to log and track complaints online.  
- **Email/SMS Gateway** – Sends automated notifications and updates to consumers about complaint progress.  
- **Telephone System** – Routes consumer phone calls to help desk agents, enabling complaints to be logged via voice channels.  
- **Chatbot (Future)** – A potential integration for automated complaint logging and resolution.  

## Key Interactions
- Consumers interact with CMS through the web/mobile app or by calling the help desk via the telephone system.  
- CMS sends updates back to consumers via email or SMS.  
- Help Desk Agents use CMS to log complaints, update progress, and confirm resolution.  
- Support Persons use CMS to provide detailed resolution notes.  
- Help Desk Managers use CMS for oversight, monitoring, and reporting.  
- System Administrators maintain CMS, configure tenants, and ensure secure multi-tenant data isolation between different organisations.  

---
