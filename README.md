## Installation of Anaconda distribution on Linux OS

* Refer to the following website for instructions on how to install the anaconda distribution on Linux OS: http://docs.anaconda.com/anaconda/install/linux/

## Post-Installation of Anaconda distribution of Linux OS

* To avoid strange errors during installation of new python packages using conda, run the following two commands in a shell

	* `conda upgrade conda`
	* `conda upgrade --all`

## Installing Keras with Tensorflow

* Run the following commands in the terminal:

	* `conda install -y tensorflow`
	* `conda install -y keras`

* Note that -y simply means install without prompts -- This flag is optional

## Installing matplotlib (if needed)

* Some practice examples that you may encounter that uses the standard scientific Python suite (like the one that comes with the Anaconda distribution) might make use of this library to show something.

* Though this module comes pre-installed with Anaconda, either the previous two steps might have corrupted the module or the module was not properly installed by Anaconda (version 5.3.1). In any case, if you try to use matplotlib in your code and it gives you error saying it can't find the module, run the following:

	* `conda install -f matplotlib -y`

* Note that -y simply means install without prompts -- This flag is optional

## Starting Jupyter Notebook on your local machine

* Running the installation script for Anaconda 5.3.1 installs Jupyter Notebook for you by default

* To start this application on your project's root directory, run the following:

	* `cd /path/to/project_root_dir`
	* `jupyter notebook &`

* Note that if you run the last command without the ampersand (&), you will have to open a new terminal to run other commands while the notebook is running
