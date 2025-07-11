# Gitter

A gitter chat has been set up as a test on CEMAC_generic. I've added the Tech Team and anyone can click to join. 

## Why 

1. A possible way to get non-codey users to interact with Repo. E.g. SWIFT I can add a link on the page on the site and so if someone finds an issue with the site they can report it easily without giving 40 people my individual email address or sharing a tool. 

2.  There is functionality to add a webhook to a repo to have continuous integration. I've set this up as an example for this repo. 

## Setup 

1. Set up a community at [https://gitter.im/](https://gitter.im/). 
2. Added a badge to README 
3. added Team as admin
4. Personal choice; I turned off all email notifications
4. Set up continuous integration: Manual config means permissions are limited to this repo only, ignore the token screen and click done, then use the information in CI list to fill in the webhook settings on git hub for chosen repo. I chose to configure this to only notify of wiki pages, releases added etc.