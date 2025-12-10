from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host="db",        # 'db' is the name of our database container
            database="postgres",
            user="postgres",
            password="example"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"✅ Connected to PostgreSQL!<br>Version: {version}"
    except Exception as e:
        return f"❌ Could not connect to DB.<br>Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

