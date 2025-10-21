# JASMIN Tape Storage

*Coming soon NLDS*

Due to space constraints, tape storage may need to be used on JASMIN

GWS by default have access to tape; for additional users you must email the helpdesk

The easiest way to access the tape storage is via JDMA: [Link to JDMA documentation](https://help.jasmin.ac.uk/docs/short-term-project-storage/jdma/)

## Setting up JDMA

```python
python -m venv ~/venvs/jdma-venv
source ~/venvs/jdma-venv/bin/activate
pip install git+https://github.com/cedadev/jdma_client
jdma init <email> -w <group-workspace-name>
```

## Using JDMA

View the tape storage by showing every get and put command:

`jdma request -f workspace -w <gws-name>`

Each batch ID is a separate folder sent to tape. Ideally, you label the folder that is being sent to tape something useful or tar'ed up folders with descriptive names. 

### To view files in a batch:

```
jdma -t files <batch-id>
```

You'll probably need to pipe a grep command to help find single files, the least messy way would be to have batch ids to be single tarred folders that you put and fetch as one unit.

### To send to tape:

````
jdma -s elastictape -w <group-workspace-name> migrate <foldername>
````

If the folder is not in the top level of the gws make sure to give full path to it.

### To fetch from tape

Create a directory in which to put the folder in **This is very important**, find the batch ID and then give a list of files or easier just the whole top-level folder to stop things from getting messy.

```
 jdma -r jdma_downloads/ get <batch-id> <filelist.txt>
```

If you do not send to a separate folder the file permission can go haywire and lock the whole group out the the gws.

## IMPORTANT TIPS

* Never make a blank get request: this will mess up the permissions of the entire gws for everyone!
* Always create a new folder into which the 'got' items will go. 
* Keep everything in clearly labelled folders and separate by batch id
* Never access the same batch id at the same time as anyone else - only the help desk can fix this.
* For ease of access, break things up or tar stuff e.g. restarts w1, w2, w3 separately so the tape storage is less of a maze to navigate
