from fabric.api import run, sudo, task, put, get

def hola_mundo():
  print('Hola munod desde fabric')

def bye():
  print('bye desde fabric')

def show_dir():
  run('ls')

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
@task
def pull():
  run('cd python-web && git pull')