connect from docker to dbvisualizer using ubuntu WSL:
`docker run -p 5432:5432 --name sa-db -e POSTGRES_USER=sa_user -e POSTGRES_PASSWORD=mypasswd -e POSTGRES_DB=sentimentanalysis -d postgres`

create virtual environment in vscode from search bar
create requirements file so that virtual environment can read from and install packages
open powershell terminal in vscode and install requirements:
`pip install -r .\requirements.txt`