import os

def run_main_script():
    """
    this function run main script
    using env python interpreter.
    """
    os.system("cd env/Scripts/ && activate && cd ../.. && cd src/ && python main.py")
    
if __name__=="__main__":
    run_main_script()