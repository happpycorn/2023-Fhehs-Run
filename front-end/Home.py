def hello_http(request):
  html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #ffffff;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            form {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 200px;
                width: 100%;
            }

            label {
                display: block;
                margin-bottom: 8px;
            }

            select, input {
                width: 100%;
                padding: 8px;
                margin-bottom: 0px;
                box-sizing: border-box;
            }

            input[type="submit"] {
                background-color: #B38540;
                color: #fff;
                cursor: pointer;
                border: none;
                outline: none;
                border-radius: 2px;
            }
        </style>
    </head>
    <body>
        <form action="https://asia-east1-score-search-404211.cloudfunctions.net/loading" method="get" target="_self">
            <label for="gradename">選擇年級：</label>
            <select id="gradename" name="gradename">
                <option value="0">國三</option>
                <option value="1">國二</option>
                <option value="2">國一</option>
                <option value="3">高三</option>
                <option value="4">高一</option>
                <option value="5">老師</option>
            </select>
            <br></br>
            <label for="number">號碼：</label>
            <input type="text" id="number" name="number">
            <br></br>
            <input type="submit" value="提交">
        </form>
    </body>
    </html>
  """
  return html
