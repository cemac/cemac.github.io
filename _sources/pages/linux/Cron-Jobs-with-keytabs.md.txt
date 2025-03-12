# Cronjobs with keytabs

Access to the file systems on the central storage systems requires a
credential which is usually created when you log in to a system with a
password, or can be created by running the `'kinit'` command. The
credential needs to be refreshed regularly.

With cron jobs, an alternative way to provide this credential is by
using a file called a keytab, which is a way of saving your user
credentials in a file.

As this file can be used to access various things using the stored
credential, it's best to try and keep it stored in a place which is only
accessible by the person who owns the credential.

Creating a keytab file which contains the credentials of your own
account is quite straight forward, e.g. as me:

````bash

mkdir ~/.krb5
chmod 700 ~/.krb5
cd ~/.krb5
ktutil
````

````bash

ktutil:  
    addent -password -p <username>@DS.LEEDS.AC.UK -k 1 -e aes256-cts
    Password for <username>@DS.LEEDS.AC.UK:
    ktutil:  wkt <username>.keytab
    ktutil:  q
````


This would create the keytab file within my home directory at:

   `~/.krb5/<username>.keytab`

This file can then be used for authentication to access file systems and
so on. If I change my password the keytab file will no longer be valid,
and can be recreated in the same way.

It is worth checking the keytab file has been created correctly (i.e.
the password was entered correctly when creating the file), e.g.:

   `kinit -k -t <username>.keytab <username>@DS.LEEDS.AC.UK`

should not return an error ('Preauthentication failed while getting
initial credentials').

Once the keytab file has been created, to make sure all of your cron
jobs are able to access the storage, a single extra cron job can be
created on the systems which run the jobs.

For example, if I had a cron job running on see-gw-01, which accessed
the /nfs/earcemac storage, I could add a job:

`   */15 * * * * kinit -k -t ~/.krb5/<username>.keytab <username>@DS.LEEDS.AC.UK >&
/dev/null && \ls /nfs/earcemac >& /dev/null`

Every 15 minutes, this would initialise the credentials for <username>
from the keytab file (`kinit -k -t ~/.krb5/<username>.keytab
<username>@DS.LEEDS.AC.UK`), and then access the earcemac file system (\ls
/nfs/earcemac), to make sure that the authentication between see-gw-01
and the file server is set up for `<username>`.

All being well, other cron jobs should be able to access the files and
SSH key authenticated file transfers should also work.

*Notes Kindly provided by Richard Repeatedly via email so I've added them here*