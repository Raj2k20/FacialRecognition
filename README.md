We first need to activate the virtual environment named myenv
For that we need to go to the folder FACE_RECOGNITION and open the folder in terminal.
After that,run the command:
$ source ./myenv/bin/activate (for linux)


After that,run the file AddEmployee.py using the command:
$ python3 AddEmployee.py

Enter the details of the employee,and then take 5 pictures of the employee(that you want to add to the database) 
using the camera of your device.
Press key "s" for taking the picture.
Press key "q" to exit the window.



After storing the details,run the file Recognition.py using the command:
$ python3 Recognition.py
A window appears,in which it recognizes the person whose data is already stored before.
Press key "q" to exit the window.