#import docker
import os
#client = docker.from_env()

def stringtie(input_command):
        #b = client.containers.run('3aec4555231e',input_command)
        #b = os.system("docker run 3aec4555231e "+input_command)
        b = os.system(input_command)
        return b