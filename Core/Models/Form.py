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
        for s in data['form_metadata']['steps']:
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
