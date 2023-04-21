def printSQLException(exception):
    print("Error no "+str(exception.errno))
    print("Error Msg"+exception.msg)
    print("SQL state"+exception.sqlstate)
