from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import csv
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from CSV into a dictionary
marks_data = {}
with open("marks.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:  # avoid empty lines
            name, mark = row
            marks_data[name.strip()] = int(mark.strip())

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
