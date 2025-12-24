# logAnalyzer
We are building a CLI tool called logAnalyzer that read and analyze log files to find failed login attempts. This analyzer can be used in both terminal and as web interface. for the web interface you can just drag and drop your log files and the system will analyze for you. We are making this using python. 


## LogAnalyzer

**LogAnalyzer** is a Python-based security tool designed to detect brute force attacks by parsing Linux SSH logs (`auth.log`). 

It separates the **Core Logic** from the **Interface**, making it capable of running as a **CLI tool** (included) or acting as the engine for a Web Dashboard.

## Features
- ** Automated Parsing:** Instantly reads raw `auth.log` files.
- ** Brute Force Detection:** Aggregates failed login attempts by IP address.
- ** User Tracking:** Identifies exactly which usernames are being targeted (e.g., `root`, `admin`).
- ** Clean Output:** Displays a sorted, readable table of top offenders.
- ** Modular Design:** The logic (`analyzer.py`) is decoupled for easy integration into Flask/Django apps.

## Project Structure

LogAnalyzer folder: 
analyzer.py # The Core Logic (Brain) - Shared Library
cli.py     # The CLI Tool (Interface) - Run this!
test.log   # Sample data for testing

## Project Structure
- Prerequisites
Python 3.x installed

- Usage
1. Clone the repository:
git clone https://github.com/cheetahh1/LogAnalyzer.git
cd LogAnalyzer

2. Run the tool against a log file: 
python cli.py test.log
