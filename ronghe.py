import cv2
import numpy as np

# 读取两幅图片转换为矩阵
img = cv2.imread("./pic12.jpeg").astype(np.float32)
H, W, C = img.shape

img2 = cv2.imread('./pic13.jpg').astype(np.float32)
img = cv2.resize(img, (499, 375));

# 设置图像的融合的权重
a = 0.5


out = img * a + img2 * (1 - a)
out = out.astype(np.uint8)

# 保存图像的融合的结果显示
cv2.imwrite("result.jpg", out)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
