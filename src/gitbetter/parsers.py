from argshell import ArgShellParser, Namespace
from pathier import Pathier


def new_remote_parser() -> ArgShellParser:
    parser = ArgShellParser()
    parser.add_argument(
        "--public",
        action="store_true",
        help=""" Set the new remote visibility as public. Defaults to private. """,
    )
    return parser


def commit_files_parser() -> ArgShellParser:
    parser = ArgShellParser()
    parser.add_argument(
        "files", type=str, nargs="*", help=""" List of files to stage and commit. """
    )
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        required=True,
        help=""" The commit message to use. """,
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help=""" If a file name is not found in the current working directory,
        search for it in subfolders. This avoids having to type paths to files in subfolders,
        but if you have multiple files in different subfolders with the same name that have changes they
        will all be staged and committed.""",
    )
    return parser


def add_files_parser() -> ArgShellParser:
    parser = ArgShellParser()
    parser.add_argument(
        "files",
        type=str,
        nargs="*",
        default=None,
        help=""" List of files to stage and commit. 
        If not given, all files will be added.""",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help=""" If a file name is not found in the current working directory,
        search for it in subfolders. This avoids having to type paths to files in subfolders,
        but if you have multiple files in different subfolders with the same name that have changes they
        will all be staged and committed.""",
    )
    return parser


def delete_branch_parser() -> ArgShellParser:
    parser = ArgShellParser()
    parser.add_argument(
        "branch", type=str, help=""" The name of the branch to delete. """
    )
    parser.add_argument(
        "-r",
        "--remote",
        action="store_true",
        help=""" Delete the remote and remote-tracking branches along with the local branch.
        By default only the local branch is deleted.""",
    )
    return parser


def recurse_files(filenames: list[str]) -> list[str]:
    files = []
    for filename in filenames:
        if not Pathier(filename).exists():
            results = list(Pathier.cwd().rglob(f"{filename}"))
            if not results:
                print(f"WARNING: Could not find any files with name {filename}")
            else:
                files.extend([str(result) for result in results])
        else:
            files.append(filename)
    return files


def files_postparser(args: Namespace) -> Namespace:
    if args.recursive:
        args.files = recurse_files(args.files)
    return args
