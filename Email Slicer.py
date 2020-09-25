useremail = input("What's your email?: ")

#slicing out the username
username = useremail[:useremail.index("@")]
domain = useremail[useremail.index("@") + 1 :]


output = "Your username is {} and your domain name is {}".format(username, domain)
print(output)


