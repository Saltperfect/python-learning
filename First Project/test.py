library(ggplot2)
data(diamonds)
summary(diamonds)
names(diamonds)
ggplot(aes(x= price), data = diamonds)+
  geom_histogram(color = 'black', fill = 'blue', binwidth= 200)+
  scale_x_continuous(limits = c(15000,20000))+
  facet_wrap(~cut, scales = 'free_y')
by(diamonds$price , diamonds$cut , max)
by(diamonds$price , diamonds$cut , min)
by(diamonds$price , diamonds$cut , median)
summary(diamods)

ggplot(aes(x= price/carat), data = diamonds)+
  geom_histogram(color = 'black', fill = 'blue', binwidth= 0.01)+
  scale_x_log10()+
  facet_wrap(~cut)

qplot(y= price, x = clarity, data =  diamonds, geom = 'boxplot')

ggsave('priceHistogram.png')