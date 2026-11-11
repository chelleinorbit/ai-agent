import os.path

# allows agent to list contents of a directory and see each files metadata
def get_files_info(working_directory: str, directory: str = ".") -> str:
    # absolute path of working directory
    working_dir: str = os.path.abspath(working_directory)
    # combines working directory with directory arg and then collapses redundant separators
    target_dir: str = os.path.normpath(os.path.join(working_dir, directory))
    # checks if target dir is within working dir by checking if working dir and target dir match
    valid_path: bool = os.path.commonpath([working_dir, target_dir]) == working_dir
    if not valid_path:
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    # warning: without the above restriction, the LLM might run amok anywhere on the machine, reading sensitive files
    # or overwriting important data. This is a very important step to bake into every function the LLM can call.
    if not os.path.isdir(target_dir):
        return f"Error: \"{directory}\" is not a directory"
    return f"Success: \"{directory}\" is within the working directory"

# TO DO:
# catch errors in try/except blocks for convenience and practice.
# if any new errors are raised by standard library functions, add a catch with a string describing the error