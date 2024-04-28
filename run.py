### Flask 웹 서버 코드 작성

아래는 Flask 웹 서버와 MySQL을 연동하는 기본적인 코드 예제입니다. 이 코드는 사용자가 웹 페이지에서 데이터를 입력하면, 해당 데이터를 MySQL 데이터베이스에 저장하는 간단한 어플리케이션입니다.

```python
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL 연결 설정
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 폼에서 데이터 가져오기
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        # 데이터베이스에 데이터 삽입
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return '성공적으로 등록되었습니다!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```
