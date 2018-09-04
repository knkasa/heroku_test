from flask import Flask, render_template

# specify image folder if loading image
app = Flask(__name__, static_url_path="/image", static_folder="image")


@app.route("/")
def hello():
	return  render_template('home.html')
	

@app.route("/about")
def about():
    return  render_template('about.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	#app.run(port=33507)
	#app.run(port=5432)
	
	