import os
import shutil


def rename_and_move_video_files(base_directory, target_directory):
    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Iterate through each item in the base directory
    for folder_name in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder_name)

        # Check if the item is a directory
        if os.path.isdir(folder_path):
            video_path = os.path.join(folder_path, 'video_left.avi')

            new_name = f"{folder_name}.avi"
            new_video_path = os.path.join(folder_path, new_name)

            # Check if video_left.avi exists in the directory
            if os.path.exists(video_path) or os.path.exists(new_video_path):
                if(os.path.exists(video_path)):
                    # Rename the file
                    os.rename(video_path, new_video_path)
                    print(f"Renamed: {video_path} to {new_video_path}")

                # Define the destination path
                destination_path = os.path.join(target_directory, new_name)

                # Move the renamed file to the target directory
                shutil.move(new_video_path, destination_path)
                print(f"Moved: {new_video_path} to {destination_path}")

if __name__ == "__main__":
    # Path to the training set directory
    training_set_path = r'E:\DataSets\sar_rarp50\test_set'

    # Path to the target directory where videos will be moved
    target_video_path = r'E:\DataSets\sar_rarp50\test_set_video'

    # Call the function to rename and move the video files
    rename_and_move_video_files(training_set_path, target_video_path)

