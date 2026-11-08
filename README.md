# AARS — Automatic Retrieval System

## Steps to Operate

### 1. Extract the Project
1. Extract `aars.zip` to a folder on your computer.
2. Open the extracted `aars` folder in Visual Studio Code or a terminal.

### 2. Install Python
1. Make sure Python 3 is installed.
2. On Windows, open Command Prompt or the VS Code terminal in the project folder.
3. Check the installation:

```bash
python --version
```

### 3. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
```

On Windows Command Prompt:

```bash
venv\Scripts\activate
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Flask

```bash
python -m pip install Flask
```

### 5. Start the Application

Make sure the terminal is in the folder containing `aars.py`, then run:

```bash
python aars.py
```

Wait until Flask displays a local address, normally:

```text
http://127.0.0.1:5000
```

### 6. Open the Application
1. Open a web browser.
2. Visit `http://127.0.0.1:5000`.
3. The AARS login page will appear.

### 7. Register an Account
1. Select **Create account**.
2. Enter your full name, email address, and password.
3. Select **Create account**.
4. Return to the login page.

### 8. Log In
1. Enter the email address and password you registered with.
2. Select **Enter AARS**.
3. The dashboard will open.

### 9. Submit an Item Retrieval Request
1. Browse the available items on the dashboard.
2. Use the search box to find an item.
3. Select the arrow on the item card.
4. Set the required quantity using the **+** and **−** buttons.
5. Choose **Normal** or **Urgent** priority.
6. Select **Initiate Retrieval**.

### 10. View the Request Status
1. After submitting the request, the retrieval status page opens.
2. Review the item, rack location, and displayed status.
3. Select **Back to Control Desk** to return to the dashboard.

### 11. Log Out
1. Select **Exit** in the dashboard header.
2. You will be returned to the login page.

### 12. Stop the Application
1. Return to the terminal where Flask is running.
2. Press `Ctrl + C` to stop the server.
3. If you activated the virtual environment, type `deactivate` to exit it.

## Important Notes
- This ZIP contains a Flask web application prototype. The listed inventory and requests are stored in memory; they reset when the Python application is restarted.
- The current code displays the request status as **Searching**. The interface does not currently control physical retrieval hardware or automatically progress through the picking and delivery stages.
- Run the application locally and keep the terminal window open while using it.
