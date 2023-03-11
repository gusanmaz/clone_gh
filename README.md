# Github Cloner (clone_gh)

`clone_gh` is a command-line tool that allows you to clone all of your Github repositories, or repositories belonging to any user, into a local directory. You can optionally filter repositories by programming language and specify an output directory for the cloned repositories.

## Installation

To install `clone_gh`, you can use pip:

`pip install clone_gh`

## Usage

### Clone Starred Repositories

To clone all of your starred Github repositories, simply run:

`clone_gh <username> -t clone-likes`

Replace `<username>` with your Github username. This will clone all of your starred repositories into the current working directory.

You can also specify a programming language to filter by:

`clone_gh <username> -t clone-likes -l python`

This will clone only your starred repositories that are written in Python.

You can specify an output directory for the cloned repositories:

`clone_gh <username> -t clone-likes -o /path/to/output/directory`

This will clone all of your starred repositories into the specified output directory.

### Clone User Repositories

To clone all of the repositories for a specific Github user, run:

`clone_gh <username> -t clone-user -u <target_username>`

Replace `<target_username>` with the Github username of the user whose repositories you want to clone. This will clone all of the repositories for the specified user into the current working directory.

You can also specify a programming language to filter by:

`clone_gh <username> -t clone-user -u <target_username> -l python`

This will clone only the repositories for the specified user that are written in Python.

You can specify an output directory for the cloned repositories:

`clone_gh <username> -t clone-user -u <target_username> -o /path/to/output/directory`

This will clone all of the repositories for the specified user into the specified output directory.

---

If you have a Github access token that you want to use for the API requests, you can provide the file path to the access token file:

`clone_gh <username> -t <task> -a /path/to/access/token/file`

Replace `<task>` with either `clone-likes` or `clone-user` depending on which action you want to perform.

## License

`clone_gh` is licensed under the MIT License. See `LICENSE` for more information.

## Credits

`clone_gh` was created by Güvenç USANMAZ.