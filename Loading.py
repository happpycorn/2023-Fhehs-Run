def hello_http(request):
    gradename = request.args.get('gradename')
    number = request.args.get('number')
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>正在重定向...</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #ffffff;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            p {{
                font-size: 18px;
                color: #333;
            }}
        </style>
        <script type="text/javascript">
            window.onload = function() {{
                setTimeout(function() {{
                    window.location.href = "https://asia-east1-score-search-404211.cloudfunctions.net/score-search?gradename={gradename}&number={number}";
                }}, 1);
            }}
        </script>
    </head>
    <body>
        <p>搜尋中...</p>
    </body>
    </html>
    """
    return html
