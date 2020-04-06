# references https://github.com/adwalvekar/PDFViewer
# https://www.reddit.com/r/flask/comments/3qywg2/af_best_way_to_display_a_pdf/
# https://www.youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
from flask import Flask,render_template,request,url_for
from signpdf import merge_multiple_files
import json
import os

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    path = "static/pdf/"
    a = os.listdir(path)
    a.remove(".DS_Store")
    text = json.dumps(sorted(a))
    return render_template("index.html", contents = text)

#the following part is added only to make html and css updated directly in
#brwoser, before adding this code, i change css and i see no effect in 127.0.0.1
# browser
#/////////////////////////////////////////////////////////////
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
#///////////////////////////////////////////////////////////////
if __name__=="__main__":
    app.run(host="localhost",port=5000,debug=True)
