# ERAU CS 399 2024 
### Status ..
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![run-tests](../../actions/workflows/build_deploy.yml/badge.svg)](../../actions/workflows/build_deploy.yml)
![up badge](https://img.shields.io/website-up-down-green-red/http/webapp-kvwgvfria3juk.azurewebsites.net.svg)

## CI/CD
CI is a software development practice in which incremental code changes are made frequently and reliably. 
Automated build-and-test steps triggered by CI ensure that code changes being merged into the repository are reliable. 
The code is then delivered quickly and seamlessly as a part of the CD process.

## Objectives
Learn how continuous integration and deployment (CI/CD) allows professional teams to make dozens of changes while making sure everyone is coordinated and nothing is broken. 

Create a complete CI/CD pipeline and experience how pushing code into a source code repository triggers linting and tests to being performed, and if passed your application being built and deployed as an Azure web application.

## Prerequisites
### git and GitHub
GitHub is an Internet hosting service for software development and version control using git. However, it also provides tools to run tests and perform continuous integration tasks. You can signup here: https://github.com/signup
- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
Windows: winget install Git.Git

### Azure Account
Azure is Microsoft’s public cloud computing platform with solutions including Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS) and can be used to replace or supplement on-premise solutions. You can signup here: https://azure.microsoft.com/en-us/free/students/

### Python and VSCode
To build, test, and run your appliaction locally, you need python 3.11 or greater.
- Python 3.11 (or better): https://www.python.org/downloads/
Windows: winget install -e –id Python.Python.3.11
- VSCode (optional but convenient): https://code.visualstudio.com
The GUI installer apps work just fine, but if you really want to use the cli for this as well ….
Windows: winget install -e –id Microsoft.VisualStudioCode
Mac: brew install –cask visual-studio-code (downloading the installe)

## Step by Step - detailed instructions
1. [Fork and clone a git repository](instructions/1.md)
1. [Run the web application locally](instructions/2.md)
1. [Create an Azure Web application](instructions/3.md)
1. [Inspect the application's log](instructions/4.md)
