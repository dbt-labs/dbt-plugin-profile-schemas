quicktype --lang js -s schema --src v1/dbt-plugin.schema.json -o gen/js/profile_schema.js
quicktype --lang go -s schema --src v1/dbt-plugin.schema.json -o gen/go/profile_schema.go
quicktype --lang python -s schema --src v1/dbt-plugin.schema.json -o gen/python/dbt-plugin/profile_schema.py