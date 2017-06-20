from step import Step


class Form:
    def __init__(self, uuid, form_data, form_metadata):
        self.uuid = uuid
        self.form_data = form_data
        self.form_metadata = form_metadata

    @staticmethod
    def create_from_dictionary(data):
        from form_metadata import FormMetadata
        from step import Step

        steps = []
        for s in data['form_metadata']['next_steps']:
            steps.append(Step.create_step_from_dictionary(s))

        metadata_dict = data['form_metadata']
        metadata = FormMetadata(steps,
                                metadata_dict['creation_time'],
                                metadata_dict['last_update_time'],
                                metadata_dict['id'],
                                metadata_dict['creator_id'],
                                metadata_dict['displayName'])
        form = Form(data['uuid'], data['data'], metadata)
        return form

    @staticmethod
    def serialize_to_json(form):
        data = dict()
        data['uuid'] = form.uuid
        data['form_data'] = form.form_data
        data['form_metadata'] = dict()
        data['form_metadata']['creation_time'] = form.form_metadata.creation_time
        data['form_metadata']['last_update_time'] = form.form_metadata.last_update_time
        data['form_metadata']['id'] = form.form_metadata.id
        data['form_metadata']['creator_id'] = form.form_metadata.creator_id
        data['form_metadata']['displayName'] = form.form_metadata.displayName
        data['form_metadata']['next_steps'] = []
        for step in form.form_metadata.steps:
            data['form_metadata']['next_steps'].append(Step.serialize_to_json(step))
        return data