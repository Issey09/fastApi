from typing import Annotated

from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.responses import HTMLResponse

app = FastAPI()





@app.post("/files/")
async def create_upload_files(files:  UploadFile):
    contents = await files.read()
    return {"file": [contents]}


@app.get("/")
async def main():
    content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>zxc</title>
    <style>
        body {
            background-color: rgb(255, 255, 255);
        }
        header {
            background-color: rgb(207, 207, 207);
            text-align: center;
        }
        ul {
            margin: 0;
            list-style: none;
            padding: 20px;
        }
        a {
            font-size: 20px;
            padding: 200px;
            text-decoration: none;
            color: #ffffff;
        }
        a:hover {
            color: black;
        }
        li {
            display: inline;
        }
    </style>
</head>
<body>
    <div class="top-container">
        <header>
            <ul>
                <li><a href="/">Main</a></li>
                <li><a href="#">About</a></li>
                <li><a href="/login/">Login</a></li>                    
            </ul>
        </header>
    </div>
    <h1>Yuu! Whats up bro!</h1>
</body>
</html>

"""
    return HTMLResponse(content=content)

@app.get("/login")
async def main():
    content2 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href='https://fonts.googleapis.com/css?family=Courier Prime' rel='stylesheet'>
    <style>
        body {
            background-color: rgb(255, 255, 255);
        }
        header {
            background-color: rgb(207, 207, 207);
            text-align: center;
        }
        ul {
            margin: 0;
            list-style: none;
            padding: 20px;
        }
        a {
            font-size: 20px;
            padding: 200px;
            text-decoration: none;
            color: #ffffff;
            font-family: 'Courier Prime';
        }
        a:hover {
            color: black;
        }
        li {
            display: inline;
        }

        .login-container {
            text-align: center;
            margin: 0;
            padding: 100px;
        }

        .other-container {
            background-color: rgb(207, 207, 207);
            border-radius: 20px;
            height: 300px;
        }

        input {
            font-size: 25px;
            margin: 20px;
            border-radius: 15px;
        }

        input::placeholder {
            text-align: center;
            font-family: 'Courier Prime';
        }

        input::value {
            font-family: 'Courier Prime';
        }
    </style>
</head>
<body>
    <div class="top-container">
        <header>
            <ul>
                <li><a href="/">Main</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Login</a></li>                    
            </ul>
        </header>
    </div>
    <div class="login-container">
        <div class="other-container">
            <form action="/uploadfile/" action="/process-form"  method="post">
            <input type="text" placeholder="login" name='login'>
            <input type="password" placeholder="password" name='password'>
            <p><input type="submit" name="Submit" value="Послать" ></p>
            </form>
        </div>
    </div>
</body>
</html>

    """
    return HTMLResponse(content=content2)

@app.post("/uploadfile/")
async def save_cookie(login: str = Form(...), password: str = Form(...)):
    return {'login': login , 'password': password}
