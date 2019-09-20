from flask import Flask
app = Flask(__name__)

@app.route("/") # 函式的裝飾
def home():
    return "Hello Flask!"

@app.route("/test") #代表我們要處理的網站路徑
def test():
	return "This is Test"

if __name__ == "__main__": #如果以主程式執行
    app.run()