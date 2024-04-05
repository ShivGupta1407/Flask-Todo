from app import app

if __name__ == "__main__":
    app.run(debug=True)
else:
    # This block is executed when running under a WSGI server like Gunicorn
    # Use Gunicorn to serve the Flask application
    from gunicorn.app.wsgiapp import WSGIApplication
    application = WSGIApplication()
    application.run()
