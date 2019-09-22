# image_similarity_plus

rest_server_ssim.py 为使用Flask的SSIM图片比较服务      
image_similarity_plus.py 是使用MobileNet深度神经网络的图片比较服务，此服务目前比较速度慢     

SSIM比较方法需要pip install 如下组件           
Flask        
opencv-python      
scikit-image
imutils      
numpy       

不使用Flask服务的比较程序见ssim_get_similarity.py    
SSIM原理见:     
`https://blog.csdn.net/xiaohaijiejie/article/details/47816485`     
SSIM python版本的资料见   
`https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/`     
SSIM使用的scikit-image也需要安装opencv     
安装opencv的方法在Mac上面需要使用brew        
`brew install pkg-config`      
`brew install opencv@2`      
`brew link --force opencv@2`      


对于使用nodejs来进行比较的可以参考`https://github.com/peterbraden/node-opencv`      
在此项目的examples中有dissimilarity.js进行比较图片的不同性     
注意的是此项目使用的是opencv的绑定，需要额外安装opencv      

