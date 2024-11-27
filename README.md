# Пример CI/CD с github actions
В этом репозитории описан пример сетапа CI/CD с Github Actions.

## Структура проекта
- `app/main.py` - простое приложение, выводящее "Hello, World!" каждые 2 секунды
- `tests/` - модульные тесты
- `.github/workflows/` - конфигурация CI/CD пайплайнов
- `Dockerfile` и `docker-compose.yml` - конфигурация для контейнеризации

## CI/CD Пайплайны
В проекте настроены три GitHub Actions workflow:

1. **Hello World** (hello-world.yml)
   - Запускается при любом push
   - Демонстрирует базовый пример GitHub Action

2. **Tests** (run-tests.yml)
   - Запускается при создании pull request
   - Устанавливает зависимости
   - Запускает модульные тесты

3. **Deploy** (deploy.yml)
   - Запускается при push в main ветку
   - Деплоит приложение на сервер через SSH
   - Обновляет и перезапускает Docker контейнер

## Другие данные
[Ссылка на презентацию](https://docs.google.com/presentation/d/1OUmoYoDGPweKPGQCKsVN1K-o-UksVvw_BOnXgFNKkS0/edit#slide=id.g27f99cccac5_2_43)

## Автор
[Михаил Хромов](https://t.me/mikhail_khromov)
