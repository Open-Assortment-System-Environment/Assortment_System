# SPDX-License-Identifier: GPL-3
import git
from git import Repo
import fileinput

def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as f:
        for line in f:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')

#Define the mainpage readme location
this_readme = 'README.md'

#Clones the boxes-lc git repo and replaces the the pathes
Repo.clone_from("https://github.com/tobiasfalk/Boxes-LC.git", "./hardware/boxes-lc/")
boxes_lc_readme = './hardware/boxes-lc/README.md'
#Mainpage README replacement
replace_in_file(this_readme, '[1]: https://github.com/tobiasfalk/Boxes-LC/blob/master/img/70x210x40.png', '[1]: ./boxes-lc/img/70x210x40.png')
replace_in_file(this_readme, '[2]: https://github.com/tobiasfalk/Boxes-LC/blob/master/img/70x70x40.png', '[2]: ./boxes-lc/img/70x70x40.png')
replace_in_file(this_readme, '[3]: https://github.com/tobiasfalk/Boxes-LC/blob/master/README.md', '[3]: ./boxes-lc/README.md')
#Cloned README replacement
replace_in_file(boxes_lc_readme, '[0]: https://github.com/tobiasfalk/Assortment_System_Main_Page/blob/master/README.md', '[0]: ../../README.md')

#Clones the management-software/server/ git repo and replaces the the pathes
Repo.clone_from("https://github.com/tobiasfalk/server.git", "./management-software/server/")

#Clones the management-software/librarys/label-library/ git repo and replaces the the pathes
Repo.clone_from("https://github.com/tobiasfalk/label-library.git", "./management-software/librarys/label-library/")
