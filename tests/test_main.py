from pathlib import Path
from unittest import TestCase

import main


class Test(TestCase):

    def setUp(self) -> None:
        print("setUp")
        # Create a file
        self.file_path = Path('./test_file_manipulation.txt')
        self.file_path.touch()

        # Write to the file
        self.file_path.write_text('Hello World!')

    def tearDown(self) -> None:
        print("tearDown")
        # Delete the file
        self.file_path.unlink(missing_ok=True)

    def test_rename_file(self):
        print("test_rename_file")
        part_to_remove = 'file'
        part_to_add = 'something'
        self.file_path = main.rename_file(self.file_path, part_to_remove, part_to_add)
        self.assertEqual(self.file_path, Path("./test_something_manipulation.txt"))