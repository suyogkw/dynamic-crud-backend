
import confighelper as config
import databasehelper
from serverdatahelper import ServerData

def getall(reference):
    try:
        getdata_query = config.references[reference].queries.DATA

        data = databasehelper.getdata(getdata_query)

        print("retrieved successfully")
        return True, data

    except Exception as e:
        print(f"retrieval failed. error : {str(e)}")
        return False,None

def insert(reference, client_data):
    try:

        server_data = ServerData(reference, client_data, 'INSERT')
        ref_queries = config.references[reference].queries
        unique_check_query = ref_queries.UNIQUE_CLAUSE.format(client=client_data,server=server_data)

        verify = databasehelper.getdata(unique_check_query)
        if len(verify)!=0:
            print("uniqueness check failed")
            return False,verify

        insert_query = ref_queries.INSERT.format(client=client_data,server=server_data)
        databasehelper.execute(insert_query)

        verify = databasehelper.getdata(unique_check_query)        
        if len(verify) != 1:
            print("insert verification failed")
            return False, verify if len(verify)>1 else None
    
        loghistory_query = ref_queries.HISTORY.format(data=verify[0],client=client_data,server=server_data)
        databasehelper.execute(loghistory_query)

        print("inserted successfully")
        return True, verify[0]

    except Exception as e:
        print(f"insertion failed. error : {str(e)}")
        return False,None

def update(reference, client_data):
    try:

        server_data = ServerData(reference, client_data, 'UPDATE')
        ref_queries = config.references[reference].queries
        id_check_query = ref_queries.IDENTITY_CLAUSE.format(client=client_data,server=server_data)

        verify_id = databasehelper.getdata(id_check_query)
        if len(verify_id)!=1:
            print("uniqueness check failed or record doesn't exist")
            return False, verify_id if len(verify_id)>1 else None

        unique_check_query = ref_queries.UNIQUE_CLAUSE.format(client=client_data,server=server_data)

        verify = databasehelper.getdata(unique_check_query)
        if len(verify)!=0:
            if len(verify)>1 or (len(verify)==1 and verify[0] != verify_id[0]):
                print("uniqueness check failed")
                return False, verify          

        update_query = ref_queries.UPDATE.format(client=client_data,server=server_data)
        databasehelper.execute(update_query)

        update_check_query = ref_queries.UPDATE_VERIFY.format(client=client_data,server=server_data)
        verify = databasehelper.getdata(update_check_query)        
        if len(verify) != 1:
            print("update verification failed")
            return False, verify if len(verify)>1 else None
    
        loghistory_query = ref_queries.HISTORY.format(data=verify[0],client=client_data,server=server_data)
        databasehelper.execute(loghistory_query)

        print("updated successfully")
        return True, verify[0]

    except Exception as e:
        print(f"update failed. error : {str(e)}")
        return False,None

def delete(reference, client_data):
    try:

        server_data = ServerData(reference, client_data,'DELETE')
        ref_queries = config.references[reference].queries
        id_check_query = ref_queries.IDENTITY_CLAUSE.format(client=client_data,server=server_data)

        verify_id = databasehelper.getdata(id_check_query)
        if len(verify_id)!=1:
            print("uniqueness check failed or record doesn't exist")
            return False, verify_id if len(verify_id)>1 else None

        delete_query = ref_queries.DELETE.format(client=client_data,server=server_data)
        databasehelper.execute(delete_query)

        verify = databasehelper.getdata(id_check_query)        
        if len(verify) != 0:
            print("delete verification failed")
            return False, verify
    
        loghistory_query = ref_queries.HISTORY.format(data=verify_id[0],client=client_data,server=server_data)
        databasehelper.execute(loghistory_query)

        print("deleted successfully")
        return True, verify_id[0]

    except Exception as e:
        print(f"deletion failed. error : {str(e)}")
        return False,None

    


