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

    def test_rename_all_files(self):
        print("test_rename_all_files")
        # Create a directory
        self.dir_path = Path('./test_dir_manipulation')
        self.dir_path.mkdir()
        # Create multiple files
        for i in range(3):
            self.dir_path.joinpath(f'file_{i}.txt').touch()
        # Rename all files
        main.rename_all_files(self.dir_path, 'file', 'something')
        # Check if all files are renamed
        for i in range(3):
            self.assertEqual(self.dir_path.joinpath(f'something_{i}.txt'), Path(f'./test_dir_manipulation/something_{i}.txt'))
        # Remove files
        for i in range(3):
            self.dir_path.joinpath(f'something_{i}.txt').unlink()
        # Remove directory
        self.dir_path.rmdir()
