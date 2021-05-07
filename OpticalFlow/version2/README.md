# 객체 추적과 모션 벡터

> 배경차분(Background Substraction : BS)
- 등록된 배경 모델과 현제 입력 프레임과의 차영상을 이용하여 전경 객체를 검출
- 움직이는 전경 객체 검출을 위한 기본적인 방법입니다.

## bs_static(배경차분 결과)
![Screenshot from 2021-05-06 18-00-43](https://user-images.githubusercontent.com/72845895/117271389-158f3900-ae95-11eb-84e4-4632cccb7311.png)

- background substraction으로 배경 - 입력 영상의 차를 가지고 전경 객체를 검출해서 표시해주고
- rounding box을 픽셀 개수가 75개 이상인 객체에 표시했다.

- 전반적으로 드론이 잘 검출이 되나.. 영상 잔상이 남아서.. 바운딩 박스가 필요 없는곳에 있다.(배경 문제?)

## moving_average(이동 평균 배경)
![Screenshot from 2021-05-07 18-47-14](https://user-images.githubusercontent.com/72845895/117432823-be0cce00-af65-11eb-8da3-6df63870f57b.png)

- moving_average를 사용해서 메 프레임이 들어올 떄마다 평균 영상을 갱신한다
- $dst(x,y) = (1-\alpha) * dst(x, y) + \alpha * src(x, y) if mask(x, y) not 0
- cv2.accumulateweighted(src, dst, alpha. mask=None) -> dst
- src : np.uint8 , dsk : np.float32
- accumulateweight alpha value, gaussian value, image pixel value 등 다양한 하이퍼 파라미터를 영상을 보면서 조절하는 경험을 했습니다
- moving average cons : 드론이 hovering 하는 오래 하는 상황이 되면 배경으로 인식이 되는 단점이 생긴다..
![Screenshot from 2021-05-07 18-47-34](https://user-images.githubusercontent.com/72845895/117433802-dc26fe00-af66-11eb-966b-7746870b837e.png)

## Conclution
- 배경 차분, 이동 평균 배경을 이용한 드론 탐색은 가능은 하나.. 잔상, hovering 문제 때문에 다음 mog알고리즘을 사용해보자