class Step:
    def __init__(self, description, status, approver_id, steps=[]):
        self.description = description
        self.status = status
        self.approver_id = approver_id
        self.steps = steps
