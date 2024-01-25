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
              padding: 100px;
              border-radius: 10px;
              box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          }

          label {
              display: block;
              margin-bottom: 8px;
              color: #966F33;
              font-weight: bold;
          }
      </style>
      <title>表單美化</title>
  </head>
  <body>     
    <form>
        <label>功能尚未開放...</label>
    </form>
  </body>
  </html>
  """
  return html
