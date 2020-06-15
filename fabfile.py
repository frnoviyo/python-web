from fabric.api import run, sudo, task, put, get, cd, prefix, local, env

def hola_mundo():
  print('Hola munod desde fabric')

def bye():
  print('bye desde fabric')

#def show_dir():
 # run('ls')

def create_folder(folder):
  run(f'mkdir {folder}')

def delete_folder(folder):
  sudo(f'rm -rf {folder}')

@task
def upload_txt_file():
  put(
    local_path='./example.txt',
    remote_path='./python-web'
  )

@task
def get_txt_file(file):
  get(
    local_path='./descargas',
    remote_path=f'./python-web/{file}'
  )

# cd
# @task
# def pull():
#   #run('cd python-web && git pull')
#   #Esto es equivalente a la linea anterior
#   with cd('python-web'):
#     run('git pull')

#EJECUCION BAJO DEMANDA
@task
def install_requirements():
  #run('cd python-web && source env/bin/activate && pip install -r requirements.txt')
  #with cd('python-web'):
  with prefix('source env/bin/activate'):
    run('pip install -r requirements.txt')

#COMANDOS LOCALES

@task
def show_dir():
  local('ls -l')

#Entornos, con esto ya no nos pide el usuario y el host
env.hosts = ['192.81.213.190']

env.user = 'freddy'

env.key_filename = '~/.ssh/id_rsa.pub'

@task
def pull():
  #with cd ('python-web'):
  run('git pull')

#Funcion que permite reiniciar nuestra aplicacion de flask
@task 
def deploy():
  with cd('python-web'):
    pull()

    with prefix('source env/bin/activate'):
      install_requirements()

    sudo('systemctl restart nginx')