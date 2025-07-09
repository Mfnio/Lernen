#!/bin/bash
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.dragon(sys.argv[1])