#!/bin/bash
echo "-----------------------------------------"
echo "      SYSTEM INFORMATION REPORT"
echo "-----------------------------------------"

echo "Kernel Version:"
uname -r
echo ""

echo "Current User:"
whoami
echo ""

echo "Virtualization Info:"
lscpu | grep 'Virtualization'
echo ""

echo "-----------------------------------------"
