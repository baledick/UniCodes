#include <stdio.h>
#include <math.h>

int main(){
	int n, i;
	double a, b, sum, h, ex;
	printf("Give me the lower bound ");
	scanf("%lf", &a);
	printf("%lf\n", a);
	printf("Now for the upper bound ");
	scanf("%lf", &b);
	printf("%lf\n", b);
	printf("And finally, the number of steps ");
	scanf("%d", &n);
	printf("%d\n", n);
	sum=0.0;
	h=(b-a)/n;
	for(i=0; i<=n; i++){
		sum+=(cos(a+h*i)*h);
		}
	sum-=(cos(a)+cos(b))*(h/2);
	ex=sin(b)-sin(a);
	printf("%lf, %lf\n", sum, ex);
return 0;
}
