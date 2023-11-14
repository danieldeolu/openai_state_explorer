# openai_state_explorer
A Python script that utilizes the OpenAI API to retrieve an array of states/provinces for a given country. The script dynamically creates Excel files, organizing state information for each queried country. Explore and export state-level data effortlessly with OpenAI State Explorer! 



# OpenAI State Explorer

## Overview

OpenAI State Explorer is a Python script designed to interact with the OpenAI API to retrieve information about states or provinces for various countries. The script dynamically generates Excel files, organizing state-level data for each country code in the country_code_list array.

## Features

- **Country Information:** Retrieve a list of states/provinces for a specified country.
- **Excel Export:** Automatically create Excel files for each country, containing detailed state information.

## Getting Started

### Prerequisites

Before running the script, make sure you have:

- Python installed (version X.X.X)
- OpenAI API key

### Installation

1. Clone this repository:


git clone https://github.com/your-username/openai-state-explorer.git
cd openai-state-explorer

Install dependencies:
>>> pip install openai
>>> pip install xlsxwriter
>>> pip install json

2. Set your OpenAI API key:
Replace "YOUR_API_KEY" in the script with your actual OpenAI API key.

Usage
Run the script by executing:
>>> python openai_state_explorer.py

The script will generate Excel files containing state information for each country code in the array list.

Contributing
If you'd like to contribute to this project, please follow the contribution guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.
