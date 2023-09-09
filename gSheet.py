# for Google sheet functions
 
def returnsheetdata(sheet):
    worksheet = sheet.worksheet("NPCs(4)")
    data = worksheet.get_all_values()
    return data
  
#gSheet.printsheetdata(sheet)
def printdata(data):
    for row in data:
        print(row)

def findnpc(sheet):
    worksheet = sheet.worksheet("NPCs(4)")
    data = worksheet.get_all_values()

    # Printing data
    for row in data:
        print(row)

