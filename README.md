# car_rental_mini_project
A fully functional CAR RENTAL SYSTEM deployed on a Linux based container using Docker, MySQL Connectivity and Python. 

## Setting Up the Environment
*Note that you can run the source code without Docker as well.*

The first step is to set up your Linux/Unix machine for the project to run. Requirements:
* Docker
* Git

Note: Other dependencies will be installed in the container itself.

### Docker
Update System Packages:
```bash
sudo apt update
sudo apt upgrade
```
Install Required Packages:
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
Add Docker's Official GPG Key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
Add Docker Repository:
```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
Update Packages:
```bash
sudo apt update
```
Install Docker Engine:
```bash
sudo apt install docker-ce docker-ce-cli containerd.io
```
Add Your User to the Docker Group (optional, allows running Docker without sudo):
```bash
sudo usermod -aG docker $USER
```
Log out and Log back in for the group changes to take effect.

Verify Docker Installation:
```bash
docker --version
```
This command should display the Docker version if it was installed successfully.

### Git
Update System Packages (if you haven't done it already):
```bash
sudo apt update
```
Install Git:
```bash
sudo apt install git
```
Verify Git Installation:
```bash
git --version
```
Set Git Configuration:
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
Clone this repository:
```bash
git clone repository_url
```
Replace "repository_url" with the URL of this repository.

From here you can set up the files in the required destination.

## Running the Application
The main file to run this python application is DBConnection.py
The other dependencies are:
> Database.py
> MenuControl.py
> PrintTools.py
> MainMenu.py
> AdminPortal.py
> CustomerPortal.py

* Before ruiing the sript. Make sure you have MySQL installed on you machine and have the MySQL library installed in Python environment.
* Also make sure to get the details of your 'username' and 'password' for the Database access
and change them in the DBConnection.py and Database.py files. Also update the global variable 'paas' in rest of the files to your 'password'.

DATABASE INFORMATION
If you are running the code for the application again and don't want to reset the Database then, in DBConnection.py, comment the following sinppet:
```python
Database.create_database()
Database.create_tables()
Database.populate_tables()
```
### Running using Docker
Now, this repository has a Dockerfile and requirements.txt files with the dependencies that
will be required to run the app in the container.

Build the Docker Image:
Open a terminal, navigate to your project directory (where the Dockerfile is located), and run the following command:
```bash
docker build -t your_image_name .
```
The image name can be car_rental_app

Run the Docker Container:
Use the following command to run the Docker container:
```bash
docker run -it your_image_name
```

**NOTE:** You might get an port error related to MySQL. So make sure that you port number 3306 is unoccupied. (Or change the port while initiatiation of the connection in DBConnection.py)

## Screenshots of the Working app

When the app launches, the first prompt will be to connect to you local database. Enter the correct password to proceed.
![Database Login](/Screenshots/1.png)

Upon successful connection, you'll be prompted to the Main Menu. From there, you can either login as an Admin or Continue as an Customer.
![Main Menu](/Screenshots/2.png)

If we select to Login as Admin, a password authentication will be needed 
(the password for which is initialized in Database.py in the admins table). 

![Admin Authentication](/Screenshots/3.png)

After Succesful Login, you'll have access to Admin Portal

![Admin Portal](/Screenshots/4.png)

Let's see the available list of cars for rent. So, we'll enter into the Garage.
![Garage Menu](/Screenshots/5.png)

From here, select the View Cars Option
![View Available Cars](/Screenshots/6.png)

Now, if a car is to be added to the existing pool, return back to the Garage Menu and from there select Add Car and fill the required details
![Add Car](/Screenshots/7.png)

Once, done the added car wi'll be reflected in the Database.
![Added Car](/Screenshots/8.png)

Now, let's rent a car. For this, return to the Main Menu and select Customer Portal:
![Customer Portal](/Screenshots/9.png)

From here, go to Rent Cars and enter the required details:
![Rent Cars](/Screenshots/10.png)

Upon making the selection, a recipt will be generated with your rental details. Confirm the order to proceed.
![Order Recipt](/Screenshots/11.png)

After every succesful order customers will be prompted to an information page that contains necessary details about the terms and conditions.
![Terms Cond](/Screenshots/12.png)

Now, if we view the cars from the Customer Portal, we'll see the status of the rented cars as 'RENTED' and they are no longer available.
![View After Rent](/Screenshots/13.png)

The Admin will have all the Details of the Currently Rented Cars. This can be checked using the Current Rentings option from the Admin Portal.
![Current Rentings](/Screenshots/14.png)

Let's add a few more rentals to see it's use better:
![Current Rentings More](/Screenshots/15.png)

Now, let's return a car. To do so, in the Customer Portal, select Return Cars. Enter the rent id to Return.
![Return](/Screenshots/16.png)

The final recipt (based on the actual number of days rented irrespective of booking) will be generated. The customer needs to accept the payment.
![Final Recipt](/Screenshots/17.png)

Now, after returning of cars by one of the users, it reflects in the Current Rentings Table
![Curr Rentings Updated](/Screenshots/18.png)

The succesfully returned cars and when the payment is done, are addedd to the Sales Table of the rental Company. This can be viewed from the Sales Table in the Admin Portal.
![Sales Table](/Screenshots/19.png)

When done, exit the portal. The data remains in the Databse.

![Bye Bye](/Screenshots/20.png)

*That's all about the entire walkthrough of this Mini Project*
