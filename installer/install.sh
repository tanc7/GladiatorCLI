aptlist=apt_repos.txt
ghlist=github_repo_urls.txt
piplist=requirements.txt

for pkg in $(cat $aptlist)
	do sudo apt-get update
	sudo apt-get install -y $pkg
	done

sudo pip install -r requirements.txt

for repo in $(cat $ghlist)
	do git clone $repo
	done)


