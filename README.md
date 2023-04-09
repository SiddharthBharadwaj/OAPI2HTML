# OAPI2HTML

This tool was created to solve personal issues while working with Redocly and other API deployment tools. It converts an OpenAPI 3.0 YAML file to a static HTML file that can be hosted on a web server.

## Usage
Python 3 should be installed for this to work.

1. Clone the repository

```bash
git clone https://github.com/SiddharthBharadwaj/oapi2html.git
```

2. Install the dependencies

```bash
cd oapi2html
pip3 install -r requirements.txt
```

3. Run oapi2html

```bash
python oapi2html.py <input_file> <output_file>
```
where <input_file> is the path to the OpenAPI YAML file and <output_file> is the path to the HTML output file.

## Features
- Generates a modern and responsive HTML documentation page
- Supports Bootstrap and CSS styling
- Includes a search bar to easily find endpoints
- Displays detailed information for each endpoint, including parameters and responses

## Example
To see an example of the HTML output, you can view the scrrenshot below or the example_output.html file included in the repository.

![Example Image](http://i.imgur.com/RfhcPRI.jpg)

## Contributing
Pull requests are welcome! Please open an issue first to discuss any changes you would like to make.