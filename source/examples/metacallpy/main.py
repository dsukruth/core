#!/usr/bin/python3.4

from metacall import metacall_initialize, metacall_load, metacall, metacall_destroy

# Initialize metacall
metacall_initialize();

# Example call
metacall("hello");

# Destroy metacall
metacall_destroy();
