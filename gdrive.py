
from google.colab import auth
auth.authenticate_user()

from googleapiclient.discovery import build
drive_service = build('drive', 'v3')

def make_sample_file(name):
	# Create a local file to upload.
	with open('./{}'.format(name), 'w') as f:
	  f.write('my sample file')

	#print('/tmp/to_upload.txt contains:')
	#!cat /tmp/to_upload.txt

def upload_file(name, mime= 'text/plain'):
	# Upload the file to Drive. See:
	#
	# https://developers.google.com/drive/v3/reference/files/create
	# https://developers.google.com/drive/v3/web/manage-uploads
	from googleapiclient.http import MediaFileUpload

	file_metadata = {
	  'name': name,
	  'mimeType': mime
	}

	media = MediaFileUpload(name, 
	                        mimetype= mime,
	                        resumable=True)

	created = drive_service.files().create(body=file_metadata,
	                                       media_body=media,
	                                       fields='id').execute()
	print('File ID: {}'.format(created.get('id')))

def download_file(file_id,filename):

	import io
	from googleapiclient.http import MediaIoBaseDownload

	request = drive_service.files().get_media(fileId=file_id)
	#downloaded = io.BytesIO()
	downloaded = io.FileIO(filename, 'wb')
	downloader = MediaIoBaseDownload(downloaded, request)
	done = False
	while done is False:
	  # _ is a placeholder for a progress object that we ignore.
	  # (Our file is small, so we skip reporting progress.)
	  _, done = downloader.next_chunk()

	downloaded.seek(0)
	#print('Downloaded file contents are: {}'.format(downloaded.read()))

