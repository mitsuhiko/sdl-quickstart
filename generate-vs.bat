@echo off

if not exist vs\nul mkdir vs
cd vs

cmake ..
cd ..
