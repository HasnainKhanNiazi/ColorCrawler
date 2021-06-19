import cv2 
   
path = r'C:/Users/HP/Desktop/ColorCrawler/1e23c283-7047-4377-ad8a-46d60ec54033.jpg'
   
image = cv2.imread(path)
   
window_name = 'Image'

start_point = (1590, 400)

end_point = (1700, 3758)
  
color = (255, 0, 0)
  
thickness = 2
  
image = cv2.rectangle(image,start_point,end_point,(0,255,0),2)
cv2.imshow(window_name, image)
cv2.imwrite("Result.jpg", image)
cv2.waitKey(0)