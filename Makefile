.PHONY: *
BUILD_DIR=build
COOKIECUTTER_OUTPUT_DIR=$(BUILD_DIR)/python_boilerplate

help:
	@echo "help"

setup-cicd:
	pip install --upgrade pip
	pip install cookiecutter

refresh:
	rm -rf $(BUILD_DIR)
	cookiecutter --default-config --no-input -o $(BUILD_DIR) .

setup: refresh
	@echo "setting up poetry in directory $(COOKIECUTTER_OUTPUT_DIR)"
	@$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) setup-dev-env-minimal

clean-setup:
	rm -rf build/
	@$(MAKE) setup

#%: refresh
#	@echo "calling target(s) [$(MAKECMDGOALS)] on Makefile in directory $(COOKIECUTTER_OUTPUT_DIR)"
#	@$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) $(MAKECMDGOALS)

#################################################################
# git targets
#################################################################

prune-branches:
	git remote prune origin
	git branch -vv | grep ': gone]'|  grep -v "\*" | awk '{ print $$1; }' | xargs git branch -d


prune-branches-force:
	git remote prune origin
	git branch -vv | grep ': gone]'|  grep -v "\*" | awk '{ print $$1; }' | xargs git branch -D

pbf: prune-branches-force

post-PR-merge-sync-step-1:
	git switch master
	git pull

pms: post-PR-merge-sync-step-1 prune-branches-force
