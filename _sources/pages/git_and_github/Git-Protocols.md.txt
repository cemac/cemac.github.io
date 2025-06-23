# Good working practices for GitHub

:construction: In Progress :construction: 

## Branches

* **master**: For minor updates and documentation updates or initial dev phase with one worker
* **Dev1**: create sensibly named braches e.g. a feature that's being introduced
* **Dev2**: new branches for new features, can be done simultaneously. 

```bash
git branch testing
git checkout testing
# swap back
git checkout master
# merge
git merge testing -m ":twisted_rightwards_arrows:"
# or 
git push origin testing:master
```

When features are complete can merge back into master.

to delete branches run `git branch -D branchname`

## Releases/ tags

Good practice when taking over work is to tag the original version.

1. Clean: use command line or web interface
  ```bash
  git tag -a v1.0 -m ":bookmark: v1.0 original version"
  git push --tags origin master
  ```
2. Retrospectively: command line only use commit ID
  ```bash 
  git tag -a v1.2 9fceb02 -m "Message here"
  git push --tags origin master
  ```
These tags can be used to allow for DOI to credit the original author only, for example, allow people to clearly see the difference by viewing set snapshots.

## Difference

Difference between remote and 

```bash
git diff branch_1..branch_2
# Remote vs local
git diff remotes/origin/some-branch my-local-branch
# commonly remote vs local
git diff remotes/origin/master master
```

## Troubleshooting

1. Rewrite history:
  Accidentally committed a large file (too large), you have to remove the mistake from the commit history and force push it. 
  ```bash
  git filter-branch --tree-filter 'rm -rf path/to/your/file' HEAD
  git push -f origin master
  ```


## DOI 

1. link your GitHub account with [zenodo](https://zenodo.org/)
2. Make sure you have admin access (to allow webhooks to be created)
3. Navigate to [https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)
4. Switch the flag on desired repository to on
5. Create a Release - these files will appear on the DOI - make sure you are happy with the repo in it exact state
6. Navigate to [https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)
7. Click on the badge for the repo and copy the markdown code into the READEME.md of the repo
8. Wait a few mins and click on the DOI badge on the repo
9. Edit the meta data, authors full names not github IDs, adtional authors, license, title may need modifies. **Save** and then **Publish**
10. Share the DOI with relevant people
11. All future releases will automatically update the DOI. Please check the meta data each time