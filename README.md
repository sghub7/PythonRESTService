# Run REST Flask App

cd PythonRESTService\src

set FLASK_APP=app.py

fask run

#Run Service Sidecar
python Service.py

# REST Client 
python client.py

