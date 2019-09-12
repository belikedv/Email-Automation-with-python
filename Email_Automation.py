import pandas as pd 					#IS used to read excel or any other files
import smtplib							# used to connect server
import imghdr   						#It is used to determine the type of image 
from email.message import EmailMessage	#To send email in proper format their is already function ad EmailMeaage

df = pd.read_excel('Emails.xlsx')
emails = df['Emails'].values


message = EmailMessage()				
message['Subject'] = "Testing of automation"
message['From'] = 'yoursenderemail@gmail.com'
message['To'] = emails
message.set_content('Hey this is working..... Pdf and images are attched')


#You can add img/pdf or other set of files   OR  just html, You cant use both at the time

#To add image in attachment
img = ['AB.jpeg','Ab1.jpg','AB@.jpg']

for file in img:
	with open(file, 'rb') as img:
		file_name = img.name
		file_data = img.read()
		file_type = imghdr.what(img.name)

	message.add_attachment(file_data, maintype = 'image', filename= file_name, subtype='file_type')


#To add pdf in attachment
pdfs = ['the-trial.pdf']
for pdf in pdfs:
	with open(pdf, 'rb') as pdff:
		file_name = pdff.name
		file_data = pdff.read()

	message.add_attachment(file_data, maintype = 'application', filename= file_name, subtype='octet-strem')
	



#To add html section in attachment
message.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
<h2 style='color:green;'>Hey this is also working </h2>
</body>
</html>				
""", subtype='html')				#Triple qoute because this indicates that content is multi-line string



#connection to server and sending the email
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("yoursenderemail@gmail.com", 'Passwordofsender')
print("Emails are been send. Wait")

server.send_message(message)
server.quit()
print('Server Quitted. No worries')