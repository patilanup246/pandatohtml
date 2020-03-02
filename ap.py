html = """<!DOCTYPE html>   
<html lang="en">   
<head>   
<meta charset="utf-8">   
<title>Example of Employee Table with twitter bootstrap</title>   
<meta name="description" content="Creating a Employee table with Twitter Bootstrap. Learn with example of a Employee Table with Twitter Bootstrap.">  
<link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">   
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<link rel="stylesheet" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.min.css"></style>
<script type="text/javascript" src="http://cdn.datatables.net/1.10.2/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>  
<body style="margin:20px auto">  
<div class="container">
<div class="row header" style="text-align:center;color:green">
<h3>Bootstrap Table With sorting,searching and paging using dataTable.js (Responsive)</h3>
</div>
{0}
	  </div>
</body>  

</html>  """

import glob, os
import pandas as pd

path = 'data/'
fileList = os.listdir(path)
appended_data = []


df = pd.DataFrame(columns=['CompanyTicker',
'CompanyName',
'PressReleasesTitle',
'PressReleasesDateTime',
'Description',
'PressReleasesUrl'])
for file in fileList:
    xls = pd.ExcelFile(path + file)
    df1 = pd.read_excel(xls, 'Sheet1')
    df1.reset_index()
    del df1['Unnamed: 0']
    df.concat(df1)

print(html.format("".join(df.to_html())))

