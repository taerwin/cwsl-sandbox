## Workshop notes

#### Pitch

The CWSLab workflow tool: A solution to the duplication of effort in climate data analysis

Duplication of effort has always been a problem in the weather and climate sciences. 
You've downloaded a copy of some CMIP5 data (for example) onto your computer, 
a colleague has downloaded a copy of the same data onto their computer, and so on. 
What's more, 
you've just spent hours developing code to perform common processing tasks on that data 
(e.g. regridding, locating the depth of a particular isotherm), 
completely unaware that a colleague across the hall already has a script for exactly those tasks. 
Duplication like this is not only incredibly inefficient from a time and code-quality perspective, 
in today's world of multi-petabyte datasets it's also putting a massive strain on data storage infrastructure.

In an attempt to solve this problem, 
the Bureau of Meteorology, CSIRO, ARC Centre of Excellence for Climate System Science, NeCTAR and NCI 
have teamed up to launch the Climate and Weather Science Laboratory (http://cwslab.nci.org.au/). 
They've already gone a long way to solving the data duplication problem 
(you can analyse large datasets like CMIP5 on the NCI machines rather than downloading your own copy), 
however in some respects that's the easy part. 
Unlike the data duplication problem,
which simply involved employing some developers and buying some storage, 
the code duplication problem will require active participation from the whole community of climate scientists.
Those scientists will need to resist the urge write code in isolation, 
overcome the embarrassment of having others read their code 
and learn the vagaries of code sharing facilities like GitHub.

To help the community with this daunting endeavour, 
a team of support scientists from the Bureau, CSIRO and the Centre of Excellence 
have been working on a data analysis workflow tool. 
The tool takes code that the community has contributed 
and plugs it into a workflow management system called VisTrails, 
so that you can mix and match the code to create the workflow you need. 
The system keeps track of provenance information 
like the version of the code that was executed and the order of the processing steps, 
which means each workflow is highly reproducible.

This workshop will teach participants everything they need to know 
in order to contribute code to the workflow tool. 
It will be very hands on, 
so participants will need to bring a laptop that is able to access the CWSLab Virtual Desktop 
(https://github.com/CWSL/cwsl-mas/wiki/Connecting-to-the-CWSLab).
 

#### Participant requirements

All participants should be able to access to the NCI Virtual Desktop environment from their laptop. 
See [here](https://github.com/CWSL/cwsl-mas/wiki/Connecting-to-the-CWSLab) for instructions.


#### Workshop agenda

* Intro: History of the CWSLab 
  * Need to avoid duplication of data *and* code
  * Going forward there probably won't be much developer time devoted to the project, so it needs to be a community code development effort (which isn't necessarily a bad thing)
* Task 1: Everyone create GitHub account
* Task 2: Everyone fork CWSLab Workflow Tool (instructions [here](https://github.com/CWSL/cwsl-mas/wiki/Installation))
* Task 3: Configure vistrails (instructions [here](https://github.com/CWSL/cwsl-mas/wiki/Configuration))
* Demonstration: Everyone follows along on their own laptop as I construct an example oceanography workflow
  * Point out the workflow design features (modules do single discrete things, etc)
  * Explore the [provenance information](https://github.com/CWSL/cwsl-mas/wiki/Metadata) that is available after you run a workflow
* Task 4: I'll guide everyone through the process of writing their own module (following [these instructions](https://github.com/CWSL/cwsl-mas/wiki/Adding-modules)):
  * Participants should pick a simple module like a bash script that implements `cdo trend` or `cdo mul/add/sub/divc`. Along the way they will be introduced to basic GitHub usage and will submit a pull request for their new module which I will review on the spot.
* Concluding remarks:
  * How to get help (see [here](https://github.com/CWSL/cwsl-mas/wiki/Getting-help))
  * Roadmap for future development of the workflow tool (see [here](https://github.com/CWSL/cwsl-mas/wiki/Development-roadmap))
