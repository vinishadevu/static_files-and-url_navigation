from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/static_files')
def static_files():
    return render_template('static_files.html')
@FAI.route('/newdata')
def new():
    return render_template('new.html')
   

if __name__=='__main__':
    FAI.run(debug=True)