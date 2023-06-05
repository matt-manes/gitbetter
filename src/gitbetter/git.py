import shlex
import subprocess
from contextlib import contextmanager
from pathier import Pathier
from pathlib import Path
from urllib.parse import urlparse


class Git:
    def __init__(self, capture_stdout: bool = False):
        """If `capture_stdout` is `True`, all functions will return their generated `stdout` as a string.
        Otherwise, the functions return the call's exit code."""
        self.capture_stdout = capture_stdout

    @contextmanager
    def capture_output(self):
        self.capture_stdout = True
        yield self
        self.capture_stdout = False

    @property
    def capture_stdout(self) -> bool:
        """If `True`, member functions will return the generated `stdout` as a string,
        otherwise they return the command's exit code."""
        return self._capture_stdout

    @capture_stdout.setter
    def capture_stdout(self, should_capture: bool):
        self._capture_stdout = should_capture

    def _run(self, args: list[str]) -> str | int:
        if self._capture_stdout:
            return subprocess.run(args, stdout=subprocess.PIPE, text=True).stdout
        else:
            return subprocess.run(args).returncode

    # |===================================================Core===================================================|
    def execute(self, command: str) -> str | int:
        """Execute git command.

        Equivalent to executing `git {command}` in the shell."""
        args = ["git"] + shlex.split(command)
        return self._run(args)

    def add(self, args: str = "") -> str | int:
        """>>> git add {args}"""
        return self.execute(f"add {args}")

    def am(self, args: str = "") -> str | int:
        """>>> git am {args}"""
        return self.execute(f"am {args}")

    def annotate(self, args: str = "") -> str | int:
        """>>> git annotate {args}"""
        return self.execute(f"annotate {args}")

    def archive(self, args: str = "") -> str | int:
        """>>> git archive {args}"""
        return self.execute(f"archive {args}")

    def bisect(self, args: str = "") -> str | int:
        """>>> git bisect {args}"""
        return self.execute(f"bisect {args}")

    def blame(self, args: str = "") -> str | int:
        """>>> git blame {args}"""
        return self.execute(f"blame {args}")

    def branch(self, args: str = "") -> str | int:
        """>>> git branch {args}"""
        return self.execute(f"branch {args}")

    def bugreport(self, args: str = "") -> str | int:
        """>>> git bugreport {args}"""
        return self.execute(f"bugreport {args}")

    def bundle(self, args: str = "") -> str | int:
        """>>> git bundle {args}"""
        return self.execute(f"bundle {args}")

    def checkout(self, args: str = "") -> str | int:
        """>>> git checkout {args}"""
        return self.execute(f"checkout {args}")

    def cherry_pick(self, args: str = "") -> str | int:
        """>>> git cherry-pick {args}"""
        return self.execute(f"cherry-pick {args}")

    def citool(self, args: str = "") -> str | int:
        """>>> git citool {args}"""
        return self.execute(f"citool {args}")

    def clean(self, args: str = "") -> str | int:
        """>>> git clean {args}"""
        return self.execute(f"clean {args}")

    def clone(self, args: str = "") -> str | int:
        """>>> git clone {args}"""
        return self.execute(f"clone {args}")

    def commit(self, args: str = "") -> str | int:
        """>>> git commit {args}"""
        return self.execute(f"commit {args}")

    def config(self, args: str = "") -> str | int:
        """>>> git config {args}"""
        return self.execute(f"config {args}")

    def count_objects(self, args: str = "") -> str | int:
        """>>> git count-objects {args}"""
        return self.execute(f"count-objects {args}")

    def describe(self, args: str = "") -> str | int:
        """>>> git describe {args}"""
        return self.execute(f"describe {args}")

    def diagnose(self, args: str = "") -> str | int:
        """>>> git diagnose {args}"""
        return self.execute(f"diagnose {args}")

    def diff(self, args: str = "") -> str | int:
        """>>> git diff {args}"""
        return self.execute(f"diff {args}")

    def difftool(self, args: str = "") -> str | int:
        """>>> git difftool {args}"""
        return self.execute(f"difftool {args}")

    def fast_export(self, args: str = "") -> str | int:
        """>>> git fast-export {args}"""
        return self.execute(f"fast-export {args}")

    def fast_import(self, args: str = "") -> str | int:
        """>>> git fast-import {args}"""
        return self.execute(f"fast-import {args}")

    def fetch(self, args: str = "") -> str | int:
        """>>> git fetch {args}"""
        return self.execute(f"fetch {args}")

    def filter_branch(self, args: str = "") -> str | int:
        """>>> git filter-branch {args}"""
        return self.execute(f"filter-branch {args}")

    def format_patch(self, args: str = "") -> str | int:
        """>>> git format-patch {args}"""
        return self.execute(f"format-patch {args}")

    def fsck(self, args: str = "") -> str | int:
        """>>> git fsck {args}"""
        return self.execute(f"fsck {args}")

    def gc(self, args: str = "") -> str | int:
        """>>> git gc {args}"""
        return self.execute(f"gc {args}")

    def gitk(self, args: str = "") -> str | int:
        """>>> git gitk {args}"""
        return self.execute(f"gitk {args}")

    def gitweb(self, args: str = "") -> str | int:
        """>>> git gitweb {args}"""
        return self.execute(f"gitweb {args}")

    def grep(self, args: str = "") -> str | int:
        """>>> git grep {args}"""
        return self.execute(f"grep {args}")

    def gui(self, args: str = "") -> str | int:
        """>>> git gui {args}"""
        return self.execute(f"gui {args}")

    def help(self, args: str = "") -> str | int:
        """>>> git help {args}"""
        return self.execute(f"help {args}")

    def init(self, args: str = "") -> str | int:
        """>>> git init {args}"""
        return self.execute(f"init {args}")

    def instaweb(self, args: str = "") -> str | int:
        """>>> git instaweb {args}"""
        return self.execute(f"instaweb {args}")

    def log(self, args: str = "") -> str | int:
        """>>> git log {args}"""
        return self.execute(f"log {args}")

    def maintenance(self, args: str = "") -> str | int:
        """>>> git maintenance {args}"""
        return self.execute(f"maintenance {args}")

    def merge(self, args: str = "") -> str | int:
        """>>> git merge {args}"""
        return self.execute(f"merge {args}")

    def merge_tree(self, args: str = "") -> str | int:
        """>>> git merge-tree {args}"""
        return self.execute(f"merge-tree {args}")

    def mergetool(self, args: str = "") -> str | int:
        """>>> git mergetool {args}"""
        return self.execute(f"mergetool {args}")

    def mv(self, args: str = "") -> str | int:
        """>>> git mv {args}"""
        return self.execute(f"mv {args}")

    def notes(self, args: str = "") -> str | int:
        """>>> git notes {args}"""
        return self.execute(f"notes {args}")

    def pack_refs(self, args: str = "") -> str | int:
        """>>> git pack-refs {args}"""
        return self.execute(f"pack-refs {args}")

    def prune(self, args: str = "") -> str | int:
        """>>> git prune {args}"""
        return self.execute(f"prune {args}")

    def pull(self, args: str = "") -> str | int:
        """>>> git pull {args}"""
        return self.execute(f"pull {args}")

    def push(self, args: str = "") -> str | int:
        """>>> git push {args}"""
        return self.execute(f"push {args}")

    def range_diff(self, args: str = "") -> str | int:
        """>>> git range-diff {args}"""
        return self.execute(f"range-diff {args}")

    def rebase(self, args: str = "") -> str | int:
        """>>> git rebase {args}"""
        return self.execute(f"rebase {args}")

    def reflog(self, args: str = "") -> str | int:
        """>>> git reflog {args}"""
        return self.execute(f"reflog {args}")

    def remote(self, args: str = "") -> str | int:
        """>>> git remote {args}"""
        return self.execute(f"remote {args}")

    def repack(self, args: str = "") -> str | int:
        """>>> git repack {args}"""
        return self.execute(f"repack {args}")

    def replace(self, args: str = "") -> str | int:
        """>>> git replace {args}"""
        return self.execute(f"replace {args}")

    def request_pull(self, args: str = "") -> str | int:
        """>>> git request-pull {args}"""
        return self.execute(f"request-pull {args}")

    def rerere(self, args: str = "") -> str | int:
        """>>> git rerere {args}"""
        return self.execute(f"rerere {args}")

    def reset(self, args: str = "") -> str | int:
        """>>> git reset {args}"""
        return self.execute(f"reset {args}")

    def restore(self, args: str = "") -> str | int:
        """>>> git restore {args}"""
        return self.execute(f"restore {args}")

    def revert(self, args: str = "") -> str | int:
        """>>> git revert {args}"""
        return self.execute(f"revert {args}")

    def rm(self, args: str = "") -> str | int:
        """>>> git rm {args}"""
        return self.execute(f"rm {args}")

    def scalar(self, args: str = "") -> str | int:
        """>>> git scalar {args}"""
        return self.execute(f"scalar {args}")

    def shortlog(self, args: str = "") -> str | int:
        """>>> git shortlog {args}"""
        return self.execute(f"shortlog {args}")

    def show(self, args: str = "") -> str | int:
        """>>> git show {args}"""
        return self.execute(f"show {args}")

    def show_branch(self, args: str = "") -> str | int:
        """>>> git show-branch {args}"""
        return self.execute(f"show-branch {args}")

    def sparse_checkout(self, args: str = "") -> str | int:
        """>>> git sparse-checkout {args}"""
        return self.execute(f"sparse-checkout {args}")

    def stash(self, args: str = "") -> str | int:
        """>>> git stash {args}"""
        return self.execute(f"stash {args}")

    def status(self, args: str = "") -> str | int:
        """>>> git status {args}"""
        return self.execute(f"status {args}")

    def submodule(self, args: str = "") -> str | int:
        """>>> git submodule {args}"""
        return self.execute(f"submodule {args}")

    def switch(self, args: str = "") -> str | int:
        """>>> git switch {args}"""
        return self.execute(f"switch {args}")

    def tag(self, args: str = "") -> str | int:
        """>>> git tag {args}"""
        return self.execute(f"tag {args}")

    def verify_commit(self, args: str = "") -> str | int:
        """>>> git verify-commit {args}"""
        return self.execute(f"verify-commit {args}")

    def verify_tag(self, args: str = "") -> str | int:
        """>>> git verify-tag {args}"""
        return self.execute(f"verify-tag {args}")

    def version(self, args: str = "") -> str | int:
        """>>> git version {args}"""
        return self.execute(f"version {args}")

    def whatchanged(self, args: str = "") -> str | int:
        """>>> git whatchanged {args}"""
        return self.execute(f"whatchanged {args}")

    def worktree(self, args: str = "") -> str | int:
        """>>> git worktree {args}"""
        return self.execute(f"worktree {args}")

    # |=================================================Convenience=================================================|
    def new_repo(self) -> str | int:
        """Executes `git init -b main`."""
        return self.execute("init -b main")

    def loggy(self) -> str | int:
        """Equivalent to `git log --oneline --name-only --abbrev-commit --graph`."""
        return self.execute("log --oneline --name-only --abbrev-commit --graph")

    def add_all(self) -> str | int:
        """Stage all modified and untracked files."""
        return self.add(".")

    def add_files(self, files: list[str | Pathier | Path]) -> str | int:
        """Stage a list of files."""
        args = " ".join([str(file) for file in files])
        return self.add(args)

    def commit_files(
        self, files: list[str | Pathier | Path], message: str
    ) -> str | int:
        """Stage and commit a list of files with commit message `message`."""
        return self.add_files(files) + self.commit(f'-m "{message}"')  # type: ignore

    def initcommit(self) -> str | int:
        """Equivalent to
        >>> git add .
        >>> git commit -m "Initial commit" """
        return self.add_all() + self.commit('-m "Initial commit"')  # type: ignore

    def amend(self, files: list[str | Pathier | Path] | None = None) -> str | int:
        """Stage and commit changes to the previous commit.

        If `files` is `None`, all files will be staged.

        Equivalent to:
        >>> git add {files}
        >>> git commit --amend --no-edit
        """
        return (self.add(files) if files else self.add_all()) + self.commit("--amend --no-edit")  # type: ignore

    def add_remote_url(self, url: str, name: str = "origin") -> str | int:
        """Add remote url to repo."""
        return self.execute(f"remote add {name} {url}")

    def push_new_branch(self, branch: str) -> str | int:
        """Push a new branch to origin with tracking.

        Equivalent to `git push -u origin {branch}`."""
        return self.push(f"-u origin {branch}")

    @property
    def current_branch(self) -> str:
        """Returns the name of the currently active branch."""
        capturing_output = self.capture_stdout
        current_branch = ""
        with self.capture_output():
            branches = self.branch().splitlines()  # type: ignore
            for branch in branches:
                if branch.startswith("*"):
                    current_branch = branch[2:]
                    break
        self.capture_stdout = capturing_output
        return current_branch

    def list_branches(self) -> str | int:
        """>>> git branch -vva"""
        return self.branch("-vva")

    def switch_branch(self, branch_name: str) -> str | int:
        """Switch to the branch specified by `branch_name`.

        Equivalent to `git checkout {branch_name}`."""
        return self.checkout(branch_name)

    def create_new_branch(self, branch_name: str) -> str | int:
        """Create and switch to a new branch named with `branch_name`.

        Equivalent to `git checkout -b {branch_name} --track`."""
        return self.checkout(f"-b {branch_name} --track")

    def delete_branch(self, branch_name: str, local_only: bool = True) -> str | int:
        """Delete `branch_name` from repo.

        #### :params:

        `local_only`: Only delete the local copy of `branch`, otherwise also delete the remote branch on origin and remote-tracking branch.
        """
        output = self.branch(f"--delete {branch_name}")
        if not local_only:
            return output + self.push(f"origin --delete {branch_name}")  # type:ignore
        return output

    def undo(self) -> str | int:
        """Undo uncommitted changes.

        Equivalent to `git checkout .`."""
        return self.checkout(".")

    def origin_url(self) -> str | int:
        """>>>  git remote get-url origin"""
        return self.remote("get-url origin")

    # ===============================Requires GitHub CLI to be installed and configured===============================

    def create_remote(self, name: str, public: bool = False) -> str | int:
        """Uses GitHub CLI (must be installed and configured) to create a remote GitHub repo.

        #### :params:

        `name`: The name for the repo.

        `public`: Set to `True` to create the repo as public, otherwise it'll be created as private.
        """
        visibility = "--public" if public else "--private"
        return self._run(["gh", "repo", "create", name, visibility])

    def create_remote_from_cwd(self, public: bool = False) -> str | int:
        """Use GitHub CLI (must be installed and configured) to create a remote GitHub repo from
        the current working directory repo and add its url as this repo's remote origin.

        #### :params:

        `public`: Create the GitHub repo as a public repo, default is to create it as private.
        """
        visibility = "public" if public else "private"
        return self._run(
            ["gh", "repo", "create", "--source", ".", f"--{visibility}", "--push"]
        )

    def _owner_reponame(self) -> str:
        """Returns "owner/repo-name", assuming there's one remote origin url and it's for github."""
        with self.capture_output():
            return urlparse(self.origin_url().strip("\n")).path.strip("/")  # type: ignore

    @property
    def owner(self) -> str:
        return self._owner_reponame().split("/")[0]

    @property
    def repo_name(self) -> str:
        return self._owner_reponame().split("/")[1]

    def _change_visibility(self, owner: str, name: str, visibility: str) -> str | int:
        return self._run(
            ["gh", "repo", "edit", f"{owner}/{name}", "--visibility", visibility]
        )

    def make_private(self, owner: str, name: str) -> str | int:
        """Uses GitHub CLI (must be installed and configured) to set the repo's visibility to private.

        #### :params:

        `owner`: The repo owner.

        `name`: The name of the repo to edit."""
        return self._change_visibility(owner, name, "private")

    def make_public(self, owner: str, name: str) -> str | int:
        """Uses GitHub CLI (must be installed and configured) to set the repo's visibility to public.

        #### :params:

        `owner`: The repo owner.

        `name`: The name of the repo to edit."""
        return self._change_visibility(owner, name, "public")

    def delete_remote(self, owner: str, name: str) -> str | int:
        """Uses GitHub CLI (must be isntalled and configured) to delete the remote for this repo.

        #### :params:

        `owner`: The repo owner.

        `name`: The name of the remote repo to delete."""
        return self._run(["gh", "repo", "delete", f"{owner}/{name}", "--yes"])
