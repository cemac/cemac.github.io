# Globus Transfers (JASMIN ARC4 example)

*AUTHORS: Richard Rigby and Helen Burns*

Web links:

  * [https://help.jasmin.ac.uk/article/4480-data-transfer-tools-globus-command-line-interface](https://help.jasmin.ac.uk/article/4480-data-transfer-tools-globus-command-line-interface)
  * [https://docs.globus.org/how-to/globus-connect-personal-linux/](https://docs.globus.org/how-to/globus-connect-personal-linux/)

Requires globus-cli:

  * [https://github.com/globus/globus-cli](https://github.com/globus/globus-cli)

and Globus Personal Connect:

  * [https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz](https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz)

* Requirements for Jasmin transfer
 * CEDA account (*NB passwords must be short here*)
 * Jasmin account
 * Request access to xhpcfer service
 * link CEDA account
 * *wait ~ 48 hours if updating access on ceda/jasmin*


**NB Jasmin will require you to give IP address of the machine you will connect with**

## Step by step

On the machine that you wish to transfer from:

## First set up

```
git clone "https://github.com/globus/globus-cli"
python3 -m venv gc
. ./gc/bin/activate
cd globus-cli/
python setup.py install
cd ..
globus login
```
Navigate to the url displayed and login with globus credetials e.g. with your ORCID - you may need to register with globus

Now set up your personal endpoint:
```
wget "https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz"
tar xzf globusconnectpersonal-latest.tgz 
./globusconnectpersonal-3.1.2/globusconnectpersonal -start >& gcp.log &
globus endpoint create --personal <user>_endpoint
```
This will display a long string of numbers and letters for the set-up key and endpoint address. Set these as named variables rather than trying to remember a string:

```
ep2=<string1>
setkey=<string2>
```

Before setting up your end point first create a transfer folder that globus will be able to see and set it up: 

```
mkdir /nobackup/<user>/globustransfer` 
cat ~/.globusonline/lta/config-paths
/nobackup/<user>/globustransfer/,0,1
```

use the set up key displayed earlier or your variable 

```
./globusconnectpersonal-3.1.2/globusconnect -setup $setkey
./globusconnectpersonal-3.1.2/globusconnectpersonal -start
```

Check it's there:
`globus endpoint search --filter-scope my-endpoints`
your endpoint should appear and you should be able to see in that folder with globus

```
touch /nobackup/<user>/globustransfer/test
globus ls b96e2d7e-f01e-11e9-8a5b-0e35e66293c2
```

Now set up the Jasmin endpoint:

```
globus endpoint search "jasmin gridftp server"

```
name the string displayed

```
ep1=<string3>
globus ls $ep1
globus endpoint activate $ep1 --myproxy -U <cedausername>
globus ls $ep1
```

do a test transfer

```
globus transfer $ep2:test $ep1:/dev/shm/gc/data/test
globus task list
./globusconnectpersonal-2.3.9/globusconnectpersonal -stop
```
## After installation

```
. ./gc/bin/activate
globus login
./globusconnectpersonal-3.1.2/globusconnectpersonal -start >& gcp.log &
globus endpoint create --personal helen_endpoint
./globusconnectpersonal-3.1.2/globusconnect -setup <set-up-key>
globus endpoint search --filter-scope my-endpoints
ep1=<my-endpoint>
globus endpoint search "jasmin gridftp server"
ep2=<jasmincd-endpoint>
globus endpoint activate $ep2 --myproxy -U <USERNAME>
```

<hr>

## Gotchas

* To do globus transfers you need access to all the different components. Remember to use your CEDA (rather than Jasmin) credentials (which must be linked with a Jasmin account)
* Globus transfers can time out and take a while to let you know they failed, so check the status here: [https://app.globus.org/activity](https://app.globus.org/activity)
* *file path not allowed* errors: The end point is set up from a specific folder (by default your home directory) you can edit this file
`~/.globusonline/lta/config-paths`
