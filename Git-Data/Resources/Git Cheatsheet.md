# Git Cheatsheet

### Git Basics

` git init ` : Initializes git inside the directory, or creates a local git repository

`git add file.txt` : Adds the file(s) to staging. Use [.] instead of file to add all files in the current directory

`git commit -m "commit message"` : Commit the changes that are in staging to the local respository. 

`git remote add origin https://github.com/NetSecQuin/ExampleProject.git`: Link your local repository to a Github repository. 

`git push -u origin [branch-name]` : Push your local commits to Github or Online repository. Primary branch defaults to *Master* or *Main*

`git status` : Show status of changes. Displays what has been added to staging, and what has been commited locally. 

### Branches

`git branch new-branch` : Creates a new branch.

`git switch new-branch` : Switches to a different branch

`git checkout -b new-branch` : Creates a new branch and switches too it

### Revisiting Past Changes

`git log` : See all historical changes/commits to the repository

`git checkout [commit hash]`: Travel back to a historical change/commit.

### Merging

`git merge [branch]` : Merge a branch with the current operating branch.

`git config --global user.name "Your Name"` : Tie an username to be assocaited to the merge request

`git config --global user.email "you@example.com"` : Tie an email address to be assocaited to the merge request
