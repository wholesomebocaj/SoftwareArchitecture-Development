# System Context Diagram (C4 Level 1)

## Diagram
<img width="1133" height="732" alt="c4 level 1 python django" src="https://github.com/user-attachments/assets/08b7e4e8-0eb7-48ca-bd10-0e6ccbaac671" />
At the system context level, the Complaint Management System (CMS) is the central system in scope, surrounded by the different users (people) and external systems it interacts with. 

People (Actors) 

*   Consumers—customers of banking, telecom, or airline companies who use the system to log complaints, check complaint status, and confirm when issues are resolved via web/mobile apps or phones. 
    

*   Help Desk Agents – Frontline staff who receive consumer calls, log complaints, resolve simple issues immediately, assign complex problems to support staff, and update consumers about their resolution status. 
    

*   Support Persons – Technical specialists who work on assigned complaints, provide detailed resolutions, update resolution notes, and change complaint status in the system. 
    

*   Help Desk Managers – Supervisors who monitor complaint resolution times (SLAs), track performance of support staff and agents, generate reports, and optimise help desk operations. 
    

*   System Administrators – ABC Limited’s internal administrators who onboard new clientorganisations, configure multi-tenant settings, manage user roles and permissions, and maintain system-wide operations. 
    

External Systems 

*   Email Service – Sends automated notifications and status updates to consumers about complaint progress and resolutions. 
    

*   SMS Gateway – Delivers text message alerts and reminders to consumers about complaint status changes and required actions. 
    

*   Payment Gateway – Processes refunds and financial transactions related to complaint resolutions (future capability). 
    

*   Chatbot Service (Future) – AI-powered system for automated complaint logging, initial triage, and basic problem resolution. 
    

*   SSO/Identity Provider (Optional) – External authentication service for secure user login across multiple client organisations. 
    

Key Interactions 

*   Consumers interact with CMS through web/mobile applications to log complaints and check status or call help desk agents who use the system on their behalf. 
    

*   CMS sends automated notifications to consumers via email and SMS about complaint progress, resolution updates, and satisfaction surveys. 
    

*   Help Desk Agents use CMS to log complaints from phone calls, provide immediate solutions when possible, assign complex issues to support staff, and close complaints after consumer confirmation. 
    

*   Support Persons access CMS to update resolution details, add technical notes, and progress complaint status through the resolution workflow. 
    

*   Help Desk Managers utilise CMS dashboards and reporting features to monitor team performance, track SLA compliance, and identifyoperational improvements. 
    

*   System Administrators manage the multi-tenant architecture, ensuring data isolation between different client organisations while maintaining system configuration and user access controls. 
    

Key System Characteristics 

*   Multi-tenant Architecture – Ensures complete data isolation between different client companies (banks, telecom providers, airlines) 
    

*   Scalable Design – Built to handle large user bases (20+ million customers) with 10% annual growth capacity. 
    

*   24/7 Availability – Online services available continuously, with telephone services following organization-specific operating hours 
    

*   WCAG 2.1 Compliant – Meets accessibility standards for users with disabilities across all channels 
    

*   Extensible Platform – Designed for future expansion, including chatbot integration and global deployment beyond UK/Europe
