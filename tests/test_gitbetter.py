from datetime import datetime

import pytest
from pathier import Pathier

from gitbetter import Git

root = Pathier(__file__).parent

""" All tests should be run sequentially in the order written. """


# Everything should use `dummyrepo` b/c it ensures it's the cwd before running tests
@pytest.fixture(scope="module")
def dummyrepo(tmp_path_factory) -> Pathier:
    dummyrepo = Pathier(tmp_path_factory.mktemp("dummyrepo"))
    dummyrepo.mkcwd()
    return dummyrepo


@pytest.fixture(scope="module")
def git() -> Git:
    return Git()


def test__new_repo(dummyrepo: Pathier, git: Git):
    assert git.new_repo().return_code[0] == 0


def test__init_commit(dummyrepo: Pathier, git: Git):
    (dummyrepo / "file.py").write_text("file = 'test'")
    assert git.initcommit(["file.py"]).return_code[0] == 0


def test__current_branch(dummyrepo: Pathier, git: Git):
    assert git.current_branch == "main"


def test__create_new_branch(dummyrepo: Pathier, git: Git):
    assert git.create_new_branch("new-branch").return_code[0] == 0
    assert git.current_branch == "new-branch"


def test__commit_files(dummyrepo: Pathier, git: Git):
    (dummyrepo / "file.py").write_text("file = 'test2'")
    assert (
        git.commit_files(["file.py"], "refactor: change string value").return_code[0]
        == 0
    )


def test__commit_all(dummyrepo: Pathier, git: Git):
    (dummyrepo / "file2.py").write_text("import time")
    assert git.commit_all("Init commit").return_code[0] == 0


def test__undo(dummyrepo: Pathier, git: Git):
    file = dummyrepo / "file2.py"
    original_text = file.read_text()
    file.write_text("import datetime")
    assert file.read_text() == "import datetime"
    assert git.undo().return_code[0] == 0
    assert file.read_text() == original_text


def test__switch_branch(dummyrepo: Pathier, git: Git):
    assert git.switch_branch("main").return_code[0] == 0
    assert git.current_branch == "main"
    git.switch_branch("new-branch")


def test__merge_to(dummyrepo: Pathier, git: Git):
    output = git.merge_to()
    assert all(return_code == 0 for return_code in output.return_code)


def test__delete_branch(dummyrepo: Pathier, git: Git):
    with git.capturing_output():
        assert len(git.list_branches().stdout.splitlines()) == 2
    assert git.delete_branch("new-branch").return_code[0] == 0
    with git.capturing_output():
        assert len(git.list_branches().stdout.splitlines()) == 1


def test__rename(dummyrepo: Pathier, git: Git):
    git.rename_file("file2.py", "file9000.py")
    assert "file9000.py" in [path.name for path in dummyrepo.glob("*.py")]
    assert "file2.py" not in [path.name for path in dummyrepo.glob("*.py")]
    git.commit('-m "file test"')


def test__untrack(dummyrepo: Pathier, git: Git):
    assert all(
        code == 0 for code in git.untrack(*list(dummyrepo.rglob("*.py"))).return_code
    )


def test__dob(dummyrepo: Pathier, git: Git):
    assert datetime.now().strftime("%Y-%m-%d") == git.dob.strftime("%Y-%m-%d")
