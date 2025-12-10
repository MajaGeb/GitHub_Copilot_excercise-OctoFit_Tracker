OctoFit Tracker — Backend Setup

1. Create a Python virtual environment:

```bash
python3 -m venv octofit-tracker/backend/venv
```

2. Activate the virtual environment and install requirements:

```bash
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

Notes:
- Use Django's ORM for database operations.
- Check for `mongod` with `ps aux | grep mongod` if using MongoDB.
- Follow project `.github/instructions` for exact package versions.
