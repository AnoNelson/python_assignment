
---
## Assignment presentation

#### Group 3 MEMBERS
- GIRAMAHORO Sandrine: 223028220
- ISHIMWE Nelson: 223026666
- NKUNDIMANA Jean Claude: 214002796

### Purpose of the project 
The purpose of this project is to build a robust hospital management system that integrates with Authentication and Logging,
Distributed Data Processing and Kafka for asynchronous messaging


### Function
#### Admin
- Signup their account. Then Login (No approval Required).
- Can register/view/approve/reject/delete doctor (approve those doctor who applied for job in their hospital).
- Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
- Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge and other charge).
- Can view/book/approve Appointment (approve those appointments which is requested by patient).

#### Doctor
- Apply for job in hospital. Then Login (Approval required by hospital admin, Then only doctor can login).
- Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
- Can view their discharged(by admin) patient list.
- Can view their Appointments, booked by admin.
- Can delete their Appointment, when doctor attended their appointment.

#### Patient
- Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
- Can view assigned doctor's details like ( specialization, mobile, address).
- Can view their booked appointment status (pending/confirmed by admin).
- Can book appointments.(approval required by admin)
- Can view/download Invoice pdf (Only when that patient is discharged by admin).

---

## VIDEO LINK
- link: https://drive.google.com/file/d/1TZTWi5tZp3k-SkWjV6NyrmtYplrvC-yh/view?usp=sharing

## HOW TO RUN THIS PROJECT
- Install Python (Don't Forget to Tick Add to Path while installing Python)
- Install Kafka
- make sure you have hadoop installed, and you may edit setting.py to change the hadoop configuration
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf
pip install mysql-client
pip install confluent_kafka
pip install hdfs
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```