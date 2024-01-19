from pkg import app

if __name__ == '__main__':
    # app.config['Admin_email']='test@corona.com'
    app.config.from_pyfile('config.py')
    app.run(debug=True)