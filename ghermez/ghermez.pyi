def startAria(port: int, aria2_path: str | None=None) -> str: ...
def aria2Version() -> str: ...
def new_date() -> str: ...

def determineConfigFolder() -> str: ...
def humanReadableSize(size: float, input_type: str='file_size') -> str: ...
def convertToByte(file_size: str) -> float: ...
def osAndDesktopEnvironment() -> (str, str | None): ...
def returnDefaultSettings(available_styles: list[str]) -> dict[str, str]: ...

def checkstartup() -> bool: ...
def addstartup() -> None: ...
def removestartup() -> None: ...

def init_create_folders() -> None: ...
def init_log_file() -> None: ...

class TempDB:
  def __init__(self) -> None: ...
  def createTables(self) -> None: ...
  def insertInSingleTable(self, gid: str) -> None: ...
  def insertInQueueTable(self, category: str) -> None: ...
  def updateSingleTable(self, download_dict: dict[str, str]) -> None: ...
  def updateQueueTable(self, category_dict: dict[str, str]) -> None: ...
  def returnActiveGids(self) -> list[str]: ...
  def returnGid(self, gid: str) -> dict[str, str] | None: ...
  def returnCategory(self, category: str) -> dict[str, str] | None: ...
  def resetDataBase() -> None: ...

class PluginsDB:
  def __init__(self) -> None: ...
  def createTables(self) -> None: ...
  def insertInPluginsTable(self, download_list: list[dict[str, str]]) -> None: ...
  def returnNewLinks(self) -> list[dict[str, str]]: ...
  def deleteOldLinks(self) -> None: ...

class DataBase:
  def __init__(self) -> None: ...
  def createTables(self) -> None: ...
  def insertInCategoryTable(self, category_dict: dict[str, str]) -> None: ...
  def insertInDownloadTable(self, download_list: list[dict[str, str]]) -> None: ...
  def insertInAddLinkTable(self, addlink_list: list[dict[str, str]]) -> None: ...
  def insertInVideoFinderTable(self, video_list: list[dict[str, str]]) -> None: ...
  def searchGidInVideoFinderTable(self, gid: str) -> dict[str, str] | None: ...
  def searchGidInDownloadTable(self, gid: str) -> dict[str, str] | None: ...
  def returnItemsInDownloadTable(self, category: str | None) -> dict[str, str]: ...
  def searchLinkInAddLinkTable(self, link: str) -> bool: ...
  def searchGidInAddLinkTable(self, gid: str) -> dict[str, str] | None: ...
  def returnItemsInAddLinkTable(self, category: str | None) -> dict[str, dict[str, str]]: ...
  def updateDownloadTable(self, download_list: list[dict[str, str]]) -> None: ...
  def updateCategoryTable(self, category_list: list[dict[str, str]]) -> None: ...
  def updateAddLinkTable(self, addlink_list: list[dict[str, str]]) -> None: ...
  def updateVideoFinderTable(self, video_list: list[dict[str, str]]) -> None: ...
  def setDefaultGidInAddlinkTable(self, gid: str, start_time: bool, end_time: bool, after_download: bool) -> None: ...
  def searchCategoryInCategoryTable(self, category: str) -> dict[str, str] | None: ...
  def categoriesList(self) -> list[str]: ...
  def setDBTablesToDefaultValue(self) -> None: ...
  def findActiveDownloads(self, category: str | None) -> list[str]: ...
  def returnDownloadingItems(self) -> list[str]: ...
  def returnPausedItems(self) -> list[str]: ...
  def returnVideoFinderGids(self) -> (list[str], list[str], list[str]): ...
  def deleteCategory(self, category: str) -> None: ...
  def resetDataBase(self) -> None: ...
  def deleteItemInDownloadTable(self, gid: str, category: str) -> None: ...
  def correctDataBase(self) -> None: ...
