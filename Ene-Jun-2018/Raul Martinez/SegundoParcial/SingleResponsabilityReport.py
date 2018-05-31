from abc import ABCMeta, abstractmethod
import json

class IReport(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getTitle(self):
        pass

    @abstractmethod
    def getDate(self):
        pass

    @abstractmethod
    def getContents(self):
        pass

class Report(IReport):


     def getTitle(self):
        return 'Title!'

    def getDate(self):
        return '2018-05-23'

    def getContents(self):
        return {
            'title': self.getTitle(),
            'date': self.getDate()
        }

    def __str__(self):

        return json.dumps(self.getContents())


def main():

    report = Report()
    print(report.getContents())

if __name__ == '__main__':
    main()





