# github-actions-udemy
# Running the Flask API Project Locally

To run the Flask API project locally, follow these steps:

1. Clone the GitHub repository for the project to your local machine.
2. Navigate to the project directory in your terminal.
3. Install Flask and pytest using `pip`:

pip install flask pytest


4. Install `flasgger` using `pip`:

pip install flasgger

5. Run the unit tests to make sure everything is working correctly:

pytest

6. If the tests pass, start the Flask development server:

python app.py


7. Open your web browser and navigate to `http://localhost:5000/` to test the "Hello, World!" endpoint.
8. Test the other API endpoints using a tool like `curl` or a web API testing tool like Postman.
9. To view the Swagger documentation, navigate to `http://localhost:5000/apidocs` in your web browser.
10. When you're finished testing the app, stop the Flask development server by pressing `Ctrl + C` in your terminal.


## Reusable Worfklows

**Inputs**:
| ``Name``              | ``Description``                              | ``Required`` | ``Default``         |
| ------------------|------------------------------------------| ---------|-----------------|
| python_version     | Python version for the virtual environment| true     | 3.9             |
| tests_folder       | Location of the test folder               | true     | tests           |
| requirements_file  | Path to requirements.txt file             | true     | requirements.txt|

```
name: Example usage of Automated Testing Workflow 🤖🧪

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Run Automated Testing Workflow
        uses: ./.github/workflows/automated_testing_workflow.yml
        with:
          python_version: '3.9'
          tests_folder: 'tests'
          requirements_file: 'requirements.txt'



```