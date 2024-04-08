# Project Name

Parallelized Derivation Algorithm for Anomaly Detection in the Internet of Things Environement

## Table of Contents

- [About](#about)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)

## About

This project provides the implementation of different algorithms such as Context making, Lightwieght Derivation algorithm, and its parallelized variant Parallelized LCDA (PLCDA) for anomaly detection in IoT enviroment. The project contain different experiements including the main Smart Home use case, where there are three sub cases for Intrusion Detection, Anomaly Detection, and Unauthorized Access in Smart Home. 


## Features

The project incorporates the following features:

1. **Semantic Modeling**: Utilize Knowledge Base System (KBS) for semantic modeling to understand user IoT device usages and applications for enhanced security.

2. **Context-Based Knowledge Base**: Provide Implementation of algorithm for Knowledge Base (KB) rewriting into context-based KBs.

4. **Lightweight Contextual Derivation Algorithm (LCDA)**: Implementation LCDA for efficient inconsistency checking in KBS.

5. **Parallel LCDA (PLCDA)**: Improve LCDA by introducing parallelization techniques to accelerate the derivation process for enhanced performance.

6. **Practical Use Case Implementation**: Implement and test the algorithms in a practical use case scenario, such as a smart home environment, to demonstrate effectiveness in cybersecurity applications.

## Usage

To use this project:

- For LCDA, PLCDA Project: run the "main.py" file. 
- For LCDA testing the project, run the jupyter file.

## Installation

To use this project, you need to have Python 3.11.0 installed on your system along with the following libraries:

- time
- itertools
- multiprocessing
- random

You can install Python from the official [Python website](https://www.python.org/downloads/).

Once you have Python installed, you can install the required libraries using pip:

```bash
pip install time itertools multiprocessing random 
