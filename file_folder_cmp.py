import os
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command()
@click.argument('path1', type=click.Path(exists=True))
@click.argument('path2', type=click.Path(exists=True))
@click.argument('choice', type=click.INT)
def cli(path1, path2, choice, s):

    '''This Command helps Scan 2 folder to search for similar/different files or folders in Them.
        The syntax of this command is fld_cmp [PATH1] [PATH2] 1/2 where PATH1 represents the address
        of one of the folder you want to scan and PATH2 is the address of the folder you want to
        compare it to and finally you have to type 1 if you want to scan for similar files/folder
        or 2 for different files/folders.'''

    count = 0
    temp = 0

    file_list1 = os.listdir(path1)
    file_list2 = os.listdir(path2)
    result_list = []

    print("\n")

    if choice == 1:
        for i in file_list1:
            for j in file_list2:
                if i == j:
                    result_list.append(i)
                    print(i)
                    file_list2.pop(file_list2.index(j))
                    count += 1
        print("\n{} Similar files/folder Found".format(count))

    else:
        for i in file_list1:
            for j in file_list2:
                if i == j:
                    count += 1
                    file_list2.pop(file_list2.index(j))
            if count == 0:
                print(i)
                temp += 1
        for i in file_list2:
            print(i)
            temp += 1
        print("\n{} Different files/folders Found".format(temp))
