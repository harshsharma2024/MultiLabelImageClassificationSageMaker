import os
from PIL import Image

def retrieve_and_save_images(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Walk through all files and subdirectories in the input folder
    for foldername, subfolders, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(foldername, file)

            # Check if the file is an image (customize the image extensions if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif','.webp')):
                try:
                    # Open the image
                    # print (file)
                    with Image.open(file_path) as img:
                        # Create the output file path
                        relative_path = os.path.relpath(file_path, input_folder)
                        output_path = os.path.join(output_folder, file)

                        # Ensure the output directory structure exists
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)

                        # Save the image to the output folder
                        img.save(output_path)

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
            else:
                print(file)
                

if __name__ == "__main__":
    # Specify your input and output folders
    input_folder = "/home/harsh_arma/Documents/Coding stuff/Intern__/TASK/Image_tagging/ImageClassification/muti_label_aws/dataset_image"
    output_folder = "/home/harsh_arma/Documents/Coding stuff/Intern__/TASK/Image_tagging/ImageClassification/muti_label_aws/prepare_data/img_clf_multilabel_lst/all_images_gt"

    # Call the function
    retrieve_and_save_images(input_folder, output_folder)
