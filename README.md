# Logistics App

Конзолно приложение за управление на доставки между хъбове в големите австралийски градове. Разработено като екипен проект в Telerik Academy, курс по Python с ООП фокус.

## Описание на проекта

Приложението се използва от служители на голяма австралийска компания, разширяваща дейността си във freight индустрията. Служителите могат да:

- записват детайли на нов пакет за доставка,
- създават и търсят подходящи маршрути,
- назначават камиони и пакети към маршрути,
- преглеждат текущото състояние на пакети, камиони и маршрути.

Поддържани градове (хъбове): **Sydney (SYD), Melbourne (MEL), Adelaide (ADL), Alice Springs (ASP), Brisbane (BRI), Darwin (DAR), Perth (PER)**.

## Екип

Проектът е разработен от трима души, разпределени по отговорности:

- **Тинко** — models (`Customer`, `Package`, `Route`, `Truck`) и unit тестове за тях
- **Крис** — `core/` (`ApplicationData`, `Engine`, `CommandFactory`) и всички `commands/`
- **Тонката** — `helpers/` (разстояния, валидация, изчисление на време) и unit тестове за тях

Работата бе организирана през отделни Git branches (`Models`, `core`, `tests`), обединени накрая в `main`.

## Структура на проекта

```
Logistics-App-ATK/
├── main.py
├── Models/
│   ├── Customer.py
│   ├── Package.py
│   ├── Route.py
│   └── Truck.py
├── core/
│   ├── application_data.py
│   ├── command_factory.py
│   └── engine.py
├── commands/
│   ├── base_command.py
│   ├── create_package.py
│   ├── create_route.py
│   ├── assign_truck_to_route.py
│   ├── assign_package_to_route.py
│   ├── find_routes_for_package.py
│   ├── show_packages.py
│   ├── show_routes.py
│   ├── show_trucks.py
│   ├── show_unassigned_packages.py
│   ├── show_package_info.py
│   └── show_routes_in_progress.py
├── helpers/
│   ├── distance_helper.py
│   ├── time_helper.py
│   └── validation_helpers.py
└── Tests/
    └── ...
```

## Изисквания

- Python 3.10+
- Няма външни зависимости — само вградени модули (`datetime`, `abc`, `unittest`)

## Стартиране

```bash
python main.py
```

При стартиране системата автоматично зарежда флота от 40 камиона по условие:

| Марка | ID диапазон | Капацитет | Обхват |
|---|---|---|---|
| Scania | 1001–1010 | 42000 kg | 8000 km |
| Man | 1011–1025 | 37000 kg | 10000 km |
| Actros | 1026–1040 | 26000 kg | 13000 km |

Приложението чете команди ред по ред от конзолата, докато не се въведе `end`.

## Команди

| Команда | Параметри | Описание |
|---|---|---|
| `create_package` | `start_location end_location weight first_name last_name email phone address` | Създава нов пакет (адресът може да съдържа интервали) |
| `create_route` | `departure_time(ISO, напр. 2026-10-10T06:00) stop1 stop2 ...` | Създава нов маршрут (мин. 2 спирки) |
| `assign_truck_to_route` | `route_id` | Назначава първия свободен камион с достатъчен капацитет и обхват |
| `assign_package_to_route` | `package_id route_id` | Качва пакет на маршрут, ако има свободен капацитет |
| `find_routes_for_package` | `package_id` | Търси съществуващи маршрути, покриващи локациите на пакета в правилната посока |
| `show_packages` | — | Показва всички регистрирани пакети |
| `show_trucks` | — | Показва целия флот камиони |
| `show_routes` | — | Показва всички маршрути с часове на пристигане по спирки |
| `show_unassigned_packages` | — | Показва пакети, които все още нямат назначен маршрут |
| `show_package_info` | `package_id` | Пълна информация за конкретен пакет и клиента му |
| `show_routes_in_progress` | — | Показва маршрути, които в момента са между тръгване и пристигане |
| `end` | — | Спира програмата |

## Пример за сесия

```
show_trucks
create_package SYD MEL 45 Ivan Ivanov ivan@test.com 0888123456 Sofia Vitosha Street 25
create_package BRI ADL 3000 Petar Petrov petar@test.com 0899112233 Plovdiv Central Square 1
show_packages
show_unassigned_packages
create_route 2026-10-10T06:00 BRI SYD MEL
create_route 2026-10-12T06:00 SYD MEL ADL
show_routes
find_routes_for_package 1
assign_truck_to_route 1
assign_truck_to_route 2
assign_package_to_route 1 1
show_package_info 1
show_unassigned_packages
show_routes_in_progress
end
```

## Тестове

Unit тестовете се намират в папка `Tests/` и покриват models и helper функциите:

```bash
python -m unittest discover Tests
```

