import re
from pathlib import Path


class SearchFiles(object):
    def __init__(self, path="."):
        self.path = Path(path).absolute()
        self.out = ""

    def __str__(self):
        return self.out

    def ls(self, owner: bool = False, size: bool = False):
        """List files in the specified directory
        
        Args:
            owner (bool, optional): Show owner of file. Defaults to False.
            size (bool, optional): Show size of file. Defaults to False.
        
        Returns:
            SearchFiles: SearchFiles object
        """
        found = []
        files = self.path.glob("**/*")
        for file in files:
            details = []
            if owner:
                details.append(str(file.owner()))
            if size:
                details.append(str(file.stat().st_size))
            details.append(str(file))
            found.append(" ".join(details))
        self.out = "\n".join(found)
        return self

    def grep(self, pattern: str):
        """Search for match in list of files
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            SearchFiles: SearchFiles object
        """
        pattern = ".*" + pattern + ".*"
        self.out = "\n".join(re.findall(pattern, self.out))
        return self