import time
import json
import hl7
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# --- CONFIGURATION ---
ADT_PATH = Path(r"C:\mirth_output\adt")
ORU_PATH = Path(r"C:\mirth_output\oru")
OUTPUT_PATH = Path(r"C:\hl7-demo-project\json_output")

# Create output folder if it doesn’t exist
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

def hl7_to_json(file_path):
    """Parse HL7 file and return JSON structure."""
    with open(file_path, 'r') as f:
        data = f.read()
    try:
        message = hl7.parse(data)
        msg_dict = {}
        for segment in message:
            seg_name = segment[0][0]
            msg_dict.setdefault(seg_name, [])
            fields = [str(field) for field in segment[1:]]
            msg_dict[seg_name].append(fields)
        return json.dumps(msg_dict, indent=4)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

class HL7Handler(FileSystemEventHandler):
    """Watches for new HL7 files and converts them to JSON."""

    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".hl7"):
            return

        hl7_file = Path(event.src_path)
        print(f"New HL7 file detected: {hl7_file.name}")

        json_data = hl7_to_json(hl7_file)
        if json_data:
            output_file = OUTPUT_PATH / f"{hl7_file.stem}.json"
            with open(output_file, "w") as f:
                f.write(json_data)
            print(f"Converted {hl7_file.name} → {output_file.name}")

def start_watcher():
    """Start monitoring both ADT and ORU directories."""
    event_handler = HL7Handler()
    observer = Observer()
    observer.schedule(event_handler, str(ADT_PATH), recursive=False)
    observer.schedule(event_handler, str(ORU_PATH), recursive=False)
    observer.start()
    print("Watching for new HL7 files... (Press Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watcher()
