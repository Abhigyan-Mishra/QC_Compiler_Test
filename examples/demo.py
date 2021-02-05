#!/usr/bin/env python
import qcc

Nbits=1

# Create Bell state
s=qcc.operator(Nbits).X(0)* qcc.state(Nbits)

# Print state
print("Qubit state")
print(s)

# Perform 10 measurements
for n in range(10):
    s0,v0=s.measure(0)
    
    # And print results of state and classical bits
    print("Measurement # %d:| %d" % (n,v0))
