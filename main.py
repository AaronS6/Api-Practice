import requests

API_KEY = ""

headers = {
    "X-Api-Key":API_KEY
}

print("LETS HELP YOU DECIDE WHICH DOG TO ADOPT FOR YOUR FAMILY!! :)")
dogbreed = input("Enter the breed of your first dog choice: ")
dogbreed2 = input("Enter the breed of the second dog: ")

#DOG BREED 1#


url = "https://api.api-ninjas.com/v1/dogs?name=" + dogbreed
result = requests.get(url,headers=headers)
resultList =result.json()
resultDict = resultList[0]
result1 = resultDict["good_with_children"]



#DOG BREED 2#


url2 = "https://api.api-ninjas.com/v1/dogs?name=" + dogbreed2
result = requests.get(url2,headers=headers)
resultList =result.json()
resultDict = resultList[0]
result2 = resultDict["good_with_children"]

if result1 > result2:
    print(dogbreed, "is a better choice for your family!")
elif result2 > 1:
    print(dogbreed2,"is better choice for your family!")
else:
    print("both",dogbreed,"and",dogbreed2,"are equally as good with children")
