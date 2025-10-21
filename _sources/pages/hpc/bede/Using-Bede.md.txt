<div align="center">
<a href="https://www.cemac.leeds.ac.uk/">
  <img src="https://github.com/cemac/cemac_generic/blob/master/Images/cemac.png"></a>
  <br>
</div>

# Using Bede
## What is Bede?

Bede is the N8’s Tier 2 Power and GPU-based high-performance computing (HPC) platform. the main nodes are IBM P9 and each one has 4 GPU cards. there is also a GH200 node.

## Resources available

#### 32x Main GPU nodes, each node (IBM AC922) has:
* 512GB DDR4 RAM
* 2x IBM POWER9 CPUs (and two NUMA nodes), with
* 4x NVIDIA V100 GPUs (2 per CPU)
* Each CPU is connected to its two GPUs via high-bandwidth, low-latency NVLink interconnects (helps if you need to move lots of data to/from GPU memory)
#### 4x Inferencing Nodes:
* Equipped with T4 GPUs for inference tasks.
#### Other
* 2x Visualisation nodes
* 2x Login nodes


## Filestores
The filestore layout is similar to that of the ARC system. In addition to the locations below, there is also a 20GB project folder that persists. 
* `/home` - 4.9TB shared (Lustre) drive for all users.
* `/nobackup` - 2PB shared (Lustre) drive for all users.
* `/tmp` - Temporary local node SSD storage.

## Logging in
`ssh -l <username> bede.dur.ac.uk`

## Saving project name as env variable
Add the following line to your `.bashrc` file. 

`export cemac='<your project name>'`

## Loading an interactive shell
`srun -A $cemac --job-name=”prototyping" --gres=gpu:1 --time=00:20:00 --pty bash`

Options and submission scripts info can be found <a href='https://bede-documentation.readthedocs.io/en/latest/usage/index.html#login'> here </a>



## Installing MiniConda with Power 9 support

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh;
bash Miniconda3-latest-Linux-ppc64le.sh
```


## Creating a Test Conda Environment

```
module load cuda/10.2.89;
module load llvm/11.0.0;
mkdir /nobackup/projects/$cemac/$USER ; 
cd $_;
conda create --prefix ./gpuenv python=3.7 --yes; 
conda activate /nobackup/projects/$cemac/$USER/gpuenv;
conda install ipython;
```


### Add conda channels (optional)
```
conda config --add default_channels https://repo.anaconda.com/pkgs/main
conda config --prepend channels https://public.dhe.ibm.com/ibmdl/export/pub/software/server/ibm-ai/conda/
```


## Installing common libraries with conda
You can check which linux-ppc64lpython packages are available by looking by visiting <a href='https://docs.anaconda.com/anaconda/packages/py3.8_linux-ppc64le/'> here </a>.

### Tensorflow
```
conda install -c conda-forge bazel
conda install tensorflow-gpu
conda install tensorflow-estimator --no-deps
```

### AWS CLI
This also works for non-python packages such as the AWS command-line interface
`conda install -c conda-forge awscli`


### GPFlow
```
conda install -c conda-forge bazel
conda install tensorflow-probability
conda install tensorflow-gpu
conda install tensorflow-estimator --no-deps
pip install gpflow — use-deprecated=legacy-resolver
```

## Useful Links:
* https://gpuhackshef.readthedocs.io/en/latest/bede/index.html
* https://bede-documentation.readthedocs.io/_/downloads/en/latest/pdf/

