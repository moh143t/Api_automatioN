import requests
import json
from Util.util import readCellValue,writeCellValue,readConfigValue



def get_api(i,filepath):
    try:
        head = {
            'Authorization': 'Bearer ' + readCellValue (i, 4, filepath),
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'}

        API_ENDPOINT = (readConfigValue (2, 2, filepath))+(readCellValue (i, 2, filepath))

        r = requests.get (API_ENDPOINT, headers=head)
        writeCellValue (i, 7, r.status_code, filepath)
        writeCellValue (i, 10, r.text, filepath)
        if (r.status_code == 405):
            try:
                response_native = json.loads (r.text)
                if 'StatusMessage' in str (response_native):
                    Message = response_native.get ('Message')
                    writeCellValue (i, 9, Message, filepath)
                if 'detail' in str (response_native):
                    detail = response_native.get ('detail')
                    writeCellValue (i, 9, detail, filepath)
                else:
                    writeCellValue (i, 9, 'Not Message Found', filepath)
                    writeCellValue (i, 10, r.text, filepath)

            except ValueError:
                writeCellValue (i, 9, "Invalid jason", filepath)
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
                    writeCellValue (i, 9, "Not Message Found", filepath)
                    writeCellValue (i, 10, r.text, filepath)
            except ValueError:

                writeCellValue (i, 9, "invalid json", filepath)

        print (API_ENDPOINT)
        print (r.status_code)
        print (r.text)
        if (r.status_code == readCellValue (i, 6, filepath)):
            writeCellValue (i, 8, 'Pass', filepath)
        else:
            writeCellValue (i, 8, 'Fails', filepath)

    except Exception, err:
        print "Error IN the File "