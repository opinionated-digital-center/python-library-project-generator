.PHONY: *
BUILD_DIR=build
COOKIECUTTER_OUTPUT_DIR=$(BUILD_DIR)/a-generated-python-project

help:
	@echo "help"

#################################################################
# setting up dev env
#################################################################

dev-env-minimal = -E format
dev-env-full = -E test -E git -E gitlab -E format -E lint -E repl

setup-dev-env-minimal: clean
	poetry install --no-root $(dev-env-minimal)

setup-dev-env-full: clean
	poetry install --no-root $(dev-env-full)

setup-dev-host:
	./scripts/install_pyenv.sh
	./scripts/install_poetry.sh
	@echo "Host setup correctly. Restart your shell or source your shell config file to be up and running :)"

setup-pre-commit-hooks:
	pre-commit install --hook-type pre-commit

#################################################################
# setting dependencies for automation (tox, cicd)
#################################################################

install-template-generation-dependencies:
	poetry install --no-dev --no-root

install-test-dependencies:
	poetry install --no-dev --no-root -E test

install-gitlab-pipelines-test-dependencies:
	poetry install --no-dev --no-root -E test -E git -E gitlab

install-format-dependencies:
	poetry install --no-dev --no-root -E format

install-lint-dependencies:
	poetry install --no-dev --no-root -E lint

install-docs-dependencies:
	poetry install --no-dev --no-root -E docs

#################################################################
# setting up ci-cd env
#################################################################

setup-cicd:
	pip install --upgrade pip

#################################################################
# cleaning
#################################################################

clean:
	rm -rf $(BUILD_DIR)

#################################################################
# generate project
#################################################################

overwrite:
	# `rm` necessary due to bug in cookicutter, which does not overwrite all directories
	rm -rf $(COOKIECUTTER_OUTPUT_DIR)/behave* $(COOKIECUTTER_OUTPUT_DIR)/features
	poetry run cookiecutter --overwrite-if-exists --default-config --no-input -o $(BUILD_DIR) .

refresh: clean
	poetry run cookiecutter --default-config --no-input -o $(BUILD_DIR) .

refresh-: refresh

refresh-pytest: refresh

refresh-cli-cleo: refresh

refresh-cli-click: clean
	poetry run cookiecutter --overwrite-if-exists --default-config --no-input -o $(BUILD_DIR) . command_line_interface=Click

refresh-cli-none: clean
	poetry run cookiecutter --overwrite-if-exists --default-config --no-input -o $(BUILD_DIR) . command_line_interface=None

refresh-gitlab: clean
	poetry run cookiecutter --overwrite-if-exists --default-config --no-input -o $(BUILD_DIR) . hosting=GitLab

#################################################################
# template generation testing
#################################################################

test-generated-project: refresh-$(OPTION)
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) install-test-dependencies
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) test

bdd-generated-project: refresh-$(OPTION)
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) install-bdd-dependencies
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) bdd

format-generated-project: refresh-$(OPTION)
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) install-format-dependencies
	# seed-isort-config needs a `git` repository to work
	cd $(COOKIECUTTER_OUTPUT_DIR) && git init .
	cd $(COOKIECUTTER_OUTPUT_DIR) && git config user.name "foo" && git config user.email "foo@bar.com"
	cd $(COOKIECUTTER_OUTPUT_DIR) && git add --all && git commit -m'foo'
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) format

lint-generated-project: refresh-$(OPTION)
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) install-lint-dependencies
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) lint

type-generated-project: refresh-$(OPTION)
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) install-type-dependencies
	$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) type

test-gitlab-cleanness: refresh-gitlab
	poetry run pytest tests/test_no_github_in_gitlab_generated_project.py

#################################################################
# template pipelines/workflows testing
#################################################################

test-gitlab-pipeline:
	poetry run pytest tests/test_gitlab_pipeline.py

#################################################################
# other (to cleanup)
#################################################################

setup: refresh
	@echo "setting up poetry in directory $(COOKIECUTTER_OUTPUT_DIR)"
	@$(MAKE) -C $(COOKIECUTTER_OUTPUT_DIR) setup-dev-env-minimal

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
