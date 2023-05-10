import logging
import sys
import time

import aws_lambda_logging
from scrapy.utils.project import get_project_settings


def setup_log(context=None):
    project_settings = get_project_settings()
    job_id = str(int(time.time()))

    log_context = {
        'aws_request_id': getattr(context, 'aws_request_id', None),
        'job_id': job_id
    }
    log_level = project_settings.get('LOG_LEVEL')

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(aws_lambda_logging.JsonFormatter(**log_context))
    handler.setLevel(log_level)
    logging.root.addHandler(handler)
    logging.root.setLevel(log_level)

    return job_id, project_settings
