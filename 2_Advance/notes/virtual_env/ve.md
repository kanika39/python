what is virtual environment?
→ A virtual environment in Python is an isolated environment that allows a project to have its own dependencies and Python version without interfering with other projects.

so to manage these venv we're going to be using conda which comes part of the anaconda distribution. Conda provides a lot of documentation, we can have a whole user guide. It provide a cheatsheet button in which all the conda commands are present which we need to know in order to manage venv. 

So where do we run these commands they are runned on anaconda cmnd prompt. we will list all the venv using conda env list command, well but vs code provide an easy way to access the terminal inside your coding window

so firstly we will start by making our own venv.we will make a new jupyter notebook test.ipynb, now you can see in upper right hand corner it's using the base environment we want to create a new environment

follow the conda cheatsheet for commands
create environment with Python version ->  conda create --name ENVNAME python=3.12
delete environment ->conda remove --name ENVNAME --all

okay so now we downloaded python version 3.11 cz in python 3.12 datasets was not fully introduced and all so we used 3.11 but if we want to test some new feature of 3.12 we can make a whole new env with .12 version and can test those features seperately from my my project so completely seperate things are maintained by these environments, so we don't have to worry about conflicts

