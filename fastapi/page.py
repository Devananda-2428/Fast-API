import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


DATA_FILE = "data.json"


def read_json():
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
      
def write_json(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FastAPI Webpage</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        .button-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        button {
            width: 150px;
            height: 50px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #007BFF;
            color: white;
            transition: background-color 0.3s ease;
            margin-bottom: 10px;
        }
        button:hover {
            background-color: #0056b3;
        }
        p {
            font-size: 18px;
            margin-top: 20px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>FastAPI JSON Data Handling</h1>
    
    <div class="button-container">
        <button onclick="sendRequest('GET')">GET Request</button>
        <button onclick="sendRequest('POST')">POST Request</button>
        <button onclick="sendRequest('PUT')">PUT Request</button>
        <button onclick="sendRequest('DELETE')">DELETE Request</button>
    </div>

    <p id="response"></p>

    <script>
        function sendRequest(method) {
            let body = method === "GET" || method === "DELETE" ? null : JSON.stringify({ "message": "Updated by " + method });

            fetch('/api', {
                method: method,
                headers: { "Content-Type": "application/json" },
                body: body
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('response').innerText = "Response: " + JSON.stringify(data);
            })
            .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def serve_html():
    return html_content

@app.get("/api")
def get_data():
    data = read_json()
    return data

@app.post("/api")
def post_data():
    data = {"message": "Data added"}
    write_json(data)
    return data

@app.put("/api")
def put_data():
    data = {"message": "Data updated"}
    write_json(data)
    return data

@app.delete("/api")
def delete_data():
    data = {"message": "Data deleted"}
    write_json(data)
    return data
