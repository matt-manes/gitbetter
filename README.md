# gitbetter

Custom git shell to type less and commit more.

## Installation

Install with:

<pre>
pip install gitbetter
</pre>

## Usage
Launch from a terminal by entering `gitbetter`.<br>
Type `help` or `?` for a list of commands.<br>
Type `help {command}` for detailed help with a specific command.<br>
<pre>
>gitbetter
Starting gitbetter...
Enter 'help' or '?' for command help.
gitbetter>help

Documented commands (type help <topic>):
========================================
add      commitall       help           make_public    pull_branch  undo
add_url  commitf         ignore         merge          push
amend    cwd             initcommit     new_branch     push_new
cd       delete_branch   list_branches  new_gh_remote  quit
cmd      delete_gh_repo  loggy          new_repo       switch
commit   git             make_private   pull           tag

gitbetter>help commitf
Stage and commit a list of files.
Parser help for commitf:
usage: gitbetter [-h] -m MESSAGE [-r] [files ...]

positional arguments:
  files                 List of files to stage and commit.

options:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        The commit message to use.
  -r, --recursive       If a file name is not found in the current working directory, search for it in subfolders. This avoids having to type paths to files in subfolders,
                        but if you have multiple files in different subfolders with the same name that have changes they will all be staged and committed.
gitbetter>help loggy
Execute `git --oneline --name-only --abbrev-commit --graph`.
gitbetter>loggy
*   3e780ec (HEAD -> main, tag: v1.0.0) Merge branch 'my-feature'
|\
| * b4478a3 feat: new print statement
| | test.py
* | eb89c2e docs: update readme
|/
|   README.md
* fc6b7ac (origin/main) docs: update readme
| README.md
* 2a75c0c docs: added a comment
| test.py
* d22129a feat: new print statement
| gitbetter_test.py
* 1a002d7 chore: add items to ignore
| .gitignore
* 92cb7e7 Initial commit
  .gitignore
  LICENSE.txt
  README.md
  gitbetter_test.py
  test.py
  test.txt
</pre>

Bindings can be accessed programmatically:
<pre>
>>> from gitbetter import git
>>> git.loggy()
*   3e780ec (HEAD -> main, tag: v1.0.0) Merge branch 'my-feature'
|\
| * b4478a3 feat: new print statement
| | test.py
* | eb89c2e docs: update readme
|/
|   README.md
* fc6b7ac (origin/main) docs: update readme
| README.md
* 2a75c0c docs: added a comment
| test.py
* d22129a feat: new print statement
| gitbetter_test.py
* 1a002d7 chore: add items to ignore
| .gitignore
* 92cb7e7 Initial commit
  .gitignore
  LICENSE.txt
  README.md
  gitbetter_test.py
  test.py
  test.txt
>>> git.list_branches()
* main                3e780ec [origin/main: ahead 3] Merge branch 'my-feature'
  remotes/origin/main fc6b7ac docs: update readme
</pre>

### Future Features
* Redirect the output of git commands so the bindings return the output instead of only being able to print.
* Make pushing to remote after creating it smoother (make it so you don't manually have to add the url).