from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template ("index.html")

@app.route("/projects")
def projects():
  return render_template ('projects.html')

@app.route("/work")
def work():
  return render_template ('work.html')

@app.route("/education")
def education():
  return render_template ('education.html')

@app.route("/resume")
def resume():
  return render_template ('file:///Users/danielfritsch/Desktop/Daniel_Fritsch_Resume.pdf')

@app.route("/contact")
def contact():
  return render_template ('contact.html')

if __name__ == "__main__":
  app.run()


