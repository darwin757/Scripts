import os

def scan_drives():
    # Platform specific implementation might be needed here
    if os.name == 'nt':  # For Windows
        drives = [f"{drive}:\\" for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{drive}:\\")]
    else:  # For Unix/Linux
        drives = ['/']  # Root directory as a starting point, could be adjusted for mounted drives
    return drives

def get_user_choice(choices, prompt):
    print(prompt)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")
    selection = int(input("Select an option: ")) - 1
    return choices[selection]

def list_files():
    # Scan and let the user select the drive
    drives = scan_drives()
    chosen_drive = get_user_choice(drives, "Please select the drive where your file is located:")
    
    # Ask for directory path and output file name
    relative_path = input(f"Enter the directory path relative to {chosen_drive} (e.g., 'Users\YourName\Documents'): ").strip()
    start_path = os.path.join(chosen_drive, relative_path.replace('/', os.sep).replace('\\', os.sep))  # Ensuring the path is correctly formatted
    
    output_file_name = input("Enter the name of the output file (e.g., 'file_list.txt'): ").strip()
    output_dir = os.path.dirname(start_path)
    output_file_path = os.path.join(output_dir, output_file_name)
    
    # List files and directories
    with open(output_file_path, 'w', encoding='utf-8') as f_out:
        for root, dirs, files in os.walk(start_path):
            level = root.replace(start_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f_out.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f_out.write('{}{}\n'.format(subindent, file))
    1
    print(f"File structure has been saved to {output_file_path}")

if __name__ == "__main__":
    list_files()  # Updated to include dynamic path and user interactions
