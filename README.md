# PasswordGenerator
Building a password generator python program. 

The program accepts user input, then generates a password and run it against a dictionary for non-overlap password.
Eventually it writes user details into a log, on third party server (hostname, socket, password)

Please be aware you have the following moudles already installed -

+ Should be already installed when you install python for the first time : **random,string,socket**
+ Manually install : **prettytable, PySimpleGUI**

You can install it with the command -

``` python -m pip install "SomePackage" ```

Please be aware to change the dictionary location in code **"PasswordGenerator.py" in line - 26**

and the **server ip address in line - 108**

Also notice to change the location it will create the log in code **"Server.py" in line 8** 
