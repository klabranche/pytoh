# https://code.visualstudio.com/docs/python/python-tutorial
# https://www.tutorialspoint.com/How-to-run-Python-functions-from-command-line
# https://www.pythonpool.com/tower-of-hanoi-python/
# https://mauroterraneo.wordpress.com/2015/12/27/solution-for-the-tower-of-hanoi-with-python-script/
# https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?toc=%2Fazure%2Fdeveloper%2Fpython%2Ftoc.json&bc=%2Fazure%2Fdeveloper%2Fbreadcrumb%2Ftoc.json&tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli
# https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application
# https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack
# https://code.visualstudio.com/docs/azure/extensions
# https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli

def toh(steps,discCount, source_rod, destination_rod, placeholder_rod):           
    if discCount == 1:
        #print("Move disc 1 from rod",source_rod,"to rod",destination_rod)
        steps.append((1,source_rod,destination_rod))
        return
    toh(steps,discCount-1, source_rod, placeholder_rod, destination_rod)
    #print("Move disc",discCount,"from rod",source_rod,"to rod",destination_rod)
    steps.append((discCount,source_rod,destination_rod))
    toh(steps,discCount-1, placeholder_rod, destination_rod, source_rod)

def main():
    try:
        discCount = int(input("How many disks do you want to move?"))
    except ValueError:
        print()
        print("discCount is not a number... defaulting to 3")
        discCount=3

    print()
    print("Moving",discCount,"discs from rod A to rod C", end="\n\n")
    steps=[]
    toh(steps,discCount, 'A', 'C', 'B')
    print(steps)
