# Rd - A Random Choice Generator

## Description

Rd is a random choice generator written in Python using the Tkinter library. It allows you to generate a random number within a specified range, excluding any numbers you choose.

## Installation

1. Clone the repository: `git clone https://github.com/shs-plus/Rd.git`
2. Navigate to the project directory: `cd Rd`
3. Run the program: `py main.pyw`

## Usage

When you run the program, a window will appear with a "Random Choice" button. Click the button to generate a random number. The number will appear in the window.

You can customize the program by editing the `settings.json` file. Here are the available settings:

- `title`: The title of the window.
- `geometry`: The size and position of the window.
- `n`: The range of numbers to choose from.
- `coef`: The degree of likeliness for a number generated recently to be generated again.
- `debug`: Whether to enable debug mode.
- `exception`: A list of numbers that should not be generated.

## License

This project is licensed under the GPL v3. For more information, see the `LICENSE` file in the project root.
