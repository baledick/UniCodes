#include <stdio.h>
#include <math.h>

int main(){
	int n, i;
	double a, b, sum, h, ex;
	printf("Dose to kato akro ");
	scanf("%lf", &a);
	printf("%lf\n", a);
	printf("Dwse kai to panw ");
	scanf("%lf", &b);
	printf("%lf\n", b);
	printf("Kai ton arithmo twn vimatwn ");
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
