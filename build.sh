#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
 