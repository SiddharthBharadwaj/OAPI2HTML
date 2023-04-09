import argparse
import yaml
from jinja2 import Environment, FileSystemLoader

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Path to OpenAPI YAML file")
parser.add_argument("output_file", help="Path to output HTML file")
args = parser.parse_args()

# Load the OpenAPI YAML file
with open(args.input_file, "r") as file:
    openapi_data = yaml.safe_load(file)

# Extract the required data from the parsed YAML
title = openapi_data["info"]["title"]
paths = openapi_data["paths"]

# Render the HTML documentation using the Jinja2 template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.html")

html_output = template.render(
    title=title,
    paths=paths,
)

# Save the rendered HTML to a file
with open(args.output_file, "w") as file:
    file.write(html_output)