# CSV Splitter

## Overview

This Python application allows users to split a large CSV file into smaller files with a specified maximum number of lines. The program retains the header row in each output file and saves the files in the directory where the script is executed.

## Features

- Simple GUI built with `tkinter` for selecting the CSV file and specifying the number of lines per output file.
- Automatically splits the CSV file and saves the parts with the original file name followed by the max lines and part number.
- Displays the total number of lines in the original file and the number of output files created after the split.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/butyoucancallmesteve/csv_split_app.git
   cd csv-splitter
   ```

2. **Install the required dependencies:**

   Make sure you have Python installed. You can install the required Python packages using pip:

   ```bash
   pip install pandas
   ```

   The `tkinter` library should be included with Python by default.

## Usage

1. Run the script:

   ```bash
   python csv_splitter.py
   ```

2. Use the GUI to:
   - Select the CSV file.
   - Enter the maximum number of lines per output file.
   - Click the "Split CSV" button to split the file.

3. The program will save the split files in the current directory and display the total number of lines and the number of output files.

## Example

Here is an example of how the output files are named:
   - originalfile_100_part1.csv
   - originalfile_100_part2.csv

## License

This project is licensed under the MIT License.
