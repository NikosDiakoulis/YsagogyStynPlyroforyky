import datetime
import time
from calendar import monthrange

def getDate(): #Συνάρτηση εισόδου ημερομηνίας από τον χρήστη και ελέγχου για την μορφή της.
    isValid = True
    while isValid:
        userInput = input("Πληκτρολογήστε μία ημερομηνία στη μορφή ΗΗ/ΜΜ/ΕΕΕΕ: ")
        try:
            year, month, day = map(int, userInput.split('/'))
            userDate = datetime.datetime(day, month, year)
            isValid = False
        except:
            print("Λάθος μορφή ημερομηνίας\n")
    return userDate

userDate = getDate() #Δοσμένη ημερομηνία.
currentDate = datetime.datetime.now() #Τωρινή ημερομηνία.

if userDate > currentDate:
    currentDate = datetime.datetime.now() #Τωρινή ημερομηνία.
    dif = userDate - currentDate #Διαφορά μεταξύ της δοσμένης ημερομηνίας και της τωρινής.
    s = dif.seconds #Η διαφορά σε δευτερόλεπτα.
    hours = s // 3600 #Ώρες.
    s = s - (hours * 3600) #Υπόλοιπο δευτερολέπτων.
    minutes = s // 60 #Λεπτά.
    seconds = s - (minutes * 60) #Δευτερόλεπτα.
    print("Η ημερομηνία αυτή απέχει {} μέρα(εs) {} ώρα(ες) {} λεπτό(ά) {} δευτερόλεπτο(α).".format(dif.days, hours, minutes, seconds), end='\r')
    #Εμφάνιση πόσες ημέρες/ώρες/λεπτά/δευτερόλεπτα απέχει η δοσμένη ημερομηνία από την τρέχουσα ημερομηνία του υπολογιστή.

weekday, monthdays = monthrange(userDate.year, userDate.month)
#Από την monthrange θέλω μόνος της μέρες του μήνα κι όχι την θέση της μέρας μέσα στη βδομάδα.

print("\nΟ μήνας αυτής της ημερομηνίας έχει", monthdays, "ημέρες.")
#Εμφάνιση των ημερών του μήνα της δοσμένης ημερομηνίας.