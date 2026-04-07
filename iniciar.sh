#!/bin/bash
cd ~/arkhe-finance-api
source venv/bin/activate
xdg-open ~/arkhe-finance-frontend/index.html
python -m uvicorn main:app
