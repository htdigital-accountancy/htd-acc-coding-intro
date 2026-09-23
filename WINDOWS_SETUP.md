# Windows Setup Guide

This guide explains how to set up a Windows laptop for the coding sessions. We will use:

- **Anaconda** to install and manage Python
- **Visual Studio Code (VS Code)** to edit and run code
- The **Python** and **Jupyter** VS Code extensions

## 1. Install Anaconda

1. Visit the [Anaconda download page](https://www.anaconda.com/download).
2. Download the **Windows 64-bit graphical installer**.
3. Run the installer.
4. Choose **Just Me** if asked who should use the installation.
5. Keep the default installation options and complete the installation.

> You do not need to add Anaconda to the Windows `PATH`. The steps below use **Anaconda Prompt**, where the `conda` command is available automatically.

Open the Windows Start menu, search for **Anaconda Prompt**, and open it. Check the installation:

```bat
conda --version
python --version
```

Both commands should display a version number.

## 2. Install VS Code

1. Visit the [VS Code download page](https://code.visualstudio.com/Download).
2. Download the **Windows User Installer**.
3. Run the installer.
4. When shown additional tasks, select:
   - **Add "Open with Code" action**
   - **Add to PATH**
5. Complete the installation and open VS Code.

## 3. Install the VS Code extensions

In VS Code, click the **Extensions** icon on the left-hand side, or press `Ctrl+Shift+X`.

Search for and install these Microsoft extensions:

1. **Python**
2. **Jupyter**

## 4. Save and extract a session ZIP file

Each session will be sent as a separate ZIP file, such as `00_python_fundamentals.zip`.

1. Download the ZIP file sent by the course instructor.
2. In File Explorer, open your **Downloads** folder.
3. Right-click the ZIP file and choose **Extract All**.
4. Choose a permanent location that is easy to find, such as:

   ```text
   C:\Users\YourName\Documents\acc-coding
   ```

5. Click **Extract**.

Do not work on files while they are still inside the ZIP file. Always extract them first.

For later sessions, extract each new ZIP into the same `acc-coding` location. For example, it might eventually contain:

```text
acc-coding
├── 00_python_fundamentals
├── 01_intro_to_jupyter_and_pandas
└── 02_intro_to_APIs
```

## 5. Create the course Python environment

Open **Anaconda Prompt** and create an environment for the course:

```bat
conda create -n acc-coding python=3.12
```

Type `y` and press Enter if asked to continue. Activate the environment:

```bat
conda activate acc-coding
```

Your prompt should now begin with `(acc-coding)`.

## 6. Install the course packages

With the `acc-coding` environment active in Anaconda Prompt, install the packages used across the sessions:

```bat
python -m pip install jupyterlab pandas openpyxl plotly requests
```

You only need to do this once. The same `acc-coding` environment can be reused for every session.

## 7. Open a session in VS Code

In Anaconda Prompt, activate the environment:

```bat
conda activate acc-coding
```

Move into the extracted session folder. For example:

```bat
cd "%USERPROFILE%\Documents\acc-coding\00_python_fundamentals"
```

Then open that folder in VS Code:

```bat
code .
```

Alternatively, open VS Code, select **File → Open Folder**, and choose the extracted session folder.

Repeat this step with the relevant folder when a new session ZIP is provided.

## 8. Select the Python environment

In VS Code:

1. Press `Ctrl+Shift+P`.
2. Search for **Python: Select Interpreter**.
3. Select the interpreter named **acc-coding**.

When you open a `.ipynb` notebook:

1. Click **Select Kernel** in the top-right corner.
2. Choose **Python Environments**.
3. Select **acc-coding**.

You should now be able to run notebook cells by clicking the play button next to each cell.

## Checking that everything works

Open `python_fundamentals.ipynb` inside the extracted `00_python_fundamentals` folder, select the `acc-coding` kernel, and run its first code cell.

You can also test Python from Anaconda Prompt:

```bat
conda activate acc-coding
python -c "import pandas; print('Setup successful')"
```

If the output says `Setup successful`, Python and the course packages are ready.

## Troubleshooting

### `conda` is not recognised

Make sure you are using **Anaconda Prompt**, not Command Prompt or PowerShell.

### `code` is not recognised

Open the folder through **File → Open Folder** in VS Code. You can also rerun the VS Code installer and select **Add to PATH**.

### VS Code cannot find `acc-coding`

1. Close and reopen VS Code after creating the environment.
2. Press `Ctrl+Shift+P`.
3. Run **Python: Select Interpreter**.
4. Choose **acc-coding**.

### A notebook asks for a kernel

Click **Select Kernel** and choose the `acc-coding` Python environment. Also confirm that the Microsoft **Python** and **Jupyter** extensions are installed.

### A package is missing

Open Anaconda Prompt and run:

```bat
conda activate acc-coding
python -m pip install jupyterlab pandas openpyxl plotly requests
```

### The `cd` command cannot find the folder

Open the course folder in File Explorer, click the address bar, and copy its full path. In Anaconda Prompt, type `cd`, followed by a space and the path in quotation marks:

```bat
cd "C:\full\path\to\00_python_fundamentals"
```
