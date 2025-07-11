# Containers WorkShop 2021

Various members of the CEMAC team attended the ARCHER 2 containers workshop in July 2021.

Here's a quick start guide from that tutorial

## Set Up

* Installation of docker and sigularity are out lined [here](
https://epcced.github.io/2021-07-28_Containers_Online/setup.html)

## Day 1 - Containers

The course outline is found [here](https://epcced.github.io/2021-07-28_Containers_Online/)

**Why use containers?** - main point is reproducibility with software i.e.
* time goes by and dependencies break
* missing bits of documentation
* systems no longer exist with software stack
* cloud system no longer have access to


### [Docker command line](https://epcced.github.io/2021-07-28_Containers_Online/02-meet-docker/index.html)

To not have to run as sudo look [here](https://docs.docker.com/engine/install/linux-postinstall/)

Once docker is installed

Start the docker engine

```bash
dockerd
```

check commands work

```bash
docker --version
docker container ls
docker container --help
docker container ls --help  
docker build --help
```

### hello world example

```bash
docker container ls
docker pull hello-world
docker container ls
docker run hello-world
```

## [Running a linux container](https://epcced.github.io/2021-07-28_Containers_Online/03-running-containers/index.html)

You don't have to bother with `pull` command `docker run` will do this if the container isn't found locally e.g.

```bash
docker run alpine
```

we can get the container to print its os info or print hello world

```bash
docker run alpine cat /etc/os-release
docker run alpine echo 'Hello World'
```
**note the speed of this compared to a VM**

we can also run this **interactively**

```bash
docker run -it alpine sh
```

you can run various linux commands now and and run `exit` to stop

## [Finding Containers on docker hub](https://epcced.github.io/2021-07-28_Containers_Online/04-docker-hub/index.html)

Owned by docker team:

```bash
# docker pull CONTAINER:TAG
docker pull python:3.8
```

Docker hub community space (check the containers are legit before downloading)

```bash
# docker pull OWNER/CONTAINER:TAG
docker pull rocker/tidyverse:3.6.1
```

### Tidying up

#### Check whats Running

```bash
# running
docker ps
# run recently and get list of recent exited containers
docker container ls --all
```

#### remove exited container

```bash
# single container
docker container rm <container ID>
# tidy all
docker container prune
```

Now we can remove images (if you've not done the steps above you may get an error)

```bash
# get image id
docker image ls
docker image rm <image id>
```

## [Creating your own container](https://epcced.github.io/2021-07-28_Containers_Online/05-creating-container-images/index.html)

* Create [Dockerfile](/Docker_example/Dockerfile)

```bash
docker build -t <username>/docker_example Docker_example/
```

`docker` will build any `Dockerfile` it finds in the directory specified

now you can run:

```bash
docker image ls
docker run <username>/docker_example echo "Hello World"
```

### Pushing to dockerhub

```bash
docker login
docker tag <username>docker_example <username>/docker_test_example:v1
docker push <username>/docker_test_example:v1
```
### Starting points

* keep simple software stack
* use linux flavours like ubuntu or centos

### mounting files

```bash
docker run -v <pathtodirhost>:/temp <username>/docker_example python3 <pathtodircontainer>/sum.py
```

`sum.py` takes input vars and sums them so you can add numbers to the end of the above script to alter the output

### creating a more complex container

This [Dockerfile]() will build the container with the sum function as the default fuction with some default input options

This [Dockerfile]() will build the container with the sum function added to the path but you can also use other functions and commands easily

```bash
docker build -t <username>/complex_docker_example:v1 <pathtodirwithdockerfile>
```

This example `COPY` local files but you can also get files via wget or git

```bash
RUN git clone https://github.com/<username>/<repo>
RUN wget <url>
```

## Archiving and reproducibility

This is mostly explained in the course documentation [here](https://epcced.github.io/2021-07-28_Containers_Online/08-reproducibility/index.html)


<hr>

## [Singularity](https://epcced.github.io/2021-07-29_Singularity_Online/)

Singularity is availble on archer2 and arc4 you might need to `module load` it in


on archer2

```bash
singularity --version
```
shows its working.


No need to start daemone like with docker. I a test dir

### Pull, run and inspect:

```bash
singularity pull hello-world.sif shub://vsoch/hello-world
singularity run hello-world.sif
singularity inspect -r hello-world.sif
```

### tidying up caches

```bash
rm hello-world.sif
singularity pull hello-world.sif shub://vsoch/hello-world
singularity cache list
singularity cache list -v
singularity cache clean
````

## Run vs exc

exec allows us to run the non default command

```bash
singularity exec hello-world.sif /bin/echo Hello World!
singularity exec hello-world.sif /bin/date
```

### interactive shell and files

enter the container with the shell command

```bash
singularity shell hello-world.sif
```

running `whoami` will display your username rather than root and will show the current directory, often bind mounting to home dir - works for  your work directory as well

you won't be able to access the other files on the system e.g. other users directory

you can create files on the host system with in the container

### adding shared directories

```bash
singularity shell -B /work/z19/shared hello-world.sif
```
###


### opening docker images with singularity

you can pull docker images and convert to sif files

```bash
singularity pull python-3.9.6.sif docker://python:3.9.6-slim-buster
```

### Making SIF files

You need route access to create SIF files

There are three different options for accessing a suitable environment to undertake the material in this part of the course:

1. Run Singularity from within a Docker container - this will enable you to have the required privileges to build images
2. Install Singularity locally on a system where you have administrative access
3. Use Singularity on a system where it is already pre-installed and you have administrative (root) access

sigularity Installation on a local machine requires lots of dependencies so this tutorial uses a docker singularity contaier and aliases it as singularity

```bash
alias singularity='docker run --privileged -v ${PWD}:/home/singularity quay.io/singularity/singularity:v3.5.3-slim'
```

*NB might need sudo in the alias on linux*
