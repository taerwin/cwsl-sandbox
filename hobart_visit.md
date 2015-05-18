### Mini-workshop notes

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
  * Explore the provenance information (code and data) that is available after you run a workflow
* Task 4: I'll guide everyone through the process of writing their own module (following [these instructions](https://github.com/CWSL/cwsl-mas/wiki/Adding-modules)):
  * Participants should pick a simple module like a bash script that implements `cdo trend` or `cdo mul/add/sub/divc`. Along the way they will be introduced to basic GitHub usage and will submit a pull request for their new module which I will review on the spot.
* Concluding remarks:
  * How to get help (see [here](https://github.com/CWSL/cwsl-mas/wiki/Getting-help))
  * Roadmap for future development of the workflow tool (see [here](https://github.com/CWSL/cwsl-mas/wiki/Development-roadmap))
