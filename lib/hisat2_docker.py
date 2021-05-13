#import docker
import os

#client = docker.from_env()

def hisat2(input_command):
        #a = client.containers.run(image='336d8edb337f',command=input_command,volumes=['/home/aditya/Documents/MSC-DS/Sem3/Biocontainerproject/Bio-container-pipeline-automation/testing_files/'])
        #a = os.system("docker run 336d8edb337f "+input_command)
        a = os.system(input_command)
        return a