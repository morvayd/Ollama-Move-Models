# Ollama Downloaded Model Mover

A Python script to zip downloaded Ollama models for easy transfer between computers.

## Description

This tool helps you prepare Ollama models for migration to another machine. It creates compressed archives containing all the necessary files (manifests and blobs) for each downloaded model, making it simple to move models without re-downloading them.

## Features

- **Cross-platform**: Supports Windows, macOS, and Linux
- **Automatic detection**: Finds all downloaded Ollama models
- **Complete packaging**: Includes all model files (manifests and blobs)
- **Compression**: Uses 7z on Windows/Linux, zip on macOS
- **Logging**: Detailed operation logs for troubleshooting

## Requirements

- Python 3.x
- Ollama installed and models downloaded
- 7-Zip (Windows/Linux) or zip (macOS)

### Python Libraries

```bash
pip install ollama
ollama pull <model to download>
```

## Installation

1. Clone or download this repository
2. Ensure Ollama is installed and you have downloaded models
3. Run the script

## Usage

```bash
python Ollama-Move-Models.py
```

The script will:
1. Detect your operating system
2. Locate the Ollama models directory
3. List all downloaded models
4. Create compressed archives for each model in the models folder

### Output

- **Windows/Linux**: `.7z` files containing model data
- **macOS**: `.zip` files containing model data

These archives can be transferred to another computer and extracted to the appropriate Ollama models directory.

## How It Works

Ollama stores models in a structured format with:
- Manifest files describing the model
- Blob files containing the actual model data

This script reads the manifest for each model, collects all associated blob files, and compresses them together for easy transport.

## Model Locations

- **macOS**: `~/.ollama/models`
- **Linux**: `/usr/share/ollama/.ollama/models` or `~/.ollama/models`
- **Windows**: `C:\Users\%username%\.ollama\models`

## Logs

Operation logs are saved in the `PythonLogs/` folder with detailed information about the compression process.

## Author

Daniel Morvay (morvayd@gmail.com)

## License

MIT License
