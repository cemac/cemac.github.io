# Creating forks on GitHub

_The following notes assume that you have git running locally and that you have set up authentication for working remotely with GitHub._

GitHub forks allow you to create a working copy of a git repository on GitHub which you can adapt and modify before submitting your changes back to the original repository as a pull request. 

## Creating a fork

From the repository view, click on "Fork" at the top of the page to open the "Create a new fork" page. 

<p><img src="https://user-images.githubusercontent.com/10053102/182353209-e6b04919-6494-4364-ba33-01049abad66e.png" width=600></p>

By default the fork will be created in your personal account with the same name as the original repository. The owner and name of the fork can be adjusted if required. 

You can choose whether to copy the main branch only – this is fine unless you need to work with a different branch in the repository e.g. to collaborate on a feature which has not yet been merged into the main branch or on work which takes place in a specific development branch. 

Click on "Create fork". You'll be directed to the main page of your fork of the repository. You'll see "forked from <repo>" at the top of the page which indicates that this repository is a fork. 

## Working with forks

Having created a fork, you can clone a copy of the repository from your fork. Click on "Code" to bring up the URL for cloning the repository. 

<p>
<img src="https://user-images.githubusercontent.com/10053102/182353401-60c3afc9-5cd7-4256-8cd5-3cf3ab2faa18.png" width=600>
</p>

At a command line prompt/terminal window, change directory to a suitable location and clone the repository:

```
cd path/to/project
git clone git@github.com:ghuser/project_repo.git
```

This creates a local copy of the repository which is linked to your fork: 
```
$ cd project_repo 
$ git remote –v 
origin git@github.com:ghuser/project_repo.git (fetch) 
origin git@github.com:ghuser/project_repo.git (push) 
```

You should also add the original repository as an upstream remote. This will allow you to keep your fork up-to-date with the original repository (updating can also now be done via the GitHub user interface).

```
git remote add upstream git@github.com:orig/project_repo.git
```

If you have already cloned the original repository and started working with your local copy, you can modify the remote URLs so that your fork is the origin and the original repository is upstream:

```
git remote set-url origin git@github.com:ghuser/project_repo.git
git remote add upstream git@github.com:orig/project_repo.git
```

## Creating a feature branch
It's good practice to make your changes in a separate [branch](https://www.atlassian.com/git/tutorials/using-branches) of the repository:

```
git checkout -b my-feature-branch       <- create feature branch 
```

If your changes are to be made on top of an existing branch in the repository you can specify the branch on which to create your feature branch:
```
git checkout -b my-feature-branch dev   <- create feature branch based on dev branch
```

Now you are ready to commit your changes and push to your fork:
```
<commit changes on feature branch> 
git push origin my-feature-branch 
```
## Making a pull request 

After pushing commits to your fork you will be prompted to create a pull request on GitHub. Doing so will send a request to the owner of the original repository to merge your changes into the repository. 

Note that your pull request should merge the feature branch back into the upstream branch on which your feature branch was based. The default branch selected when you create a pull request is the main branch so make sure that you change this if your work is based on a different branch.

## Fetch upstream 

If changes are made in the upstream repository you will need to bring your fork of the repository up-to-date. To update your main branch from the upstream repository:

```
git fetch upstream 
git checkout main 
git merge upstream/main 
```

Alternatively, you can update your fork via GitHub by clicking on "Fetch upstream" then "Update branch". If you take this approach, you'll need to follow it up by pulling the changes into your local copy: 

```
git fetch origin 
git checkout main 
git merge origin/main 
```

## Working with branches 

Making your changes in a separate branch makes it easier to keep your repository up-to-date with upstream changes. Working on a feature branch allows you to use rebase to replay your local changes on top of the upstream changes: 

```
git checkout -b my-feature-branch         <- create feature branch 
<commit changes on feature branch> 
git fetch upstream 
git rebase upstream/main                  <- replay changes in feature branch on top of upstream/main
```

When you have finished working with a branch (i.e. when you have completed a pull request to merge your branch with the upstream repository) you can delete the local copy:

```
git checkout main
git branch -d my-feature-branch
```