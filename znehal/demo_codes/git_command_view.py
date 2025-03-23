import flet as ft

class GitView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/git", controls=[self.build_content(page)], scroll=ft.ScrollMode.ADAPTIVE)

    def build_content(self, page: ft.Page):
        def create_card(serial, command, description, example):
            card = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"{serial}. {command}", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_ACCENT_400),
                            ft.Text(description, color=ft.Colors.GREY_700),
                            ft.Container(
                                content=ft.Text(example, font_family="monospace", color=ft.Colors.BLACK),
                                bgcolor=ft.Colors.WHITE70,
                                padding=12,
                                border_radius=8,
                            ),
                        ],
                        tight=True,
                    ),
                    padding=20,
                    width=380,
                ),
                margin=10,
                elevation=4,
            )
            card.animate = ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT)

            def on_hover(e):
                if e.data == "true":
                    card.elevation = 8
                    card.content.scale = 1.03
                    card.content.update()
                else:
                    card.elevation = 4
                    card.content.scale = 1.0
                    card.content.update()

            card.content.scale = 1.0
            # card.mouse_cursors = ft.MouseCursor.POINTER
            card.on_hover = on_hover
            return card

        git_commands = [
            ("git init", "Initializes a new Git repository.", "git init"),
            ("git clone", "Clones a repository into a new directory.", "git clone https://github.com/user/repo.git"),
            ("git add", "Adds file changes to the staging area.", "git add filename.txt\ngit add ."),
            ("git commit", "Records changes to the repository.", 'git commit -m "Add descriptive commit message"'),
            ("git status", "Displays the state of the working directory and staging area.", "git status"),
            ("git branch", "Lists, creates, or deletes branches.", "git branch\ngit branch feature-branch"),
            ("git checkout", "Switches branches or restores working tree files.", "git checkout feature-branch\ngit checkout main"),
            ("git merge", "Joins development histories together.", "git merge feature-branch"),
            ("git pull", "Fetches from and integrates with a remote repository.", "git pull origin main"),
            ("git push", "Updates remote refs along with associated objects.", "git push origin main"),
            ("git log", "Shows commit logs.", "git log"),
            ("git diff", "Shows changes between commits, commit and working tree, etc.", "git diff filename.txt"),
            ("git stash", "Temporarily saves changes that you don't want to commit immediately.", "git stash\ngit stash pop"),
            ("git reset", "Resets the current HEAD to the specified state.", "git reset HEAD filename.txt\ngit reset --hard HEAD"),
            ("git remote -v", "View configured remote repositories.", "git remote -v"),
            ("git tag", "Creates, lists, deletes, or verifies a tag object signed with GPG.", "git tag -a v1.0 -m 'Release v1.0'"),
            ("git show", "Shows various types of objects.", "git show HEAD"),
            ("git rm", "Removes files from the working tree and from the index.", "git rm filename.txt"),
            ("git mv", "Moves or renames a file, a directory, or a symbolic link.", "git mv oldname.txt newname.txt"),
            ("git bisect", "Uses binary search to find the commit that introduced a bug.", "git bisect start\ngit bisect bad\ngit bisect good v1.0"),
            ("git revert", "Reverts some existing commits.", "git revert HEAD"),
            ("git cherry-pick", "Applies the changes introduced by some existing commits.", "git cherry-pick commit_hash"),
            ("git remote add", "Adds a remote repository.", "git remote add origin https://github.com/user/repo.git"),
            ("git remote remove", "Removes a remote repository.", "git remote remove origin"),
            ("git remote rename", "Renames a remote repository.", "git remote rename old_name new_name"),
            ("git fetch", "Downloads objects and refs from another repository.", "git fetch origin"),
            ("git branch -d", "Deletes a branch.", "git branch -d branch_name"),
            ("git branch -m", "Renames a branch.", "git branch -m old_name new_name"),
            ("git checkout -b", "Creates a new branch and switches to it.", "git checkout -b feature_branch"),
            ("git config --global user.name", "Sets the name you want attached to your commit transactions.", 'git config --global user.name "Your Name"'),
            ("git config --global user.email", "Sets the email you want attached to your commit transactions.", 'git config --global user.email "your.email@example.com"'),
            ("git config --global core.editor", "Sets the text editor used by Git.", 'git config --global core.editor "vim"'),
            ("git clean", "Removes untracked files from the working tree.", "git clean -n\ngit clean -f"),
            ("git submodule add", "Adds a submodule to the repository.", "git submodule add https://github.com/user/submodule.git path/to/submodule"),
            ("git submodule update", "Updates submodules to match the version specified in the superproject.", "git submodule update --init --recursive"),
            ("git rebase", "Reapplies commits on top of another base tip.", "git rebase main"),
            ("git describe", "Shows the most recent tag that is reachable from a commit.", "git describe"),
            ("git shortlog", "Summarizes git log output.", "git shortlog"),
            ("git blame", "Shows what revision and author last modified each line of a file.", "git blame filename.txt"),
            ("git fsck", "Verifies the connectivity and validity of the objects in the database.", "git fsck"),
            ("git archive", "Creates an archive of files from a named tree.", "git archive --format=zip HEAD > archive.zip"),
            ("git stash apply", "Applies a stashed change.", "git stash apply"),
            ("git stash drop", "Removes a stashed change.", "git stash drop"),
            ("git remote update", "Fetch updates from all remotes.", "git remote update"),
            ("git branch -r", "Lists remote-tracking branches.", "git branch -r"),
            ("git branch -a", "Lists both remote-tracking and local branches.", "git branch -a"),
            ("git config --list", "Lists all Git configuration variables.", "git config --list"),
            ("git reflog", "Manages reflog information.", "git reflog"),
            ("git rev-parse", "Pick out and massage parameters.", "git rev-parse HEAD"),
            ("git verify-commit", "Checks the GPG signature of commits.", "git verify-commit HEAD"),
            ("git verify-tag", "Checks the GPG signature of tags.", "git verify-tag v1.0"),
            ("git worktree add", "Adds a linked working tree.", "git worktree add ../new_worktree feature_branch"),
            ("git worktree list", "Lists linked working trees.", "git worktree list"),
            ("git worktree remove", "Removes a linked working tree.", "git worktree remove ../new_worktree"),
        ]

        cards = [create_card(i + 1, command, description, example) for i, (command, description, example) in enumerate(git_commands)]

        # self.controls.append(ft.Column(controls=cards))
        # page.update()
        return ft.Column(controls=cards)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Git Commands App"
        page.views.append(GitView(page))
        page.go("/git")
        page.update()

    ft.app(target=main)