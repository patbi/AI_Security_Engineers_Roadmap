- What is PIP & why it is needed ?

Standard distribution: (modules, packages, libraries)

BUT, python has huge community, it is impossible to give all packages with standard distribution.

PIP(Package Installer for Python) Tool:-

Python gives a tool called as 'pip' using which you can Install, manage additional packages and libraries.

PIP is a package manager in python

While working on projects, you will need additional packages. Hence, it is essential tool for pythonists



---How to install PIP ?

PIP has been included with the python installer since version 3.4

Now, PIP is distributed with python unless you use older versions.



---Verify pip is installed or not

pip --version | pip -V | py -m pip --version | pip (usage)



---Python programs

modules & scripts (standalone programs)



---Executing python programs

Modules:- py modulename.py | Scripts:- py -m modulename

1 - create file example.py

2 - insert: print("hello world")

3 - py example.py | py -m example




---How to update pip ?

pip install --upgrade pip
py -m pip install --upgrade pip



---How to get help ?

pip help | pip help install



---Installing packages with pip:-

pip install [packagename/module]

py -m pip install [packagename/module]

***There are two sources

--Online repo (PyPI and Github)

--Distribution file (From the local storage/file)


***Two main online repo

--Pypi (python package index)

-- Github

pip list
- What is Pypi ?
- How to manage third party packages ?
- How pip works ?