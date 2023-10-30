import pandas as pd
import sys 


print(sys.argv)
day = sys.argv[1]

print("Job finished successfully! for the {day}")



# docker run -it \
#     -e POSTGRES_USER="root" \
#     -e POSTGRES_PASSWORD="root" \
#     -e POSTGRES_DB="ny_taxi" \
#     -v $(pwd)/ny_taxi_postgres:/var/lib/postgresql/data \
#     -p 5432:5432 \
#     postgres:13


