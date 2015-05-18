### Mini-workshop notes

#### Participant requirements

All participants should be able to access to the NCI Virtual Desktop environment from their laptop. 
See [here](https://github.com/CWSL/cwsl-mas/wiki/Connecting-to-the-CWSLab) for instructions.


#### Workshop agenda

* Intro: History of the CWSLab 
  * Need to avoid duplication of data *and* code
  * Not much developer time devoted to the project so it needs to be a community effort
* Task 1: Everyone create GitHub account
* Task 2: Everyone fork CWSLab Workflow Tool (instructions [here](https://github.com/CWSL/cwsl-mas/wiki/Installation))
* Task 3: Configure vistrails (instructions [here](https://github.com/CWSL/cwsl-mas/wiki/Configuration))
* Demonstration: Everyone follows along as I construct an example oceanography workflow
  * Point out the workflow design features (modules do single discrete things, etc)
  * Explore the provenance information (code and data) available after you run a workflow
* Task 4: Write your own module (following [these instructions](https://github.com/CWSL/cwsl-mas/wiki/Adding-modules)):
  * Pick from easy examples like implementing `cdo trend` or `cdo mul/add/sub/divc`
  * Submit pull request
* Going forward:
  * How to get help (see [here](https://github.com/CWSL/cwsl-mas/wiki/Getting-help))
  * Roadmap for future development of the workflow tool (see [here](https://github.com/CWSL/cwsl-mas/wiki/Development-roadmap))
