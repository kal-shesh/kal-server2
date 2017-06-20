class Step:
    def __init__(self, step_name, status, approver, next_steps=list()):
        self.step_name = step_name
        self.status = status
        self.approver = approver
        self.next_steps = next_steps

    @staticmethod
    def create_step_from_dictionary(data):
        step_name = data['step_name']
        status = data['status']
        approver = data['approver']
        next_steps = []

        for s in data['next_steps']:
            next_steps.append(Step.create_step_from_dictionary(s))

        step = Step(step_name, status, approver, next_steps)
        return step

    @staticmethod
    def serialize_to_json(step):
        data = dict()
        data['step_name'] = step.step_name
        data['status'] = step.status
        data['approver'] = step.approver
        data['next_steps'] = []
        for s in step.next_steps:
            data['next_steps'].append(Step.serialize_to_json(s))
        return data
