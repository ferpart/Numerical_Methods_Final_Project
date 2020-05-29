# Steps to use the application.

## If you have windows follow this steps:

**1st.** The first thing you have to do is to download python (If you already have it, you can skip this part and go to the 2nd point):

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/python.png" width="70" height="70">

[Python](https://www.python.org/downloads/)

Click on the button that says: **"Download Python 3.8.3"** and your download will start.

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/downloadpython.jpeg">

**2nd.** Now, once that is downloaded you have to launch the installer and you will see a pop up.

**3rd.** Now in the main window of the installer you have click the checkbox that says **"Add Python 3.5 to PATH"** and then click **"Install Now"**.

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/popuppython.jpeg">

**4rd.** Once is finish the installation you can go to the Command prompt of your computer.
	
 #### - **How to enter to the "command prompt":**
 ```
 - Press the "windows" key + the key "s".
 - Now that pop up a menu, just write the word "command prompt".
 - And select the application.
 - Congratulations! You are now in the command prompt window.
  ```
**5th.** Now in the command prompt you have to write this command:
 > python --version

**6th.** This message have to appear after the command:
> Python (the number of version)

**LIKE THIS**

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/versionpython1.jpeg">

- If appears, **CONGRATULIONS!** you are one step closer to use the application.
	- Now still in the "command prompt" write the next command:
		> pip install numpy
	
	**wait until the message: "Successfully installed numpy-no.version" appears**
	
	- If it appears an **ERROR message**, please use the next command:
		> pip install --user numpy
		
	**wait until the message: "Successfully installed numpy-no.version" appears**
	
	- Next, if it appears a warning message saying that you are using and **old pip version and is a new version available**, please introduce this command:
		> python -m pip install --upgrade pip
		
	**wait until the message: "Successfully installed pip-no.version" appears**
	
	- If appears an **ERROR message**, please introduce this command:
		> python -m pip install --user --upgrade pip
		
	**wait until the message: "Successfully installed pip-no.version" appears**
	
	- Now put the command:
		> pip list
		
	- **You have to see a list where appears the library numpy listed.**
	
	<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/piplist.jpeg">
	
	- If it appears you are now ready to use the application. **If not** please return to the step **6th.**
		
**7th.** Please download all the github in a **ZIP**, once you downloaded please **unzip** the file and put it your computer desktop.

**8th.** Now, **still in the command prompt**, please write the next command step by step:
- **step one:** write 
	> cd desktop 
	
and press enter.

- **step two:** you have to see something like this in the command prompt: 
	> C:\Users\username\desktop

- **step three:** Now, just put 
	> main.py 
	
<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/directionpython.jpeg">
	
and then press the key enter.
		
**Note: To know how to use the application, please go to the bottom of this manual. To the section "Now let´s start with the application"**.

## If you have MAC follow this steps:

**1st.** The first thing you have to do is to download python (If you already have it, you can skip this part and go to the 2nd point):

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/python.png" width="70" height="70">

[Python](https://www.python.org/downloads/)

Click on the button that says: **"Download Python 3.8.3"** and your download will start.

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/downloadpython.jpeg">

**2nd.** Now, once that is downloaded you have browse to the download folders and launch the installer and you will see a pop up.

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/installpythonmac.jpeg">

**3rd.** Accept all the terms & conditions and press the button "continue" till you see the button "close".

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/finishpythonmac.jpeg">

**4rd.** Open your terminal to check if python is installed correctly.

- In the terminal you have to write the word

	> python3 --version (all lowercase, without quotes intothe terminal) 

and press **enter**.
		
**5th.** This message have to appear:
	> Python (the number of version) 

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/terminalmac.jpeg">
	
- If appears, **CONGRATULATIONS!** you are one step closer to use the application.
	- Now still in the terminal write the next command:
		> pip install numpy
		
	**wait until the message: "Successfully installed numpy-no.version" appears.**
	
	- If not, please try the command:
		> sudo pip install numpy
		
	**wait until the message: "Successfully installed numpy-no.version" appears.**
	
- If it appears you are now **ready** to use the application. **If not please** return to the step 5th.
	- If still does not work, please return to the **1st step.**
	
**6th.** Please download all the github in a **ZIP**, once you downloaded please **unzip** the file and put it your computer desktop.

**7th.** Now, **still in terminal**, please follow the next instructions step by step:
- **step one:** First put the command 
	> cd 
	
And then drag the folder to the terminal and press the enter key.

- **step two:** Now, just put 
	> python main.py
	
and then press again the key enter.
		
**Note: To know how to use the application, please go to the bottom of this manual. To the section "Now let´s start with the application"**

## If you have Linux follow this steps:

**1st.** In Linux the python language most be installed by default.

**2nd.** Open up a terminal window and then type:

	> python3 --version

**3rd.** It would appear a messaage like this:

	> Python (the number of version)
	
<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/linuxpython.jpeg">
	
- If appears, **CONGRATULIONS!** you are one step closer to use the application.

- **If not**, please put the next command:
	> sudo apt-get install python3

- Now still in the terminal window in case you have numpy installed please still write the next command to **upgrade or intall** numpy´s library:
	> $ pip3 install numpy

- Now, one more step, let´s gonna install the **tkinter library**, still in the terminal write this command:
	> sudo apt install python3-tk
	
- Finally **you are now ready to use the application**. **If still there´s a problem** please return to the beginning of this part after 3rd step.

**Now you are ready to use the program.**

**4rd.** Once you all the github in a **ZIP** and **unzip** the application in the terminal put the next command:

	> python3 "main.py" 

and then press the key enter.

**Note: To know how to use the application, please go to the bottom of this manual. To the section "Now let´s start with the application"**.


## Now let´s start with the application

- Once you open the program, you are going to see something like this.

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/main.jpeg">

**Now follow this instructions:**

- **1st** Select the option **Load**.

- It will open a window where you have to select a csv file to be solve:

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/opcionarchivo.jpeg">

- Example of the ecuations that are in the file

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/problem.jpeg">

- **2nd** Now, once you upload the file press the option **Solve**.

- **3rd** You will see that the botton **Save** it will available and would have two options to save the file as you want. Now please press the **Save** button and save your file with the name you like.

- Once you save it and open the file. It will look like this the solution:

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/solution.jpeg">

**Note: the program is designed to only use csv files.**

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/csv.jpeg">

### How to create an csv file.

- Please open the windows office application **Excel**.

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/excel.jpeg">

- Now, once you put the values like in this example, **please don´t forget to put the same values that are in the row 1 of the example in your file**

<img src="https://github.com/ferpart/Numerical_Methods_Final_Project/blob/media/Images_MD/problem.jpeg">

- Now, go to the spreadsheet, click in **file** and then click **Save As**. Choose where you want to save your file and then select **CSV** from the **Save as type** drop-down menu. And just click **Save**.

**Congratulations!** you just created a **CSV file**. 
