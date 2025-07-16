# How to deal with locked down University Linux machines
A web page for dealing with super locked down laptops.

1. [Installing software](#Installing-software)
2. [Minimize buttons](#Minimize-buttons)
3. [Troubleshooting](#Troubleshooting)

## Installing software

### Installing .rpm software without sudo

1. Download .rpm file
2. Create a file structure

````bash
mkdir -p ~/local/pkg
mkdir -p ~/local/src/<software name>
mkdir -p ~/local/bin
````

3. Extract the .rpm

````bash
cp Downloads/<software name>.rpm ~/local/pkg
cd ~/local/src/<software name>
rpm2cpio ~/local/pkg/<filename>.rpm | cpio -id
````

4. Link libraries (if needed)
5. Find binary and link to ~/local/bin

```bash
ln -sf ~local/src/<softwarename>/usr/bin ~/local/bin
````

6. Add `~/local/bin/` to your path by pasting the following into your `.bashrc`

````bash
for dir in "$HOME/local/bin"; do
  if [ -d "$dir" ]; then
    PATH="$dir:$PATH"
  fi
done
````

7. reload (`source .bashrc`) your `.bashrc` and run your application 

8. In order to run this from the applications menu you need to follow the steps below:
   1. Go to settings --> search --> cog in right bottom corner --> Other --> Add the location of your bin folder
   2. Change the name of your sym links to end in `.sh`
   3. Open Files, cling on settings menu (top left)  --> Preferences --> Behaviour --> Executable Text Files --> Run Them*
   4. Now you can run your applications

`*` *Select this option at your own peril, no downloading untrusted random files and opening them!*  
  
### Notes for specific software

* Slack works out the box this way, but certain workspaces need a further work around to log in [see below](Troubleshooting)
* Google chrome requires you to link a bunch of libraires that should be found in `/lib64/` or `/usr/lib64` into `~/local/src/chrome/opt/google/chrome/`

*please add to this any further tips*

# Minimize buttons

RHEL - obtaining a more standard desktop environment

* Search for tweaks in Activities (or gnome-tweaks in terminal)
* Click windows and scroll down to add back in minimise and maximise buttons 
* Extenstions tab allows you to add back in windows list, and additional menus rather than the default activities for navigation 

## Troubleshooting

### TimeErrors

Plug directly into uni network to sync with time servers ( will not work on eduroam or via vpn) 

### Logging in to Slack Work Spaces

1. Open a terminal and leave this code running

````bash
while sleep .1; do ps aux | grep slack | grep -v grep | grep magic; done
````

2. try to log into slack, in app say log in via browser

3. The following should appear in the terminal with the code running:
````bash
kde-open5 slack://WORKSPACE_ID/magic-login/...
/usr/lib/slack/slack --enable-crashpad slack://workspace_id/magic-login/...
````

4. Open that link with slack rather than kde:

````bash
slack --enable-crashpad slack://WORKSPACE_ID/magic-login/...
````

