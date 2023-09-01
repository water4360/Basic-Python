import matplotlib.pyplot as plt

#선을 그리는 기본 그래프
plt.title('plot test')
plt.plot([10,20,30,40])
plt.show() #주피터에서는 생략 가능.



# X축, Y축
plt.plot([10,20,30,40], [1,2,3,4])
plt.show()

# X축, Y축 크로스
#단 key없이 color 적는 경우 순서 지킬 것.
#linestyle은 solid(-), dashed(--), dotted(:), dash-dot(-.)
#컬러명도 축약 가능 r, g, b 등
plt.plot([10,20,30,40], label='asc',  color='pink', linestyle='--')
plt.plot([40,30,20,10], 'g', label='desc', ls=':')
# plt.legend()
plt.legend(loc=6)
plt.show()
