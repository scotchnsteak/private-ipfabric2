
class CleanTables:

    def clean_tables(self):

        import os
        import pandas as pd
        from pathlib import Path

        Path("DOWNLOADS/cleaned-tables").mkdir(parents=True, exist_ok=True)

        path = 'DOWNLOADS/raw-tables/'
        dirs = os.listdir(path)

        for csv_file in dirs:

            df = pd.read_csv(path + csv_file)

            if 'id' in df.columns:
                df = df.drop(['id'], axis=1)
            if 'siteKey' in df.columns:
                df = df.drop(['siteKey'], axis=1)
            if 'memoryTotalBytes' in df.columns:
                df = df.drop(['memoryTotalBytes'], axis=1)
            if 'memoryUsedBytes' in df:
                df = df.drop(['memoryUsedBytes'], axis=1)
            if 'snHw' in df:
                df = df.drop(['snHw'], axis=1)
            if 'siteKey' in df:
                df = df.drop(['siteKey'], axis=1)
            if 'siteName' in df:
                df = df.drop(['siteName'], axis=1)
            if 'objectId' in df:
                df = df.drop(['objectId'], axis=1)
            if 'deviceId' in df:
                df = df.drop(['deviceId'], axis=1)
            if 'neiSiteName' in df:
                df = df.drop(['neiSiteName'], axis=1)
            if 'neiSiteKey' in df:
                df = df.drop(['neiSiteKey'], axis=1)
            if 'blobKey' in df:
                df = df.drop(['blobKey'], axis=1)
            if 'params' in df:
                df = df.drop(['params'], axis=1)
            df.to_csv('DOWNLOADS/cleaned-tables/' + csv_file, index=False)

        print('All the downloaded tables have been successfully cleaned.')

