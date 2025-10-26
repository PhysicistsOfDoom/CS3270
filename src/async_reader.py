"""
This module is focused on providing asynchronous programming capabilities to speed up the reading of the CSV file and trying to async workloads
"""

import aiofiles
import pandas as pd
from io import StringIO

class AsyncFileReader:
    @staticmethod
    async def read_file_async(file_path: str) -> pd.DataFrame:
        """
        Reads a CSV file asynchronously and returns a pandas DataFrame.
        """
        async with aiofiles.open(file_path, mode='r') as f:
            content = await f.read()
        return pd.read_csv(StringIO(content))
