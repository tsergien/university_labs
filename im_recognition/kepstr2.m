%кепстр
clc
clear
a=imread('moon.tif');
imshow(a)
x=double(a(:,:,1));

 [m,n]=size(x);
 f=fft2(x);
 a1=1;
 b1=1;
 %фаза комплексного числа__________
 angl=zeros(m,n);
 mod=abs(f);
 for k=1:m
     for j=1:n
       im=imag(f(k,j));
       re=real(f(k,j));
       if re > 0 & im >= 0
           angl(k,j)=atan(im/re);
       end
       if re < 0 & im >= 0
           angl(k,j)=pi-atan(abs(im/re));
       end
       if re < 0 & im < 0
           angl(k,j)=pi+atan(abs(im/re));
       end
       if re > 0 & im < 0
           angl(k,j)=2*pi-atan(abs(im/re));
       end
       if re == 0 & im > 0
           angl(k,j)=pi/2;
       end
       if re == 0 & im < 0
           angl(k,j)=pi*3/2;
       end
      end
 end
%_____________________________________
% z=(mod.^0.5.*exp(i.*angl));
%z=(abs(f)).^0.5.*exp(i.*atan((imag(f)./real(f))));
z=log(1+mod).*exp(i.*angl);

%z=mod.^0.5.*exp(i.*angle(f));
 zinv=ifft2(z);
 %z1=abs(zinv);
 z1=real(zinv);
   max1=max(max(z1));
   min1=min(min(z1));
    z2=255*(z1-min1)/(max1-min1);
   figure
   imshow(uint8(z2));
