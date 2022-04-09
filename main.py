# This is a sample Python script.

def rename_file(file: Path, part_to_remove: str, part_to_add: str):
    """
    Rename a file with the new name
    :param file: Path to the file
    :param part_to_remove: Part of the filename to remove
    :param part_to_add: Part of the filename to add
    :return:
    """
    new_name = file.name.replace(part_to_remove, part_to_add)
    new_path = file.parent / new_name
    file.rename(new_path)
    return new_path


def rename_all_files(directory: Path, old_part: str, new_part: str):
    """
    Rename all files in a directory
    :param directory: Path to the directory
    :param old_part: Part of the filename to remove
    :param new_part: Part of the filename to add
    :return:
    """
    for file in directory.iterdir():
        rename_file(file, old_part, new_part)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
