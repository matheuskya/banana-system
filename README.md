## About

<a href="https://matheuskya.pythonanywhere.com/main/index/">The project.</a>
<br>
This is a project inspired by <a href="https://www.youtube.com/watch?v=RELWFGJnKE0&list=LL&index=6&t=86s">this video.</a>
Since I had never built something like this before, I decided to give it a try, and it turned out great!
Through this project, I practiced key skills such as Django, profile management, chatting, and authentication. I hope you enjoy it!

## Setup for Linux Users

### Creating and Activating a Virtual Environment

To set up the project on Linux, follow these steps to create and activate a virtual environment:

1. Open a terminal in your project directory.

2. Ensure you have Python 3 installed:
   ```
   python3 --version
   ```

3. Install the venv module if it's not already installed:
   ```
   sudo apt-get install python3-venv
   ```

4. Create a virtual environment named 'venv':
   ```
   python3 -m venv venv
   ```

5. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

   You should see (venv) appear at the beginning of your terminal prompt, indicating that the virtual environment is active.

6. To deactivate the virtual environment when you're done, simply run:
   ```
   deactivate
   ```

Remember to activate the virtual environment every time you want to run the project.

## Setup for Windows Users

### Creating and Activating a Virtual Environment

To set up the project on Windows, follow these steps to create and activate a virtual environment:

1. Open Command Prompt or PowerShell in your project directory.

2. Ensure you have Python 3 installed:
   ```
   python --version
   ```

3. Create a virtual environment named 'venv':
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - If using Command Prompt:
     ```
     venv\Scripts\activate.bat
     ```
   - If using PowerShell:
     ```
     .\venv\Scripts\Activate.ps1
     ```

   You should see (venv) appear at the beginning of your prompt, indicating that the virtual environment is active.

5. To deactivate the virtual environment when you're done, simply run:
   ```
   deactivate
   ```

Remember to activate the virtual environment every time you work on the project.

### Installing Dependencies

After activating your virtual environment, you need to install the project dependencies. These are listed in the `requirements.txt` file.

1. Ensure you're in your project directory and your virtual environment is activated.

2. Install the dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

3. Wait for the installation to complete. Pip will download and install all the packages listed in the requirements.txt file.

4. Once the installation is complete, you can verify the installed packages by running:
   ```
   pip list
   ```

   This will show all packages installed in your virtual environment.

Note: If you encounter any issues during installation, ensure that your pip is up to date:
```
pip install --upgrade pip
```

Then try the installation command again.

## Running the Django Development Server

After setting up your virtual environment and installing dependencies, you can start the Django development server:

1. Ensure your virtual environment is activated.

2. Navigate to the project directory:
   ```
   cd banana-system/bananasystem
   ```

3. Start the Django development server:
   ```
   python manage.py runserver
   ```

4. You should see output similar to this:
   ```
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).
   Month Day, Year - HH:MM:SS
   Django version X.X.X, using settings 'bananasystem.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
   ```

5. Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

6. To stop the server, press CTRL+C in the terminal where the server is running.

Note: This server is for development purposes only. For production deployment, please refer to Django's deployment documentation.
