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
        aprrover = data['aprrover']
        next_steps = []

        for s in data['next_steps']:
            next_steps.append(Step.create_step_from_dictionary(s))

        step = Step(step_name, status, aprrover, next_steps)
        return step