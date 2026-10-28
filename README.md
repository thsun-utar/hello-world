# Hello World

Developer: sun

A small local web experience with a colorful fruit collection and browser-based calculation tools. The app uses Python's built-in HTTP server and does not need third-party packages.

## Start the application

1. Install Python 3 if it is not already available.
2. Open a terminal in this directory and run:

	```sh
	python app.py
	```

3. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in a browser.
4. Keep the terminal open while using the app. Press `Ctrl+C` in that terminal to stop the server.

The server is available only on this computer. The fruit home page links to the calculation lab, and the calculation lab has a link back to the home page.

## Use the calculators

Choose a calculator from the tabs at the top of the calculation lab. You can click a tab, or focus the tab row and use Left and Right Arrow to move between tabs. Home selects the first tab and End selects the last.

### Scientific

Enter an expression in the field or build it with the keypad. Press `=` or Enter to calculate. `DEL` removes the last character; `AC` or Escape clears the expression. Use the Angle mode menu to switch between degrees and radians for `sin`, `cos`, and `tan`.

Supported operators are `+`, `-`, `*`, `/`, and `^`, with parentheses and unary signs. Multiplication must be explicit, for example `2*pi`. Supported constants are `pi` and `e`; supported functions are `sin(...)`, `cos(...)`, `tan(...)`, `sqrt(...)`, `ln(...)`, and `log(...)` (base 10). Function arguments must be in parentheses. For example:

```text
(2 + 3) * sqrt(16)
sin(30) + log(100)
```

The calculator reports invalid syntax, division by zero, invalid square roots or logarithms, and other non-finite results instead of displaying them as successful calculations.

### Compound interest

Enter a starting amount, annual interest rate as a percentage, and investment period in years. Choose annual, semi-annual, quarterly, monthly, or daily compounding, then select **Estimate growth**.

The planner accepts a starting amount greater than 0 and no more than 1 trillion, a rate from 0% through 100%, and a period from 0 through 100 years. Daily compounding uses 365 periods per year. The result shows estimated future value and interest earned; taxes, fees, and additional deposits are excluded. Use a consistent unit for the starting amount and interpret the result in that same unit.

### Statistics

Enter finite numbers separated by commas or whitespace. For example, `12, 18 19, 24 27` is valid. Select **Summarize data** to see count, sum, mean, median, minimum, maximum, population standard deviation, and sample standard deviation. For a single value, sample standard deviation is reported as unavailable. Empty input, malformed separators, and invalid numbers are rejected.

### Unit converter

Choose **Length**, **Mass**, or **Temperature**. Select the source and destination units, enter a value, then select **Convert value**. Changing the measurement type refreshes the available units.

- Length: meters, kilometers, centimeters, feet, and miles.
- Mass: grams, kilograms, ounces, and pounds.
- Temperature: Celsius, Fahrenheit, and Kelvin.

Temperatures below absolute zero are not accepted.

## Privacy and limitations

All calculations run in your browser. The app does not save or send your inputs elsewhere. Results use ordinary JavaScript number precision and are formatted for readability; they are not intended for accounting-grade precision. The compound-interest planner does not include taxes, fees, or recurring contributions.

## Tests

Run the standard-library HTTP route tests from this directory:

```powershell
python -m unittest discover -s tests
```