
import confighelper as config
import databasehelper
from serverdatahelper import ServerData
from utilities import get_sqlquery 

def getall(reference):
    try:
        getdata = get_sqlquery(config.references[reference].queries.DATA)

        data = databasehelper.getdata(*getdata)

        print("retrieved successfully")
        return True, data

    except Exception as e:
        print(f"retrieval failed. error : {str(e)}")
        return False,None

def insert(reference, client_data):
    try:

        server_data = ServerData(reference, client_data, 'INSERT')
        ref_queries = config.references[reference].queries
        q_unique_check = get_sqlquery(ref_queries.UNIQUE_CLAUSE, client=client_data,server=server_data)
        
        verify = databasehelper.getdata(*q_unique_check)
        if len(verify)!=0:
            print("uniqueness check failed")
            return False,verify

        q_insert = get_sqlquery(ref_queries.INSERT, client=client_data,server=server_data)
        databasehelper.execute(*q_insert)

        verify = databasehelper.getdata(*q_unique_check)        
        if len(verify) != 1:
            print("insert verification failed")
            return False, verify if len(verify)>1 else None
    
        q_loghistory = get_sqlquery(ref_queries.HISTORY, client=client_data,server=server_data, data=verify[0])
        databasehelper.execute(*q_loghistory)

        print("inserted successfully")
        return True, verify[0]

    except Exception as e:
        print(f"insertion failed. error : {str(e)}")
        return False,None

def update(reference, client_data):
    try:

        server_data = ServerData(reference, client_data, 'UPDATE')
        ref_queries = config.references[reference].queries

        q_id_check = get_sqlquery(ref_queries.IDENTITY_CLAUSE, client=client_data,server=server_data)

        verify_id = databasehelper.getdata(*q_id_check)
        if len(verify_id)!=1:
            print("uniqueness check failed or record doesn't exist")
            return False, verify_id if len(verify_id)>1 else None

        q_unique_check = get_sqlquery(ref_queries.UNIQUE_CLAUSE, client=client_data,server=server_data)

        verify = databasehelper.getdata(*q_unique_check)
        if len(verify)!=0:
            if len(verify)>1 or (len(verify)==1 and verify[0] != verify_id[0]):
                print("uniqueness check failed")
                return False, verify          

        q_update = get_sqlquery(ref_queries.UPDATE, client=client_data,server=server_data)
        databasehelper.execute(*q_update)

        q_update_check = get_sqlquery(ref_queries.UPDATE_VERIFY, client=client_data,server=server_data)

        verify = databasehelper.getdata(*q_update_check)        
        if len(verify) != 1:
            print("update verification failed")
            return False, verify if len(verify)>1 else None
    
        q_loghistory = get_sqlquery(ref_queries.HISTORY, client=client_data,server=server_data, data=verify[0])
        databasehelper.execute(*q_loghistory)

        print("updated successfully")
        return True, verify[0]

    except Exception as e:
        print(f"update failed. error : {str(e)}")
        return False,None

def delete(reference, client_data):
    try:

        server_data = ServerData(reference, client_data,'DELETE')
        ref_queries = config.references[reference].queries
        q_id_check = get_sqlquery(ref_queries.IDENTITY_CLAUSE, client=client_data,server=server_data)

        verify_id = databasehelper.getdata(*q_id_check)
        if len(verify_id)!=1:
            print("uniqueness check failed or record doesn't exist")
            return False, verify_id if len(verify_id)>1 else None

        q_delete = get_sqlquery(ref_queries.DELETE, client=client_data,server=server_data)
        databasehelper.execute(*q_delete)

        verify = databasehelper.getdata(*q_id_check)        
        if len(verify) != 0:
            print("delete verification failed")
            return False, verify
    
        q_loghistory = get_sqlquery(ref_queries.HISTORY, client=client_data,server=server_data, data=verify_id[0])
        databasehelper.execute(*q_loghistory)

        print("deleted successfully")
        return True, verify_id[0]

    except Exception as e:
        print(f"deletion failed. error : {str(e)}")
        return False,None

    


