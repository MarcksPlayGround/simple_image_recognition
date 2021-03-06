# simple_image_recognition

First option for installation:

Installation requirement:

1. python 3.6.7
2. numpy
3. tensorflow (latest)
4. Django version 2.1.4
5. RAM of at least 3gb. (or you could test with 2gb. When i tested this app on 1gb, the app was killed by the server because of high memory usage. )
<br /> <br /> 
Installation instruction:
<br /> 
1. Download repo from this Git.<br /> 
2. run python manage.py migrate<br /> 
3. python3 manage.py runserver<br /> 

<br /> 
<br /> <br /> 
Second Option for installation (using Docker):
<br /> 
Installation requirement:
<br /> 
1. Docker (www.docker.com)
2. RAM of at least 3gb. (or you could test with 2gb. When i tested this app on 1gb, the app was killed by the server because of high memory usage. )
<br /> 
Installation instruction:
<br /> 
1. Download Git repo<br /> 
2. navigate inside the "simple_image_recognition" folder<br /> 
3. run "docker build -t <name of image> ."  (for example:  "docker build -t testpython_image_rec ."  <br /> 
	note: don't forget the "."<br /> 
4. to run the image and logging in to its bash, run "docker run -it -p 8000:8000 <name of image> /bin/bash".  (for example: "docker run -it -p 8000:8000 testpython_image_rec /bin/bash") <br /> 
5.  You will be logged in inside your running container.  navigate to the $HOME directory and run "python manage.py migrate".<br /> 
6.  to run the server execute the command: python manage.py runserver 0.0.0.0:8000<br /> 
7.  On your Host compute, navigate your browser to "0.0.0.0:8000" to access the website<br /> 
<br /> 
Note:
1. It may take some time the first time you upload an image for image recognition because at first execution, the app will download the image "models" from the server.  The succeeding upload would be faster as the image model database is already downloaded.
<br /> <br /> 


2. To run the docker image on interactive mode, run the following command:<br /> 
	<br /> a. docker run -it -d -p 8000:8000 testpython_image_rec /bin/bash
	<br /> b.  docker container ls   (get the container id of your image)
 	<br /> c. docker exec -d  <container id> python manage.py runserver 0.0.0.0:8000   (example: docker exec -d  665fa5295f1f python manage.py runserver 0.0.0.0:8000)
	
