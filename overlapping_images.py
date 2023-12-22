import os
import pandas as pd

count = 0

def mark_matching_images(excel_path, folder_path, result_column):
    # Load the Excel file into a DataFrame without header
    df = pd.read_excel(excel_path, header=None)
    global count
    # Get the list of image names from the Excel file
    excel_image_names = df.iloc[:, 0].tolist()

    # Get the list of image files in the specified folder
    folder_image_names = os.listdir(folder_path)

    # Create a new column in the DataFrame to store the results
    df[result_column] = 'N'  # Initialize with 'N'

    # Mark 'Y' for matching images
    for i, image_name in enumerate(excel_image_names):
        if image_name in folder_image_names:
            df.at[i, result_column] = 'Y'
            count = count + 1
    # Save the updated DataFrame to a new Excel file
    df.to_excel(excel_path, index=False, header=False)

if __name__ == "__main__":
    # Specify the paths and column names
    excel_file_path = "imagedata.xlsx"
    folder_path = "/home/harsh_arma/Documents/Coding stuff/Intern__/TASK/Image_tagging/ImageClassification/muti_label_aws/prepare_data/img_clf_multilabel_lst/all_images_gt"
    result_column_name = "ResultColumn"  # Replace with the desired result column name

    # Call the function
    mark_matching_images(excel_file_path, folder_path, result_column_name)
    print(count)