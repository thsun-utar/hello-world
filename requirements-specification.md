# Requirements Specification: Hello World Web Application

## 1. Purpose

The application is a small, locally hosted web experience with a colorful fruit collection and a browser-based calculation toolkit. It is intended as a simple example that can be run with Python and used in a standard web browser.

## 2. Scope

The application includes:

- A home page that introduces the site and displays five illustrated fruits.
- An advanced calculations page containing a scientific calculator, compound-interest planner, statistics summary, and unit converter.
- A Python HTTP server that serves the application pages and their static assets on the local machine.

All calculations are performed in the browser. The application does not require a database, user accounts, or third-party Python packages.

## 3. Users

- **Local user:** Starts the server and visits the application in a web browser.
- **Calculator user:** Uses one or more calculation tools and views the results on the calculations page.

## 4. Functional Requirements

### FR-1: Start the local web server

The application shall be startable by running `python app.py` from the `hello-world` directory with Python 3 installed.

**Acceptance criteria**

- The server listens on `127.0.0.1:8000`.
- The server prints a message identifying the local application URL when it starts.
- The server can be stopped by interrupting the process.

### FR-2: Serve application routes and assets

The server shall respond to `GET` requests for the registered application pages, stylesheet, and fruit illustrations.

**Acceptance criteria**

- `/` serves the Hello World home page.
- `/calculations` and `/advanced-calculations.html` serve the advanced calculations page.
- `/style.css` serves the shared stylesheet.
- `/images/apple.svg`, `/images/banana.svg`, `/images/orange.svg`, `/images/grapes.svg`, and `/images/strawberry.svg` serve their corresponding image assets.
- An unregistered path returns an HTTP 404 response.

### FR-3: Display the fruit collection

The home page shall display a Hello World heading, a short introduction, a link to the calculations page, and a collection of five fruit cards: apple, banana, orange, grapes, and strawberry.

**Acceptance criteria**

- Each fruit card shows its name and corresponding illustration.
- Each illustration has alternative text identifying the fruit.
- The fruit collection adapts to available screen width.

### FR-4: Navigate between pages

Users shall be able to navigate from the home page to the calculations page and back using visible links.

**Acceptance criteria**

- The home page provides a link to `/calculations`.
- The calculations page provides a link to `/`.

### FR-5: Select a calculator

The calculations page shall provide tabs for Scientific, Compound interest, Statistics, and Unit converter.

**Acceptance criteria**

- The scientific calculator is selected when the page first loads.
- Selecting a tab displays its associated calculator panel and hides the other panels.
- Users can change tabs with the left/right arrow keys and move to the first or last tab with Home or End.
- Tab selection is exposed to assistive technology through appropriate tab and panel semantics.

### FR-6: Calculate scientific expressions

The scientific calculator shall evaluate numeric expressions using addition, subtraction, multiplication, division, powers, unary signs, and parentheses. It shall also support the constants `pi` and `e`, and the functions `sin`, `cos`, `tan`, `sqrt`, `ln`, and `log` (base 10).

**Acceptance criteria**

- The user can enter expressions using the keypad or keyboard.
- The user can calculate with the equals button or Enter, delete the last expression character, and clear the expression with AC or Escape.
- Trigonometric functions use the selected degree or radian mode.
- Standard arithmetic precedence and parentheses are honored.
- Invalid expressions, division by zero, negative square roots, non-positive logarithm inputs, and non-finite results produce an understandable error instead of a result.
- Calculator input is parsed as an expression and is not executed as JavaScript.

### FR-7: Estimate compound-interest growth

The compound-interest planner shall estimate a future value from a starting amount, annual interest rate, investment period, and compounding frequency.

**Acceptance criteria**

- The user can enter the starting amount, annual rate, and period, and select annual, semi-annual, quarterly, monthly, or daily compounding.
- A successful calculation displays the estimated future value and estimated interest earned.
- Negative, non-finite, or out-of-range assumptions produce an error message.
- The displayed estimate identifies that taxes, fees, and additional deposits are excluded.

### FR-8: Summarize a data set

The statistics calculator shall accept a list of numbers separated by commas or whitespace and calculate descriptive statistics.

**Acceptance criteria**

- For valid input, the result includes count, sum, mean, median, minimum, maximum, population standard deviation, and sample standard deviation.
- A data set with one value reports that sample standard deviation is unavailable.
- Empty input, malformed separators, invalid numbers, and non-finite results produce an error message.

### FR-9: Convert common units

The unit converter shall convert values between supported units of length, mass, and temperature.

**Acceptance criteria**

- Length units are meters, kilometers, centimeters, feet, and miles.
- Mass units are grams, kilograms, ounces, and pounds.
- Temperature units are Celsius, Fahrenheit, and Kelvin.
- Changing the measurement type updates the available source and destination units.
- A successful conversion displays the entered value, source unit, converted value, and destination unit.
- Non-finite values and temperatures below absolute zero produce an error message.

## 5. Non-Functional Requirements

### NFR-1: Local operation and dependencies

- The application shall run locally and perform its calculations in the user's browser.
- The server shall use Python's built-in HTTP server facilities; no third-party Python package or virtual environment shall be required.
- Core page assets shall be served from the project directory.

### NFR-2: Browser usability and accessibility

- Pages shall use responsive layouts suitable for narrow and wide viewports.
- Interactive controls shall be operable by keyboard.
- Forms shall have associated labels, and result or error updates shall be announced through status semantics.
- Interactive controls shall have a visible keyboard-focus indicator.
- Motion shall respect the user's reduced-motion preference.

### NFR-3: Error handling

- Invalid or unsupported input shall result in a clear, user-visible error.
- The application shall not present an invalid calculation as a successful result.

## 6. Constraints and Assumptions

- Python 3 is installed and available as `python` in the command shell.
- The user has access to a web browser and can connect to the local loopback address.
- The configured server address and port are fixed at `127.0.0.1:8000`.
- Calculation values use ordinary JavaScript numeric precision; displayed values are formatted for readability and are not intended as accounting-grade precision.
- Currency, tax, fee, and recurring-contribution calculations are outside the current compound-interest estimate.

## 7. Out of Scope

- Public internet hosting, deployment, or multi-user access.
- User registration, authentication, saved calculations, or a database.
- External APIs or server-side calculation services.
- Additional calculator categories, units, or configurable exchange rates not listed in this specification.