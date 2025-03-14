from pathlib import Path

def get_resource_path(resource_type, filename):

    base_path = Path(__file__).parent / 'resources' / resource_type
    return str(base_path / filename)