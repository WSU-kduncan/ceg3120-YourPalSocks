## Welcome to the Git Guide!
### Created by Ethan Heinlein CEG 3120-01
### NOTE: '...' implies a file or directory name

---

Commands:

**status** -- Shows status of the local repository (repo). This status includes:
		
- number of local commits that have not been synced with remote (Github)
- list of files in local folders than are NOT being tracked by git
- list of files in local folder that have changes that need to be committed
>git status

**clone** -- Duplicates an existing repo onto the machine locally, allowing for changes to be made and pushed

>git clone ...

**add** -- Adds files that Git should track for changes

- Use the '-f' argument to add files that are ignored (see git.ignore)

>git add ...

**rm** -- Removes file from project

- unless using the '--cached' argument, this does remove the file from the machine as well
 >git rm ...

**commit** -- Stage added/stages changes to be added to the repository

- this doesn't automatically push, use the 'push' command for that
- use the '-a' argument to automatically add all tracked changes
- use the '-m' argument to add a message without opening a seperate editor to do so

>git commit

**push** -- Push commits from local repository to the cloud repository (current branch)

>git push

**fetch** -- Download any changes from the cloud repository, but don't apply them to the local repository

>git fetch

**merge** -- Join the fetched changes with the local changes

>git merge

**pull** -- A combination of 'fetch' and 'pull' that downloads and combines changes from the cloud repository with the localrepository

>git pull

**branch** -- Creates/edits a branch from the current local repository

- use the '-l' argument to list the branches of the repository
- use the '-m' argument to move or rename the branch

>git branch ...

**checkout** -- Switches the current branch to another branch

 - use the '-b' argument to create a branch

>git checkout ...

---

Git Files and Folders:

**.git folder** -- The folder where file change information is stored
- also contains repository addresses, logs, and more files that make the magic of git happen
- can also be used to help "roll back" changes in event of error

**.gitignore file** -- A file containing a list of untracked files that git shouldn't warn you about not being added

---

GitHub:

**Pull Requests** -- Branch merge requests set up in Github
- these pull requests can then be approved and merged into the requested branch, or denied
- comments can also be left on requests in a forum-style thread

**SSH Authentication to Repos** -- Passwordless authentication to read/write Github repositories