import glob
import os

path_ = "/Volumes/BAYMAC/Users/anggabayu/Documents/Develop/workspace/REPOGIC/work/kmz_gsmap/"
path_names_kmz = glob.glob(path_+"*.kmz")
#print path_names_kmz
maps = []
for path_name in path_names_kmz:
	path_wo_ext = path_name.replace(".kmz", "")
	if os.path.exists(path_wo_ext) == False:
		print "not exists"
	else:
		print "exists"
		file_name_arr = path_wo_ext.split('/')
		file_name_time = file_name_arr[len(file_name_arr)-1]
		file_name_time = file_name_time.replace("gsmap_nrt.", "")
		print file_name_time
		path_wo_ext_full = path_wo_ext+"/file/"
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x0y3.png -append "+path_wo_ext_full+"mapx0_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x1y3.png -append "+path_wo_ext_full+"mapx1_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x2y3.png -append "+path_wo_ext_full+"mapx2_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x3y3.png -append "+path_wo_ext_full+"mapx3_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x4y3.png -append "+path_wo_ext_full+"mapx4_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x5y3.png -append "+path_wo_ext_full+"mapx5_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x6y3.png -append "+path_wo_ext_full+"mapx6_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x7y3.png -append "+path_wo_ext_full+"mapx7_rain.png")
		os.system("convert "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y0.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y1.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y2.png "+path_wo_ext_full+"gsmap_rain."+file_name_time+"_x8y3.png -append "+path_wo_ext_full+"mapx8_rain.png")
		os.system("convert "+path_wo_ext_full+"mapx5_rain.png "+path_wo_ext_full+"mapx6_rain.png "+path_wo_ext_full+"mapx7_rain.png "+path_wo_ext_full+"mapx8_rain.png "+path_wo_ext_full+"mapx0_rain.png "+path_wo_ext_full+"mapx1_rain.png "+path_wo_ext_full+"mapx2_rain.png "+path_wo_ext_full+"mapx3_rain.png "+path_wo_ext_full+"mapx4_rain.png +append "+path_+"result/one_image/map_rain_"+file_name_time+".png")
		maps.append(path_+"result/one_image/map_rain_"+file_name_time+".png")

if len(maps)>0:
	os.system("convert -delay 150 -loop 0 -alpha set -dispose previous "+path_+"result/one_image/*.png "+path_+"result/map_rain.gif")
