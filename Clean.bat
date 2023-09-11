@echo off

if exist "./dist" rd /s /q "./dist"
if exist "./build" rd /s /q "./build"
if exist "./src/PyTrivialOpenGL.egg-info" rd /s /q "./src/PyTrivialOpenGL.egg-info"
if exist "./TestResults" rd /s /q "./TestResults"

echo done