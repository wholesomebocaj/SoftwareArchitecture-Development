# C4 Level 4: Code Diagram


![C4 level 4 python django](https://github.com/user-attachments/assets/57d0d0b9-9069-4f94-8a7d-3603e7a1f8c0)

## Classes

### ComplaintData
- `title`
- `description`
- `category`
- `priority`

### ComplaintService
- `create_complaint(user_id, complaint_data)`
- `get_complaint(user_id, complaint_id)`

### Complaint
- `complaint_id`
- `company_id`
- `user_id`
- `description`
- `status`
- `created_date`

### ComplaintStatus
- `open`
- `closed`
- `in_progress`
- `resolved`

### ComplaintValidator
- `validate_complaint_data(complaint_data)`
- `validate_user_permissions(user_id, company_id)`

## Workflow
ComplaintData
→ ComplaintValidator validates it
→ ComplaintService processes it
→ Creates Complaint with ComplaintStatus
