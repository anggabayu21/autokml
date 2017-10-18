import glob
import os
import urllib

request_date = "20170914-20170918/"
path_ = "/your_work_path/kmz_gsmap/"

date_arr = ["20170914","20170915","20170916","20170917","20170918"]
full_path = path_+request_date
#http://sharaku.eorc.jaxa.jp/GSMaP/archive/kmz/201707/gsmap_nrt.20170717.0100.kmz
if not os.path.exists(full_path):
    os.makedirs(full_path)

for date_ in date_arr:
	for j in range(0,25):
		time_ = str(j)
		if j < 10:
			time_ = "0"+str(j)
		if not os.path.exists(full_path+"gsmap_nrt."+date_+"."+time_+"00.kmz"):
			try:
				testfile = urllib.URLopener()
				testfile.retrieve("http://sharaku.eorc.jaxa.jp/GSMaP/archive/kmz/"+date_[:-2]+"/gsmap_nrt."+date_+"."+time_+"00.kmz", full_path+"gsmap_nrt."+date_+"."+time_+"00.kmz")
				os.system("unzip "+full_path+"gsmap_nrt."+date_+"."+time_+"00.kmz -d "+full_path+"gsmap_nrt."+date_+"."+time_+"00")
			except IOError as ex:
				print "error"

path_names_kmz = glob.glob(full_path+"*.kmz")
#print path_names_kmz
maps = []
map_path_x_y_ = []
map_path_x_y_.append([])
map_path_x_y_.append([])
map_path_x_y_.append([])
map_path_x_y_.append([])
map_path_x_y_.append([])
map_path_x_y_.append([])
map_path_x_y_.append([])
map_path_x_y_.append([])
map_path_x_y_.append([])

for path_name in path_names_kmz:
	path_wo_ext = path_name.replace(".kmz", "")
	if os.path.exists(path_wo_ext) == True:
		#print "exists"
		file_name_arr = path_wo_ext.split('/')
		file_name_time = file_name_arr[len(file_name_arr)-1]
		file_name_time = file_name_time.replace("gsmap_nrt.", "")
		#print file_name_time
		path_wo_ext_full = path_wo_ext+"/file/"

		map_path_x_y_[0].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y3.png"])
		map_path_x_y_[1].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y3.png"])
		map_path_x_y_[2].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y3.png"])
		map_path_x_y_[3].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y3.png"])
		map_path_x_y_[4].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y3.png"])
		map_path_x_y_[5].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y3.png"])
		map_path_x_y_[6].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y3.png"])
		map_path_x_y_[7].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y3.png"])
		map_path_x_y_[8].append([path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y0.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y1.png", path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y2.png",path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y3.png"])

		maps.append(file_name_time)

if len(maps)>0:
	if not os.path.exists(full_path+"result"):
		os.makedirs(full_path+"result")
	for i in range(0,9):
		cmd_arr_ = []
		cmd_arr = ["","","",""]
		for j in range(0,len(maps)):
			for k in range(0,4):
				map_path = map_path_x_y_[i][j][k]
				cmd_arr[k] = cmd_arr[k] + " " + map_path
		for k in range(0,4):
			#print cmd_arr[k]
			os.system("convert -delay 150 -loop 0 -alpha set -dispose previous "+cmd_arr[k]+" "+full_path+"result/map_rain_x"+str(i)+"y"+str(k)+".gif")
