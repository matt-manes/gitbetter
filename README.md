# gitbetter

Custom git shell. Type less, commit more.

## Installation

Install with:

<pre>
pip install gitbetter
</pre>

## Usage
Launch from a terminal by entering `gitbetter`.<br>
Type `help` or `?` for a list of commands.<br>
Type `help {command}` for detailed help with a specific command.<br>
By default, If you enter a command that isn't built into `gitbetter`, it will be executed directly with `os.system()`,
allowing you to perform any command not defined by `gitbetter` that your shell supports without having to exit.<br>
To toggle this behavior, run the `toggle_unrecognized_command_behavior` 
(`gitbetter` uses `tab` for autocomplete, so you can type `"tog"`+`tab` instead of typing out the whole command name).<br>
When toggled to off, an unrecognized syntax message will be printed if you type in a command `gitbetter` doesn't recognize.<br>
The current state of this setting is printed at the bottom when running the `help` command.<br>
You can still execute a command in the shell regardless of this setting with the `sys` command.
<pre>
C:\gitbetter>gitbetter
Starting gitbetter...
Enter 'help' or '?' for command help.
gitbetter::C:\gitbetter>help

Documented commands (type help <topic>):
========================================
add             ignore         pull_branch
add_url         initcommit     push
amend           list_branches  push_new
cd              loggy          quit
commit          make_private   status
commitall       make_public    switch
commitf         merge          sys
delete_branch   new_branch     tag
delete_gh_repo  new_gh_remote  toggle_unrecognized_command_behavior
git             new_repo       undo
help            pull

Unrecognized command behavior: Execute in shell with os.system()
^Essentially makes this shell function as a super-shell of whatever shell you launched gitbetter from.^

gitbetter::C:\gitbetter>help commitf
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
                        
gitbetter::C:\gitbetter>help loggy
Execute `git --oneline --name-only --abbrev-commit --graph`.

gitbetter::C:\gitbetter>loggy
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

Bindings can be accessed programmatically through the `Git` class.<br>
<pre>
>>> from gitbetter import Git
>>> git = Git()
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
The `stdout` of `Git` functions can be returned as a string rather than being printed to the terminal
by passing `True` to the `Git` constructor or setting the member variable `capture_stdout` to `True`.
<pre>
>>> from gitbetter import Git
>>> git = Git(True)
# or
>>> git.capture_stdout = True
>>> log = git.loggy()
>>> print(log)
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
