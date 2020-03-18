clc
clear
dt=0.003;
f1=25;
f2=10;
T=15;
t=0:dt:T;
y=30*sin(2*pi*f1*t)+7*sin(2*pi*f2*t);

n=length(t);
plot(t(1:300),y(1:300)),grid
figure
fy=fft(y);
plot(abs(fy)),grid
figure
df=1/T;
ff=0:df:n/(2*T);
plot(ff,abs(fy(1:round(n/2)))),grid
