import uvicorn
import subprocess

def run_fastapi():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


def run_streamlit():
    command = ["streamlit", "run", "app.py"]
    process = subprocess.Popen(command)

if __name__ == "__main__":
    # اجرای سرور FastAPI و Streamlit به صورت همزمان
    process_fastapi = subprocess.Popen(["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"])
    run_streamlit()
    process_fastapi.wait()
