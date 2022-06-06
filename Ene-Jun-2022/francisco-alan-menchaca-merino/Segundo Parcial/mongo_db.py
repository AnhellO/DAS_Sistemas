from github_api import GitHubAPI
import pymongo


class FlaskIssuesMongoDB:
    def __init__(self):
        self.__github_api = GitHubAPI()
        self._issues = self.__github_api.get_all_flask_repo_issues()

    # Creamos la base de datos en mongodb, la cual llamaremos flask_issues,
    # y creamos una colleción de documentos llamada issues
    def create_mongo_db(self):
        client = pymongo.MongoClient(
            host="mongodb",
            port=27017,
            username="root",
            password="mongo"
        )

        database = client["flask_issues"]
        collection_issues = database["issues"]
        collection_issues.insert_many(self._issues)
        
        issues_short = []
        for issue in self._issues:
            issue_short = {}
            
            issue_short["number"] = issue["number"]
            issue_short["title"] = issue["title"]
            issue_short["user"] = issue["user"]["login"]
            issue_short["state"] = issue["state"]
            issue_short["url"] = issue["url"]
            issues_short.append(issue_short)

        collection_issues_short = database["issues_short"]
        collection_issues_short.insert_many(issues_short)


if __name__ == '__main__':
    mongo_db = FlaskIssuesMongoDB()
    mongo_db.create_mongo_db()

# number
# title
# user, login
# state
# https://api.github.com/repos/pallets/flask/issues/4620