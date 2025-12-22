# core/parser.py

def read_log(file_path):
    """
    Reads a log file and returns all lines.
    """
    with open(file_path, "r") as f:
        return f.readlines()


def parse_line(line):
    """
    Parses a single authentication log line.
    Returns a dictionary with status and IP, or None if not relevant.
    """

    if "Failed password" in line:
        try:
            ip = line.split("from ")[1].split(" ")[0]
            return {
                "status": "failed",
                "ip": ip
            }
        except IndexError:
            return None

    elif "Accepted password" in line:
        try:
            ip = line.split("from ")[1].split(" ")[0]
            return {
                "status": "success",
                "ip": ip
            }
        except IndexError:
            return None

    return None


def parse_log(file_path):
    """
    Parses an entire log file and returns a list of events.
    """
    events = []
    lines = read_log(file_path)

    for line in lines:
        event = parse_line(line)
        if event:
            events.append(event)

    return events


# ---------------- TEST BLOCK ----------------
# This is only for local testing.
# You can keep it or remove it later.
if __name__ == "__main__":
    lines = read_log("sample_logs/auth.log")
    print("RAW LINES:")
    for line in lines:
        print(repr(line))

    events = parse_log("sample_logs/auth.log")
    print("\nParsed events:")
    for event in events:
        print(event)

