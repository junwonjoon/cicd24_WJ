# ERAU CS 399 2024 
### Status ..
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![run-tests](../../actions/workflows/build_deploy.yml/badge.svg)](../../actions/workflows/build_deploy.yml)
![up badge](https://img.shields.io/website-up-down-green-red/http/webapp-kvwgvfria3juk.azurewebsites.net.svg)

# Link to Hosted Web App (URL Table to CSV Converter)
https://webapp-kvwgvfria3juk.azurewebsites.net/

## The Purpose of the code
This is source code to my streamlit project that is currently hosted in the website listed above.

## Acknowledgements
Professor Wolf Paulus for providing the initial setup of Azure.


## Prerequisite
git and GitHub
GitHub is an Internet hosting service for software development and version control using git. However, it also provides tools to run tests and perform continuous integration tasks. You can signup here: https://github.com/signup

Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git Windows: winget install Git.Git
Azure Account
Azure is Microsoft’s public cloud computing platform with solutions including Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS) and can be used to replace or supplement on-premise solutions. You can signup here: https://azure.microsoft.com/en-us/free/students/

Python and VSCode
To build, test, and run your appliaction locally, you need python 3.11 or greater.

Python 3.11 (or better): https://www.python.org/downloads/ Windows: winget install -e –id Python.Python.3.11
VSCode (optional but convenient): https://code.visualstudio.com The GUI installer apps work just fine, but if you really want to use the cli for this as well …. Windows: winget install -e –id Microsoft.VisualStudioCode Mac: brew install –cask visual-studio-code (downloading the installe)

Install the required dependencies:
   ```bash
   pip install -r requirements.txt
