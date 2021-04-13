import docker

client = docker.from_env()

def stringtie(input_command):
        b = client.containers.run('3aec4555231e',input_command)
        #cnt_stringtie += 1
        return b