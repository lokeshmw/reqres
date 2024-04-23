import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='Api_logs.log',
    filemode='w'
)

logger = logging.getLogger(__name__)


# def convert_logs_to_json(log_data):
#     json_Data = []
#     for line in log_data.splitlines():
#         timestamp, _, level, message = line.split(" - ", 3)
#         json_Data.append({
#             "timestamp": timestamp,
#             "level": level,
#             "message": message.strip()
#         })
#     return json_Data
#
#
# with open("Api_logs.log", "r") as log_file, open("Api_logs.json", "w") as json_file:
#     log_Data = log_file.read()
#     json_data = convert_logs_to_json(log_Data)
#     json.dump(json_data, json_file, indent=4)
#
# print("Converted logs to fb.json successfully!")
#
#
# def write_yaml(file_path, data):
#     with open(file_path, 'w') as f:
#         yaml.dump(data, f, default_flow_style=False)
#
#
# def convert_logs_to_yaml(log__data):
#     yaml_Data = []
#     for line in log__data.splitlines():
#         timestamp, _, level, message = line.split(" - ", 3)
#         yaml_Data.append({
#             "timestamp": timestamp,
#             "level": level,
#             "message": message.strip()  # Remove leading/trailing whitespace
#         })
#     return yaml_Data
#
#
# with open("Api_logs.log", "r") as log_file:
#     log_data = log_file.read()
#     yaml_data = convert_logs_to_yaml(log_data)
#
# with open("Api_logs.yaml", "w") as yaml_file:
#     yaml.dump(yaml_data, yaml_file, default_flow_style=False)
#
# print("Converted logs to api_log.yaml successfully!")
