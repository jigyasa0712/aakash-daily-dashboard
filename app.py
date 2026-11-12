"""
Aakash Daily — Streamlit Cloud Entrypoint Wrapper
Permits 1-click deployment with either 'AakashDaily.py' or 'app.py' as the main entrypoint.
"""
import runpy
import os

if __name__ == "__main__":
    target = os.path.join(os.path.dirname(__file__), "AakashDaily.py")
    runpy.run_path(target, run_name="__main__")
