Toy Calculator
==============

This package is an example of how I would write a calculator using
python classes. I skipped implementing the infix model and wrote a
HP-style reverse polish notation (RPN) model to begin with.


Install
-------

::
   
   $ python3 -m pip install git+https://github.com/JnyJny/calculator
   $ hp28 --help
   ...
   $ ti88 --help


Clone
-----

To develop with this package, I recommend installing `poetry` first.

::
   
   $ python3 -m pip install -U poetry
   $ git clone https://github.com/JnyJny/calculator.git
   $ cd calculator
   $ poetry shell
   $ poetry install
   $ # edit stuff
