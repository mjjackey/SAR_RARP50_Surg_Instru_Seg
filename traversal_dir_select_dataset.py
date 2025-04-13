import os
import shutil


def process_videos(source_folder, destination_folder,dataset_folder):
    # Ensure the destination directory exists
    data_set_whole_rgb = os.path.join(destination_folder, dataset_folder, "rgb")
    data_set_whole_segmentation = os.path.join(destination_folder, dataset_folder, "segmentation")

    os.makedirs(data_set_whole_rgb, exist_ok=True)
    os.makedirs(data_set_whole_segmentation, exist_ok=True)

    # Iterate over each video_xx folder in the source folder
    for video_folder in os.listdir(source_folder):
        video_folder_path = os.path.join(source_folder, video_folder)

        # Check if it is a directory
        if os.path.isdir(video_folder_path):
            rgb_folder = os.path.join(video_folder_path, "rgb")
            segmentation_folder = os.path.join(video_folder_path, "segmentation")

            # Check if both rgb and segmentation folders exist
            if os.path.exists(rgb_folder) and os.path.exists(segmentation_folder):
                # Iterate over each file in the rgb folder
                for rgb_file in os.listdir(rgb_folder):
                    rgb_file_path = os.path.join(rgb_folder, rgb_file)

                    # Check if it is a file
                    if os.path.isfile(rgb_file_path):
                        # Construct the corresponding segmentation file path
                        segmentation_file_path = os.path.join(segmentation_folder, rgb_file)

                        # Check if the corresponding segmentation file exists
                        if os.path.exists(segmentation_file_path):
                            # Copy the rgb file to the training_set_whole/rgb folder with the prefix
                            rgb_dst_file_path = os.path.join(data_set_whole_rgb, f"{video_folder}_{rgb_file}")
                            shutil.copy(rgb_file_path, rgb_dst_file_path)
                            print(f"Copied: {rgb_file_path} to {rgb_dst_file_path}")

                            # Copy the segmentation file to the training_set_whole/segmentation folder with the prefix
                            seg_dst_file_path=os.path.join(data_set_whole_segmentation, f"{video_folder}_{rgb_file}")
                            shutil.copy(segmentation_file_path, seg_dst_file_path)
                            print(f"Copied: {segmentation_file_path} to {seg_dst_file_path}")

# Example usage:
# process_videos("/path/to/source/folder", "/path/to/destination/folder")
if __name__=="__main__":
    dataset_folder= "test_set_whole"
    process_videos(r'E:\DataSets\sar_rarp50\test_set', r'E:\DataSets\sar_rarp50\sar_rarp50_colab',
                   dataset_folder)
