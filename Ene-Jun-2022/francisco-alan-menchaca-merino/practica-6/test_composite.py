from composite import Directory, FileSystem, File
import pytest


class TestComposite():
    @pytest.fixture(autouse=True)
    def root_dirs(self):
        root_dir = Directory("C:\\Users")
        user_dir = Directory("Alan")
        root_dir.add(user_dir)
        return [root_dir, user_dir]

    @pytest.fixture(autouse=True)
    def add_desktop_dir(self, root_dirs):
        root_dir = root_dirs[0]
        user_dir = root_dirs[1]

        desktop_dir = Directory("Desktop")
        user_dir.add(desktop_dir)
        return root_dir.string_rep()

    @pytest.fixture(autouse=True)
    def add_images_dir(self, root_dirs):
        root_dir = root_dirs[0]
        user_dir = root_dirs[1]

        images_dir = Directory("Images")
        user_dir.add(images_dir)
        return root_dir.string_rep()

    def test_add_Directories(
            self,
            add_desktop_dir,
            add_images_dir):
        expected = "\nC:\\Users\\\n\nAlan\\\n"
        desktop_dir_exp = "\nDesktop\\\n"
        images_dir_exp = "\nImages\\\n"

        actual_string = add_desktop_dir
        expected += desktop_dir_exp
        assert actual_string == expected

        actual_string = add_images_dir
        expected += images_dir_exp
        assert actual_string == expected

    @pytest.fixture()
    def add_files_to_desktop(self):
        root_dir = Directory("C:\\Users")
        user_dir = Directory("Alan")
        root_dir.add(user_dir)

        desktop_dir = Directory("Desktop")
        images_dir = Directory("Images")
        user_dir.add(desktop_dir)
        user_dir.add(images_dir)

        desktop_dir.add(File("Google Chrome"))
        desktop_dir.add(File("Microsoft Edge"))
        return root_dir.string_rep()

    def test_add_Files(
            self,
            add_images_dir,
            add_files_to_desktop):
        expected = "\nC:\\Users\\\n\nAlan\\\n"
        desktop_dir_exp = "\nDesktop\\\n"
        images_dir_exp = "\nImages\\\n"

        actual_string = add_images_dir
        actual_string = add_files_to_desktop

        chrome_file_exp = "Google Chrome\n"
        edge_file_exp = "Microsoft Edge\n"

        expected += desktop_dir_exp
        expected += chrome_file_exp + edge_file_exp
        expected += images_dir_exp
        assert actual_string == expected

    def test_remove_items(self):
        root_path = Directory("C:\\Users")
        user_path = Directory("Alan")
        expected = "\nC:\\Users\\\n\nAlan\\\n"
        root_path.add(user_path)

        desktop_dir = Directory("Desktop")
        desktop_dir_exp = "\nDesktop\\\n"
        expected += desktop_dir_exp
        user_path.add(desktop_dir)

        desktop_dir.add(File("Google Chrome"))
        desktop_file_exp = "Google Chrome\n"
        expected += desktop_file_exp

        images_dir = Directory("Images")
        user_path.add(images_dir)

        images_dir.add(File("Dog.png"))

        user_path.remove(images_dir)
        assert root_path.string_rep() == expected

    def test_instances_type(self):
        root_path = Directory("C:\\Users")
        user_path = Directory("Alan")

        assert type(root_path) is Directory
        assert type(user_path) is Directory

        file_chrome = File("Google Chrome")
        file_dog = File("Dog.png")

        assert isinstance(file_chrome, FileSystem)
        assert isinstance(file_dog, FileSystem)
