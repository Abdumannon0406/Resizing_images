from pathlib import Path
import cv2
import csv


folder_path = Path("RESIZED")
output_folder = Path("CLEANED")
output_folder.mkdir(exist_ok=True)

bad_chars = ["'", "‘", "`"]

images_path = folder_path.glob("*.*")
renamed_files = []

for path in images_path:
    filename = path.name
    cleaned_name = filename
    for char in bad_chars:
        cleaned_name = cleaned_name.replace(char, "")

    new_path = output_folder / cleaned_name


    image = cv2.imread(str(path))
    if image is None:
        continue

    cv2.imwrite(str(new_path), image)

 
    if filename != cleaned_name:
        renamed_files.append((filename, cleaned_name))

for old_name, new_name in renamed_files:
    print(f"{old_name} → {new_name}")

input_csv = "restructured_sheet1 - Sheet1.csv"
output_csv = "cleaned_sheet.csv"

with open(input_csv, 'r', newline='', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        original = row[0]
        cleaned = original
        for char in bad_chars:
            cleaned = cleaned.replace(char, "")
        row[0] = cleaned
        writer.writerow(row)

        if original != cleaned:
            print(f"CSV: {original} → {cleaned}")


