from pathlib import Path
import uuid
import subprocess
import datetime


def refresh():
    subprocess.call(["sh", "./refresh.sh"])


def main():
    reporting_back()
    refresh()


def reporting_back():
    current_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    current_time = current_time.replace(":", "_")
    filename = f"hello_from_python_{current_time}"
    documents = Path("/mnt/us/documents/")
    path = documents / filename
    with open(path, "w") as f:
        f.write("Reporting back")


if __name__ == "__main__":
    main()
