from datetime import datetime

def generate_log(log_data):
    """
    Generate a log file with today's date in the filename.
    - Validates that log_data is a list, otherwise raises ValueError.
    - Creates a file named log_YYYYMMDD.txt.
    - Writes each entry from the list into the file.
    - Handles empty lists by creating a valid empty file.
    - Prints a confirmation message including the filename.
    """

    # STEP 1: Validate input
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    # STEP 2: Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write log entries to file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    # Example usage
    log_entries = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_entries)
