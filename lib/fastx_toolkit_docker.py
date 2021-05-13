#import docker
import os
#client = docker.from_env()

def fastx_toolkit(input_command):
        #a = client.containers.run('30a083c3d6fb',input_command)
        a = os.system("docker run 30a083c3d6fb "+input_command)
        return a