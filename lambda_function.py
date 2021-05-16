import json
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda-auto-new!')
    }

    modifiedFiles = event["commits"][0]["modified"]
    #full path
    for filePath in modifiedFiles:
        # Extract folder name
        folderName = (filePath[:filePath.find("/")])
        print(folderName)
        break

    if len(folderName)>0:
        # Codepipeline name is foldername-job. 
        # We can read the configuration from S3 as well. 
        returnCode = start_code_pipeline(folderName + '-job')

    return {
        'statusCode': 200,
        'body': json.dumps('Modified project in repo:' + folderName)
    }
    

def start_code_pipeline(pipelineName):
    client = codepipeline_client()
    response = client.start_pipeline_execution(name=pipelineName)
    return True

cpclient = None
def codepipeline_client():
    import boto3
    global cpclient
    if not cpclient:
        cpclient = boto3.client('codepipeline')
    return cpclient
   

# https://gitpython.readthedocs.io/en/stable/tutorial.html

# https://aws.amazon.com/blogs/devops/integrate-github-monorepo-with-aws-codepipeline-to-run-project-specific-ci-cd-pipelines/
