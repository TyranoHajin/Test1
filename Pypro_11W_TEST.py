
f1 = open("D:\PythonTest\11_Report_20220511\evenlines.txt", 'r', encoding="UTF8")
f2 = open("D:\PythonTest\11_Report_20220511\oddlines.txt", 'r', encoding="UTF8")
odds = f1.readlines()
print(odds)
for sentence in odds:
    print(sentence)
f1.close()
f2.close()