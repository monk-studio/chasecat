from fabric.api import env, cd, run

env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['duan-p0']


def deploy():
    with cd('/code/leaderboard'):
        run('git pull origin master')
        run('pipenv install')
        run('pipenv run python manage.py db upgrade')
        run('sudo systemctl restart chasecat.service')
