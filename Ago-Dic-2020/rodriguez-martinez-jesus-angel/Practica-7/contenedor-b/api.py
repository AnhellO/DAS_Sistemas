import requests

class Api:
    # Constructor
    def __init__(self, **kwargs):
        self.__base_api_path = kwargs.get("base_api_path","https://pipl.ir/v1/")
        self.__headers = kwargs.get("headers", {})
    # Getters
    def get_base_api_path(self) -> str:
        return self.__base_api_path
    def get_headers(self) -> dict:
        return self.__headers
    # Setters
    def set_base_api_path(self, base_api_path : str):
        self.__base_api_path = base_api_path
    def set_headers(self, headers : dict):
        self.__headers = headers
    # Get people information.
    def get_people(self) -> dict:
        data = {'data': []}
        for i in range(0, 5):
            response = requests.get(f"{self.get_base_api_path()}getPerson", headers=self.get_headers()).json()
            data['data'].append(response)
        return data