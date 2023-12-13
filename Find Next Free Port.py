# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:49:43 2023

@author: Filippe
"""
import socket

def find_next_free_port(portI):
    porta = portI
    while True:
        try:
            # Try binding to the port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', porta))
            # If successful, the port is available
            return porta
        except OSError:
            # Port is not available, try the next one
            porta += 1

# Usage
portS = 81  # Start searching from this port
portF = find_next_free_port(portS)
print("Next free port after", portS," is ", portF)
