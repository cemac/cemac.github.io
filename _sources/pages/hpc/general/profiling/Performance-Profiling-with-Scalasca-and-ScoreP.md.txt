# Score-P Workflow

Module and job submission details are for *archer2*.

## Load required modules

Scalasca and/or Score-P is incompatible with the Cray performance profiling tools, so these modules first need to be unloaded.
`module spider scalasca` can be used to find the most up-to-date version of Scalasca.

To load:
```
module unload perftools perftools-base  # or module unload perftools-lite perftools-base
module load other-software/1.0 scalasca/2.6.1-cray
```

## Add `scorep` to make file

The compiler alias (e.g. `ftn` for Cray Fortran on *archer2*) is prefixed with `scorep --user`, e.g. in a Makefile for Fortran:
```
PREP		= scorep --user
COMPILER        = $(PREP) ftn

# ...

$(COMPILER) $(COMPFLAGS) $(PROGDIR)main.F90
```

The executable is then built using `make` as per usual.

At this point, it is useful to designate the directory containing the executable and any required input files and submission script as Score-P-specific, and duplicate it for subsequent experiments, to avoid software outputs.

## Add `scorep` measurements to submission script

Measurements are set via environment variables. Generally best to start with summary measurements (default, when no environment variables are set).
Available measurements via: `scorep-info config-vars --full`

Good practice to specify an experiment directory for `scorep` output, e.g. `export SCOREP_EXPERIMENT_DIRECTORY=scorep_sum`.

## Submit job

`sbatch <submission_script.sh>`

## View Summary Report

To create and view a summary analysis report, use the CUBE4 GUI:
`cube scorep_sum/profile.cubex`

Alternatively, to get a hierarchy of metrics, use `scalasca examine`, which can be accessed using the alias `square`. In this case, use the experiment *directory* rather than the cubex file as the argument:
`square scorep_sum`

## Filtering for Tracing Experiments

Filtering out e.g. frequently visited but quickly executed regions helps minimise the measurement overhead. Score-P gives information to aide in setting up filtering, and also in allocating memory for the experiment.

### Summary analysis result scoring

`scorep-score <experiment_directory>/profile.cubex`

This summarises buffer sizes required for various components, alongside their stats: number of visits, total time, time/visit...
In this report "com" is for "combined".

Can break down this analysis by function, using the `-r` option.

Pay particular attention to the recommended setting for `SCOREP_TOTAL_MEMORY`.

### Filter Configuration

Filtering options are set in a text file, and can specify routines to include and exclude, e.g.
``` scorep.filt
SCOREP_REGION_NAMES_BEGIN
EXCLUDE
    *_init*
    *set*
SCOREP_REGION_NAMES_END
```

To report on only specific routines:
```
SCOREP_REGION_NAMES_BEGIN
	EXCLUDE
		*
	INCLUDE
		target1*
		target2*
SCOREP_REGION_NAMES_END
```

Using wildcards in this way accounts for compilers' adding an underscore, for example.

The effect of this filter set can be previewed using `scorep score -f scorep.filt <experiment_directory>/profile.cubex`, where `scorep.filt` is the file containing the filter specs. It predicts the resources required for the tracing experiment.

## Apply filter to new summary experiment

*Skip this step if not using filtering for trace experiment.*

Running a new summary experiment allows parameters to be checked before carrying out the tracing, and gives an indication of measurement overheads.

Set up or modify the job submission script, to include environment variables that define the trace experiment. Using the estimate from `scorep score`, it is best to set the memory allocation for the experiment, e.g.
`export SCOREP_TOTAL_MEMORY=375M`

Measurements include any available PAPI events, e.g.
`export SCOREP_METRIC_PAPI=PAPI_L2_DCM,PAPI_L2_DCH,L2_PREFETCH_HIT_L2,L2_PREFETCH_HIT_L3`
or "perf" metrics provided by Linux, e.g.
`export SCOREP_METRIC_PERF=L1-dcache-load-misses,L1-dcache-loads`

*Off-core counters like `cray_zenl3:::UNC_L3_CACHE_MISS[:ALL]` have a huge overhead, it seems; in Leeds Spherical Dynamo testing, they slowed execution about 80x.*

Apply the filter, e.g.
`export SCOREP_FILTERING_FILE=../config/scorep.filt`

Analyse the results as previously.

## Trace Experiment

Set up memory allocation and hardware performance counters as above, and add the following to the submission script:
`export SCOREP_ENABLE_TRACING=true`

## Instrumentation via Score-P API

To target a specific region in the code:
```fortran
#include "scorep/SCOREP_User.inc"

subroutine foo
	! declaration
	SCOREP_USER_REGION_DEFINE( my_region_handle )
	
	SCOREP_USER_REGION_BEGIN( my_region_handle, "foo", SCOREP_USER_REGION_TYPE_COMMON )

	! region of interest
	
	SCOREP_USER_REGION_END( my_region_handle )
end subroutine foo
```

## Scalasca Automated Trace Analysis

### Preview Trace Analysis

Scalasca's `scan -n` command can be used to verify correct setup of the experiment and suggest some configuration.

`scan -n -v <executable>` verifies required `scorep` instrumentation is present. `-v` = verbose.

Can use in conjunction with `srun` command and its options (`scan` and its options come first), along with environment variables.
Also checks that the experiment requested doesn't already exist.

### Scalasca summary profile measurement

Set up job submission script with:
```bash
# Scalasca now needs to be loaded as part of job submission script, as scan is called as prefix to srun.
module -q load other-software/1.0
module load scalasca/2.6.1-cray

# Scalasca/Score-P measurement configuration
#export SCOREP_EXPERIMENT_DIRECTORY=scorep_pretrace_sum  # Scalasca can set automatically if not specified
export SCOREP_FILTERING_FILE=../config/scorep.filt  # Best to filter, to avoid excessive overhead
export SCOREP_METRIC_PAPI=PAPI_TOT_INS,PAPI_TOT_CYC,PAPI_FP_OPS  # If required
#export SCOREP_TOTAL_MEMORY=100M  # Not needed for summary
#export SCOREP_ENABLE_TRACING=true  # False or commented out for summary
export SCAN_ANALYZE_OPTS="--time-correct --verbose"

# Launch application
scan  srun  <path to executable>
```

The `--time-correct` option accounts for any differences in clocks between compute nodes being used for the job. It is advised to use it routinely to ensure timestamps are synchronised - a necessary part of Scalasca's analyses.

`scorep.log` records output to `stdout` & `stderr`.

### Summary results

Examine results using `square`: in the `general` tab at the right of the screen, can bring up `advisor`, to look at efficiencies.

Use either `scorep score` or `square -s` to check the configuration needed for the trace experiment.

### Trace measurement

Edit/create job script to enable tracing & adjust memory requirement. Skip hardware performance counters unless absolutely necessary, as they can add a large overhead.

```bash
#export SCOREP_EXPERIMENT_DIRECTORY=scorep_trace
export SCOREP_FILTERING_FILE=../config/scorep.filt
#export SCOREP_METRIC_PAPI=PAPI_TOT_INS,PAPI_TOT_CYC,PAPI_FP_OPS
export SCOREP_TOTAL_MEMORY=100M
export SCOREP_ENABLE_TRACING=true
export SCAN_ANALYZE_OPTS="--time-correct --verbose"
```

Submit job.

The Slurm output file will now show the Scalasca analysis (`scout`) at the end.

`traces` subdirectory contains traces as two files for each thread.

Now also get a `scout.cubex` file.

### Trace results
Use `square <experiment directory>` to examine breakdown of results.
