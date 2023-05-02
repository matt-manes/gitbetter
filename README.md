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
You can still execute a command in the shell regardless of this setting with the `cmd` command.
<pre>
C:\gitbetter>gitbetter
Starting gitbetter...
Enter 'help' or '?' for command help.
gitbetter::C:\gitbetter>help

Documented commands (type help <topic>):
========================================
add        delete_branch   make_private   push
add_url    delete_gh_repo  make_public    push_new
amend      git             merge          quit
cd         help            new_branch     switch
cmd        ignore          new_gh_remote  tag
commit     initcommit      new_repo       toggle_unrecognized_command_behavior
commitall  list_branches   pull           undo
commitf    loggy           pull_branch

Unrecognized command behavior: Execute with os.system()
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