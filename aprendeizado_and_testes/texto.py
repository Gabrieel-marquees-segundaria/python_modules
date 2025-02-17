texto = """
 This script contains two separate programs. The first one is a Python script that generates a Git commit message using the OpenAI API (specifically, the Mistral model). The second one is a bash script that retrieves the Git diff and commits it with the generated message if prompted to do so.
   The Python script uses the OpenAI API to generate a Git commit message based on the provided Git diff output. It retrieves the Git diff, formats the prompt for the model, and uses the Mistral model to generate the commit message. If there's an error reading the Git diff or generating the commit message, it will display an error message and exit with status 1.

   The bash script at the bottom of the file retrieves the Git diff output using the 'git diff --staged' and 'git diff' commands, and if no staged changes are found, it uses the unstaged changes instead. It then calls the Python script to generate a commit message and commits the changes with that message if the user confirms.

   To use this script, save it as a .py file (e.g., git_commit.py) and make sure you have installed the OpenAI API client library. You can then run it from the command line like so:

   ```
   python git_commit.py
   ```

   If you want to automate the process, you can call this script as a subprocess from another bash script or integrate it into your project's build process using Makefiles or similar tools"""