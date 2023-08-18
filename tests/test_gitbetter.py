import os

import pytest
from pathier import Pathier

from gitbetter import Git

root = Pathier(__file__).parent


def test_basics():
    proj = root / "proj"
    proj.delete()
    proj.mkdir()
    proj.mkcwd()
    git = Git()
    git.new_repo()
    (proj / "file.py").write_text("file = 'test'")
    git.initcommit([proj / "file.py"])
    assert git.current_branch == "main"
    git.create_new_branch("new-test")
    assert git.current_branch == "new-test"
    (proj / "file.py").write_text("file = 'test2'")
    git.commit_files([proj / "file.py"], "refactor: change string value")
    (proj / "file2.py").write_text("import gitbetter")
    git.initcommit([proj / "file2.py"])
    (proj / "stuff.txt").write_text("stuff")
    git.ignore(["stuff.txt"])
    git.commit_all("chore: add to gitignore")
    git.ignore(["*.txt"])
    git.amend()
    git.switch_branch("main")
    git.merge("new-test")
    with git.capturing_output():
        assert len(git.list_branches().stdout.splitlines()) == 2
    git.delete_branch("new-test")
    with git.capturing_output():
        assert len(git.list_branches().stdout.splitlines()) == 1
    git.loggy()
    git.status()
