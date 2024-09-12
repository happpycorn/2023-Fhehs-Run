# import
import requests

# constant
url = "https://script.google.com/macros/s/AKfycbwlDDXSn4oyUNEAmzAayWN9bljmOkOBPjerBc3Os1jDLN-GVjgxZlxgL9GUXvkDTg/exec"
grade = ['國三', '國二', '國一', '高三', '高一', '老師', '範本']

def main_loop(turn_back):

    # get
    if not turn_back.args:
        return "OK"

    gradename = int(turn_back.args.get('gradename'))

    # shite
    shite = grade[gradename]
    web = requests.get(f'{url}?name={shite}')
    
    # find
    have = False

    for i in range(0, len(web.json())):
        if web.json()[i][0] == turn_back.args.get('number'):
            number = web.json()[i][0]
            name = web.json()[i][1]
            score = web.json()[i][6]
            have = True
            break

    # html
    if have:
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

                form {{
                    background-color: #fff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 200px;
                    width: 100%;
                }}

                label {{
                    display: block;
                    margin-bottom: 6px;
                    color: #333;
                    text-align: left;
                    font-weight: bold;
                }}

                text {{
                    display: block;
                    margin-bottom: 10px;
                    color: #555;
                    text-align: left;
                }}

                input[type="submit"] {{
                    width: 100%;
                    background-color: #B38540;
                    color: #fff;
                    cursor: pointer;
                    border: none;
                    outline: none;
                    border-radius: 2px;
                    padding: 10px 20px;
                    font-size: 16px;
                }}
            </style>
        </head>
        <body>     
            <form action="https://asia-east1-score-search-404211.cloudfunctions.net/home-2" target="_self">
                <label>號碼</label>
                <text>{number}</text>
                <label>姓名</label>
                <text>{name}</text>
                <label>成績</label>
                <text>{score}</text>
                <br>
                <input type="submit" value="回上頁">
            </form>
        </body>
        </html>
        """
    else:
        html = """
        <!DOCTYPE html>
        <html lang="zh-Hant">
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
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 200px;
                    width: 100%;
                }

                label {
                    display: block;
                    margin-bottom: 8px;
                    color: #8B4513;
                    text-align: left;
                    font-weight: bold;
                }

                text {
                    display: block;
                    margin-bottom: 16px;
                    color: #555;
                    text-align: left;
                }

                input[type="submit"] {
                    width: 100%;
                    background-color: #B38540;
                    color: #fff;
                    cursor: pointer;
                    border: none;
                    outline: none;
                    border-radius: 2px;
                    padding: 10px 20px;
                    font-size: 16px;
                }
            </style>
        </head>
        <body>     
            <form action="https://asia-east1-score-search-404211.cloudfunctions.net/home-2" target="_self">
                <label>查無此人...</label>
                <text>請確認年級與號碼是否有誤</text>
                <input type="submit" value="回上頁">
            </form>
        </body>
        </html>
        """
    return html
