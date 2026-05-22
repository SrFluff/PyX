import kernel
def error(process_name,error_message, error_code=1):
    print(f"{process_name}: Error, {error_message}")
    kernel.STDERR = error_code
