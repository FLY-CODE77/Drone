# 객체 추적과 모션 벡터

> 배경차분(Background Substraction : BS)
- 등록된 배경 모델과 현제 입력 프레임과의 차영상을 이용하여 전경 객체를 검출
- 움직이는 전경 객체 검출을 위한 기본적인 방법입니다.

## bs_static(배경차분 결과)
![Screenshot from 2021-05-06 18-00-43](https://user-images.githubusercontent.com/72845895/117271389-158f3900-ae95-11eb-84e4-4632cccb7311.png)

- background substraction으로 배경 - 입력 영상의 차를 가지고 전경 객체를 검출해서 표시해주고
- rounding box을 픽셀 개수가 75개 이상인 객체에 표시했다.

- 전반적으로 드론이 잘 검출이 되나.. 영상 잔상이 남아서.. 바운딩 박스가 필요 없는곳에 있다.(배경 문제?)


