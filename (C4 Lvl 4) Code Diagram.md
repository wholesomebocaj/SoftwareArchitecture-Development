# C4 Level 4: Code Diagram


![C4 level 4 python django](https://github.com/user-attachments/assets/57d0d0b9-9069-4f94-8a7d-3603e7a1f8c0)
Code-Level Components 

Complaint Service 

Responsibility: Coordinate complaint-related operations within the Proof\-of-Concept 

*   Creates and retrieves complaint records 
    

*   Acts as the central entry point for complaint workflows 
    

*   Coordinates validation and persistence of complaint data 
    

Complaint Validator 

Responsibility: Enforce validation and permission rules 

*   Validates incoming complaint data 
    

*   The system ensures that users have the necessary permissions to create or access complaints within their specific tenant. 
    

Complaint Data 

Responsibility: Represent complaint input data 

*   Keeps information about complaints sent by users (title, description, category, importance) 
    

*   Moved between the approval and service parts 
    

Complaint 

Responsibility: Represent the complaint domain entity 

*   Stores complaint details and tenant ownership 
    

*   Maintains the current status of the complaint 
    

*   Persisted in the database through the service layer. 
    

Complaint Status 

Responsibility: Define valid complaint lifecycle states 

*   Open 
    

*   In Progress 
    

*   Resolved 
    

*   Closed 
    

These status values are used consistently across the service and domain model to enforce valid state transitions.
