#backup with schedule library

#import
import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\Admin\Desktop\Personal Work\Automation\PNG"
destination_dir = r"C:\Users\Admin\Desktop\Personal Work\Automation\backup"

# Remove all contents of the destination directory
def clear_destination_dir(dest):
    for item in os.listdir(dest):
        item_path = os.path.join(dest, item)
        if os.path.isfile(item_path):
            os.unlink(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

#backup function
def copy_folder_to_directory(source, dest):
    today = datetime.date.today()   #create new folder according to backup date
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

# Clear the destination directory first
clear_destination_dir(destination_dir)

# Copy the folder to the destination directory
copy_folder_to_directory(source_dir, destination_dir)

####################################### scheduler #################################################################

# # Define the job to clear the destination directory and copy the folder at a specific time
# def scheduled_tasks():
#     clear_destination_dir(destination_dir)
#     copy_folder_to_directory(source_dir, destination_dir)

# # Schedule the job to run every day at 18:57
# schedule.every().day.at("18:57").do(scheduled_tasks)

# # Loop to keep the script running and check for scheduled tasks
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Sleep for 60 seconds before checking again