BACKEND_DIR = server
FRONTEND_DIR = src

# --- Установка ---
install-frontend:
	@yarn install

install-backend:
	@poetry env use 3.12.1
	@poetry install --no-root
	@poetry run python $(BACKEND_DIR)/settings/environment.py && echo .env successfully created

.PHONY: install
install:
	@make -j 2 install-backend install-frontend

# --- Запуск ---
.PHONY: run-backend
run-backend:
	@poetry run uvicorn server.app:app --reload

.PHONY: run-frontend
run-frontend:
	@yarn dev

.PHONY: run
run:
	@make -j 2 run-backend run-frontend