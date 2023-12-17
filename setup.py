import os

def main():
    print("start setup project...")
    inp = input("install virtualenv ? [y/n]:")
    match inp:
        case "y":
            os.system("python -m pip install --user virtualenv")
            print("virtualenv installed.")
            
            
    inp = input("create /env ? [y/n]:")
    match inp:
        case "y":
            os.system("python -m venv env")
            print("/env created successfully.")
            
            
    inp = input("install dependencies ? [y/n]:")
    match inp:
        case "y":
            os.system("cd env/Scripts && activate && cd ../.. && pip install -r requirements.txt")    
            print("dependencies installed successfully.")
    
    inp = input("Run Program ? [y/n]:")
    match inp:
        case "y":
            os.system("deactivate")
            os.system("python env.py")

    

def check_libs():
    user_libs = os.popen("pip freeze").read().split("\n")
    
    with open("requirements.txt","r") as f:
        program_libs = (f.read()).split("\n")
        f.close()
        
    for _ in program_libs:
        if not _ in user_libs:
            os.system("pip install {_}")
    
    
    

if __name__ == "__main__":
    main()