## Installation of Anaconda distribution on Ubuntu 18.04

* Refer to the following website for instructions on how to install the anaconda distribution on Linux OS: http://docs.anaconda.com/anaconda/install/linux/

## Post-Installation of Anaconda distribution of Ubuntu 18.04

* To avoid strange errors during installation of new python packages using conda, run the following two commands in the terminal:

	* `conda upgrade conda`
	* `conda upgrade --all`

## Installing Keras with Tensorflow

* Run the following commands in the terminal:

	* `conda install -y tensorflow`
	* `conda install -y keras`

* Note that -y simply means install without prompts --> This flag is optional

## Installing matplotlib

* The matplotlib is a module that comes as part of the standard scientific Python suite (like the one that comes with the Anaconda distribution). Some deep learning related code samples which you may encounter might make use of this modul to plot graphs to portray the accuracy metrics measuring the performance of the deep learning neural network model created.

* Though this module comes pre-installed with Anaconda, either the previous two steps might have corrupted the module or the module was not properly installed by Anaconda (the latest version 5.3.1 as of the time of this writing). In any case, if you try to use matplotlib in your code and it gives you error saying it can't find the module, run the following:

	* `conda install -f matplotlib -y`

* Note that -y simply means install without prompts --> This flag is optional

## Starting Jupyter Notebook on your local machine

* Running the installation script for Anaconda 5.3.1 installs Jupyter Notebook for you by default

* To start this application on your project's root directory, run the following:

	* `cd /path/to/project_root_dir`
	* `jupyter notebook &`

* Note that if you run the last command without the ampersand (&), you will have to open a new terminal to run other commands while the notebook is running

* To make this process more convenient, one can choose to write a bash script instead:

	* start.sh
	
	```shell
	#!/bin/bash
	#
	# Name of script: start.sh
	#
	
	cd /path/to/project_root_dir
	jupyter notebook
	```

* Then, run the following to provide permissions to your own user account to execute this script:

	* `chmod u+x start.sh`

* Now, assuming you have created this script in your home directory, you can run it (regardless of your current working directory) as follows:

	* `~/start.sh`
