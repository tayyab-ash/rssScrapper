from utils.constants import config

class LocalDB:
    file_handle = None

    @staticmethod
    def write_data(key, value):
        if LocalDB.file_handle is None:
            LocalDB.file_handle = open("database.db", "a+")

        data = LocalDB.retrieve_data(key)
        if data:
            LocalDB.delete_data(key)
        LocalDB.file_handle.write(f"{key}: {value}\n")
        LocalDB.file_handle.flush()

    @staticmethod
    def retrieve_data(key):
        if LocalDB.file_handle is None:
            LocalDB.file_handle = open(config.local_db_name, "a+")

        LocalDB.file_handle.seek(0)

        for line in LocalDB.file_handle:
            if line.startswith(f"{key}:"):
                return line.split(":")[1].strip()

        return None

    @staticmethod
    def delete_data(key):
        if LocalDB.file_handle is None:
            LocalDB.file_handle = open(config.local_db_name, "a+")

        LocalDB.file_handle.seek(0)
        lines = LocalDB.file_handle.readlines()
        LocalDB.file_handle.seek(0)
        LocalDB.file_handle.truncate()

        for line in lines:
            if not line.startswith(f"{key}:"):
                LocalDB.file_handle.write(line)

        LocalDB.file_handle.flush()