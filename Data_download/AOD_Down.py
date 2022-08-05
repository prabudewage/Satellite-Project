

####################	AOD Data Download	#########################################################################



import s3fs   
import os
import datetime
from datetime import timedelta

# The top-level class S3FileSystem holds connection information and allows typical -
# -file-system style operations like cp, mv, ls, du, glob, etc., as well as put/get of local files to/from S3.
fs = s3fs.S3FileSystem(anon=True)       

year = 2021

month_start = 12
month_end = 12

day_start = 31
day_end = 31

hour = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]

#download_directory = "/home/prabu/Desktop/test1/ddd/"
download_directory = "/home/prabu/Desktop/test1/AOD_data/raw/"


# Find Julian day from given year/month/day
calendar_start = datetime.datetime(year, month_start, day_start)
julian_day_start = calendar_start.strftime('%j')

calendar_end = datetime.datetime(year, month_end, day_end)
julian_day_end = calendar_end.strftime('%j')


for x in range(int(julian_day_start), int(julian_day_end)+1):
  monthh = datetime.datetime.strptime(str(x), '%j').strftime("%m")
  dayy = datetime.datetime.strptime(str(x), '%j').strftime("%d")
  print(x, monthh, dayy)
  
  for i in hour:
  	download_path = download_directory + str(year) + '/'
  	download_path = download_directory + str(year) + '/' + str(monthh) + '/'
  	download_path = download_directory + str(year) + '/' + str(monthh) + '/' + str(dayy) + '/'
  	#download_path = download_directory + str(year) + '/' + str(monthh) + '/' + str(dayy) + '/' + str(i) + '/'
  	download_path = download_directory + str(year) + '/' + str(monthh) + '/' + str(dayy) + '/' + str(i) 
  	
  	digit = len(str(x))
  	if digit == 1:
  		julian_day = '0' + '0' + str(x)
  	elif digit == 2:
  		julian_day = '0' + str(x)
  	else:
  		julian_day = str(x)
  	
  	
  	AWS_path = 'noaa-goes16/ABI-L2-AODC/' + str(year) + '/' + julian_day + '/' + str(i) + '/*'
  	files= fs.glob(AWS_path)
  	last_file = len(files) - 1

  	try:
  	    fs.get(files[0], download_path)        # Downloading only second last file in hour
  	    #fs.get(files, download_path)                  # Downloading all the files in hour
  	except:
  	    print("An exception occurred") 

print("Download complete")
