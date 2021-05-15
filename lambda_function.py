import json
import boto3
import git 

codepipeline_client = boto3.client('codepipeline')

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda-auto-new!')
    }

    #Get commit differences
    commit = git.commit('master')
    print(commit)


# https://gitpython.readthedocs.io/en/stable/tutorial.html