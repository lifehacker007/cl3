# cl3
This Repository Contain Practicals of BE-Computer Subject CL3 of Pattern 2012
  Before all Type This in Terminal :- sudo apt-get update

------------------------------  For Booth Python Program ------------------------------------



Booths Multiplication requires bitstring


--------------------- Installing Bitstring -----------------
Type Following to install:-


sudo apt-get install python-setuptools

sudo easy_install pip

sudo pip install bitstring


------------------- How to Run ? - Running pgm ----------------

Terminal 1 :-  python server.py

Open Terminal 2 :- python client.py
 
Give 2 integer to client pgm ( *Terminal 2* ) and it will display's multiplication on server's ( *Terminal 1*)

Note :-The Booths multiplication done by client bcoz in client.py there is direct call to  booth.py  hence no need to directly run booth.py from terminal🤪


-------------------------- Odd Even + Plagiarism --------------------------------


Odd even , plagiarism Requires to install flask as a localhost


--------------------- Installing Flask ------------------

sudo apt-get install python-setuptools

sudo easy_install pip

sudo pip install Flask 

------------------ Conitinue to enable Virtual env -----------------

sudo apt-get install python-virtualenv

sudo apt-get install python-pip

mkdir flask-application

cd flask-application

virtualenv flask-env



------------------- Running pgm ----------------

Change Home directory to *flask-application*

 
cd flask-application


Next command is

source flask-env/bin/activate

Then install Flask by

pip install flask
Or
sudo pip install flask



Then change directory to  *home* by

cd ..

and type:- pip install flask

Make a folder namely *templates* in home directory.

Keep your (index.html ) file in that folder


Then simply run pgm  :-

*python filename.py*
It will display an ip address - 

127.0.0.1:5000 ...just right click and open the link.
Then it will display (index.html)
Insert the no for oddeven *OR* Enter two strings to check plagiarism. Hit the button.


Done.🤪
