class IServerClientDataExchangeAdapter(object):
    def match_server_to_client(self, key):
        raise NotImplementedError()

    def match_client_to_server(self, key):
        raise NotImplementedError()

