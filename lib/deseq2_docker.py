import docker

client = docker.from_env()

def deseq2(input_command):
        c = client.containers.run('8d620dc67af7',input_command)
        #cnt_deseq2 += 1
        return c