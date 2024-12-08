from hdfs import InsecureClient
from django.conf import settings

log_file = 'auth_logs.log'
hdfs_dir = '/upload/logs/authentication'

def upload_to_hdfs():
    print("starting upload_to_hdfs")
    client = InsecureClient(settings.HDFS_CONFIG['url'], user=settings.HDFS_CONFIG['user'])
    hdfs_directory = '/upload'
    try:
        local_path = 'C:/Users/STUDENT/Documents/project/hospitalmanagement_/hospitalmanagement_/auth_log.log'
        # Upload the file to HDFS
        client.upload(hdfs_dir, local_path, overwrite=True)
        return f"File uploaded to {hdfs_directory}"
    except Exception as e:
        return str(e)


def parse_logs(file_path):
    parsed_logs = []
    with open(file_path, 'r') as log_file:
        for line in log_file:
            parts = line.strip().split()
            if len(parts) > 4:
                event = {
                    'level': parts[0],
                    'timestamp': f"{parts[1]} {parts[2]}",
                    'action': parts[3],
                    'details': " ".join(parts[4:]),
                }
                parsed_logs.append(event)
    return parsed_logs

def fetch_mapreduce_results(hdfs_file_path):
    client = InsecureClient(settings.HDFS_CONFIG['url'], user=settings.HDFS_CONFIG['user'])
    with client.read(hdfs_file_path) as reader:
        return reader.read().decode('utf-8')


def auth_log_analysis():
    hdfs_output_path = '/upload/logs/authentication/output/part-00000'
    results = fetch_mapreduce_results(hdfs_output_path)
    return results
