from Core.Interfaces.DataAdapters.i_server_client_data_exchange_adapter import IServerClientDataExchangeAdapter


class DisplayNameToHRServerClientDataExchangeMatcher(IServerClientDataExchangeAdapter):
    def __init__(self, mapping_list):
        self._mapping_list = mapping_list

    def match_server_to_client(self, key):
        for client_key, server_key in self._mapping_list:
            if server_key == key:
                return client_key

    def match_client_to_server(self, key):
        for client_key, server_key in self._mapping_list:
            if client_key == key:
                return server_key
