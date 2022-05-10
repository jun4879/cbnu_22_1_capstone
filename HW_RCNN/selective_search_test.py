import selectivesearch
import cv2
import matplotlib.pyplot as plt

# 테스트 이미지를 cv2로 로드하고 matplotlib으로 시각화
img = cv2.imread('./data/test.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print('img shape:',img.shape )

plt.figure(figsize=(8,8))
plt.imshow(img_rgb)
plt.show()

_, regions = selectivesearch.selective_search(img_rgb, scale=100, min_size=2000)
print(type(regions), len(regions))

# rect 정보 출력
cand_rects = [cand['rect'] for cand in regions]
print(cand_rects)

# opencv의 rectangle()을 이용하여 시각화
# rectangle()은 이미지와 좌상단 좌표, 우하단 좌표, box 컬러 색, 두께 등을 인자로 입력하면 원본 이미지에 box를 그려줌.

green_rgb = (125, 255, 51)
img_rgb_copy = img_rgb.copy()
for rect in cand_rects:
    left = rect[0]
    top = rect[1]
    # rect[2], rect[3]은 너비와 높이이므로 우하단 좌표를 구하기 위해 좌상단 좌표에 각각을 더함.
    right = left + rect[2]
    bottom = top + rect[3]
    img_rgb_copy = cv2.rectangle(img_rgb_copy, (left, top), (right, bottom), color=green_rgb, thickness=2)

plt.figure(figsize=(8, 8))
plt.imshow(img_rgb_copy)
plt.show()
