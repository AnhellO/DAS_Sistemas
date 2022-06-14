import itertools
import requests
import json


class GitHubAPI:
    def __init__(self):
        self.__load_api_auth_data()

    # Cargamos los datos necesarios (el token generado y el usuario) para,
    # realizar peticiones a la api de github.
    def __load_api_auth_data(self):
        with open('./api_auth_data.json') as json_file:
            api_auth = json.load(json_file)

        self.__user = api_auth["user"]
        self.__token = api_auth["token"]
        self.__auth = (self.__user, self.__token)

    # Obtenemos 100 issues (100 issues es lo máximo que la api de github permite
    # obtener del repositorio de Flask en issues) de acuerdo a la página actual.
    def _get_flask_repo_issues(self, page):
        flask_issues_url = "https://api.github.com/repos/pallets/flask/issues"
        params = {
            "owner": "pallets",  # The account owner of the repository.
            "repo": "flask",     # The account owner of the repository.
            "state": "all",      # Indicates the state of the issues to return.
            "per_page": 100,     # The number of results per page (max 100).
            "page": page         # Page number of the results to fetch.
            # flask issues have 46/47 pages, 4506 issues
        }

        flask_issues = requests.get(
            url=flask_issues_url,
            auth=self.__auth,
            params=params
        ).json()

        return flask_issues

    # Utilizando la función anterirormente definida obtenemos todas las issues
    # existentes (abiertas/cerradas) del resporio de Flask.
    def get_all_flask_repo_issues(self):
        issues_batches = []
        page = 1

        while True:
            issues_batch = self._get_flask_repo_issues(page)
            is_batch_empty = issues_batch

            if not is_batch_empty:
                break

            issues_batches.append(issues_batch)
            page += 1

        issues = list(itertools.chain.from_iterable(issues_batches))
        return issues
