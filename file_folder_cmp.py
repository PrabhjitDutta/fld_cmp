import os
import click
from dirsync import sync
from progressbar import *

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command()
@click.option('--verbose', '-v', is_flag=True)
@click.argument('path1', type=click.Path(exists=True))
@click.argument('path2', type=click.Path(exists=True))
@click.argument('choice', type=click.INT)
def cli(path1, path2, choice, verbose):

    '''This command helps scan 2 folder to search for similar/different files or folders in them and you also have
            the option to sync those directories.


            PATH1 :- Address of one of the folder you want to scan.


            PATH2 :- Address of the folder you want to
            compare it to.


            Choice :- Type 1 if you want to scan for similar files/folder, 2 for different files/folders or 3 to sync the two folders.'''

    count = 0
    temp = 0

    file_list1 = os.listdir(path1)
    file_list2 = os.listdir(path2)
    sync_list1 = []
    sync_list2 = []

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

    elif choice == 2:
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

    else:
        for i in file_list1:
            for j in file_list2:
                if i == j:
                    count += 1
                    file_list2.pop(file_list2.index(j))
            if count == 0:
                sync_list1.append(i)
                temp += 1
        for i in file_list2:
            sync_list2.append(i)
            temp += 1

        for i in file_list1:
            os.system(f'copy "{path1}\\{i}" "{path2}"')
        for i in file_list2:
            os.system(f'copy "{path2}\\{i}" "{path1}"')
