import boto3

# Specify the region, e.g., 'us-west-2'
ecr_client = boto3.client('ecr', region_name='us-west-2')

repository_name = 'my-cloud-native-repository'
responce = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = responce['repository']['repositoryUri']
print(repository_uri)
