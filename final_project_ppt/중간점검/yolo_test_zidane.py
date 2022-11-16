import torch

# # Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
#
# # Images
# img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
#
# # Inference
# results = model(img)
#
# # Results
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
# results.show()

import torch

print("쿠다 가능 :{}".format(torch.cuda.is_available()))
print("현재 디바이스 :{}".format(torch.cuda.current_device()))
print("디바이스 갯수 :{}".format(torch.cuda.device_count()))

for idx in range(0, torch.cuda.device_count()):
    print("디바이스 :{}".format(torch.cuda.device(idx)))
    print("디바이스 이름 :{}".format(torch.cuda.get_device_name(idx)))


