#!/bin/bash

# This will work if you have MySQL client installed on your machine.
# This script is for Mac/Linux users. For Windows users, you can use Git Bash 
# to run this script or use the powershell script.

# This script will reset the database schema and insert the data into the database.

# Get the directory where the script is located
SCRIPT_DIR="$(dirname "$0")"

# MySQL connection details
MYSQL_USER="your username for the MySQL client"
MYSQL_HOST="localhost"
MYSQL_DATABASE="testbank"

# Enter your MySQL password
read -s -p "Enter your MySQL password: " MYSQL_PASSWORD

# Paths to SQL scripts
RESET_SCHEMA_SCRIPT="$SCRIPT_DIR/reset_schema.sql"
INSERT_SCRIPT_1="$SCRIPT_DIR/data_statements/questions_insert.sql"
INSERT_SCRIPT_2="$SCRIPT_DIR/data_statements/question_options_insert.sql"
INSERT_SCRIPT_3="$SCRIPT_DIR/data_statements/question_answers_insert.sql"

# Check if mysql client is mysqlsh or mysql
if command -v mysqlsh &> /dev/null
then
    echo "Using mysqlsh"
    MYSQL="mysqlsh"
elif command -v mysql &> /dev/null
then
    echo "Using mysql"
    MYSQL="mysql"
else
    echo "MySQL client not found. Please install MySQL client."
    exit
fi

# Function to execute SQL scripts
execute_sql_script() {
    local script=$1

    $MYSQL -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -D"$MYSQL_DATABASE" --file "$RESET_SCHEMA_SCRIPT"
    $MYSQL -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -D"$MYSQL_DATABASE" --file "$INSERT_SCRIPT_1"
    $MYSQL -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -D"$MYSQL_DATABASE" --file "$INSERT_SCRIPT_2"
    $MYSQL -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -D"$MYSQL_DATABASE" --file "$INSERT_SCRIPT_3"
}

execute_sql_script

echo "Data insertion completed."

