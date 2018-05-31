import json
from abc import ABCMeta, abstractmethod

class Report(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getTitle(self, title):
        pass

    @abstractmethod
    def getDate(self, date):
        pass


class Contents(Report):

    def __init__(self, title, date):
        self.title = None
        self.date = None

    def getTitle(self, title):
        self.title = title

    def getDate(self, date):
        self.date = date

    def getContents(self):
        return {
        'title': self.getTitle(),
        'date': self.getDate()
        }

class format(Contents):
    def formatJson(self):
    	return json.dumps(self.Contents())

def main():
    report = Contents()
    print(Contents.getContents())


if __name__ == '__main__':
    main()
