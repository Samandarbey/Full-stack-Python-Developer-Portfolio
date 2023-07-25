import urllib.request as urllib

# input_url = input("Enter the url of the site that you are gonna check: \n ")

def main(url):
    print("Checking connectivity: \n")
    
    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("The response code was:",response.getcode())
    
    
print("This is a site connectivity checker program ")
input_url = input("Input the url of the site that you wanna check: ")
 
main(input_url)
    