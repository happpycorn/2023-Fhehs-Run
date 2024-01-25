import datetime

def clock(request):
    html_content = """
    <!doctype html>
    <html>
    <head>
        <title>時鐘</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
            }
            .clock {
                font-size: 48px;
                margin-top: 50px;
            }
        </style>
        <script>
            function updateClock() {
                var now = new Date();
                var hours = now.getHours().toString().padStart(2, '0');
                var minutes = now.getMinutes().toString().padStart(2, '0');
                var seconds = now.getSeconds().toString().padStart(2, '0');
                var timeString = hours + ":" + minutes + ":" + seconds;
                document.getElementById('clock').textContent = 'Current time: ' + timeString;
            }

            setInterval(updateClock, 1000); // 每秒更新一次时钟
        </script>
    </head>
    <body>
        <div class="clock" id="clock"></div>
    </body>
    </html>
    """
    return html_content, 200, {'Content-Type': 'text/html; charset=utf-8'}
