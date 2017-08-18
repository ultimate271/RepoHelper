XML should have this format
The python file should be run in the directory with the repo file.
reponame should have the file names of the repo (either full unqualified URI or just local filename)
destination should be the same, although I'd highly recommend full unqualified URI (it will be local to your machine, not on github)
add a new setting element for each file you want to keep in version control

<?xml version="1.0" encoding="utf-8"?>
<settingfiles>
	<setting>
		<name></name>
		<reponame></reponame>
		<destination></destination>
	</setting>
</settingfiles>
