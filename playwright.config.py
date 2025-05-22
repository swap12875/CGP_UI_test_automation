import os
from typing import Dict

def is_running_on_vm() -> bool:
    # Check if running on a cloud VM (this is a simple check, you might want to make it more robust)
    return os.path.exists('/etc/cloud/cloud.cfg')

def pytest_configure(config):
    config.option.browser = ['webkit']  # Use only webkit by default

def browser_context_args(browser_name: str) -> Dict:
    return {
        "viewport": {
            "width": 1280,
            "height": 720
        },
        "record_video_dir": "test-results/videos",
        "record_har_path": f"test-results/har/{browser_name}.har",
        "base_url": "https://opensource-demo.orangehrmlive.com",
        "headless": is_running_on_vm()  # Run headless on VM, non-headless locally
    }
