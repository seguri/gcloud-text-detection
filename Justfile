set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

python_dir := ".venv/" + if os_family() == "windows" { "Scripts" } else { "bin" }
python := python_dir + if os_family() == "windows" { "/python.exe" } else { "/python3" }

system-info:
    @echo "This is an {{arch()}} machine,"
    @echo "With {{num_cpus()}} CPUs,"
    @echo "Running on {{os()}} ({{os_family()}})."

setup:
    {{ python }} -m pip install -r requirements.txt

detect_text image:
    {{python}} text_detection.py "{{ image }}"
