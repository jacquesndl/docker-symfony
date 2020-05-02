from fabric.api import local

def docker_compose(command):
    """
    Docker Compose
    """
    local('docker-compose -f infrastructure/docker-compose.yml '+ command)

def logs(container = ''):
    """
    Display infrastructure logs
    """
    docker_compose('logs -f --tail=150 ' + container)

def ps():
    """
    List containers
    """
    docker_compose('ps')

def stop():
    """
    Stop the infrastructure
    """
    docker_compose('down')

def build():
    """
    Build the infrastructure
    """
    local('cp -n infrastructure/services/.env.dist infrastructure/services/.env')
    docker_compose('build')

def php(command):
    docker_compose('exec --user $(id -u):$(id -g) php ' + command)

def composer(command):
    """
    Composer
    """
    php('composer ' + command)

def up():
    """
    Build and start the infrastructure
    """
    build()
    local('mkdir -p application/var')
    docker_compose('up -d')

def create():
    """
    Create
    """
    composer('create-project symfony/website-skeleton app')
    local('mv application/app/* application/app/.[^.]* application/.')
    local('rm -R application/app > /dev/null 2>&1')

def configure():
    """
    Configure the application
    """
    local ('rm -f application/.env.local')
    local('echo MAILER_DSN=smtp://mailcatcher:1025 >> application/.env.local')
    local('echo DATABASE_URL=mysql://user:password@mysql:3306/database >> application/.env.local')

def start():
    """
    Build and start the infrastructure, then install the application (composer, yarn, ...)
    """
    up()
    install()
    fixtures()

def install():
    """
    Install the application (composer, yarn, ...)
    """
    composer('install -n --prefer-dist --optimize-autoloader')

def symfony(command):
    php('php bin/console ' + command)

def migrate():
    """
    Migrate database schema
    """
    symfony('doctrine:database:create --if-not-exists')
    symfony('doctrine:migration:migrate -n')

def fixtures():
    """
    Generate fixtures
    """
    symfony('doctrine:database:drop --force')
    migrate()
    # symfony('doctrine:fixtures:load -n')

def cache_clear():
    """
    Clear the application cache
    """
    symfony('cache:clear')
