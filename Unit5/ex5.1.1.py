def mystery(index):
     print("z" * len(index))

mystery(3)

func = mystery
func("python")


# A: המשתנה index הוא פרמטר של הפונקציה mystery. -- correct

# B: המשתנה index הוא ארגומנט שמועבר לפונקציה mystery. -- wrong

# C: הערך 3 הוא פרמטר שמועבר לפונקציה func. -- correct

# D: הערך 3 הוא ארגומנט שמועבר לפונקציה func. -- wrong

# mystery :E ו-func מצביעות לאותו מקום בזיכרון המחשב. -- correct

# F: הפלט מהרצת קטע קוד מספר 2 (לאחר קטע קוד מספר 1) הוא zzz. -- wrong

# G: הפלט מהרצת קטע קוד מספר 3 (לאחר קטע קוד מספר 1) הוא zzzzzz. -- correct

# H: הקריאה לפונקציה mystery מתבצעת בקטע קוד מספר 2. -- correct

# I: הקריאה לפונקציה mystery מתבצעת בשורה מספר 1 בקטע קוד מספר 1. -- wrong

# J: הקריאה לפונקציה mystery מתבצעת בשורות מספר 2-1 בקטע קוד מספר 1. -- wrong
