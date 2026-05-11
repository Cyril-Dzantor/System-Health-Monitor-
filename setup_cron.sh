#!/bin/bash 

PROJECT_DIR="/mnt/d/Projects/System Health Monitor"
SCRIPT_PATH="$PROJECT_DIR/monitor.py"

PYTHON_INTERPRETER="$PROJECT_DIR/venv/bin/python"



#!/bin/bash 

PROJECT_DIR="/mnt/d/Projects/System Health Monitor"
SCRIPT_PATH="$PROJECT_DIR/monitor.py"

PYTHON_INTERPRETER="$PROJECT_DIR/venv/bin/python"



CRON_JOB="*/5 * * * * cd "$PROJECT_DIR" && "$PYTHON_INTERPRETER" "$SCRIPT_PATH" 

echo "$CRON_JOB" 