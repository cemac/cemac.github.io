<div align="center">
<a href="https://www.cemac.leeds.ac.uk/">
  <img src="https://github.com/cemac/cemac_generic/blob/master/Images/cemac.png"></a>
  <br>
</div>

# Github Access tokens - 2FA

With the introduction of two factor authentication, we are now required to change the way we access our repositories. There are now two main methods to upload to Github: using ssh keys or access tokens. This page describes the latter.

## Generating a Token
1. Click on your `user icon` (right)
2. Select `Settings`
3. From the left-hand menu, select `Developer Settings`
4. `Personal Access Tokens`
5. Right Top `Generate New Token`

Copy and **SAVE** the token, **you will not get to view it again without generating a new one!**

## Storing the token
### Caching for a TEMPORARY period in time
If we wish to store our token for a fixed period in time we may cache it with a predefined timeout.

`git config --global credential.helper 'cache --timeout=31540000'`

Here the timeout corresponds to that of a year, and you should not need to re-enter it during that time.


### Storing the token in plaintext
It is also possible to save it within your home directory as a plaintext file, serving much the same purpose.

`git config credential.helper store`



## Finally, we need to enter the token itself.

We can do this by running a git pull command, entering our username and using the token when prompted for a password.
```
Username for 'https://github.com': <user>
Password for 'https://<user>@github.com': <your token>
```