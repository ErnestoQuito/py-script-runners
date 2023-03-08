import pysftp
import os

class ServicesSFTP(object):
    host = None
    username = None
    password = None
    cnopts = None

    def __init__(self, host, user, password):
        self.host = host
        self.username = user
        self.password = password

    def set_cnopts(self, path_file: str):
        self.cnopts = pysftp.CnOpts(knownhosts=path_file)
        self.cnopts.hostkeys = None

    def upload_files(self, local_path_file: list, remote_path_file: str):
        with pysftp.Connection(
            host=self.host,
            username=self.username,
            password=self.password,
            cnopts=self.cnopts
        ) as sfpt:
            sfpt.put(localpath=local_path_file, remotepath=remote_path_file)

    def download_files(self, remote_path_file: list, local_path_file: str):
        path_saved = []
        with pysftp.Connection(
            host=self.host,
            username=self.username,
            password=self.password,
            cnopts=self.cnopts
        ) as sfpt:
            for pr in remote_path_file:
                local_path_contruyed = os.path.abspath(os.path.join(local_path_file, os.path.basename(pr)))
                sfpt.get(
                    remotepath=pr,
                    localpath=local_path_contruyed
                )
                path_saved.append(local_path_contruyed)
        return path_saved

    def list_files(self, remote_path_file):
        list_path_files: list = []
        with pysftp.Connection(
            host=self.host,
            username=self.username,
            password=self.password,
            cnopts=self.cnopts
        ) as sfpt:
            files = sfpt.listdir(remotepath=remote_path_file)[:10]
            for f in files:
                path_file = f'{remote_path_file}/{os.path.basename(f)}'
                if len(f.split('.')) > 1:
                    list_path_files.append(path_file)
        return list_path_files
