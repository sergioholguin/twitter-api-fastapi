
# Libraries
import json


# Function
def write_notification(email: str, message: str):
    with open("email.json", "r+", encoding="utf-8") as f:
        content = json.loads(f.read())

        if email not in content:
            content[email] = []

        content[email].append(message)

        # Overwrite
        f.seek(0)
        f.write(json.dumps(content))
        f.truncate()
