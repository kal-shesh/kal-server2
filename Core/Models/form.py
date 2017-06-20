from step import Step


class Form:
    def __init__(self, uuid, data, metadata):
        self.uuid = uuid
        self.data = data
        self.metadata = metadata

    @staticmethod
    def create_from_dictionary(data):
        from form_metadata import FormMetadata
        from step import Step

        steps = []
        for s in data['metadata']['next_steps']:
            steps.append(Step.create_step_from_dictionary(s))

        metadata_dict = data['metadata']
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
        data['data'] = form.data
        data['metadata'] = dict()
        data['metadata']['creation_time'] = form.metadata.creation_time
        data['metadata']['last_update_time'] = form.metadata.last_update_time
        data['metadata']['id'] = form.metadata.id
        data['metadata']['creator_id'] = form.metadata.creator_id
        data['metadata']['displayName'] = form.metadata.displayName
        data['metadata']['next_steps'] = []
        for step in form.metadata.next_steps:
            data['metadata']['next_steps'].append(Step.serialize_to_json(step))
        return data