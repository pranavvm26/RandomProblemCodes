example1 = "dir1\n\tdir11\n\tdir12\n\t\tpicture.jpeg\n\t\tdir121\n\t\t\tfile1.txt\n\t\tdir122\ndir2\n\tfile2.gif"
example2 = "dir1\n\tdir11\n\t\tpictures1.png\n\tdir12\n\t\tpicture.jpeg\n\t\tdir121\n\t\t\tfile1.txt\n\t\tdir122\n\tdir13\ndir2\n\tfile2.gif"
example3 = "dir1\n\tdir11\n\t\tpictures1.png\n\tdir12\n\t\tpicture.jpeg\n\t\tdir121\n\t\t\tfile1.txt\n\t\t\tdir1211\n\t\t\t\tfile2.txt\n\t\tdir122\n\tdir13\ndir2\n\tfile2.gif"
example4 = "dir1\n\tdir11\n\t\tpictures1.png\n\tdir12\n\t\tpicture.jpeg\n\tdir12A\n\t\tdir121\n\t\t\tfile1.txt\n\t\t\tdir1211\n\t\t\t\tfile2.txt\n\t\tdir122\n\tdir13\ndir2\n\tfile2.gif"


def remove_white_space(_string):
    _string = _string.split("\t")
    for strs in _string:
        if strs != "":
            return strs


def build_dir_structure(file_system):
    objects_file_system = file_system.split("\n")
    file_system_structure = []
    open_folders = []
    cnt_old = -1
    for i, folder_name in enumerate(objects_file_system):
        files_string = []
        cnt = folder_name.count('\t')
        if cnt == 0:
            open_folders = []
            cnt_old = -1
        if cnt > cnt_old:
            folder_name = remove_white_space(_string=folder_name)
            files_string.append(folder_name)
            files_string.append("/"+"/".join(open_folders))
            open_folders.append(folder_name)
            cnt_old = cnt
        elif cnt == cnt_old:
            folder_name = remove_white_space(_string=folder_name)
            length = len(open_folders)
            del open_folders[length-1]
            # open_folders[cnt] = folder_name
            files_string.append(folder_name)
            curr_open_folders = open_folders[0:cnt]
            files_string.append("/"+"/".join(curr_open_folders))
            open_folders.append(folder_name)
        elif cnt < cnt_old:
            folder_name = remove_white_space(_string=folder_name)
            length = len(open_folders)
            # diff = length - cnt
            del open_folders[length - cnt]
            open_folders[cnt] = folder_name
            files_string.append(folder_name)
            curr_open_folders = open_folders[0:cnt]
            files_string.append("/" + "/".join(curr_open_folders))
            open_folders.append(folder_name)
        file_system_structure.append(files_string)
    return file_system_structure


if __name__ == "__main__":
    example = example4
    file_system = example
    print(example)
    file_system_parsed = build_dir_structure(file_system)

    for individual_files in file_system_parsed:
        print(individual_files)
