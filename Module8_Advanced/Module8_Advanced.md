- Pip in python


---What is PIP & why it is needed ?

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

pip install --upgrade pip | py -m pip install --upgrade pip



---How to get help ?

pip help | pip help install



---Installing packages with pip:-

1 - pip install [packagename/module]

2 - py -m pip install [packagename/module]

***There are two sources

--Online repo (PyPI and Github)

--Distribution file (From the local storage/file)


***Two main online repo

--Pypi (python package index)

-- Github

pip list: ( To see packages installed ) | pip install/uninstall requests | pip install requests==2.28.1

2 - pip list --outdated --verbose

3 - pip install requests --target .


---Installing packages from github

1 - pip install Github repository URL

ex. pip install git+https://github.com/example-package.git

---Installing packages from dist.

1 - py -m pip install sampleproject-1.0.tar.gz

2 - py -m pip install sampleproject-1.0-py3-none-any.whl


---Install multiple packages using a requirements file

Project:- numpy, pandas, matplotlib, requests (specific versions)

1 - pip install -r requirements.txt | pip freeze

2 - pip install --upgrade requests


Benefits:- 

1 - simplifies the process of managing dependencies

2 - helps maintain consistency in package versions

3 - allows you to easy share and distribute dependencies

---pip show requests | pip check | pip inspect | pip debug | import numpy as np



- What is PYTHONPATH ?

The "Python Path" refers to the list of directories that Python uses to search for modules, packages and other files when executing a script or importing modules.

	- How Python search for imported module/package ?

		* Current Directory
		* PYTHONPATH Environment Variables
		* Standard Library
		* Site-packages

	- How to check python search path ?
			
			* create python file example.py
			* insert this code

		import sys

		print(sys.path)

			* run 

		py example.py

We can add but we should prefer other way (Graphic method).


- Enumeration | Enumerate in python