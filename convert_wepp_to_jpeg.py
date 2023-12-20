import os
from PIL import Image

def convert_and_delete_webp_images(folder_path):
    try:
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if the file is a WebP image
            if os.path.isfile(file_path) and filename.lower().endswith(".webp"):
                # Open the WebP image
                webp_image = Image.open(file_path)

                # Create the output JPG filename
                jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                jpg_output_path = os.path.join(folder_path, jpg_filename)

                # Save the image in JPG format
                webp_image.convert("RGB").save(jpg_output_path, "JPEG")

                print(f"Conversion successful. Image saved as {jpg_output_path}")

                # Delete the original WebP image
                os.remove(file_path)
                print(f"Original WebP file deleted: {file_path}")

    except Exception as e:
        print(f"Error converting and deleting images: {e}")

def convert_images_to_jpg(folder_path):
    try:
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if the file is an image
            if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']):
                # Open the image
                image = Image.open(file_path)

                # Create the output JPG filename
                jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                jpg_output_path = os.path.join(folder_path, jpg_filename)

                # Save the image in JPG format
                image.convert("RGB").save(jpg_output_path, "JPEG")

                print(f"Conversion successful. Image saved as {jpg_output_path}")

                # Delete the original image if it's not already a JPG
                if not filename.lower().endswith('.jpg') and not filename.lower().endswith('.jpeg'):
                    os.remove(file_path)
                    print(f"Original file deleted: {file_path}")

    except Exception as e:
        print(f"Error converting and deleting images: {e}")
        
# Example usage:
folder_path = "prepare_data/img_clf_multilabel_lst/all_images_gt"
convert_and_delete_webp_images(folder_path)
convert_images_to_jpg(folder_path)

