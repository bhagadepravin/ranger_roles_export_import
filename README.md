```markdown
# Ranger Roles Export and Import Scripts

This repository contains scripts to export and import roles from Apache Ranger. The export script downloads roles from a source Ranger instance and saves them to a JSON file. The import script uploads roles from a JSON file to a destination Ranger instance.

## Scripts

1. **export_roles.py**: This script exports roles from a source Ranger instance to a JSON file.
2. **import_roles.py**: This script imports roles from a JSON file to a destination Ranger instance.

## Prerequisites

- Python 2.7 or Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

### Export Roles

The `export_roles.py` script fetches roles from a source Ranger instance and saves them to a JSON file.

#### Running the Script

```bash
python export_roles.py
```

#### Script Prompts

- `SOURCE_RANGER URL`: The URL of the source Ranger instance.
- `SOURCE_RANGER ADMIN USER`: The admin username for the source Ranger instance.
- `SOURCE_RANGER ADMIN PASSWORD`: The admin password for the source Ranger instance.

#### Output

The roles will be saved to a file named `exported_roles.json` in the current directory.

### Import Roles

The `import_roles.py` script imports roles from a JSON file to a destination Ranger instance.

#### Running the Script

```bash
python import_roles.py
```

#### Script Prompts

- `Path to exported roles JSON file`: The path to the JSON file containing the exported roles.
- `DEST_RANGER URL`: The URL of the destination Ranger instance.
- `DEST_RANGER ADMIN USER`: The admin username for the destination Ranger instance.
- `DEST_RANGER ADMIN PASSWORD`: The admin password for the destination Ranger instance.

#### Output

The script will print the status of each role import operation, listing successfully imported and failed roles.

## Example

### Exporting Roles

```bash
$ python export_roles.py
SOURCE_RANGER URL:- http://source-ranger-host:6080
SOURCE_RANGER ADMIN USER:- admin
SOURCE_RANGER ADMIN PASSWORD:-
Total number of roles 10 will be exported.
Roles have been successfully exported to 'exported_roles.json'.
```

### Importing Roles

```bash
$ python import_roles.py
Path to exported roles JSON file:- exported_roles.json
DEST_RANGER URL:- http://destination-ranger-host:6080
DEST_RANGER ADMIN USER:- admin
DEST_RANGER ADMIN PASSWORD:-
Total number of roles 10 will be imported.
Successfully Imported Role role1 with status 200
Successfully Imported Role role2 with status 200
...
10 roles were imported successfully.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Notes:
- **Replace `http://source-ranger-host:6080` and `http://destination-ranger-host:6080` with the actual URLs of your Ranger instances.**
- **Ensure the `export_roles.py` and `import_roles.py` scripts are in the same directory as this README file.**
- **You might want to add more detailed error handling and validation depending on your specific requirements.**

Feel free to customize this README to better suit your project's needs.
