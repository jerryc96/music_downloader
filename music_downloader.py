import paramiko

music_dir = "./music/"
file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"


HOSTNAME = ""
USERNAME = ""
PASSWORD = ""

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def download(remotepath, localpath, client):
    client.connect(HOSTNAME, username=USERNAME, password=PASSWORD)
    ftp_client = client.open_sftp()
    ftp_client.get(remotepath, localpath)
    ftp_client.close()

def upload(localpath, remotepath, client):
    client.connect(HOSTNAME, username=USERNAME, password=PASSWORD)
    ftp_client = client.open_sftp()
    ftp_client.put(localpath, remotepath)
    ftp_client.close()


if __name__ == "__main__":
    remotedirpath = "./music_files/"
    localdirpath = music_dir
    localfilepath = music_dir + "python.pdf"
    upload(localfilepath, remotedirpath, ssh_client)
