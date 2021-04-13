import docker

client = docker.from_env()

def hisat2(input_command):
        a = client.containers.run('336d8edb337f',input_command)
        #cnt_hisat2 += 1
        return a