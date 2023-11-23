#!/bin/bash
python app/save_openapi.py
speakeasy generate sdk --schema openapi.yaml --lang python --out ./sdk