class Step:
    def __init__(self, description, status, approver_id, steps=list()):
        self.description = description
        self.status = status
        self.approver_id = approver_id
        self.steps = steps

    @staticmethod
    def create_step_from_dictionary(data):
        desc = data['description']
        status = data['status']
        approver_id = data['approver_id']
        steps = []

        for s in data['steps']:
            steps.append(Step.create_step_from_dictionary(s))

        step = Step(desc, status, approver_id, steps)
        return step