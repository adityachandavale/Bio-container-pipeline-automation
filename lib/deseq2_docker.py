#import docker
import os
#client = docker.from_env()

def deseq2(input_command):
        #c = client.containers.run('8d620dc67af7',input_command)
        c = os.system("docker run 8d620dc67af7 "+input_command)
        return c