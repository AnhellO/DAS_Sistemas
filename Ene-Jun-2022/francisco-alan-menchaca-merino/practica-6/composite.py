from abc import ABC, abstractmethod


class FileSystem(ABC):
    """The base Component class declares common operations
    for both simple and complex objects of a composition"""

    @abstractmethod
    def string_rep(self, file):
        pass


class File(FileSystem):
    """The leaf class represents the end objects of a composition.
    A leaf can't have any children.
    Usually, it's children the Leaf objects that do the actual work,
    whereas Composite objects only delegate to their sub-components."""

    def __init__(self, file_name):
        self.file_name = file_name

    def string_rep(self):
        return self.file_name + "\n"


# Component class
class Directory:
    """The Composite class represents the complex components that
    may have children. Usually, the Composite objects delegate the
    actual work to their children and then "sum-up" the result."""

    def __init__(self, dir_name):
        self.__dir_name = dir_name + "\\\n"
        self.__childrens = []

    def add(self, item):
        self.__childrens.append(item)

    def remove(self, item):
        self.__childrens.remove(item)

    def string_rep(self):
        complete_root = "\n" + self.__dir_name

        for item in self.__childrens:
            complete_root += item.string_rep()

        return complete_root


if __name__ == '__main__':
    root_path = Directory("C:\\Users")
    user_path = Directory("Alan")
    root_path.add(user_path)

    documents_dir = Directory("Documents")
    desktop_dir = Directory("Desktop")
    images_dir = Directory("Images")

    user_path.add(documents_dir)
    user_path.add(desktop_dir)
    user_path.add(images_dir)

    documents_dir.add(File("factory_method.py"))
    documents_dir.add(File("r_programming.R"))
    desktop_dir.add(File("Google Chrome"))
    desktop_dir.add(File("Microsoft Edge"))
    images_dir.add(File("Dog.png"))
    images_dir.add(File("Cat.png"))

    user_path.remove(images_dir)
    print(root_path.string_rep())
