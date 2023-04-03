Simulating a dice roll using 3 approaches.

To run the code a python package is needed and can be installed using pip as follows in the terminal or shell:
pip install qiskit

quantum.py
This file contains the code to simulate the dice in a quantum computer using qiskit to create the circuit and simulate it.
The results are plotted on a histogram

classical.py
This file contains the code to simulate a dice by using the random function in python from the random library.
The results are plotted on a histogram

amalgamation.py
This file contains the code to simulate a dice using both the classical and quantum computers. The quantum computer is simulated using qiskit and return
a value betweem 0-7 and the classical computer evaluates and reruns the quantum circuit if an unwanted value is given.
The results are plotted on a histogram.