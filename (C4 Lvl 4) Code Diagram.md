class ComplaintData:
  title, description, category, priority

class ComplaintService:
  def create_complaint(user_id, complaint_data: ComplaintData)
  def get_complaint(user_id, complaint_id)

class Complaint:
  complaint_id, company_id, user_id, description, status, created_date

class ComplaintStatus:
  open, closed, in_progress, resolved

class ComplaintValidator:
  def validate_complaint_data(complaint_data: ComplaintData)
  def validate_user_permissions(user_id, company_id)
