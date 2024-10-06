def extraPairShoes(leftShoe, rightShoe):
    if leftShoe > rightShoes:
        return "left"
    else:
        return"right"
def findShoeOrShoes(shoeLeft):
    if shoeLeft == 0:
        return " shoe"
    else:
        return " shoes"

leftShoes = int(input("Number of left shoes: "))
rightShoes = int(input("Number of right shoes: "))
minShoes = min(leftShoes,rightShoes)
maxShoes = max(leftShoes,rightShoes)
message = "There"
if minShoes > 1:
    message += " are " + str(minShoes) + " pairs and "
else:
    message += " is " +  str(minShoes) + " pair and "
shoesLeft = maxShoes - minShoes

if shoesLeft > 0 :
    message += str(shoesLeft) + " leftover " + str(extraPairShoes(leftShoes, rightShoes) + str(findShoeOrShoes(shoesLeft)))
else:
    message += "no leftover shoes."
print (message)
#print(message {minShoes} "and" {maxShoes-minShoes} "leftover shoes.")