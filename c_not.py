from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
# from qiskit import execute

from qiskit import IBMQ

# token_string = 'abc123...321cba'
IBMQ.save_account('abc123...321cba')

# Sets a Quantum Register with n qubits
qr = QuantumRegister(3)  # this case - 3 qubits

# Setup a Classical Register with n bits
cr = ClassicalRegister(3) # 3 bits

# In order to have a Quantum Circuit
circuit = QuantumCircuit(qr, cr)

# Quantum gate: CNOT
# Controlled NOT gate from qubit 0 to qubit 1
circuit.cx(qr[0], qr[1])

print('You setup your Controlled NOT gate, now go solve challenging problems!')
