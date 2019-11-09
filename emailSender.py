import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("sumukhbhandarkar", "Nandita@1008")
server.sendmail(
  "steve@apple.com" 
  ["sidharth.kanwaria759@gmail.com"],
  "this message is from python")
server.quit()
