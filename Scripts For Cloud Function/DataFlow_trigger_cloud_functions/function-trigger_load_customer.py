from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "supply-chain-001"

    template_path = "gs://dataflow-templates-us-east4/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq_load_customers",
        "environment": {
        "bypassTempDirValidation": false,
        "numWorkers": 2,
        "tempLocation": "gs://sn_data_tempfile/temp/",
        "ipConfiguration": "WORKER_IP_UNSPECIFIED",
        "enableStreamingEngine": false,
        "additionalExperiments": [
            "use_runner_v2"
        ],
        "additionalUserLabels": {}
    },
    "parameters": {
        "inputFilePattern": "gs://sn_data_processing_zone/Customers.csv",
        "JSONPath": "gs://sn_data_metadata/schema/bq-customer.json",
        "outputTable": "supply-chain-001:supply_chain_data.Customers",
        "bigQueryLoadingTemporaryDirectory": "gs://sn_data_tempfile",
        "javascriptTextTransformGcsPath": "gs://sn_data_metadata/udf/udf-customer.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
