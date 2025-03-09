# Useful UNIX tools

## Permissions related ##

1. To enable readability of files for all
```bash
setfacl -m other:r-x */*
chmod og+rx */*
```

make your home directory readable

```bash
nfs4_setfacl -a A::<USER>@ds.leeds.ac.uk:RX $HOME
```

## Background tasks after log out ##

1. Screen
   * ```bash
      ssh -Y $USER@<host>
      screen -S <task-related-name>
      < Start whatever process >
      ```
   * Detach the screen with: **cntrl + a+ d**
   * Exit and return later
   ```bash
   exit
   < some time later... >
   ssh -Y $USER@<host>
   screen -r <task-related-name>
   <horrah its done>
   exit  
   ```
   * `screen ls` and `screen kill` are useful commands for multiple screens

