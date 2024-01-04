import pandas as pd
import shutil
import os

# Load the original Excel file
input_excel_path = 'imagedata.xlsx'
df = pd.read_excel(input_excel_path)

# Specify the folder containing the images
image_folder = 'valid_data'

# Create a new DataFrame for the rows that match the image names
matched_rows = pd.DataFrame()

# Iterate through the images in the folder
for image_name in os.listdir(image_folder):
    # Check if the image name is present in the first column of the Excel file
    if image_name in df.iloc[:, 0].values:
        # Append the matching row to the new DataFrame
        matched_rows = pd.concat([matched_rows, df[df.iloc[:, 0] == image_name]])

# Save the matched rows to another Excel file
output_excel_path = 'validdata.xlsx'
matched_rows.to_excel(output_excel_path, index=False)

print(f"Matched rows saved to {output_excel_path}")
