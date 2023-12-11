# PowerShell script to reset schema and insert data on windows
# Only for development purposes

# This script assumes you have MySQL installed and added to your PATH
# Please change the following variables to match your MySQL connection details
# MySQL connection details
$MYSQL_USER = "enter your user name for MySQL"
$MYSQL_HOST = "localhost"
$MYSQL_DATABASE = "testbank" # if you have a different database name please adjust as needed

# Prompt for the MySQL password to avoid storing it in the script
$MYSQL_PASSWORD = Read-Host "Enter MySQL Password" -AsSecureString
$MYSQL_PASSWORD = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($MYSQL_PASSWORD))

# You will not need to change the following variables
# Paths to SQL scripts
$RESET_SCHEMA_SCRIPT = ".\db\reset_schema.sql"
$INSERT_SCRIPT_1 = ".\db\data_statements\questions_insert.sql"
$INSERT_SCRIPT_2 = ".\db\data_statements\question_options_insert.sql"
$INSERT_SCRIPT_3 = ".\db\data_statements\question_answers_insert.sql"

# Choose the MySQL client, first it will try mysql then mysqlsh 
$mysqlClient = "mysql"
if (Get-Command "mysqlsh" -ErrorAction SilentlyContinue) {
    $mysqlClient = "mysqlsh"
}


# Function to execute SQL scripts
function Invoke-SqlScript {
    param (
        [string]$scriptPath
    )
        try {
            # Use the mysql client to execute the SQL script file directly
            & $mysqlClient -h"$MYSQL_HOST" -u"$MYSQL_USER" --password="$MYSQL_PASSWORD" -D"$MYSQL_DATABASE" --file "$RESET_SCHEMA_SCRIPT"
            & $mysqlClient -h"$MYSQL_HOST" -u"$MYSQL_USER" --password="$MYSQL_PASSWORD" -D"$MYSQL_DATABASE" --file "$INSERT_SCRIPT_1"
            & $mysqlClient -h"$MYSQL_HOST" -u"$MYSQL_USER" --password="$MYSQL_PASSWORD" -D"$MYSQL_DATABASE" --file "$INSERT_SCRIPT_2"
            & $mysqlClient -h"$MYSQL_HOST" -u"$MYSQL_USER" --password="$MYSQL_PASSWORD" -D"$MYSQL_DATABASE" --file "$INSERT_SCRIPT_3"
        }
    catch {
        Write-Host "An error occurred: $_"
        exit
    }
}

Invoke-SqlScript

Write-Host "Data insertion completed."

