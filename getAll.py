import git
from git import Repo
import fileinput

def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as f:
        for line in f:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')


this_readme = 'README.md'

Repo.clone_from("https://github.com/tobiasfalk/Boxes-LC.git", "./boxes-lc/")
replace_in_file(this_readme, '[1]: https://github.com/tobiasfalk/Boxes-LC/blob/master/img/70x210x40.png', '[1]: ./boxes/img/70x210x40.png')
replace_in_file(this_readme, '[2]: https://github.com/tobiasfalk/Boxes-LC/blob/master/img/70x70x40.png', '[2]: ./boxes/img/70x70x40.png')
replace_in_file(this_readme, '[3]: https://github.com/tobiasfalk/Boxes-LC/blob/master/README.md', '[3]: ./boxes/README.md')