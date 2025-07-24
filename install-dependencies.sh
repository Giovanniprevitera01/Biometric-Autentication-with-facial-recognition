#!/bin/bash

# Install Python dependencies
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

deactivate

# Install frontend dependencies
cd ../frontend/face-recognition-dashboard
npm install

cd ../../
echo "Installazione completata con successo."

