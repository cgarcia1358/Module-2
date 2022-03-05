#import and find path to for csv file.
from pathlib import Path
my_directory = Path('.')
print("my_directory")
print(my_directory)
csvpath = Path("Qualifying_Loan_Data.csv")
print(csvpath)
print(f"The relative CSV path is {csvpath}")
print(f"The absolute CSV path is {csvpath.absolute()}")
#create a function to save to csv
import csv
def save_csv():
    import csv
    with open(csvpath, 'w', newline='') as csvfile:
        csvfile = csvwriter = csv.writer(csvpath.absolute())
        return save_csv
save_csv()
# Save this as first version.