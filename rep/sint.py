try:
    # Code that may raise a FileNotFoundError or IOError
except (FileNotFoundError, IOError) as ex:
    # Code to handle the FileNotFoundError or IOError
    print(f"An error occurred: {ex}")
