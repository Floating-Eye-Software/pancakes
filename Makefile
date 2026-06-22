.PHONY: check-work check-plans check-todo check-workflow check-docs mount umount links nolinks upload download

PYTHON ?= python3
FLEY_ORG ?= ../fley-org

check-work: check-plans check-todo check-workflow check-docs

check-plans:
	@$(PYTHON) $(FLEY_ORG)/scripts/repo_tour.py --check-csv "$(CURDIR)/_work/plans/plans.csv"

check-todo:
	@$(PYTHON) $(FLEY_ORG)/scripts/repo_tour.py --check-csv "$(CURDIR)/_work/todo.csv"

check-workflow:
	@cmp -s "$(FLEY_ORG)/process/repo-workflow.md" _work/repo-workflow.md
	@echo "_work/repo-workflow.md: synced"

check-docs:
	@$(PYTHON) _work/check-diff-whitespace.py
	@echo "Pancakes document whitespace: ok"

mount:
	sshfs pancakes.love:pancakes apps/legacy-auth-webapp/remote-server

umount:
	sudo umount apps/legacy-auth-webapp/remote-server

links:
	-ln -s ~/sandbox/pancakes/data/ ~/data

nolinks:
	-rm ~/data

upload:
	rm -rf apps/legacy-auth-webapp/remote-server/app/

	mkdir apps/legacy-auth-webapp/remote-server/app
	cp .env apps/legacy-auth-webapp/remote-server/app/
	cp apps/legacy-auth-webapp/auth.py apps/legacy-auth-webapp/remote-server/app/
	cp apps/legacy-auth-webapp/main.py apps/legacy-auth-webapp/remote-server/app/
	cp apps/legacy-auth-webapp/public.py apps/legacy-auth-webapp/remote-server/app/
	cp apps/legacy-auth-webapp/user.py apps/legacy-auth-webapp/remote-server/app/

	mkdir apps/legacy-auth-webapp/remote-server/app/data
	cp apps/legacy-auth-webapp/data/db.py apps/legacy-auth-webapp/remote-server/app/data/

	mkdir apps/legacy-auth-webapp/remote-server/app/static
	cp apps/legacy-auth-webapp/static/favicon.ico apps/legacy-auth-webapp/remote-server/app/static/
	cp apps/legacy-auth-webapp/static/robots.txt apps/legacy-auth-webapp/remote-server/app/static/

	mkdir apps/legacy-auth-webapp/remote-server/app/templates
	cp apps/legacy-auth-webapp/templates/base.html apps/legacy-auth-webapp/remote-server/app/templates/
	cp apps/legacy-auth-webapp/templates/index.html apps/legacy-auth-webapp/remote-server/app/templates/
	cp apps/legacy-auth-webapp/templates/login.html apps/legacy-auth-webapp/remote-server/app/templates/
	cp apps/legacy-auth-webapp/templates/dashboard.html apps/legacy-auth-webapp/remote-server/app/templates/
	cp apps/legacy-auth-webapp/templates/signup.html apps/legacy-auth-webapp/remote-server/app/templates/

download:
	cp -pr apps/legacy-auth-webapp/remote-server/backup/ .
