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

    def upload_files(self, local_path_file, remote_path_file):
        with pysftp.Connection(
            host=self.host,
            username=self.username,
            password=self.password,
            cnopts=self.cnopts
        ) as sfpt:
            sfpt.put(localpath=local_path_file, remotepath=remote_path_file)

    def download_files(self, local_path_file, remote_path_file):
        with pysftp.Connection(
            host=self.host,
            username=self.username,
            password=self.password,
            cnopts=self.cnopts
        ) as sfpt:
            sfpt.get(remotepath=remote_path_file, localpath=local_path_file)

    def list_files(self, remote_path_file):
        with pysftp.Connection(
            host=self.host,
            username=self.username,
            password=self.password,
            cnopts=self.cnopts
        ) as sfpt:
            list = sfpt.listdir(remotepath=remote_path_file)
            print(list)
