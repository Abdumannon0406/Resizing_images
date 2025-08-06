from pathlib import Path
import cv2

folder_path=Path("UMUMIY")

output_folder = Path("RESIZED")
output_folder.mkdir(exist_ok=True) 

images_path=folder_path.glob("*.*")

for path in images_path:
    image=cv2.imread(str(path))
    resized=cv2.resize(image,(1000,1000))

    output_path = output_folder / path.name
    cv2.imwrite(str(output_path), resized)