# Introduction to Git

## Version control 

Version control allows you to check any changes in code, who did it, and when they did it.
To manually do version control you can copy all the files into a folder named version 1 and then make changed and then copy the changed files in to another folder
named version 2. This is okay for small changes but on large projects you want a version control system.

### Old version control 

!["old version control"](C:\Users\elena\PycharmProjects\tech241\python_variables\images\old_version_control.png)

Originally, versions were tracked in the database which stored the versions. This takes up more space as it duplicates the entire project for every version.

### New version control 

!["new version control"](C:\Users\elena\PycharmProjects\tech241\python_variables\images\new_version_control.png)

Git only saves the changes between two versions not the whole project every time.
Each version is like a snapshot in time. So a git repository is like a stream of snapshots.

### Terminal terms

- cd (change directory)
- cd .. (go back 1 folder)
- ls (lists folders and files)

### Git terms 

!["Git example img"](C:\Users\elena\PycharmProjects\tech241\python_variables\images\three_git_stages.png)

- git innit (creates a git repo)
- git add (adds a file to the stageing area)
- git commit -m "" (commits what is in the stageing area with a message)
- git status (show the status of the staging area)
- git log (shows all the local commits)
- git diff (shows the differences between what the current commit is and what there is right now)
- git diff <id> <id> (shows the differences between two commits)
- git reset --hard <id> (can go back to previous commit)