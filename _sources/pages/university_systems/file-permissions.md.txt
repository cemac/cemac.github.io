## Making files readable to your colleagues

### Centos 6
These filesystems are mounted via nfs v3 and the standard `setfacl -R -m other:rX <foldername>` will work

### Centos 7
Most Environment systems are Centos 7 and the file systems are nfs 4 so they use nfs4 acls (which get translated back to posix acls on file servers which don't support 'rich acls'

For these systems you need to use `nfs4_setfacl`

### GUI nfs4_setfacl editor

As the syntax is hard to remember Richard has this handy editor to make life easier

```
~earrr/bin/nfs4-acl-editor.el7
```

### Trouble with git cloning on NFS

The nfs4 ACLS usually cause the git problems.It's most usually the first acl that needs to be removed from the parent directory, e.g.:mkdir 

```bash
mkdir git_repository
cd git_repository
nfs4_setfacl -x 1 .
git init
```

```bash
setfacl -x 1 .
git clone  ....
```

should do the trick

<hr>

*the new central storage systems do in fact support rich acls*