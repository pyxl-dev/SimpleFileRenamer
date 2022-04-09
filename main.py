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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
