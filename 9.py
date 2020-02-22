num = float(input("Enter a number: ")) #Είσοδος αριθμού.
num = num * 3 + 1 #Τριπλασιασμός και άθροισμα με 1.
sum = 0
while num > 0: #Άθροισμα των ψηφίων του.
    d = num % 10
    num = num // 10
    sum += d
if sum <= 9: #Έλεγχος αν το άθροισμα των ψηφίων του είναι μονοψήφιος αριθμός.
    print("Result: ", sum) #Εμφάνιση του αποτελέσματος.
else:
    while sum > 9: #Αν δεν είναι μονοψήφιος η διαδικασία επαναλαμβάνεται μέχρι να γίνει.
        sum = sum * 3 + 1
        d = sum % 10
        sum = sum // 10
        sum += d
    print("Result: ", sum) #Εμφάνιση του αποτελέσματος.
input('Press ENTER to exit')
