@echo off
call venv\Scripts\activate
uvicorn backend.app:app --reload --port 8080
