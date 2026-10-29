# Understand and defend your FizzBuzz pipeline

A beginner’s guide to the current project. Read in order; run the examples yourself. The examples describe the local files, not proof of a successful hosted pipeline run.

## 1. What you are building

A script is a file containing instructions that a program can execute. Python is the language those instructions use. The Python interpreter reads and runs them.

FizzBuzz means: go through 1 to 100; print Fizz for multiples of 3, Buzz for multiples of 5, FizzBuzz for multiples of both, and the number otherwise. A multiple of 3 is something like 3, 6, 9 or 12: it divides by 3 without a remainder.

The project has three layers:

1. The function calculates the answer for one number.
2. The main function repeats that calculation and prints the results.
3. GitHub Actions runs automated checks and the script on a separate computer.

Tests check the rules. A pipeline automates running those tests. A repository stores the files and their change history.

## 2. Your complete script

```python
def fizzbuzz(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def main() -> None:
    for number in range(1, 101):
        print(fizzbuzz(number))


if __name__ == "__main__":
    main()
```

Read the next sections with fizzbuzz.py open. Python uses indentation to decide which instructions belong together. In the actual file, top-level lines start at the left edge; each nested level uses four spaces. Blank lines separate sections for readability.

## 3. What def actually does

```python
def fizzbuzz(number: int) -> str:
```

`def` tells Python to create a function. A function is a named set of instructions you can use repeatedly. Defining it stores the instructions; it does not run its body yet.

`fizzbuzz` is the chosen name, not a built-in Python keyword. We could name it differently, but callers and imports would need updating too.

The parentheses contain the inputs. `number` is a parameter: a local name for the value the caller provides. In `fizzbuzz(15)`, 15 is the argument, meaning the actual value supplied. Inside that call, number has the value 15.

`: int` is a type hint: this parameter is intended to receive an integer, such as 1 or 15. It does not convert the value or automatically reject other types.

`-> str` is another type hint: the result is intended to be a string, meaning text. For example, `"Fizz"` and `"7"` are strings. The integer `7` and the string `"7"` are different types.

The final colon starts the function’s indented body. The colon after number introduces its type hint; the colon at the end introduces a block. Same character, different positions and purposes.

An interview explanation: “This function takes one integer and returns its FizzBuzz label as text. Type hints make that intention clear.”

## 4. Conditions and arithmetic symbols

```python
if number % 15 == 0:
    return "FizzBuzz"
```

`if` means execute the following indented block only when the condition is true. A condition produces a Boolean value: True or False.

`%` is modulo: it gives the remainder after division.

```python
15 % 15  # 0: fifteen divides evenly by fifteen
16 % 15  # 1: sixteen leaves a remainder of one
6 % 3    # 0
7 % 3    # 1
```

`#` starts a comment. Python ignores the rest of that line; the text explains the example to a reader.

`==` compares two values for equality. It asks a question. A single `=` assigns a value to a variable; it does not compare values.

```python
number = 15       # assign a value
number == 15      # compare: True
number % 15 == 0  # compare remainder with zero: True
```

Multiples of both 3 and 5 are multiples of 15. We check this first because 15 also passes the individual 3 and 5 checks. If the 3 check came first, 15 would return Fizz and never reach FizzBuzz.

An equivalent condition would be `number % 3 == 0 and number % 5 == 0`. Here `and` requires both conditions to be true. Dividing by 15 is shorter for these fixed rules.

## 5. Return, strings and the order of checks

`return "FizzBuzz"` sends a value back to the caller and immediately ends this function call. Double quotes mark text; they are not part of the output. Single quotes would also work.

```python
if number % 3 == 0:
    return "Fizz"
if number % 5 == 0:
    return "Buzz"
return str(number)
```

If the first condition failed, Python continues to the 3 check, then the 5 check. If none match, it reaches the final return. `str(number)` converts the number to text. Every branch therefore returns the same kind of value.

We do not need `else` or `elif` because a successful branch already returns. `elif` means “otherwise, if” and `else` means “otherwise.” They could express the same logic, but would not make this version faster in a meaningful way.

`return` and `print` are different. Returning gives a value to other code. Printing writes text to the output stream, usually the terminal. The calculation function returns; main prints. This lets tests inspect a result without needing to capture the terminal for every rule.

## 6. Trace four calls by hand

1. `fizzbuzz(7)`: the remainders for 15, 3 and 5 are nonzero; return `"7"`.
2. `fizzbuzz(9)`: not divisible by 15; divisible by 3; return `"Fizz"`. Stop this call.
3. `fizzbuzz(10)`: fails 15 and 3; passes 5; return `"Buzz"`.
4. `fizzbuzz(15)`: passes the first check; return `"FizzBuzz"`. Never evaluate the later checks.

Try explaining those four without looking at the code. Understanding the route through the checks matters more than memorizing the lines.

## 7. Main and the loop

```python
def main() -> None:
    for number in range(1, 101):
        print(fizzbuzz(number))
```

`main` is the name we chose for the function that coordinates execution. Python does not automatically run a function because it is named main.

Empty parentheses mean no parameters are declared. `-> None` says the function does not return a meaningful result. With no explicit return, a Python function returns None automatically.

`for` repeats an indented block for each item. `in` identifies the sequence being iterated over. The loop assigns each successive item to the name number.

`range(1, 101)` represents integers starting at 1 and stopping before 101. The end is excluded, so this includes 100. The comma separates the two arguments. The default step is 1. A range does not build a full list of all the numbers in memory.

`print(fizzbuzz(number))` has nested function calls. Work from inside to outside: calculate fizzbuzz(number), then pass the result to print. Print adds a newline by default, giving one result per line.

The main body is indented four spaces. The loop body is indented eight spaces because it belongs inside both main and the loop.

## 8. Why the strange name check exists

```python
if __name__ == "__main__":
    main()
```

`__name__` is a name that Python supplies for each module. A module is a Python file that can be imported. The double underscores are part of this special name.

When you run `python3 fizzbuzz.py` directly, Python gives this module the name `"__main__"`. The condition is true, so main() runs.

When the tests use `from fizzbuzz import fizzbuzz, main`, the module name is `"fizzbuzz"`. The condition is false. Python loads the function definitions, but does not automatically print 100 lines.

`main()` calls the function; `def main()` defines it. This distinction is fundamental.

## 9. How Python executes the file

1. The interpreter reads the file from the top.
2. It encounters def fizzbuzz and creates that function.
3. It encounters def main and creates that function.
4. It evaluates the name check at the bottom.
5. When run directly, it calls main.
6. Main loops through 100 integers.
7. Each iteration calls fizzbuzz once and prints its returned string.
8. The loop finishes, main finishes, and the process exits successfully.

An unexpected unhandled exception would stop the process with a nonzero exit code. An exit code is the process’s success/failure signal to the operating system. Zero means success; nonzero means failure.

## 10. Tests: imports and the class

```python
import unittest
from contextlib import redirect_stdout
from io import StringIO
from fizzbuzz import fizzbuzz, main
```

`import` makes code from another module available. unittest is Python’s built-in testing library. `unittest.TestCase` means access the TestCase name inside the unittest module; the dot selects an attribute.

`from ... import ...` imports particular names so we can use them directly. contextlib and io are standard-library modules. The last line imports our functions from fizzbuzz.py. The comma separates the two names.

```python
class FizzBuzzTests(unittest.TestCase):
```

`class` defines a type that groups related behavior. Here it groups the tests. FizzBuzzTests is our chosen class name. The parentheses say it inherits from unittest.TestCase: it receives testing features such as assertEqual from that base class. The colon begins its body.

```python
def test_number(self):
    self.assertEqual(fizzbuzz(1), "1")
    self.assertEqual(fizzbuzz(98), "98")
```

A function defined in a class is called a method. Test discovery recognizes method names beginning with test. `self` refers to the current test object; the test runner supplies it automatically. We do not call it ourselves with an argument.

`assertEqual(actual, expected)` checks equality and fails the test if the values differ. It is an assertion, not a print statement. The test runner reports the failure and which values differed.

The four rule tests check ordinary numbers, Fizz, Buzz and FizzBuzz. Higher values such as 98, 99, 100 and 90 complement the smaller examples and check behavior near the range’s end.

## 11. Tests: capturing printed output

```python
output = StringIO()
with redirect_stdout(output):
    main()
```

`=` assigns an object to the name output. `StringIO()` creates an in-memory text buffer: a place to collect text without creating a file on disk.

Standard output, or stdout, is where print normally writes. `redirect_stdout(output)` temporarily sends that output to our buffer instead.

`with` begins a managed block. The redirection applies inside this block and is restored when the block ends, including if an exception occurs. That is why main is indented under with.

```python
lines = output.getvalue().splitlines()
```

`getvalue()` returns the captured text as one string. `splitlines()` turns it into a list of lines without newline characters. The dot calls a method on an object. These two method calls are chained: the result of the first becomes the receiver of the second.

A list is an ordered collection. Its positions, called indexes, begin at zero.

```python
self.assertEqual(len(lines), 100)
self.assertEqual(lines[:15], [
    "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
    "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
])
self.assertEqual(lines[-1], "Buzz")
```

`len(lines)` counts the items. Square brackets create a list or select from one, depending on position. `lines[:15]` is a slice: take items from the beginning up to, but excluding, index 15. That gives the first 15 lines. `lines[-1]` selects the last item; negative indexes count backward from the end.

The multiline list has matching opening and closing brackets. Commas separate items. The final trailing comma is allowed and makes editing easier. Python permits these line breaks inside brackets and parentheses.

The expected first 15 values exercise every rule and their ordering. The last line must be Buzz because 100 is divisible by 5 but not by 3.

```python
self.assertEqual(lines.count("Fizz"), 27)
self.assertEqual(lines.count("Buzz"), 14)
self.assertEqual(lines.count("FizzBuzz"), 6)
```

`count` counts exact matching list items, not substrings. FizzBuzz is not counted as Fizz.

There are 33 multiples of 3 up to 100 and 6 multiples of 15: 33 minus 6 gives 27 Fizz lines. There are 20 multiples of 5: 20 minus 6 gives 14 Buzz lines. There are 6 FizzBuzz lines. The remaining 53 lines are ordinary numbers.

Be precise about coverage: these tests check representative individual values, the first 15 output lines, the final line, total line count and label counts. They do not independently compare every later numeric line or launch the script as a separate process.

## 12. Running the tests

```sh
python3 -m unittest discover -s tests -v
```

This is a terminal command, not Python source code. python3 selects the interpreter. `-m unittest` runs the unittest module as a program. `discover` asks it to find tests. `-s tests` starts searching in the tests directory. `-v` requests verbose output with each test’s name. The default discovery pattern finds files named test*.py.

There are five test methods. Two assertions in a method do not count as two separately named tests. If an assertion fails, execution of that method normally stops at that assertion; the runner continues with other tests.

The bottom name guard in test_fizzbuzz.py calls unittest.main() when that file runs directly. Discovery has its own runner and does not rely on that guarded call.

Local commands, from the project folder:

```sh
python3 fizzbuzz.py
python3 -m unittest discover -s tests -v
```

## 13. What Git and GitHub contribute

Git tracks changes locally. GitHub hosts a remote copy. They are related, but different tools.

`git add` stages selected changes for the next commit. `git commit` records a local snapshot and a message. `git push` sends commits to the remote repository. Saving a file alone does not upload it or run GitHub Actions.

`.gitignore` contains patterns for files Git should normally leave untracked:

- `__pycache__/`: Python-generated bytecode cache directories.
- `*.py[cod]`: compiled Python files such as .pyc; the star matches a filename and [cod] matches one of those letters.
- `.venv/`: a local virtual environment directory.
- `.DS_Store`: Finder metadata created by macOS.

Ignoring files does not remove ones that are already tracked. These patterns keep generated and machine-specific files out of the project history.

## 14. Pipeline: the whole journey

Push containing workflow → GitHub detects event → starts job on runner → checks out code → selects Python → runs tests → if successful, runs script → records logs and status.

A workflow is the automation definition. A run is one execution of it. A job is a group of steps on a runner. A runner is the computer executing those steps. Our steps run sequentially in one job.

The workflow file is `.github/workflows/ci.yml`. GitHub looks for workflows in this directory. YAML is a configuration format, not Python. Indentation represents nesting; use spaces. A colon separates a key from its value. A dash starts an item in a list.

## 15. Every pipeline setting

```yaml
name: FizzBuzz CI

on:
  push:
  pull_request:
  workflow_dispatch:

permissions:
  contents: read
```

`name` is the label shown in Actions. CI stands for continuous integration: automated checks around integrating code changes.

`on` declares triggering events. `push` responds to repository pushes. `pull_request` responds to supported pull-request activity, such as opening or updating a request. A pull request proposes merging changes. `workflow_dispatch` enables manual runs; GitHub requires the workflow to exist on the default branch for this trigger. Empty event values mean no extra filters were configured.

The workflow has no branch filters. Updating a branch with an open pull request can therefore produce both a push run and a pull-request run.

`permissions` sets access for the automatically supplied GITHUB_TOKEN. `contents: read` permits reading repository contents; unspecified permissions become none. We need no write access to run this project. Private repository visibility and Actions settings still depend on the account.

```yaml
jobs:
  test-and-run:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
```

`jobs` holds the jobs. `test-and-run` is our chosen job identifier. `runs-on` selects a GitHub-hosted Ubuntu Linux runner image. `ubuntu-latest` can change over time; it is not a permanently fixed operating-system version. The five-minute timeout limits how long the job can run. It is not a five-minute repeating schedule.

`steps` holds the ordered list of actions and commands.

```yaml
      - name: Check out repository
        uses: actions/checkout@v7
      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: '3.13'
```

Each dash begins one step. `name` describes it for the logs. `uses` runs a reusable action. `actions/checkout` places repository code on the runner. Starting a runner does not automatically place our source files there.

The @ separates the action name from its version reference. v7 is the action’s version reference, not Python’s version. Major-version tags can move; pinning to a full reviewed commit SHA gives a more fixed dependency reference.

`actions/setup-python` selects the interpreter and puts it on the command path. `with` supplies inputs to that action. `'3.13'` is quoted so the version is a string. It selects a matching Python 3.13 release rather than pinning one exact patch release.

```yaml
      - name: Run tests
        run: python -m unittest discover -s tests -v
      - name: Run FizzBuzz
        run: python fizzbuzz.py
```

`run` executes a shell command on the runner. CI uses python because setup-python has selected it; our Mac commands use python3. The test command is otherwise the same.

By default, later steps run only after earlier steps succeed. Failed tests return a nonzero exit code, causing this job to fail and skipping the final script step. If the script itself raises an unhandled exception, that step also fails. There is no continue-on-error setting to hide failures.

The workflow currently reports through console logs and job status. It does not publish a downloadable test report. A failed check does not automatically prevent merging unless repository rules require it.

This implements continuous integration and execution of the requested script. There is no production deployment target or deployment stage in this assessment.

Reference for the settings: [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

## 16. How to inspect an actual run

1. Open the GitHub repository and its Actions tab.
2. Select the FizzBuzz CI workflow and a specific run.
3. Check its commit ID matches the code you want to demonstrate.
4. Open the test-and-run job.
5. Expand Run tests. Explain each test and the final OK or failure report.
6. Expand Run FizzBuzz. Inspect the sequence and its last line, Buzz.
7. If a step fails, investigate the first failing step and its error rather than assuming the application logic is wrong.

A failure during checkout or Python setup is different from a failed assertion. Local passing tests do not prove a hosted run passed. A workflow file being present does not prove it has executed.

## 17. The improvement you can implement live

The current refinement file proposes a custom start and end number while retaining 1–100 as the default. Explain this as an optional future requirement, not something the assignment already demands.

First change only main:

```python
def main(start: int = 1, end: int = 100) -> None:
    for number in range(start, end + 1):
        print(fizzbuzz(number))
```

`= 1` and `= 100` inside the parameter list provide defaults. Calling main() behaves as before. Calling main(14, 16) uses the supplied values. `end + 1` preserves an inclusive end because range excludes its stop value.

Then add this method inside the test class:

```python
def test_custom_range(self):
    output = StringIO()
    with redirect_stdout(output):
        main(14, 16)
    self.assertEqual(output.getvalue().splitlines(), ["14", "FizzBuzz", "16"])
```

Run all tests and confirm the original behavior still passes. This change allows Python callers to choose a range; it does not yet accept terminal arguments. If they ask for `python fizzbuzz.py 14 16`, explain that argument parsing is another change. Clarify reversed ranges and supported input types before adding validation.

## 18. Estimate and a short walkthrough

Proposed estimate: 2 Fibonacci story points. The Fibonacci sequence begins 1, 2, 3, 5, 8, 13. Points express relative effort, complexity and uncertainty, not a fixed number of hours. The estimate includes the script, tests, automation and refinement note. It assumes GitHub access and needs calibration against the team’s reference stories. The assessment’s two-hour cap is a separate timebox.

The brief asks for an estimate. It is currently absent from the short refinement file, so be ready to state it verbally; agree whether to put it back in the submission before presenting.

A concise opening you can explain in your own words:

“I used Python because the task is small and the code is readable. One function converts a number to its label; main prints the sequence. I check the shared multiple first. I used the standard-library test runner to avoid extra dependencies. GitHub Actions runs the tests before the script. The backlog proposes configurable bounds while preserving the default.”

## 19. Likely questions and answers

These are practice questions inferred from the brief, not confirmed questions.

### Why Python?

It is readable, fits scripting and the role’s Python tooling, and includes a test framework. This project needs no external Python packages. Avoid claiming it is always better than PowerShell.

### Why not print inside fizzbuzz?

Returning a value separates calculation from output. Callers and tests can reuse the calculation without capturing printed text.

### Why 15 before 3?

15 satisfies both rules. Returning Fizz first would end the function too early.

### Why not use three independent if statements that print?

Several conditions could be true for one number, producing several output lines. Here each successful condition returns exactly one result.

### What happens if range ends at 100?

Python excludes the stop value, so the script would stop at 99. Our total-count and final-value tests help detect that mistake.

### Are type hints input validation?

No. They describe intent for readers and tooling. The current caller only supplies positive integers in the requested range.

### What happens for zero or a negative number?

The function has no validation. Zero returns FizzBuzz because its remainder is zero for 15; negative multiples follow the same divisibility checks. Main does not generate those inputs. Clarify the requirement before changing this.

### Why unittest rather than pytest?

It is built into Python and sufficient here. Pytest could be a good team choice, but would add a dependency to this small project.

### Why test output as well as the function?

The function could be correct while the loop prints the wrong number of lines, uses the wrong boundaries, or prints extra text. The output test checks that integration.

### What do your tests not prove?

They do not exercise every possible integer or prove a successful hosted run. They test main directly, not a new operating-system process, and do not compare every numeric output line after the first 15. They give useful evidence within this small scope, not a proof of all behavior.

### How would you demonstrate a failing test?

Temporarily change an expected value locally, run the suite and inspect the failure, then restore the correct value and rerun. Use a separate branch if demonstrating a red hosted run; avoid breaking the main branch just for a demonstration.

### What happens if a test fails in Actions?

The test command exits nonzero, the job fails and the script step is skipped. The logs identify the assertion. Branch protection must separately require the status to block a merge.

### Why GitHub Actions instead of Azure DevOps?

It matches the available GitHub repository and satisfies the choice allowed in the brief. The same test and script commands could run in Azure DevOps.

### Is this a full deployment pipeline?

It is CI that runs the script and tests. There is no deployed service in the story, so there is no deployment stage.

### How fast is the algorithm?

For a generalized range of n numbers, it does a fixed number of checks per number: O(n) time. The script itself uses O(1) additional working memory apart from output buffering. The output test stores n lines, so its captured output needs O(n) memory. With the required range fixed at 100, the actual work is bounded and tiny.

### What would you improve?

Confirm whether users need custom bounds, then parameterize main and add the small range test. Keep the default output unchanged. Extra configuration is worthwhile only when it meets a need.

### Why 2 points rather than 1 or 3?

More than the arithmetic is included: tests, repository work and pipeline setup. The implementation is small and understood, so 2 is a reasonable proposal. Team calibration and uncertainty about access can change that estimate.

### What would you investigate if CI passed locally but failed remotely?

Compare the exact commit, interpreter version, working directory, filenames and paths, then read the first failing step. Separate missing access or runner setup from application/test failures. Reproduce the command locally before changing code blindly.

### What about infrastructure, containers and Databricks?

They are relevant to the broader role, but this script needs none of them to satisfy the story. Explain how you would apply the same practices to larger systems without claiming this project provisions infrastructure.

## 20. Final practice checklist

- Explain every line of fizzbuzz.py without reading this guide.
- Predict results for 1, 3, 5, 15, 98, 99 and 100.
- Explain return versus print, and definition versus call.
- Run tests and explain each assertion.
- Explain every pipeline step and the failure path.
- Demonstrate an actual hosted run if one is available.
- State the estimate and implement the custom-range change in practice.
- Prepare real examples of troubleshooting, collaboration and ownership for the panel.

## References

These official references support the language and workflow explanations; the project files determine what this particular implementation does.

- [Python 3.13 control flow: functions, return, range and annotations](https://docs.python.org/3.13/tutorial/controlflow.html)
- [Python unittest](https://docs.python.org/3.13/library/unittest.html)
- [Python redirect_stdout](https://docs.python.org/3.13/library/contextlib.html#contextlib.redirect_stdout)
- [Python StringIO](https://docs.python.org/3.13/library/io.html#io.StringIO)
- [Python main-module convention](https://docs.python.org/3.13/library/__main__.html)
- [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
