import requests
import json
from Util.util import readCellValue,writeCellValue,readConfigValue





def post_api(i,filepath):
    head = {
        'Authorization': 'Bearer ' + str(readCellValue (4, 4, filepath)),
        'Content-Type': 'application/json; charset=utf-8',
    }
    data = (readCellValue (i, 5, filepath))
    try:
        API_ENDPOINT = (readConfigValue (2, 2, filepath)) + (readCellValue (i, 2, filepath))
        r = requests.post (url=API_ENDPOINT, data=data, headers=head)
        writeCellValue (i, 7, r.status_code, filepath)
        writeCellValue (i, 9, r.text, filepath)
        print (r.status_code)
        print (API_ENDPOINT)
        print (r.text)
        if (r.status_code == 405):
            try:
                response_native = json.loads (r.text)
                if 'Message' in response_native:
                    Message = response_native.get ('Message')
                    writeCellValue (i, 9, Message, filepath)
                    writeCellValue (i, 10, r.text, filepath)
                if 'detail' in str (response_native):
                    detail = response_native.get ('detail')
                    writeCellValue (i, 9, detail, filepath)
                else:
                    writeCellValue (i, 9, "No message found", filepath)
                    writeCellValue (i, 10, r.text, filepath)

            except ValueError:
                writeCellValue (i, 9, "invalid json", filepath)
                writeCellValue (i, 10, r.text, filepath)

        else:
            try:
                response_native = json.loads (r.text)
                meta = response_native.get ('Meta')
                if 'StatusMessage' in str (meta):
                    StatusMessage = meta.get ('StatusMessage')
                    writeCellValue (i, 9, StatusMessage, filepath)
                if 'detail' in str (response_native):
                    detail = response_native.get ('detail')
                    writeCellValue (i, 9, detail, filepath)
                else:
                    writeCellValue (i, 9, "No message found", filepath)
                    writeCellValue (i, 10, r.text, filepath)
            except ValueError:
                writeCellValue (i, 9, "invalid json", filepath)
                writeCellValue (i, 10, r.text, filepath)

        if (r.status_code == readCellValue (i, 6, filepath)):
            writeCellValue (i, 8, 'Pass', filepath)

        else:
            writeCellValue (i, 8, 'Fails', filepath)

            if (r.status_code == 500):
                data = eval (readCellValue (i, 5, filepath))
                API_ENDPOINT = readCellValue (i, 2, filepath)
                r = requests.post (url=API_ENDPOINT, data=data)
                writeCellValue (i, 7, r.status_code, filepath)
                writeCellValue (i, 10, r.text, filepath)
                response_native = json.loads (r.text)
                meta = response_native.get ('Meta')
                StatusMessage = meta.get ('StatusMessage')
                writeCellValue (i, 9, StatusMessage, filepath)
                print (r.status_code)
                print (API_ENDPOINT)
                print (r.text)
                if (r.status_code == readCellValue (i, 6, filepath)):
                    writeCellValue (i, 8, 'Pass', filepath)

                else:
                    writeCellValue (i, 8, 'Fails', filepath)


    except Exception, err:
        print "Error IN the File "




