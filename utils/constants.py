from box import Box
import yaml


config = Box(yaml.safe_load(open("config.yaml")))