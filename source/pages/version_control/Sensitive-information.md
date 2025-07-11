# CEMAC - Encrypting sensitive information on GitHub

### Overview

- [Description](#Description)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Credentials](#Credentials)
- [Encrypting](#Encrypting)
- [Decrypting](#Decrypting)

## Description:

For many repositories, the code is open source some key information such as a password or API key is not to be made public. It would be useful to store this information securely on git, for jupyterhub_on_azure documentation, I highlight some security flaws that should be addressed in the future - not super critical information but not sensible to highlight to the world. This is a perfect case study for trying out [git-crypt](https://github.com/AGWA/git-crypt). Encrypts using GPG keys - i.e. can generate a CEMAC key shared between all CEMAC staff so we can version control and store the sensitive files on the repository. 

## Requirements:

* git (standard on Leeds Centos)
* openssl (standard on Leeds Centos)
* gpg (standard on Leeds Centos)

## Installation:

(UNIX)

See [documentation](https://github.com/AGWA/git-crypt/blob/master/INSTALL.md) for other platforms.

Very simple install 

```bash
git clone  https://github.com/AGWA/git-crypt.git
make
make install PREFIX=$HOME/SW/bin
```

**$HOME/SW/bin must be in your path to use git-crypt**

<hr>


## Credentials

**If using setting up new keys go to [Encrypting](#Encrypting)**

**Exporting** cemac keys

```
gpg --export-secret-key -a "cemacgeneric" > cemac_private.key
gpg --export -a "cemacgeneric" > cemac_public.key
```

These files can then be securely copied to the target machine and then imported.

**Importing** the public and private keys

```
gpg --import cemac_public.key
gpg --allow-secret-key-import --import cemac_private.key
```

You should see something like

```bash 
gpg: key 5A5E6934: public key "CEMAC (cemacgeneric) <cemac@leeds.ac.uk>" 
imported
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)
gpg: no ultimately trusted keys found


gpg: key 5A5E6934: secret key imported
gpg: key 5A5E6934: "CEMAC (cemacgeneric) <cemac@leeds.ac.uk>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1

```

**check** `gpg --list-secret-keys` shows the cemac key safely in your gpg secring

**delete** the `cemac_private.key` 


_Note: I needed to edit the trust level for the imported key_
```
gpg --edit-key <key_id>
gpg> trust
```

<hr>

## Encrypting:

*(skip to [Credentials](#Credentials) if unlocking an already git-crypted file)*

0. Generating Keys (skip if using the cemac key)
 ```bash
 gpg --gen-key
 ```
 * Select RSA and RSA (default), 4096 bits, doesn't expire, name and email, (o)kay
 * I created a key for myself and a cemac key to share

1. Initialise
 ```bash
 cd repo
 git-crypt init
 ```
2. Create a .gitattributes file. An example is in this repository
```bash
*.key filter=git-crypt diff=git-crypt
```

4. Add users to git crypt
 `git-crypt add-gpg-user USER_ID`
  e.g.
  `git-crypt add-gpg-user cemac@leeds.ac.uk`
5. Add and commit the file. Push to git.
  * see [secret.key](https://github.com/cemac/cemac_generic/blob/master/secret.key)
  * You can not view the file on git hub or download as plain text.
6. Cemac staff obtain the cemac-key from cemachelen
7. Run `git-crypt unlock` to access the file when cloning or pulling.

<hr> 

## Decrypting

Once you have installed the cemac key then you can run:

 `git-crypt unlock` 

after pulling from or cloning the target repo.

<hr> 

## Summary:

This seems like a suitable simple solution to keys and secrets being scattered across individual files spaces.

## Alternative:

1. Encrypt keys with the cemac staffs public key before sharing.
2. Add users individually with git-crypt i.e. we all store each other's public keys and add those users - could be annoying to remember to add everyone. 
3. Simply encrypt with a cemac public key so secret files simply read ---begin pgp message  kakjfshdkfhwrupg --end pgp message.  *Personal thoughts are that, that is less user friendly*.