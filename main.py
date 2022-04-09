import PySimpleGUI as sg
from pathlib import Path


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


def main():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Enter the path to the file you want to rename')],
        [sg.InputText(), sg.FolderBrowse(key="-BROWSE-")],
        [sg.Text('Enter the part to remove from the name')],
        [sg.InputText(key="-OLD_PART-")],
        [sg.Text('Enter the new name')],
        [sg.InputText(key="-NEW_PART-")],
        [sg.Button('Rename files'), sg.Button('Exit')]
    ]
    window = sg.Window('Rename', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Rename files':
            path = Path(values["-BROWSE-"])
            old_part = values["-OLD_PART-"]
            new_part = values["-NEW_PART-"]
            print(path)
            print(old_part)
            print(new_part)
            rename_all_files(path, old_part, new_part)
    window.close()


if __name__ == '__main__':
    main()

