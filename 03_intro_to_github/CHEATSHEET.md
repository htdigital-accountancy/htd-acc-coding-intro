
# GitHub Cheat Sheet — Quick Reference
## 1. GitHub Web Interface — Browser Tasks

> These tasks are done in your browser at github.com. Everything else — branches, commits, file edits — is handled via Git commands in your IDE or terminal.

| Task | How To |
|------|--------|
| **Create a repository** | Go to your org page → Click **New** → Name it (lowercase, hyphens) → Add a description → Select **Private** → Check **Add a README** → Click **Create repository** |
| **View commits / history** | Open the repo → Click **Commits** (or the clock icon) → Browse the list of changes, who made them, and when |
| **Open a Pull Request** | Go to **Pull Requests** tab → Click **New pull request** → Select your branch → Add a title & description → Click **Create pull request** |
| **Review & merge a PR** | Open the PR → Review the changes → Click **Approve** → Click **Merge pull request** → Click **Confirm merge** |

---

## 2. Essential Git Commands (use in VSCode / terminal)

These are your primary tools for everyday Git work.

| Command | What It Does | Example |
|---------|-------------|---------|
| `git clone` | Download a copy of a repository to your computer | `git clone https://github.com/org/repo.git` |
| `git status` | Check which files have been changed | `git status` |
| `git add` | Stage files for the next commit (select what to include) | `git add vat_calculator.py` |
| `git commit` | Save a snapshot of staged changes with a message | `git commit -m "Add VAT calculation script"` |
| `git push` | Upload your commits to GitHub | `git push` |
| `git pull` | Download and apply the latest changes from GitHub | `git pull` |
| `git fetch` | Check for new changes on GitHub (downloads info but doesn't change your files) | `git fetch` |
| `git branch` | List all branches or create a new one | `git branch feature/tax-calc` |
| `git checkout` | Switch to a different branch | `git checkout feature/tax-calc` |
| `git merge` | Combine changes from one branch into another | `git merge feature/tax-calc` |
| `git log` | View the history of commits | `git log --oneline` |

### Upload Workflow (Local → GitHub)
Working Files → git add → Staging Area → git commit → Local Repo → git push → GitHub


### Download Workflow (GitHub → Local)
GitHub → git fetch (check what's new) or git pull (download & apply) → Local Repo → Working Files


---

## 3. Good Commit Messages

Write messages that describe **WHAT** changed and **WHY**.

| ✅ Good | ❌ Bad |
|---------|--------|
| `Add VAT calculation script for Q3 returns` | `update` |
| `Fix rounding error in expense report totals` | `stuff` |
| `Add client name validation to input form` | `fixed it` |
| `Update README with setup instructions` | `asdfgh` |

---

## 4. .gitignore Essentials

A `.gitignore` file tells Git which files to **skip** — never commit sensitive data!

| Entry | What It Ignores |
|-------|----------------|
| `.env` | Environment files containing passwords, API keys, credentials |
| `*.csv` | CSV data files (may contain client data) |
| `*.xlsx` | Excel files (may contain client data) |
| `__pycache__/` | Python cache files (auto-generated, not needed) |
| `.ipynb_checkpoints/` | Jupyter notebook checkpoints (auto-generated) |
| `data/` | Data folders (keep client/sensitive data out of repos) |

> ⚠️ **Security Reminder:** NEVER commit passwords, API keys, or client data to GitHub. If you accidentally do, the data remains in the Git history even after deletion. Use `.gitignore` to prevent this.

---

## 5. Key Terms Glossary

| Term | Definition |
|------|-----------|
| **Repository (Repo)** | A project folder on GitHub containing code, notebooks, and documentation |
| **Commit** | A saved snapshot of changes with a descriptive message |
| **Branch** | A parallel copy of the code for safe experimentation |
| **Pull Request (PR)** | A request to merge your branch into main — allows team review |
| **Main Branch** | The official, trusted, working version of the code — the "holy grail" |
| **Merge** | Combining changes from one branch into another |
| **Clone** | Downloading a full copy of a repository to your computer |
| **Fork** | Creating your own copy of someone else's repository |
| **Issue** | A task, bug report, or idea tracked within a repository |
| **README** | A documentation file (usually README.md) that describes the project |
| **.gitignore** | A file that tells Git which files to skip (e.g., sensitive data) |
| **Markdown** | A simple formatting language used for READMEs and documentation |

---

## Helpful Links

- 📖 [GitHub Docs](https://docs.github.com)
- 🖥️ [GitHub Desktop](https://desktop.github.com)
- ✍️ [Markdown Guide](https://www.markdownguide.org)