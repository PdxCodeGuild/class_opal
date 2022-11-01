# Git steps in order

## make new branch

`git checkout main`

`git pull`

`git checkout -b my-branch-name`

## make changes to your files

make whatever changes you want to commit 

it's okay if you do this before you make your branch

## stage changes using git add

`git add .` adds all files in the current directory

`git add -A` adds all tracked and untracked files

`git add {path}` adds files at the specified path (it could be a path to a directory or just a single file)

## commit changes

files have to be added by this point or your commit will be empty

`git commit -m "commit message goes here"`

## push commits

you don't have to do this every time you commit, but you do have to push it before it exists on github (so, before you can make a pull request)

the first time you push to a brand new branch: `git push -u origin <first-name-code>`

after that:
`git push`
