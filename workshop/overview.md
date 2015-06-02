## The CWSLab workflow tool

#### Title slide

* Doing a PhD at UniMelb
* Prior to that worked at CSIRO in Aspendale
  * Part support staff role 
  * Worked on beginnings of CWS Lab workflow tool (wasn't called that back then)
* Jaci offered me a month of paid work to make the tool usable for her team

#### The data duplication panic

* Goes back to impending CMIP5 data arrival (~2010-11). There was concern about
  two types of duplication:
  * Download duplication
  * Processing duplication (e.g. someone has already regridded to a 1 by 1 deg grid)

#### Download duplication

* Addressed by two key components of the CWS Lab:
  * Data services: NCI is a major node of the Earth System Grid Federation, obs etc
  * Computational infrastucture (on top of data storage):
    * Raijin: for complex computational tasks
    * NCI High Performance cloud: scalable platform for data-intensive tasks and workflows
    * CWS Virtual Desktop: 
      * For general data analysis
      * Has IPython notebook, MATLAB, VisTrails, UV-CDAT (better solution for these than X11 forwarding)
      * 4 core, 20 GB RAM, 66GB storage = better than your laptop

* That was kind of the easy part -> no input / change of behaviour required on the part of scientists

#### Processing duplication

* Solution requires a standardised data processing procedure for common tasks:
  * A consistent data reference syntax
  * Open code repository 
    * Full transparency for traceability 
    * Scientists can contribute code themselves for the wide variety of things they do 

* If we can get this right, we can kill a number of birds with one stone:
  * Data processing duplication
  * Code duplication
    * Great resource for new staff / students
  * Reproducibility 
    * Lots of editorials point towards the reproducibility crisis in computational research,
      but nothing is changing
    * My PhD shows:
      * Minimum requirements are software description, public code repo and log files
      * It's not that easy (show a makefile and FigShare page)
    * An automated process would help enormously
  * Code review
    * Professional software developers do this all the time, scientists never do
    * When they do, the benefits are huge: 
      * https://www.mozillascience.org/code-review-for-scientists-findings-strategies
      * https://mozillascience.github.io/codeReview/intro.html
      * http://arxiv.org/pdf/1407.5648v2.pdf

* Addressed by a third key component of the CWS Lab: the workflow tool

#### The workflow tool

* Home: https://github.com/CWSL
  * cwsl-ctools = shared data analysis code
  * cwsl-mas = VisTrails plugin + wiki documentation
  * cwsl-workflows = example workflows
* Examples: 
  * Nino 3.4 step by step
    * Mention provenance information 
  * CMIP3/5 field correlation load existing workflow
* Context: Batch processing, not exploratory data analysis
* Contributing your own modules (https://github.com/CWSL/cwsl-mas/wiki/Adding-modules)
  * Write a script that parses the command line
  * Write a wrapper
  * Submit a pull request (if it would be of use to wider audience) 


* Who built this?
  * Tim Erwin, Tim Bedin (David Kent, Damien Irving)
  * Their time is limited and inconsistent
* Community help approach
  

#### Next step: A community of users

* Will require buy-in and a slight change of behaviour from climate scientists
  * Resist the urge write code in isolation
  * Overcome the embarrassment of having others read their code 
  * Write scripts that parse the command line (not natural for MATLAB, R)
  * Become GitHub literate
  * DaSH SWC workshop over six weeks, starting 26 June, will cover these skills 

* But the benefits are enormous
  * Improved code quality 
  * Stronger case for developer funding
    * [Development roadmap](https://github.com/CWSL/cwsl-mas/wiki/Development-roadmap) outlines the things we could work on 

* Vision
  * User meetings discussing improvements to the tool, code review standards, 
    unit testing
