import psutil
from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or memory_percent > 80:
        Message = "High CPU or Memory usage detected.... Please Scale up"
        
    return render_template("index.html",cpu_percent=cpu_percent,memory_percent=memory_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

