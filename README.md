# OrangeHRM UI Test Automation Project

This project contains UI test automation scripts for the OrangeHRM web application using Playwright with Python.

## Local Setup

1. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install browser binaries:
```bash
python -m playwright install
```

## GCP VM Setup

1. Create a new VM instance on GCP:
   - Machine type: e2-medium (2 vCPU, 4 GB memory) or higher
   - Boot disk: Ubuntu 20.04 LTS
   - Allow HTTP/HTTPS traffic

2. SSH into your VM instance:
```bash
gcloud compute ssh YOUR_INSTANCE_NAME --zone=YOUR_ZONE
```

3. Clone the repository:
```bash
git clone <repository-url>
cd windsurf-project
```

4. Make the setup script executable and run it:
```bash
chmod +x setup_vm.sh
./setup_vm.sh
```

## Running Tests

### Local Machine
- Run all tests:
```bash
pytest
```

- Run tests with visible browser:
```bash
pytest --headed
```

### GCP VM (Headless mode)
```bash
pytest
```

Note: On GCP VM, tests will always run in headless mode as there's no display server.

## Project Structure

- `/tests`: Contains test files
- `/pages`: Page object model classes
- `/utils`: Utility functions
- `conftest.py`: Pytest configuration
- `requirements.txt`: Python dependencies
- `setup_vm.sh`: VM setup script
