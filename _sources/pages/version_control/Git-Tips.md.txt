# Git tips and tricks

## Gotchas from the course:

Course notes:
[https://cemac.github.io/sc-git/](https://cemac.github.io/sc-git/)

* On windows git bash is preferable to use over git CMD as git bash gives you access to useful bash commands
* checkout changes: make sure to stash changes if you're unsure of reverting them
* Undoing a staging `git rm --cached <file>`
* storing credentials if you don't want to use ssh: `git config credential.helper 'cache --timeout=300' `


### Extra Tips

1. **git diff**
You can use verbose time references, quite handy for checking what you've changed since say wednesday 
```bash
 git diff HEAD@{yesterday},
 git diff HEAD@{'2 months ago'}
 git diff HEAD@{'2010-01-01 12:00:00'}
```
2. **pretty terminal git tree**
```bash
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
```
3. **Adding to commits**
Just committed something and noticed a typo and dont want a whole new commit for that typo?
```bash
git add --all; git commit --amend
```
4. **Safer git force push**

```bash
git push --force-with-lease 
```

## Large Files on git hub

If you must have a file larger than 100MB on github then it is possible via git lfs. E.g. a single data file that is not being regularly edited.

1. install [git lfs](https://git-lfs.github.com/)

2. follow these steps
```bash
# initialise git lfs in repo
cd repo
git lfs install
# tell lfs which large files need tracking
git lfs track "*.mat"
# make sure the .gitattributes file is added
git add .gitattributes
git add .
git commit -am 'adding large files'
# push the commit via git lfs
git lfs push --all origin main
# update github
git push -u origin main
```