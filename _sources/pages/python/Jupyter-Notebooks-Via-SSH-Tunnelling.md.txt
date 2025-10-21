# Jupyter Notebooks via tunnelling

## Requirements

* [Anaconda](https://docs.anaconda.com/anaconda/install/) or all relevant packages installed
* SSH connection
* [Screen](https://linuxize.com/post/how-to-use-linux-screen/) *installed by default on university systems* 

## Instructions

*if anaconda not set up on remote machine see information at the bottom of this page*

1. ssh to machine you want to run notebooks on (needs to have access to data etc) e.g. `ssh foe-linux.leeds.ac.uk`
2. Once Jupyter is installed via anaconda or other choice generate password
   ```
   jupyter notebook --generate-config
   jupyter notebook password   
   ```
3. Edit the following lines in the config file like this exampele (may require different port number)
```
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_password_change = False
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 5566
```
4. start a screen session ideally naming the session something sensible
`screen -S JupyterScreen`
5. go to desired directory and run `jupyter-notebook`
6. Take Note of port number e.g. 5566
```
[I 11:48:41.622 NotebookApp] The Jupyter Notebook is running at:
[I 11:48:41.622 NotebookApp] http://foe-linux-03.leeds.ac.uk:5566/
```
7. [detach screen](https://linuxize.com/post/how-to-use-linux-screen/): `ctr+ a`+`ctrl +d`
8. On your home computer (linux or mac) edit or create file `~/.shh/config` to contain the lines (as referenced in our [remote access page](Remote-Access))
```
Host remote-access
     User <leeds-user-name>
     ForwardAgent yes
     ForwardX11 yes
     Hostname remote-access.leeds.ac.uk
     IdentityFile ~/.ssh/id_rsa_work
     ServerAliveInterval 240

Host foe-03
     User <leeds-user-name>
     ForwardAgent yes
     ForwardX11 yes
     Hostname foe-linux-03
     IdentityFile ~/.ssh/id_rsa_work
     ServerAliveInterval 240
     Proxycommand ssh -qremote-access -W %h:%p
```
*You need config for a gateway machine: e.g. remote access or see-gw-01 and the machine you are running the notebook on*
9. generate key and copy keys to access to leeds systems as outlined in our [remote access](Remote-Access) page
   * `ssh-keygen -t rsa` *name something like `id_rsa_work` to match identity file in the config file you just created*
   * `ssh-copy-id earhbu@see-gw-01`
10. Now tunnel in
  * generic    `ssh -N -f -L localhost:<localportno>:localhost:<remoteportno> user@host`
  * following this example:
     `ssh -N -f -L localhost:5000:localhost:5566 user@foe-03`
11. Access from your local browser `http://localhost:5000/` enter your password

<hr>

## Installing anaconda

The following commands will install on a Linux machine via the terminal. After this you can `conda install -c conda-forge notebook` and 

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
chmod 755 Miniconda3-py39_4.9.2-Linux-x86_64.sh
bash Miniconda3-py39_4.9.2-Linux-x86_64.sh
```

## Saving notebooks for sharing 

Some tips for large notebooks

1. Clear output before pushing to git.
2. save as markdown `jupyter nbconvert --to markdown <file>.ipynb`
3. save as pdf `jupyter nbconvert --to pdf <file>.ipynb`
   * **NB** notebooks containing large amounts of markdown  mayrequire debugging to convert to pdf via converting latex first and running through an application that gives detailed logs like texmaker 


```bash

```
