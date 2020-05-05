
## Running locally

To run locally, you need to use gunicorn with the ``flask_socket`` worker:

    $ gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app
    
    or
    
    # gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app--access-logfile '-'
# Cloud-Computing-proj-2
# CloudComputing_CSE546_ASU
