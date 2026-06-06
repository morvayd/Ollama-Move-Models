#  Ollama model redirect

#  Original Model Location - MacOS
cd '/Users/$User/.ollama/models'

#  Models Located on USB 1TB - MacOS
cd '/Volumes/1TBSandisk/Mac DataSci/AI - Ollama Models'

#  Copied, delete the original - MacOS
cd '/Users/$User/.ollama/models/blobs'
cd '/Users/$User/.ollama/models/manifests'

#  Stop Ollama before deleting

#  Create the symbolic links - MacOS
#  ln -s /path/to/new /path/to/original
ln -s '/Volumes/1TBSandisk/Mac DataSci/AI - Ollama Models/blobs' /Users/$User/.ollama/models/blobs
ln -s '/Volumes/1TBSandisk/Mac DataSci/AI - Ollama Models/manifests' /Users/$User/.ollama/models/manifests

#  Restart Ollama - Load models and run to verify operation
ollama list

#  Run model - verify operation
#  ollama run <model name>