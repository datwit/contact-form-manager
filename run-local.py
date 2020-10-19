from application import create_app

if __name__ == '__main__':
    app = create_app('config.LocalConfig')
    app.run(host='0.0.0.0')
