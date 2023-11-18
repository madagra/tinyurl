APP_NAME = "tinyurl"

DOMAIN = "mdtiny.net"

HOSTED_ZONE = "Z00549253CLKXN3DRZZRQ"

REGION = "eu-west-3"

DOCKER_IMAGE_TAG = "dev"

DOCKER_IMAGE = f"madagra/tinyurl:{DOCKER_IMAGE_TAG}"

APP_PORT = 3000

N_TASKS = 5

REDIS_CLUSTER_NAME = f"{APP_NAME}-redis"

REDIS_CLUSTER_SIZE = 2

REDIS_CLUSTER_PORT = 6379

EC2_KEYPAIR = "ec2-keypair"
