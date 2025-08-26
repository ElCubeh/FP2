# Clases base (FileDownload, Node, DownloadManagerBase)

class DownloadManager(DownloadManagerBase):
    _global_downloaded_mb = 0.0

    def __init__(self):
        super().__init__()
        self._downloaded_mb = 0.0

    def finish_download(self, index):
        if index < 0 or index >= self.get_size():
            return None
        
        # Lógica de eliminación (similar a los anteriores)
        # ...
        file_downloaded = self.remove_and_get_item(index)

        if file_downloaded:
            self.downloaded_mb += file_downloaded.file_size_mb
            DownloadManager._global_downloaded_mb += file_downloaded.file_size_mb
        return file_downloaded
    
    # (Suponiendo un método auxiliar `remove_and_get_item`)

    @property
    def total_queued_size(self):
        total = 0
        curr = self.first
        while curr:
            total += curr.value.file_size_mb
            curr = curr.next
        return total

    @property
    def downloaded_mb(self):
        return self._downloaded_mb
    
    @downloaded_mb.setter
    def downloaded_mb(self, value):
        if value == 0:
            self._downloaded_mb = 0.0

    @classmethod
    def get_global_downloaded_mb(cls):
        return cls._global_downloaded_mb