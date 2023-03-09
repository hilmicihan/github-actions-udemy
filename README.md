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
## Reusable Workflows

### Automated Testing Workflow 🤖🧪

This GitHub workflow is designed to automate testing for Python projects. It sets up a virtual environment with a specified Python version, installs the required dependencies, and runs the tests located in a specified test folder.


**Inputs**:

| ``Name``              | ``Description``                              | ``Required`` | ``Default`` |
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
        - name: Checkout Repository
          uses: actions/checkout@v2
         - name: Run Automated Testing Workflow
           uses: ./.github/workflows/reusable-testing.yaml
           with:
              python_version: '3.9'
              tests_folder: 'tests'
              requirement_file: 'requirements.txt'
            

```