## Welcome to the Git Guide!
### Created by Ethan Heinlein CEG 3120-01
### NOTE: '...' implies a file or directory name

---

Commands:

**status** -- Shows status of the local repository. This status includes:
		
	- number of local commits that have not been synced with remote (Github)
	- list of files in local folders than are NOT being tracked by git
	- list of files in local folder that have changes that need to be committed
	- git status

**clone** -- Duplicates an existing repo onto the machine locally, allowing for changes to be made and pushed

	- git clone ...

**add** -- Adds files that Git should track for changes

	- git add ...

**rm** -- Removes file from project

	- unless using the '--cached' argument, this does remove the file from the machine as well
	- git rm ...

**commit** -- Stage added/stages changes to be added to the repository

	- this doesn't automatically push, use the 'push' command for that
	- use the '-a' argument to automatically add all tracked changes
	- use the '-m' argument to add a message without opening a seperate editor to do so
	- git commit

**push** -- Push commits from local repository to the cloud repository (current branch)

	- git push

**fetch** -- Download any changes from the cloud repository, but don't apply them to the local repository

	- git fetch

**merge** -- Join the fetched changes with the local changes

	- git merge

**pull** -- A combination of 'fetch' and 'pull' that downloads and combines changes from the cloud repository with the localrepository

	- git pull

**branch** -- Creates/edits a branch from the current local repository

	- use the '-l' argument to list the branches of the repository
	- use the '-m' argument to move or rename the branch
	- git branch ...

**checkout** -- Switches the current branch to another branch

	- git checkout ...

---

git Files and Folders:

**.git folder** -- The folder where file change information is stored