#!/usr/bin/env python
import qcc

Nbits=2

# Create Bell state
s=qcc.operator(Nbits).H(0).CNOT(0,1) * qcc.state(Nbits)

# Print state
print("Bell state")
print(s)

# Perform 10 measurements
for n in range(10):
    s0,v0=s.measure(0)
    s1,v1=s0.measure(1)
    
    # And print results of state and classical bits
    print("Measurement # %d: %s | %d%d" % (n,s1,v1,v0))
